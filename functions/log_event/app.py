import json
import os

def log_event(event, context):
    # Extract event detail from event object
    detail = event["detail"]

    print(detail)
