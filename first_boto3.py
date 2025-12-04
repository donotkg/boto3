import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='dono-boto3-41225'
)

print(response)