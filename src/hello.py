import logging
from twilio.twiml.messaging_response import MessagingResponse

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    resp = MessagingResponse()
    resp.message("Hello, sir. I have awoken")

    logger.info('Testing')

    return {
      'statusCode': 200,
      'body': str(resp) 
    }
