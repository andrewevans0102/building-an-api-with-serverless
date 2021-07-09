import os
import json
import logging
import boto3
from boto3.dynamodb.conditions import Key
import traceback
dynamodb = boto3.resource('dynamodb')

def delete(event, context):
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

        # delete the todo from the database
        table.delete_item(
            Key={
                'username': data["username"]
            }
        )

        response = {
            "statusCode": 200,
            "headers": {'Access-Control-Allow-Origin': '*'},
            "body": str("delete successful for meals " + data["username"])
        }
    except NameError as nameError:
        nameBody = str("Name error: {0}".format(nameError))
        response = {
            "statusCode": 500,
            "headers": {'Access-Control-Allow-Origin': '*'},
            "body": nameBody
        }
    except:
        errorBody = traceback.format_exc()
        response = {
            "statusCode": 500,
            "headers": {'Access-Control-Allow-Origin': '*'},
            "body": errorBody
        }

    return response