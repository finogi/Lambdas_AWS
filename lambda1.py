import boto3

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Specify the table name
table_name = 'your_table_name'
table = dynamodb.Table(table_name)

# Perform a scan operation to get all items
response = table.scan()
items = response['Items']

# Handle pagination if there are more items
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    items.extend(response['Items'])

# Print or process the items
for item in items:
    print(item)
