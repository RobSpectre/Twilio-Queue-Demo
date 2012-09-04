# Queue Demo 

A fun ten minute demo in Python featuring the new TwiML verb Queue and Twilio
Client.  This little step-by-step guide takes you through building your own demo
with Twilio's new [<Queue>](http://www.twilio.com/docs/api/twiml/queue) TwiML
verb.


[![Build
Status](https://secure.travis-ci.org/RobSpectre/Twilio-Queue-Demo.png)]
(http://travis-ci.org/RobSpectre/Twilio-Queue-Demo)

Want to take Queue for a spin or show it to your friends? Try this below.

## Features 

This demo highlights the following features:

* The [Enqueue](http://www.twilio.com/docs/api/twiml/enqueue) verb to place
  callers in a Queue with a custom waiting room.
* The [Queue](http://www.twilio.com/docs/api/twiml/queue) noun to connect the
  agent to the first person in the queue with a custom whisper for the
  dequeueing caller.
* [Twilio Client for Javascript](http://www.twilio.com/docs/client/twilio-js) to
  place the callers in the audience on the PA through the demoing devangel's
  laptop.

## Outline 

Detailed outline of the demonstration with tips on reducing or increasing total
demo time.

### Five Minute Demo

Step-by-step outline of how to present this demo.  Note code is additive - to
see finished product, check out `app.py`.

- Pre-Demo
    - Make sure environment is configured per this README doc.
    - Plug in laptop to PA system or portable speakers for the audience to hear
      themselves.
    - Rehearse.
- Introduction
    - Opening Narrative
        - You got customers that need help, but only so many people to help 
          them at once.
        - Setting up a call queue is a super common use case for companies of
          all sizes, but the hardware to do so is super expensive.
        - We just made creating common call queue functionality for call
          centers and other voice applications as easy as making Twilio
          Conference rooms
        - Enter the Twilio Queue verb.
    - Twilio
        - We're your very own programmable telephone company.
        - Make it very easy for you as a developer to send and receive text
          messages and make and receive phone calls from within your web app or
          native mobile app
        - Your bio
- Demo
    - Overview
        - Create a Flask app hosted on Heroku that will be a fully functioning
          call queue from an empty file
        - Briefly introduce Heroku
        - Briefly introduce Flask
          
            ```python
            import flask
            from flask import request
            ```

        - Briefly introduce TwiML

            ```python
            from twilio import twiml
            ```

        - Highlight usage of operating system module.

            ```python
            import os
            ```

    - Setup the queue for the audience to call.
        - Create the queue with a customized waiting room.
            
            ```python
            app = flask.Flask(__name__)

            @app.route('/queue', methods=['POST'])
            def queue():
                response = twiml.Response()
                response.enqueue("Queue Diggity Demo", waitUrl="/wait")
                return str(response)
            ```

        - Create the waiting room with personalized introduction telling the
          user where they are in the queue.

            ```python
            @app.route('/wait', methods=['POST'])
            def wait():
                response = twiml.Response()
                response.say("You are number %s in the queue. Please hold." %
                        request.form['QueuePosition'])
                response.play("http://com.twilio.music.rock.s3.amazonaws.com/jlbrock44_-_Apologize_Guitar_DropC.mp3")
                return str(response)
            ```

        - Write a little boilerplate so the app will run on Heroku.

            ```python
            if __name__ == "__main__":
                port = int(os.environ.get('PORT', 5000))
                app.debug = True
                app.run(host='0.0.0.0', port=port)
            ```
        
        - Save, commit and push to Heroku

        `git commit -a -m "Added call queue."`
        `git push heroku master`

    - Connect queue to a phone number
        - Login to [Account Dashboard](https://www.twilio.com/user/account).
        - [Buy a phone
          number](https://www.twilio.com/user/account/phone-numbers/available/local)
          from the hometown of someone in the audience.
        - Set Voice Request URL for purchased number to Heroku host and queue
          endpoint, e.g. `http://clever-subdomain.herokuapps.com/queue`.
        - Ask audience members to dial into the queue and see if it works.
    - Work the Queue
        - Ask the audience members to stay connected while you build the agent
          portion.
        - Create dial-in to first member of the queue.

            ```python
            @app.route('/dial', methods=['POST'])
            def dial():
                response = twiml.Response()
                with response.dial() as dial:
                    dial.queue("Queue Diggity Demo") 
                return str(response)
            ```

        - Save, commit and push to Heroku

        `git commit -a -m "Added call queue."`
        `git push heroku master`

        - Create [new TwiML
          application](https://www.twilio.com/user/account/apps) in Dashboard.
        - Set Voice Request URL for new AppSid to Heroku host and dial endpoint,
          e.g. `http://clever-subdomain.herokuapps.com/dial`.
        - Use Twilio Client built into the TwiML App interface in the dashboard
          to call the queue and connect to the first user.
        - Hangup and call back until everyone who called hears their voice on
          the loudspeaker.
- Conclusions
    - Just like that, you have a queue your customers can call into and your
      agents can reach to service one at a time.
    - Documentation on this new feature is available at
      [twilio.com](https://www.twilio.com/docs/api/twiml/enqueue).
    - Come find me in the red sneakers and/or track jacket if you have any
      questions.
- Post-Demo
    - Send text message to everyone who called into the number thanking them for
      their participation with link to Twilio website or contact info. 


### Time Savers

* Switch to purchasing phone number and creating TwiML app after each respective
  push to Heroku, letting it deploy in the background while you demonstrate the
  Twilio interface.
* Omit customized waiting room.
* Have phone number purchased and TwiML app already created.

### Time Extenders

* Clone [Twilio Hackpack for Heroku and
  Flask](https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask) and 
  start from fresh environment, not just fresh file.
* Add custom connection message before user connects to agent using the url
  attribute for the [Queue noun](https://www.twilio.com/docs/api/twiml/queue).
* Add Twilio Client in the app instead of using Call button in the Dashboard:

```python
from twilio.util import TwilioCapability

@app.route('/client')
def client():
    capability = TwilioCapability(os.environ.get('TWILIO_ACCOUNT_SID',
        'TWILIO_AUTH_TOKEN'))
    capability.allow_client_outgoing('APxxxxx')
    token = capability.generate()
    return flask.render_template('client.html', token=token)
```

## Installation 

Here's how to install this demo on your local environment.

### Environment

This demo requires the following software to be installed on your machine:

* [Python](http://www.python.org/download/)
* [pip and virtualenv](http://www.pip-installer.org/en/latest/installing.html)
* [git](http://git-scm.com/downloads)
* [Heroku toolbelt](https://toolbelt.heroku.com/)

Optionally, you can install these tools to make life easier.

* [make](http://www.gnu.org/software/make/)
* [foreman](http://ddollar.github.com/foreman/)

### Getting Started 

1) Grab latest source
<pre>
git clone git://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask.git 
</pre>

2) Navigate to folder and create new Heroku Cedar app
<pre>
heroku create --stack cedar
</pre>

3) Deploy to Heroku
<pre>
git push heroku master
</pre>

4) Scale your dynos
<pre>
heroku scale web=1
</pre>

5) Get the domain name and set your voice request urls.
<pre>
heroku info
</pre>

### Configuration

Here's how to configure your local and Heroku host for use with the demo.

#### Automagic Configuration

This demo ships with an auto-configure script that will create a new TwiML
app, purchase a new phone number, and set your Heroku app's environment
variables to use your new settings.  Here's a quick step-by-step:

1) Make sure you have all dependencies installed
<pre>
make init
</pre>

2) Run configure script and follow instructions.
<pre>
python configure.py --account_sid ACxxxxxx --auth_token yyyyyyy
</pre>

3) For local development, copy/paste the environment variable commands the
configurator provides to your shell.
<pre>
export TWILIO_ACCOUNT_SID=ACxxxxxx
export TWILIO_AUTH_TOKEN=yyyyyyyyy
export TWILIO_APP_SID=APzzzzzzzzzz
export TWILIO_CALLER_ID=+15556667777
</pre>

Automagic configuration comes with a number of features.  
`python configure.py --help` to see them all.


#### local_settings.py

local_settings.py is a file available in the demo route for you to configure
your twilio account credentials manually.  Be sure not to expose your Twilio
account to a public repo though.

```python
ACCOUNT_SID = "ACxxxxxxxxxxxxx" 
AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
TWILIO_APP_SID = "APzzzzzzzzz"
TWILIO_CALLER_ID = "+17778889999"
```

#### Setting Your Own Environment Variables

The configurator will automatically use your environment variables if you
already have a TwiML app and phone number you would prefer to use.  When these
environment variables are present, it will configure the Twilio and Heroku apps
all to use the demo.

1) Set environment variables locally.
<pre>
export TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxx
export TWILIO_AUTH_TOKEN=yyyyyyyyyyyyyyyyy
export TWILIO_APP_SID=APzzzzzzzzzzzzzzzzzz
export TWILIO_CALLER_ID=+15556667777
</pre>

2) Run configurator
<pre>
python configure.py
</pre>


### Development

Getting your local environment setup to work with this demo is similarly
easy.  After you configure your demo with the steps above, use this guide to
get going locally:

1) Install the dependencies.
<pre>
make init
</pre>

2) Launch local development webserver
<pre>
foreman start
</pre>

3) Open browser to [http://localhost:5000](http://localhost:5000).

4) Tweak away on `app.py`.


## Testing

This demo comes with a full testing suite ready for nose.

<pre>
make test
</pre>


## Meta 

* No warranty expressed or implied. Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html).
* Lovingly crafted by [Twilio New York](http://www.meetup.com/Twilio/New-York-NY/).
