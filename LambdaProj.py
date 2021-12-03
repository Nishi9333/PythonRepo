import boto3
import os
s3=boto3.client("s3")
AWS_REGION=os.environ["RC"]
print("you pass RC: ",AWS_REGION)
bucketName="nishibucketproj"
response=s3.create_bucket(Bucket=bucketName)
print("check: aws s3 ls")