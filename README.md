# Event-Driven Ticket Notification System

A cloud-based event-driven system built with Python, FastAPI, Amazon SQS, AWS Lambda, and Amazon SNS. When a ticket is created through the API, an event message is sent to SQS, processed asynchronously by a Lambda worker, and delivered as an email notification through SNS.

## Architecture

Client → FastAPI → Amazon SQS → AWS Lambda → Amazon SNS → Email

## Features

- Create ticket events through a REST API
- Send ticket-created events to Amazon SQS
- Process SQS messages asynchronously with AWS Lambda
- Send email notifications through Amazon SNS
- Logging for event processing and debugging

## Tech Stack

- Python
- FastAPI
- boto3
- Amazon SQS
- AWS Lambda
- Amazon SNS
- CloudWatch Logs

## API Endpoint

### POST /tickets

Creates a ticket and sends an event to SQS.

Example request:

```json
{
  "title": "Delayed baggage",
  "description": "Customer baggage did not arrive on time"
}