import os
import boto3

import string
import secrets

from dotenv import load_dotenv

load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')


def gen_name(name_len=16):
    alphabet = string.ascii_letters + string.digits
    name = ''.join(secrets.choice(alphabet) for _ in range(name_len))
    return name


def upload(in_mem_file):
    bucket_name = 'viztranz'
    file_key = f'im_{gen_name()}'

    client = boto3.client('s3',
                          aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_ACCESS_KEY,
                          )

    client.upload_fileobj(in_mem_file, bucket_name, file_key)
    print('upload successful??')


def main():
    print('Hello, world!')


if __name__ == '__main__':
    main()
