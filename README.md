# ☁️ Koufie AI Feedback Hub

An AI-powered customer feedback intelligence platform built using AWS serverless services.

---

## 📌 Project Overview

Koufie AI Feedback Hub enables customers to submit feedback through a responsive web application hosted on Amazon S3.

The platform automatically analyzes customer sentiment using Amazon Comprehend and stores feedback records in DynamoDB.

An analytics dashboard provides real-time insights into customer satisfaction, sentiment trends, and feedback history.

---

## 🚀 Features

### Customer Feedback Portal

- Submit feedback through a modern web interface
- Real-time sentiment analysis
- Automatic sentiment classification
- Responsive design
- Secure API integration

### Analytics Dashboard

- Total Feedback Count
- Positive Feedback Tracking
- Negative Feedback Tracking
- Mixed Feedback Tracking
- Customer Satisfaction Rate
- Top Contributors
- Feedback History
- Search and Filter Feedback
- CSV Export
- Real-Time Dashboard Refresh

---

## 🏗 Architecture

```text
Customer
    │
    ▼
Amazon S3 Static Website
    │
    ▼
Amazon API Gateway
    │
    ▼
AWS Lambda
    │
    ├──────────────► Amazon Comprehend
    │                     │
    │                     ▼
    │              Sentiment Analysis
    │
    ▼
Amazon DynamoDB
    │
    ▼
Analytics Dashboard
```

---

## ☁️ AWS Services Used

- Amazon S3
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Comprehend
- AWS IAM

---

## 📊 Sentiment Analysis Flow

1. Customer submits feedback.
2. API Gateway receives the request.
3. Lambda processes the request.
4. Amazon Comprehend analyzes sentiment.
5. Sentiment and metadata are stored in DynamoDB.
6. Dashboard retrieves data through a Stats API.
7. Dashboard visualizes insights and trends.

---

## 🔌 API Endpoints

### Submit Feedback

```http
POST /feedback
```

### Retrieve Dashboard Statistics

```http
GET /stats
```

---

## 📄 Sample Response

```json
{
  "total_feedback": 7,
  "sentiment_breakdown": {
    "POSITIVE": 4,
    "NEGATIVE": 2,
    "MIXED": 1
  }
}
```

---

## 📁 Repository Structure

```text
koufie-ai-feedback-hub
│
├── index.html
├── dashboard.html
│
├── lambda
│   ├── feedback_lambda.py
│   └── stats_lambda.py
│
└── README.md
```

---

## 🎯 Skills Demonstrated

- AWS Serverless Architecture
- REST API Development
- Amazon Comprehend Integration
- DynamoDB Data Modeling
- Cloud Security & IAM
- Frontend Development
- Data Visualization
- Cloud Monitoring
- API Design

---

## 👨‍💻 Author

Eric Koufie

AWS Cloud Engineering Portfolio Project

---

## 📈 Future Improvements

- Authentication with Amazon Cognito
- Historical Trend Analysis
- Advanced Dashboard Analytics
- Automated Email Alerts
- Amazon QuickSight Integration
- Machine Learning Insights
