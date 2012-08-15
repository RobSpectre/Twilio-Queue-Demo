import flask
from flask import request
from twilio import twiml
import os

app = flask.Flask(__name__)

@app.route('/queue', methods=['POST'])
def queue():
    response = twiml.Response()
    response.enqueue("Queue Demo", waitUrl='/wait')
    return str(response)

@app.route('/wait', methods=['POST'])
def wait():
    response = twiml.Response()
    response.say("Thank you for calling - you are number %s in line." %
            request.form['QueuePosition'])
    response.play("http://demo.brooklynhacker.com/music/ramones.mp3")
    return str(response)

@app.route('/dial', methods=['POST'])
def dial():
    response = twiml.Response()
    with response.dial() as dial:
        dial.queue("Queue Demo")
    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
