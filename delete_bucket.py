import boto3

s3 = boto3.client('s3')

Bucket="dono-boto3-41225"
respionse = s3.delete_bucket(
 )