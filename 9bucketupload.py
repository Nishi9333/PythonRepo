#upload_file(file_name,bucket_name, object_name)        (for binary// upload_fileobj())
import boto3
import pathlib

BASE_DIR=pathlib.Path(__file__).parent.resolve()
bucket_name="nishi9333"
bpath=BASE_DIR.__str__()
file_name=bpath+"\requirements.txt"

#object_name=file_name
object_name="requirementsv1.txt"


s3client=boto3.client("s3")
s3client.upload_file(file_name,bucket_name,object_name)
print("file uploaded")
#s3client.upload_file(r"fullpath")
#s=r"fullpath"
print(file_name)
#print(str(BASE_DIR+"\\"+file_name))
#s3client.upload_file(BASE_DIR+"/"+file_name,bucket_name,object_name)


#print(BASE_DIR)