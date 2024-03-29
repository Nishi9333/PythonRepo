import  boto3
#from botocore.exceptions import ClientError

def fnCreateDefaultVPC(vpcResource,IpCidr):
    from botocore.exceptions import ClientError
    vpcId="Notset"
    try:
        response=vpcResource.create_vpc(CidrBlock=IpCidr,
        InstanceTenancy="default",
        TagSpecifications=[{"ResourceType":"vpc","Tags":[{'Key':'Name','Value':'nishivpc933'}]}]
        )
        vpcId=response.id
        print("create custom  default vpc")
    except ClientError as ce:
        print("not created custom vpc",ce)
    return vpcId

#Driver Code-workflow
if __name__=="__main__":
    vpcresource=boto3.resource("ec2")
    ip_cidr="192.169.1.0/26"
    vpcId=fnCreateDefaultVPC(vpcresource, ip_cidr)
    print(vpcId)
