import boto3
import logging

#logger Config
logger=logging.getLogger()
logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s: %(message)s')

vpcClient=boto3.client("ec2")

def fnVPCDelete(vpcId):
    from botocore.exceptions import ClientError
    vpc=None
    try:
        vpc=vpcClient.delete_vpc(VpcId=vpcId)
        logger.info("lists vpcs")
        
    except ClientError as ce:
        print("Found Error: ",ce)
        logger.exception("not done")
    return vpc

#Driver Code- Workflow
if __name__=="__main__":
    vpc=fnVPCDelete(vpcId="vpc-0d9e15d64ffcc8abb")    
    print("deleted")