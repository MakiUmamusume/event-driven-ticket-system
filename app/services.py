import uuid
import json
import boto3

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

    return {
        "message": "Ticket created",
        "ticket": new_ticket
    }