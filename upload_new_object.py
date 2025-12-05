import boto3       

s3 = boto3.client('s3')

s3.put_object(Bucket="dono-boto3-41225", 
              Key="folder/foldera/folder1/test_text_string.txt",
              Body="Hey thid is a string", 
              ContentType="text/plain")