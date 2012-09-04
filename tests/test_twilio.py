import unittest
from .context import app

class TwiMLTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def assertTwiML(self, response):
        self.assertTrue("<Response>" in response.data, "Did not find " \
                "<Response>: %s" % response.data)
        self.assertTrue("</Response>" in response.data, "Did not find " \
                "</Response>: %s" % response.data)
        self.assertEqual("200 OK", response.status)

    def sms(self, body, path='/sms', number='+15555555555'):
        params = {
            'SmsSid': 'SMtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'Body': body,
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound'}
        return self.app.post(path, data=params)

    def call(self, path='/voice', number='+15555555555', digits=None):
        params = {
            'CallSid': 'CAtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'CallStatus': 'ringing',
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound',
            'QueuePosition': '1'}
        if digits:
            params['Digits'] = digits
        return self.app.post(path, data=params)


class TwilioTests(TwiMLTest):
    def test_caller(self):
        response = self.call(path='/caller')
        self.assertTwiML(response)
        self.assertTrue('Enqueue' in response.data, "Did not find Enqueue " \
                "verb in the response, instead: %s" % response.data)

    def test_wait(self):
        response = self.call(path='/wait')
        self.assertTwiML(response)
        self.assertTrue('Say' in response.data, "Did not find Say " \
                "announcement in wainting room, instead: %s" % response.data)
        self.assertTrue('Play' in response.data, "Did not find hold " \
                "music in waiting room, instead %s" % response.data)

    def test_agent(self):
        response = self.call(path='/agent')
        self.assertTwiML(response)
        self.assertTrue('Dial' in response.data, "Did not find Dial " \
                "in agent call-in app, instead %s" % response.data)
