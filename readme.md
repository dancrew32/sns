# Send a SMS Text Message via SNS

## Setup Credentials:

https://console.aws.amazon.com/iam/home?nc2=h_m_sc#/security_credentials

```bash
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
```

## Clone & Run:

```bash
git clone https://github.com/dancrew32/sns.git
make venv deps run
```

## Example

```
Enter Phone: +15555555555
Enter Message: Yo!
{'MessageId': '...', 'ResponseMetadata': {'RequestId': '...', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '...', 'content-type': 'text/xml', 'content-length': '294', 'date': '...'}, 'RetryAttempts': 0}}
```
