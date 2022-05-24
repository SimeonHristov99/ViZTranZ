# import json

# print('Loading function')


# def lambda_handler(event, context):
#     # 1. Parse out query string params
#     transactionId = event['queryStringParameters']['transactionId']
#     transactionType = event['queryStringParameters']['type']
#     transactionAmount = event['queryStringParameters']['amount']

#     print(f'{transactionId=}')
#     print(f'{transactionType=}')
#     print(f'{transactionAmount=}')

#     # 2. Construct the body of the response object
#     response = {
#         'transactionId': transactionId,
#         'type': transactionType,
#         'amount': transactionAmount,
#         'message': 'Hello from Lambda land!'
#     }

#     # 3. Construct http response object
#     responseObject = {
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json'
#         },
#         'body': json.dumps(response)
#     }

#     # 4. Return the response object
#     return responseObject


import boto3
from decimal import Decimal
import json
import urllib.request
import urllib.parse
import urllib.error

print('Loading function')

rekognition = boto3.client('rekognition')


# --------------- Helper Functions to call Rekognition APIs ------------------

def detect_labels(bucket, key):
    response = rekognition.detect_labels(Image={"S3Object": {"Bucket": bucket, "Name": key}})

    # Sample code to write response to DynamoDB table 'MyTable' with 'PK' as Primary Key.
    # Note: role used for executing this Lambda function should have write access to the table.
    #table = boto3.resource('dynamodb').Table('MyTable')
    #labels = [{'Confidence': Decimal(str(label_prediction['Confidence'])), 'Name': label_prediction['Name']} for label_prediction in response['Labels']]
    #table.put_item(Item={'PK': key, 'Labels': labels})
    return response

# --------------- Main handler ------------------


def lambda_handler(event, context):
    '''Demonstrates S3 trigger that uses
    Rekognition APIs to detect faces, labels and index faces in S3 Object.
    '''
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event
    try:
        # Calls rekognition DetectLabels API to detect labels in S3 object
        response = detect_labels(bucket, key)

        # Print response to console.
        print(response)

        return response
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket) +
              "Make sure your object and bucket exist and your bucket is in the same region as this function.")
        raise e
