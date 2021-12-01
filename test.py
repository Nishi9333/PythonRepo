s3Client=boto3.client("s3")
response=s3Client.OperationName(Options)
result=response["data"]

ec2Resource=boto3.resource("ec2")
ec2Resource.instances.all()[0].status

session=boto3.session(AK,SAK,RC)
s3Clienr=session.client("s3")
ec2Resource=session.resource("ec2")