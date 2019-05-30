import boto3

sns = boto3.client('sns', region_name='us-east-1')
number = input('Enter Phone: ').strip()
message = input('Enter Message: ').strip()
out = sns.publish(PhoneNumber=number, Message=message)
print(out)
