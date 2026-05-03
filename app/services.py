import uuid
import json
import boto3
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tickets = []

sqs = boto3.client("sqs", region_name="us-east-1")

QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/867490540509/ticket-events-queue"

def send_ticket_event(ticket):
    message = {
        "event_type": "ticket_created",
        "ticket": ticket
    }

    response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        MessageBody=json.dumps(message)
    )

    logger.info(f"Sent ticket event to SQS for ticket id={ticket['id']}")

    return response

def create_ticket_service(ticket):
    new_ticket = {
        "id": str(uuid.uuid4()),
        "title": ticket.title,
        "description": ticket.description,
        "status": "created"
    }

    tickets.append(new_ticket)

    send_ticket_event(new_ticket)

    logger.info(f"Created ticket id={new_ticket['id']}")

    return {
        "message": "Ticket created and event sent",
        "ticket": new_ticket
    }