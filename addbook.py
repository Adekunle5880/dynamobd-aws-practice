import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def add_book(table):
	dynamodb = boto3.resource('dynamodb')
	books_table = dynamodb.Table("Books")
	try:
		response = books_table.put_item(
			Item = {
				"book_id": 1007,
				"title": "The Gods are not to blame",
				"author": "Ola Rotimi",
				"ISBN": "0192113723",
				"year_of_publication": "1971"
			}
		)
	except ClientError as err:
		logger.error(
            "Couldn't add book to table %s. Here's why: %s: %s",
            table,
            err.response['Error']['Code'], err.response['Error']['Message'])       
	return response

if __name__ == '__main__':
	try:
		book_resp = add_book(table='Books')
	except Exception as e:
		print(e)
	else:
		print(book_resp)