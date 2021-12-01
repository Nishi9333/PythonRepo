import boto3
bucketName="nishibucket93333"
s3resource=boto3.resource("s3")
Bucket=s3resource.Bucket(bucketName)

def cleanup_bucket_objects(myBucket):
    #delete all objects
    for obj in myBucket.objects.all():
        obj.delete()
        #print(obj)


    #if object has versions with objects
    for objVer in myBucket.object_versions.all():
        objVer.delete()
    
#delete all objects from bucket
cleanup_bucket_objects(Bucket)

#delete an empty bucket
Bucket.delete()

