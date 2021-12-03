import boto3
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table("Nishidb")

def insertItem(item):
    response=table.put_iten(Item=item)
    return response

def insertItems(items):
    with table.batch_writer() as b:
        b.put_item(Item=items[0])
        b.put_item(Item=items[1])
        print(b)

def getItem(ky):
    response=table.get_item(Key=ky)
    return response["Item"]

def getAllScan():
    response=table.scan()
    return response

def deleteItem(item):
    response=table.delete_item(Key=item)
    return response

def getName(name):
    from boto3.dynamodb.conditions import Key
    response=table.query(KeyConditionExpression=Key("Name").eq("Nishi"))
    return response