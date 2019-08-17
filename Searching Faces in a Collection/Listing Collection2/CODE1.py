
import boto3

if __name__ == "__main__":

      maxResults=2
	  
      client=boto3.client('rekognition')
	  
      #Display all the collections
      print('Displaying collections...')
      response=client.list_collections(MaxResults=maxResults)
	   
      while True:
           collections=response['CollectionIds']
		   
           for collection in collections:
               print (collection)
           if 'NextToken' in response:
               nextToken=response['NextToken']
		   
               response=client.list_collections(NextToken=nextToken,MaxResults=maxResults)

           else:
                break
      print('done...')
	  
	  
	  
	  
	  