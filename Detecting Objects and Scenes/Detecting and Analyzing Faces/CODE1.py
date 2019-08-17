import boto3
import json
if __name__ == "__main__":

     photo='bark.jpg'
     bucket='rek20052019'
     client=boto3.client('rekognition')
     response = client.detect_faces(Image={'S3Object':{'Bucket':bucket,'Name':photo}},Attributes=['ALL'])
	 
     print('Detected faces for ' + photo)
     for faceDetail in response['FaceDetails']:
         print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
         print('Here are the other attributes:')
         print(json.dumps(faceDetail, indent=4, sort_keys=True))