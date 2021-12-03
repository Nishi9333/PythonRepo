import boto3

role=iam.get_role(RoleName="r1nishi03dec")
print("============")
print(role["Role"]["Arn"])
print("==============")
lambdaClient=boto3.client("lambda")
zipped_code=""

with open("lambda.zip","rb") as f:
    zipped_code=f.read()
print("======zipped code created========")

response=lambdaClient.create_function(
    FunctionName="nishifunc",
    Runtime="pyton3.8",
    Role=role["Role"]["Arn"],
    Handler="handler.lambda_handler"
    Code=dict(ZipFile=zipped_code),
    Timeout=300
)

print(response)