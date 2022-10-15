from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route('/smartBot', methods = ['POST'])
def botHandler():
    incoming_message = request.values.get('Body', "").lower()
    resp = MessagingResponse()
    msg = response.message()
    responded = False
    if 'hi' in incoming_message:
        # return a gesture or hello to sender
        msg.body("hello i am Lincoln SmartBot")
    if 'quote' in incoming_message:
        r = request.get('http://api.quotable.io/random')
        if r.status.code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = "i am unablke to retrieve quote at this time"
            msg.body('quote')
            resonded = True
        if "what kind of bot are you" in incoming_message:
            msg.body("I am a whatsappBot")
        if not responded:
            msg.body("cant unnerstand your message please. i can only tell you about quotes and myself")
        return str(resp)

if __name__=='__main__':
    app.run()
  