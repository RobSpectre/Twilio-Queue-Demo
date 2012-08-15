# Queue Demo 

A fun five minute demo in Python featuring the new TwiML verb Queue and Twilio
Client.

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


## Installation 

Here's how to install this demo on your local environment.



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

local_settings.py is a file available in the hackpack route for you to configure
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
all to use the hackpack.

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

Getting your local environment setup to work with this hackpack is similarly
easy.  After you configure your hackpack with the steps above, use this guide to
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

* Author: [Rob Spectre](http://www.brooklynhacker.com/)
* Lovingly crafted in Brooklyn, NY.
