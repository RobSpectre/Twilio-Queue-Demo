import flask
from flask import request
from twilio import twiml
import os

app = flask.Flask(__name__)

@app.route('/queue', methods=['POST'])
def queue():
    response = twiml.Response()
    response.enqueue("Marketing Demo Jam", waitUrl="/wait")
    return str(response)

@app.route('/wait', methods=['POST'])
def wait():
    response = twiml.Response()
    response.say("You are number %s in line." % request.form['QueuePosition'])
    response.play("http://demo.brooklynhacker.com/music/ramones.mp3")
    return str(response)

@app.route('/callin', methods=['POST'])
def callin():
    response = twiml.Response()
    with response.dial() as dial:
        dial.queue("Marketing Demo Jam")
    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
