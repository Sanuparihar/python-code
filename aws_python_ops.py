#login to aws  search "IAM" user->sanu-> security cred-> access key->ceate accesss key->CLI->create access
# pip istall boto3 (aws library)SDK
# instal aws cli
# aws cofigure
import boto3
s3 = boto3.resource('s3')
ec2 =boto3.resource(ec2)
print (s3.buckets.all())


for bucket in s3.buckets.all():
    print(bucket)
    c=c+1
print(c)
s3.bucket("bucket name").downlload_file("flename in S3 bucket")
