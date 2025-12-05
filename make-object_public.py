import boto3

s3 = boto3.client('s3')

response = s3.put_object_acl(ACL='public-read', 
                             Bucket="dono-boto3-41225", 
                             Key="test_text_string.txt")

print(response)