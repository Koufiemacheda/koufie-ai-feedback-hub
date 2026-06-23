# ☁️ Koufie AI Feedback Hub

An AI-powered customer feedback intelligence platform built using AWS serverless services.

---

## 🌐 Live Demo

### Customer Feedback Portal

https://d11fvyfw0evhbn.cloudfront.net

### Analytics Dashboard

https://d11fvyfw0evhbn.cloudfront.net/dashboard.html

---

## 📌 Project Overview

Koufie AI Feedback Hub is a serverless AI-powered customer feedback intelligence platform built on AWS.

The application allows customers to submit feedback through a responsive web interface hosted on Amazon S3 and accelerated globally using Amazon CloudFront.

Feedback is processed through Amazon API Gateway and AWS Lambda, where Amazon Comprehend performs sentiment analysis before results are stored in Amazon DynamoDB.

A real-time analytics dashboard provides visibility into customer sentiment trends, customer satisfaction metrics, contributor activity, and feedback history.

---

## 🚀 Features

### Customer Feedback Portal

- Submit customer feedback
- Real-time sentiment analysis
- Automatic sentiment classification
- Responsive user interface
- CloudFront-powered content delivery
- Secure API integration

### Analytics Dashboard

- Total Feedback Count
- Positive Sentiment Tracking
- Negative Sentiment Tracking
- Mixed Sentiment Tracking
- Customer Satisfaction Metrics
- Top Contributors Analysis
- Feedback History Search
- Feedback Filtering
- CSV Export
- Real-Time Dashboard Refresh

---

## 🏗 Architecture

```text
Customer
    │
    ▼
Amazon CloudFront CDN
    │
    ▼
Amazon S3 Static Website Hosting
    │
    ▼
Amazon API Gateway
    │
    ▼
AWS Lambda
    │
    ├────────► Amazon Comprehend
    │             │
    │             ▼
    │      Sentiment Analysis
    │
    ▼
Amazon DynamoDB
    │
    ▼
Analytics Dashboard
```

---

## ☁️ AWS Services Used

- Amazon CloudFront
- Amazon S3
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Comprehend
- AWS IAM

---

## 📊 Sentiment Analysis Workflow

1. Customer submits feedback.
2. API Gateway receives the request.
3. Lambda processes the feedback.
4. Amazon Comprehend performs sentiment analysis.
5. Results are stored in DynamoDB.
6. Dashboard retrieves statistics through a GET API endpoint.
7. Dashboard visualizes customer insights and trends.

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

## 📄 Sample API Response

```json
{
  "total_feedback": 7,
  "sentiment_breakdown": {
    "POSITIVE": 4,
    "NEGATIVE": 2,
    "MIXED": 1
  },
  "satisfaction_rate": 57.1
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
- Amazon CloudFront CDN
- REST API Development
- Amazon Comprehend Integration
- DynamoDB Data Modeling
- Frontend Development
- Data Visualization
- Cloud Security & IAM
- Static Website Hosting
- Cloud Application Design

---

## 📈 Future Enhancements

- User Authentication with Amazon Cognito
- Historical Sentiment Trend Analysis
- Email Notifications using Amazon SNS
- Amazon QuickSight Business Intelligence Dashboard
- Machine Learning Recommendations
- Custom Domain with SSL Certificate

---

## 👨‍💻 Author

### Eric Koufie

AWS Cloud Engineering Portfolio Project

GitHub Repository:

https://github.com/Koufiemacheda/koufie-ai-feedback-hub

---

## 🙏 Acknowledgements

This project was developed as part of my cloud engineering learning journey, focusing on AWS serverless technologies, API development, cloud architecture, and real-time analytics solutions.
