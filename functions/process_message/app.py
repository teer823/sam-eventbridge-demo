import datetime
import json
import os
import random
import boto3
# import requests

event_bus_name = os.environ['EVENT_BUS_NAME']
detail_type = os.environ['EVENT_DETAIL_TYPE']
client = boto3.client('events')

def process_message(event, context):
    
    # Extract event detail from event object
    detail = event["detail"]

    processed_messages = []

    # Convert Message
    for message in detail['messages']:
      processed_messages.append({
          'type': 'text',
          'text': 'UserId {0} sent message => \"{1}\"'.format(message['userId'], message['text'])
        })

    # Create Event Entry
    payload = json.dumps(
      {
        'messages': processed_messages
      })

    entry = {
      'Time': datetime.datetime.now(),
      'Source': 'process_message_function',
      'Resources': [],
      'DetailType': detail_type,
      'Detail': payload,
      'EventBusName': event_bus_name
    }
    
    # Publish Event to EventBridge
    response = client.put_events(
      Entries=[entry,]
    )
    print(response)
