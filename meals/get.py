import os
import json
import logging
from meals import decimalencoder
import boto3
from boto3.dynamodb.conditions import Key
import traceback
dynamodb = boto3.resource('dynamodb')

def get(event, context):
    response = {}
    try:        
        # select data
        data = json.loads(event['body'])
        # reference table
        table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        
        # if username not in body then raise exception
        if 'username' not in data:
            logging.error("Validation Failed")
            raise NameError("username is not provided")

        result = table.query(
            KeyConditionExpression=Key('username').eq(data["username"])
        )

        response = {
            "statusCode": 200,
            "headers": { 'Access-Control-Allow-Origin': '*' },
            "body": json.dumps(result['Items'],
                            cls=decimalencoder.DecimalEncoder)
        }
    except NameError as nameError:
        nameBody = str("Name error: {0}".format(nameError))
        response = {
            "statusCode": 500,
            "headers": { 'Access-Control-Allow-Origin': '*' },
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