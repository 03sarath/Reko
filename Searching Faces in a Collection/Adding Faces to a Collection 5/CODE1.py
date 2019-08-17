import boto3

if __name__ == "__main__":

    bucket='rek20052019'
    collectionId='MyCollection'
    photo='images.jpg'
	
    client=boto3.client('rekognition')
	
    response=client.index_faces(CollectionId=collectionId,Image={'S3Object':{'Bucket':bucket,'Name':photo}},ExternalImageId=photo,MaxFaces=1,QualityFilter="AUTO",DetectionAttributes=['ALL'])
    print ('Results for ' + photo)
    print('Faces indexed:')
    for faceRecord in response['FaceRecords']:
        print(' Face ID: ' + faceRecord['Face']['FaceId'])
        print(' Location: {}'.format(faceRecord['Face']['BoundingBox']))
    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print(' ' + reason)