import boto3

vpcClient=boto3.client("ec2")

sgId="sg-0876fcca126a62145"
IPPort={
    "IpProtocol":"tcp",
    "FromPort":22,
    "ToPort":22,
    "IpRanges":[{"CidrIp":"0.0.0.0/0"}]
    }
response=vpcClient.authorize_security_group_ingress(
    GroupId=sgId,
    IpPermissions=[IPPort]
)
import json
print(json.dumps(response,indent=4))