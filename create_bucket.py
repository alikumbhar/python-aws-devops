import boto3

s3 = boto3.resource("s3")
def show_bucket(S3):
    for bucket in s3.buckets.all():
        print(bucket.name)
        
     
def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={
        'LocationConstraint': region
    },)
    print("bucket created successfully")

bucket_name = 'sheryarkumbhar126'
region = 'us-east-2'
create_bucket(s3,bucket_name,region)
show_bucket(s3)
    
