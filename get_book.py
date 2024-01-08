import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

def get_book(book_id, book_title):
    dynamodb = boto3.resource('dynamodb')
    books_table = dynamodb.Table('Books')
    try:
        response = books_table.get_item(
            Key={'book_id': book_id, 'title': book_title}
		)
    except ClientError as err:
        logger.error(
			"Couldn't get book %s from table %s. Here's why: %s: %s",
			book_title, books_table.name,
			err.response['Error']['Code'], err.response['Error']['Message'])
        raise err
    else:
        return response
    
if __name__ == "__main__":
    try:
        book = get_book(1007, "The Gods are not to blame")
    except Exception as e:
        print(e)
    else:
        if 'Item' in book:
            print(book['Item'])


