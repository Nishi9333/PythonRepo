import boto3

clientobj=boto3.client('iam')
objPaginator=clientobj.get_paginator('list_roles')

#print(type(objPaginator))
#print( objPaginator)

for page in objPaginator.paginate():
    for r in page['Roles']:
        print( r["RoleName"] )
        