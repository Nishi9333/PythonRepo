import boto3
import json
test_event={
    "name": "nishi",
    "key2": "value2",
    "key3": "value3"
}

lambdaClient=boto3.client("lambda")

response=lambdaClient.invoke(Functionname="nishifndec03",Payload=json.dumps(test_events))

print(response["Payload"])
print(response["Payload"].read().decode("uft-8"))