import boto3

if __name__ == "__main__":

     sourceFile='Robert.jpg'
     targetFile='thor.jpg'
     client=boto3.client('rekognition')
	  
     imageSource=open(sourceFile,'rb')
     imageTarget=open(targetFile,'rb')
	  
     response=client.compare_faces(SimilarityThreshold=70,SourceImage={'Bytes': imageSource.read()},TargetImage={'Bytes': imageTarget.read()})
     for faceMatch in response['FaceMatches']:
          position = faceMatch['Face']['BoundingBox']
          similarity = str(faceMatch['Similarity'])
          print('The face at ' + str(position['Left']) + ' ' +str(position['Top']) +' matches with ' + similarity + '% confidence')
     imageSource.close()
     imageTarget.close()