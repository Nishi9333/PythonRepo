import boto3

#ec2=boto3.resource("ec2")
#key_pair=ec2.KeyPair("NishiKeyPair")
#print(key_pair)



ec2=boto3.client("ec2")
myKeyName="nishikeypair1"
response=ec2.create_key_pair(KeyName=myKeyName)
with open(myKeyName+".pem","w") as f:
    f.write(response["KeyMaterial"])
print(response)