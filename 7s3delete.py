import boto3

#client--> delete_bucket(), resource --> bucket.delete()
#s3client=boto3.client("s3")

#s3client.delete_bucket(Bucket="")
#print("Bucket deleted")


s3resource=boto3.resource("s3")
bucketNme=input("enter bucket name to delete:")
Bucket=s3resource.Bucket("nishibucket93333")
Bucket.delete()
print("bucket deleted")