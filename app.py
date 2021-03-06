import flask
from flask import request
from twilio import twiml
import os

app = flask.Flask(__name__)


@app.route('/caller', methods=['POST'])
def queue():
    response = twiml.Response()
    response.enqueue("Queue Diggity Demo", waitUrl="/wait")
    return str(response)


@app.route('/wait', methods=['POST'])
def wait():
    response = twiml.Response()
    response.say("You are number %s in line." % request.form['QueuePosition'])
    response.play("http://com.twilio.music.rock.s3.amazonaws.com/" \
            "jlbrock44_-_Apologize_Guitar_DropC.mp3")
    return str(response)


@app.route('/agent', methods=['POST'])
def callin():
    response = twiml.Response()
    with response.dial() as dial:
        dial.queue("Queue Diggity Demo")
    return str(response)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
