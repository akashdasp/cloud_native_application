import boto3
ecr_client = boto3.client('ecr')

repository_name= 'my_cloud_native_repository'
response=ecr_client.create_repository(repositoryName=repository_name)
respository_uri= response['repository']['repositoryUri']
print(respository_uri)
