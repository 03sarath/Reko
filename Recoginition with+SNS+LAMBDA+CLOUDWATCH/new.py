from __future__ import print_function
 
import boto3
from decimal import Decimal
import json
import urllib
 
print('Loading function')
 
rekognition = boto3.client('rekognition')
client = boto3.client('sns')
 
def detect_labels(bucket, key):
response = rekognition.detect_labels(Image={&quot;S3Object&quot;: {&quot;Bucket&quot;: bucket, &quot;Name&quot;: key}})
 
return response
 
# --------------- Main handler ------------------
 
def lambda_handler(event, context):
 
print (event)
 
      bucket = event['Records'][0]['s3']['bucket']['name']
      key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
try:
 
# Calls rekognition DetectLabels API to detect labels in S3 object
     response = detect_labels(bucket, key)
 
     message = client.publish(TargetArn='arn:aws:sns:us-east-1:923307152276:Reko', Message='String' ,Subject='Uploaded Image Labels')
 
return &quot;hello&quot;
except Exception as e:
print(e)
print(&quot;Error processing object {} from bucket {}. &quot;.format(key, bucket) +
&quot;Make sure your object and bucket exist and your bucket is in the same region as this function.&quot;)
raise e