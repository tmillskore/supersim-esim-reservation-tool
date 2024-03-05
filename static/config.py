import base64

account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
fleet = 'YOUR_FLEET_SID'

credentials = account_sid + ':' + auth_token
authorization = 'Basic ' + base64.b64encode(credentials.encode()).decode()
