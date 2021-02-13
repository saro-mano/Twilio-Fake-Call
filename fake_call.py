from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)


#Credentials: Please fill in with their corresponding credentials.
account_sid = "Your Account Sid" 
auth_token = "Your Auth Token"
my_cell = "+Your Cell Number"
my_twilio = "+Your Twilio Number"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    
    #Getting the incoming message values
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()
    
    if body == "Fake call":
        print(call_back())
        resp.message("Hang in there! Calling now....")

    else:
        #Respond to incoming calls with a simple text message.
        resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

'''Call Back function'''
def call_back():
    client = Client(account_sid, auth_token)
    call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to= my_cell,
                        from_= my_twilio
                    )
    return "Successfully called"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)