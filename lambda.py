"""The lambda function used."""

import json
import urllib.error
import urllib.parse
import urllib.request

import boto3

print('Loading function')

RES_BUCKET = 'viztranz-results'
LANGS = ['bg', 'de', 'ru']

s3 = boto3.client('s3')
translate = boto3.client('translate')
rekognition = boto3.client('rekognition')


def detect_labels(bucket, key):
    """Call rekognition DetectLabels API to detect labels in S3 object."""
    response = rekognition.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": key}}
    )

    to_translate = {d['Name']: d['Confidence']
                    for d in response['Labels']}

    return to_translate


def translate_text(text, lang_code):
    """Call the `Translate` API and get translations."""
    result = translate.translate_text(
        Text=text,
        SourceLanguageCode='en',
        TargetLanguageCode=lang_code
    )

    return result['TranslatedText']


def do_translate(to_translate):
    """Add translations to detected objects."""
    with_translations = {
        word: [conf] + [translate_text(word, code) for code in LANGS]
        for (word, conf) in to_translate.items()
    }

    return with_translations


def upl_to_s3(bucket, res, key):
    """Upload the translations along with the confidence levels to S3."""
    to_upload_bytes = bytes(json.dumps(res).encode('UTF-8'))
    s3.put_object(Bucket=bucket, Key=key, Body=to_upload_bytes)


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """Parse the S3 image, call Rekognition API and Translate API, and return result."""
    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

    try:
        to_translate = detect_labels(bucket, key)

        with_translations = do_translate(to_translate)

        upl_to_s3(RES_BUCKET, with_translations, key)

        return with_translations
    except Exception as e:
        print(e)
        print("Error processing object {} from bucket {}. ".format(key, bucket) +
              "Make sure your object and bucket exist and your bucket is in the same region as this function.")
        raise e
