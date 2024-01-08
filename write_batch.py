import json 
from decimal import Decimal
import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)


def load_batch(books, dynamodb):
    
	book_table = dynamodb.Table('Books')
    
	try:
		with book_table.batch_writer() as writer:
			for book in books:
				writer.put_item(Item=book)
	except ClientError as err:
		logger.error(
			"Couldn't load data into table %s. Here's why: %s: %s", book_table.name,
			err.response['Error']['Code'], err.response['Error']['Message'])
		raise
	# for book in books:
    #     book_id = book['book_id']
    #     title = book['title']
    #     book_table.put_item(Item=book)
    

if __name__ == '__main__':
	try:
		with open("book_data.json") as book_file:
			book_data = json.load(book_file, parse_float=Decimal)
		load_batch(book_data, boto3.resource('dynamodb'))
	except Exception as e:
		print(e)
	else:
		print("Operation Successful")