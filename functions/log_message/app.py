import json
import os

def log_message(event, context):
    # Extract event detail from event object
    detail = event["detail"]

    # Extract messages from event detail
    messages = detail['messages']

    # Log Message (View in CloudWatch Log)
    for message in messages:
      print(message)
