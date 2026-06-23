import boto3
import json
from collections import Counter
from decimal import Decimal

# DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('koufie-feedback-table')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

def lambda_handler(event, context):

    try:

        response = table.scan()
        items = response.get('Items', [])

        sentiment_counts = Counter()

        for item in items:
            sentiment = item.get('sentiment', 'UNKNOWN')
            sentiment_counts[sentiment] += 1

        feedback_history = sorted(
            items,
            key=lambda x: x.get('submitted_at', ''),
            reverse=True
        )

        total_feedback = len(items)

        positive_count = sentiment_counts.get('POSITIVE', 0)
        negative_count = sentiment_counts.get('NEGATIVE', 0)
        mixed_count = sentiment_counts.get('MIXED', 0)

        satisfaction_rate = 0

        if total_feedback > 0:
            satisfaction_rate = round(
                (positive_count / total_feedback) * 100,
                1
            )

        contributor_counter = Counter()

        for item in items:
            contributor_counter[item.get('name', 'Anonymous')] += 1

        top_contributors = contributor_counter.most_common(5)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps(
                {
                    "total_feedback": total_feedback,
                    "sentiment_breakdown": {
                        "POSITIVE": positive_count,
                        "NEGATIVE": negative_count,
                        "MIXED": mixed_count
                    },
                    "satisfaction_rate": satisfaction_rate,
                    "top_contributors": top_contributors,
                    "feedback_history": feedback_history
                },
                cls=DecimalEncoder
            )
        }

    except Exception as error:

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": str(error)
            })
        }
