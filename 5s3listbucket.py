import boto3
s3=boto3.client("s3")
response=s3.list_buckets()
for b in response["Buckets"]:
    if("bkt" in b["Name"]):
        print(b["Name"])
    #print(b ["Name"], end=" ")
