from json import dumps

def handler(event, context):
    return {
      'statusCode': 200,
      'body': dumps({ 'hello': 'world!!!' })
    }
