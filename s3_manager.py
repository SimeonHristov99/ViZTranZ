"""Code to upload file to S3."""

import os
import secrets
import string
from io import BytesIO
from time import sleep

import boto3
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')
BUCKET_RES = os.getenv('BUCKET_RES')

client = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_ACCESS_KEY,
                      )


def gen_name(name_len=16):
    """Generate random name including characters and digits."""
    alphabet = string.ascii_letters + string.digits
    name = ''.join(secrets.choice(alphabet) for _ in range(name_len))
    return name


def upload(in_mem_file):
    """Upload the file to S3."""
    bucket_name = 'viztranz'
    file_key = f'im_{gen_name()}'

    try:
        client.upload_fileobj(in_mem_file, bucket_name, file_key)
        return file_key
    except:
        return None


def get_results(file_name):
    """Return the results from the translation."""
    results = []
    with st.spinner('Translating...'):
        while 'Contents' not in results:
            results = client.list_objects_v2(
                Bucket=BUCKET_RES,
                Prefix=file_name,
                MaxKeys=1
            )
            sleep(3)

    data = client.get_object(Bucket=BUCKET_RES, Key=file_name)
    contents = data['Body'].read()
    result = contents.decode("utf-8")
    return dict(eval(result))
