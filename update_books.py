import boto3

def update_book(book_id, title):
    dynamodb = boto3.resource('dynamodb')
    
    books_table = dynamodb.Table("Books")
    summary = "An adaptation of the Greek classic Oedipus Rex, set in an indeterminate period of a Yoruba kingdom, the story centers on Odewale, who is lured into a false sense of security, only to somehow get caught up in a somewhat consanguineous trail of events."
    response = books_table.update_item(
        Key={
            'book_id' : book_id,
            'title': title
        },
        UpdateExpression= "set ISBN=:ISBN, Summary=:Summary",
        ExpressionAttributeValues = {':ISBN': "0192113585", ':Summary': summary},
		ReturnValues="UPDATED_NEW"
	)
    return response

if __name__ == '__main__':
	try:
		book_update = update_book(1007, 'The Gods are not to blame')
	except Exception as e:
		print(e)
	else:
		print(book_update["Attributes"])