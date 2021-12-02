import boto3

ec2=boto3.resource("ec2")
keyPairName="nishikeypair1"
imageId="ami-0ed9277fb7eb570c9"

instance=ec2.create_instances(
    MinCount=1,
    MaxCount=1,
    ImageId=imageId,
    InstanceType="t2.micro",
    KeyName=keyPairName,
    TagSpecifications=[{
        "ResourceType":"instance",
        "Tags":[{
            "Key":"Name",
            "Value":"Nishiinstance"
        }]
    }]
)

for instance in instance:
    print("Instance Created with id as: ",instance.id)

    instance.wait_until_running()
    print("started")

