import boto3
session = boto3.session.Session()
print(session.region_name)