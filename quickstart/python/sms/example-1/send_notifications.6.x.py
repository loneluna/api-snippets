# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['AC338e59abd0db958236385eb35190de43']
auth_token = os.environ['0288fd2fc5b445c55694d326d8fca8e7']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+9779861609973",
    from_="+18177569608",
    body="Hello there! its my first try")

print (message.sid)
