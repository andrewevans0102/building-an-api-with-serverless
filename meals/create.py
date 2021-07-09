import os
import json
import logging
from meals import decimalencoder
import boto3
import traceback
import time
dynamodb = boto3.resource('dynamodb')

initialMeals = [
    {
        "day": "0",
        "breakfast": "",
        "lunch": "",
        "dinner": ""
    },
    {
        "day": "1",
        "breakfast": "",
        "lunch": "",
        "dinner": ""
    },
    {
        "day": "2",
        "breakfast": "",
        "lunch": "",
        "dinner": ""
    },
    {
        "day": "3",
        "breakfast": "",
        "lunch": "",
        "dinner": ""
    },
    {
        "day": "4",
        "breakfast": "",
        "lunch": "",
        "dinner": ""
    },
    {
        "day": "5",
        "breakfast": "",
        "lunch": "",
        "dinner": ""
    },
    {
        "day": "6",
        "breakfast": "",
        "lunch": "",
        "dinner": ""
    }
]

def create(event, context):
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
        
        timestamp = int(time.time() * 1000)

        # create initial set of meals and then return
        item = {
            'username': data["username"],
            'meals': initialMeals,
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }

        # write the todo to the database
        table.put_item(Item=item)

        response = {
            "statusCode": 200,
            "headers": {'Access-Control-Allow-Origin': '*'},
            "body": json.dumps(item['meals'],
                                cls=decimalencoder.DecimalEncoder)
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
