import boto3
import io
from PIL import Image, ImageDraw, ExifTags, ImageColor

if __name__ == "__main__":

    bucket="rek20052019"
    photo="sharat copy.jpg"
    client=boto3.client('rekognition')
	
    # Load image from S3 bucket
    s3_connection = boto3.resource('s3')
    s3_object = s3_connection.Object(bucket,photo)
    s3_response = s3_object.get()
	
    stream = io.BytesIO(s3_response['Body'].read())
    image=Image.open(stream)
	
    #Call DetectFaces
    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name':photo}},
       Attributes=['ALL'])
	   
    imgWidth, imgHeight = image.size
    draw = ImageDraw.Draw(image)
	
    # calculate and display bounding boxes for each detected face
    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
         print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])+ ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
		 
    box = faceDetail['BoundingBox']
    left = imgWidth * box['Left']
    top = imgHeight * box['Top']
    width = imgWidth * box['Width']
    height = imgHeight * box['Height']
	
    print('Left: ' + '{0:.0f}'.format(left))
    print('Top: ' + '{0:.0f}'.format(top))
    print('Face Width: ' + "{0:.0f}".format(width))
    print('Face Height: ' + "{0:.0f}".format(height))
	
    points = (
        (left,top),
        (left + width, top),
        (left + width, top + height),
        (left , top + height),
        (left, top)
)
draw.line(points, fill='#00d400', width=2)
# Alternatively can draw rectangle. However you can't set line width.
#draw.rectangle([left,top, left + width, top + height], outline='#00d400')
image.show()