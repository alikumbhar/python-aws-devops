import boto3

s3 = boto3.resource('s3')

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name, 'rb') # reading binary file
    s3.Bucket(bucket_name).put_object(Key=key_name,Body=data) # out_object you can put your data for uploading
    print("backup uploaded...")    


file_name = r'C:\Users\PMLS\Desktop\python\ebackups\backup_2025-05-20.tar.gz'
bucket_name = 'tes-12ali'
key_name = 'my_backup.tar.gz'
upload_backup(s3,file_name,bucket_name,key_name)