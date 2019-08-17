import boto3

if __name__ == "__main__":

     collectionId='MyCollection'
     threshold = 50
     maxFaces=2
     faceId='b88fea95-b567-4754-b361-5977451c749d' #faceId='xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
	 
     client=boto3.client('rekognition')
     response=client.search_faces(CollectionId=collectionId,FaceId=faceId,FaceMatchThreshold=threshold,MaxFaces=maxFaces)
	 
     faceMatches=response['FaceMatches']
     print ('Matching faces')
     for match in faceMatches:
         print ('FaceId:' + match['Face']['FaceId'])
         print ('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")
         print