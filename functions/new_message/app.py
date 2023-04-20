import datetime
import json
import os
import time
import boto3

# import requests

event_bus_name = os.environ['EVENT_BUS_NAME']
detail_type = os.environ['EVENT_DETAIL_TYPE']
client = boto3.client('events')


def new_message(event, context):
    # Extract event body from API call
    eventBody = json.loads(event["body"])

    # Create EventBridge event entry
    entry = {
      'Time': datetime.datetime.now(),
      'Source': 'new_message_function',
      'Resources': [],
      'DetailType': detail_type,
      'Detail': json.dumps(eventBody),
      'EventBusName': event_bus_name
    }

    # Send event to EventBridge
    response = client.put_events(
      Entries=[entry,]
    )
    print(response)

    #Check result from HTTPStatusCode
    httpStatusCode = response['ResponseMetadata']['HTTPStatusCode']
    return {
      "statusCode": httpStatusCode,
      "body": json.dumps(response)
    }
      
