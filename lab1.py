import boto3
client = boto3.client('s3')
buckets = client.list_buckets()
for bucket in buckets["Buckets"]:
    print(bucket["Name"])