import flask
from twilio import twiml
from flask import request
import os


app = flask.Flask(__name__)


@app.route('/queue', methods=['POST'])
def queue():
    response = twiml.Response()
    response.enqueue("GA Demo Night", waitUrl="/wait")
    return str(response)

@app.route('/wait', methods=['POST'])
def wait():
    response = twiml.Response()
    response.say("You are number %s in the queue. Please hold." %
            request.form['QueuePosition'])
    response.play("http://demo.brooklynhacker.com/music/ramones.mp3")
    return str(response)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
