import  boto3
#from botocore.exceptions import ClientError

def fnCreateDefaultVPC(vpcClient):
    from botocore.exceptions import ClientError
    try:
        response=vpcclient.create_default_vpc()
        vpcId=response["Vpc"]["VpcId"]
        print("create default vpc")
    except ClientError:
        print("not created")

#Driver Code-workflow
if __name__=="__main__":
    vpcclient=boto3.client("ec2")
    vpcId=fnCreateDefaultVPC(vpcclient)
    print(vpcId)
