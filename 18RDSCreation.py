import boto3

rds=boto3.client("rds")

response=rds.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass="db.t2.micro",
    DBInstanceIdentifier="nishirdsinst",
    Engine="MySQL",
    MasterUserPassword="nishi123",
    MasterUsername="admin123"
)

print(response)