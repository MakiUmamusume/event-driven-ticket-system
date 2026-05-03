import json

def lambda_handler(event, context):
    print("Received event:")
    print(json.dumps(event))

    for record in event["Records"]:
        message_body = json.loads(record["body"])

        event_type = message_body.get("event_type")
        ticket = message_body.get("ticket", {})

        print(f"Processing event type: {event_type}")
        print(f"Ticket ID: {ticket.get('id')}")
        print(f"Ticket Title: {ticket.get('title')}")
        print(f"Ticket Description: {ticket.get('description')}")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "SQS messages processed successfully"
        })
    }