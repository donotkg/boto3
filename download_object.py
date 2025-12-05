import boto3
s3 = boto3.client('s3')

s3.download_file('dono-boto3-41225', 'test_text.txt', 'test_text.txt')