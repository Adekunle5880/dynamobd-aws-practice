import boto3

def update_pitr(table):
    
	client = boto3.client('dynamodb')

	response= client.update_continuous_backups(
		TableName =table,
		 PointInTimeRecoverySpecification={'PointInTimeRecoveryEnabled':False}
	)

	return response

if __name__ == '__main__':
	update_pitr = update_pitr('Books')
	print(update_pitr['ContinuousBackupsDescription'])