import json
import boto3

clientobj=boto3.client('sts')
response=clientobj.get_caller_identity()
userId= response["UserId"]
account=response['Account']
arn=response['Arn']
output={
    "UserId":userId,
    "Account":account,
    "Arn":arn
}

print(json.dumps(output, indent=4))