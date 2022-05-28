"""Code to upload file to S3."""

import os
import secrets
import string

import boto3
from dotenv import load_dotenv

load_dotenv()
ACCESS_KEY = os.getenv('ACCESS_KEY')
SECRET_ACCESS_KEY = os.getenv('SECRET_ACCESS_KEY')


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
        client = boto3.client('s3',
                            aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_ACCESS_KEY,
                            )
        client.upload_fileobj(in_mem_file, bucket_name, file_key)
        return True
    except:
        return False

def main():
    """Print a hello message from the current file."""
    print(f'Hello, from {__name__}')


if __name__ == '__main__':
    main()
