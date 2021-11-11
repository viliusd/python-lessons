import boto3
client = boto3.client('s3')
f= open('dist/pgbackup-0.1.0-py3-none-any.whl', 'rb')
client.upload_fileobj(f, 'vilius-testing-py-lesson', 'pgbackup-0.1.0-py3-none-any.whl')