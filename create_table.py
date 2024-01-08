import boto3
from botocore.exceptions import ClientError
import logging

logger = logging.getLogger(__name__)

class Books:

	def __init__(self, dynamodb):
		self.dynamodb = dynamodb
		self.table = None

	def create_books_table(self, table_name=None):
		try:
			self.table = self.dynamodb.create_table(
				TableName=table_name,
				KeySchema=[
					{
						'AttributeName': 'book_id',
						'KeyType': 'HASH'  # Partition key
					},
					{
						'AttributeName': 'title',
						'KeyType': 'RANGE'  # Sort key
					}
				],
				AttributeDefinitions=[
					{
						'AttributeName': 'book_id',
						# AttributeType refers to the data type 'N' for number type and 'S' stands for string type.
						'AttributeType': 'N'
					},
					{
						'AttributeName': 'title',
						'AttributeType': 'S'
					},
				],
				ProvisionedThroughput={
					'ReadCapacityUnits': 10,
					'WriteCapacityUnits': 10
				}
			)
			print("Creating table...")
			self.table.wait_until_exists()
			
		except ClientError as err:
			logger.error(
                "Couldn't create table %s. Here's why: %s: %s", table_name,
                err.response['Error']['Code'], err.response['Error']['Message'])
			raise
		else:
			print(self.table)
			return self.table


if __name__ == '__main__':
	dynamodb = boto3.resource('dynamodb')
	book_table = Books(dynamodb)
	table_name = "Books"
	try:
		book_table.create_books_table(table_name)
	except Exception as e:
		print(e)
	else:
		print(f"Table {table_name} created successfully")
		