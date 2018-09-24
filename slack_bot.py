#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import json
import html

# NOTE: default configuratin
DEFAULT_SLACK_WEBHOOK = os.getenv('FAB_BOT_WEBHOOK_URL')
DEFAULT_CHANNEL='sandbox'
DEFAULT_USERNAME = 'testuser'

# NOTE: environment configuration
CURL_BINARY=subprocess.check_output(['which','curl']).decode('utf-8').strip()

slack_colors = {
    'OK': '#FF3838',
    'PROBLEM': '#43F060'
}

slack_icons = {
    'Disaster': ':closed_book:',
    'High': ':orange_book:',
    'Average': ':ledger:',
    'Warning': ':notebook_with_decorative_cover:',
    'Information': ':blue_book:',
    'Not classified': ':notebook:',
}



class slack_reporter:
    def __init__(self, url=DEFAULT_SLACK_WEBHOOK, channel=DEFAULT_CHANNEL, slack_username=DEFAULT_USERNAME):
        self.slack_url = url
        self.slack_to_channel=channel
        self.slack_username = slack_username

    def encap_message(self, slack_text='test message'):
        """to encap the message to be send

        Args:
            slack_text: the message to be sent(plain text)
        """
        json_payload = {
            "channel": self.slack_to_channel,
            "username": self.slack_username,
            "text": slack_text

        }

        payload = "payload=" + json.dumps(json_payload)
        invoke = [CURL_BINARY, '-m', '5', '--data-urlencode', payload, self.slack_url]

        return subprocess.call(invoke)


    def send_message(self, msg_body):
        try:
            # NOTE: reserved for pre-processing the message
            # e.g. insert file
            result = self.encap_message(msg_body)

            return result

        except Exception as e:
            # NOTE: As this scripts is running inside the test scripts. I won't like to let the exception here trigger a fail of the whole test script. so i mute the exception here.

            utils.logv2('error occur during running send message', 'Fail')
