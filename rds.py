import boto3

client = boto3.client('rds')
response = client.create_db_cluster_snapshot(
    DBClusterSnapshotIdentifier='my-cluster-snapshot-test',
    DBClusterIdentifier='ccc-urms-staging',
    Tags=[
        {
            'Key': 'NAME',
            'Value': 'my-cluster-snapshot-test'
        },
    ]
)
print(response)