# sam-eventbridge-demo

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- **functions/new_message** - Code for the application's Lambda function to receive new message, receive the following JSON content
  ```
  {
    "messages": [
        {
            "userId": "user1",
            "text": "hello"
        },
        {
            "userId": "user2",
            "text": "hi everybody"
        }
    ]
  }
  ```
- **functions/process_message** - Code for the application's Lambda function to re-format received message
- **functions/log_message** - Code for the application's Lambda function to log re-formated message
- functions/log_event  - Code for the application's Lambda function to log event data
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions, an API Gateway API and EventBus from EventBridge. These resources are defined in the `template.yaml` file in this project.

## Validate Build and Deploy the demo application
To build and deploy the demo application, you need to [install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) on your machine and run the following commands
```bash
  sam validate
  sam build
  sam deploy -g
```