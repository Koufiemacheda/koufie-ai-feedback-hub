import boto3
import json
import uuid
from datetime import datetime

# AWS Service Clients
comprehend = boto3.client('comprehend')
dynamodb = boto3.resource('dynamodb')

# DynamoDB Table
table = dynamodb.Table('koufie-feedback-table')

# CORS Configuration
CORS = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Methods': 'POST, OPTIONS'
}

def lambda_handler(event, context):

    # Handle browser preflight requests
    if event.get('httpMethod') == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': CORS,
            'body': ''
        }

    try:
        body = json.loads(event.get('body', '{}'))

        name = body.get('name', 'Anonymous')
        email = body.get('email', '')
        message = body.get('message', '')[:5000]

        if not message:
            return {
                'statusCode': 400,
                'headers': CORS,
                'body': json.dumps({
                    'success': False,
                    'error': 'Message is required'
                })
            }

        # Sentiment Analysis
        sentiment_response = comprehend.detect_sentiment(
            Text=message,
            LanguageCode='en'
        )

        sentiment = sentiment_response['Sentiment']

        sentiment_score = sentiment_response['SentimentScore'].get(
            sentiment.title(),
            0
        )

        # Entity Detection
        entities_response = comprehend.detect_entities(
            Text=message,
            LanguageCode='en'
        )

        entities = [
            {
                'text': entity['Text'],
                'type': entity['Type']
            }
            for entity in entities_response.get('Entities', [])[:10]
        ]

        feedback_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'feedback_id': feedback_id,
                'name': name,
                'email': email,
                'message': message,
                'sentiment': sentiment,
                'sentiment_score': str(sentiment_score),
                'entities': entities,
                'submitted_at': datetime.utcnow().isoformat()
            }
        )

        return {
            'statusCode': 200,
            'headers': CORS,
            'body': json.dumps({
                'success': True,
                'feedback_id': feedback_id,
                'sentiment': sentiment,
                'sentiment_score': sentiment_score
            })
        }

    except Exception as error:
        return {
            'statusCode': 500,
            'headers': CORS,
            'body': json.dumps({
                'success': False,
                'error': str(error)
            })
        }
