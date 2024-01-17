from twilio.rest import Client

account_sid = "***************"
auth_token = "*******************"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="hi, Testing",
    from_='+0123456789',
    to='+9876543210'
)

print(message.status)
print(message.sid)
