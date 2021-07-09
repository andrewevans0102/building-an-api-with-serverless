import json
import time
import logging
import os
from meals import decimalencoder
import boto3
import traceback
dynamodb = boto3.resource('dynamodb')

def update(event, context):
    response = {}
    
    try:        
      data = json.loads(event['body'])
      if 'username' not in data:
          logging.error("Validation Failed")
          raise NameError("username was not present in request")
      if 'meals' not in data:
          logging.error("Validation Failed")
          raise NameError("meals was not present in request")

      timestamp = int(time.time() * 1000)

      table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

      # update the todo in the database
      table.update_item(
          Key={
            'username': data["username"],
          },
          ExpressionAttributeNames={
            '#meal_save': 'meals',
          },
          ExpressionAttributeValues={
            ':meals': data['meals'],
            ':updatedAt': timestamp,
          },
          UpdateExpression='SET #meal_save = :meals, '
                          'updatedAt = :updatedAt',
          ReturnValues='ALL_NEW',
      )

      # create a response
      response = {
          "statusCode": 200,
          "headers": { 'Access-Control-Allow-Origin': '*' },
          "body": json.dumps(data['meals'],
                            cls=decimalencoder.DecimalEncoder)
      }

    except NameError as nameError:
        nameBody = str("Name error: {0}".format(nameError))
        response = {
            "statusCode": 500,
            "headers": { 'Access-Control-Allow-Origin': '*'},
            "body": nameBody
        }
    except:
        errorBody = traceback.format_exc()
        response = {
            "statusCode": 500,
            "headers": { 'Access-Control-Allow-Origin': '*' },
            "body": errorBody
        }

    return response
