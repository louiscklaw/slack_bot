#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
import unittest

from slack_bot import *

# Incoming Webhooks
SLACK_WEBHOOK_URL = os.getenv('DEBUG_WEBHOOK_URL')

LOREM_IPSUM_TEST_MSG = '''What is Lorem Ipsum?
< @louis.law >
#sandbox
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a gal
<http://www.google.com|www.google.com>
louis.law@tinklabs.com
的苦或體，年引標關死每除又那科可親條開的不
# NOTE: ㊙ ️I would like to ...
# TODO: 🤦 Temporary solution ...
# QUESTION?: 🤔 What is the opinion about ... ??
'''

def setUpModule():
    print('setup module')


def tearDownModule():
    print('teardown module')


class TestReadMeDemo(unittest.TestCase):
    def test_for_readme_demo(self):
        self.assertEqual(slack_reporter().send_message('test readme demo'),0,
            'testing sending english, the sending API only')


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('teardown class')

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

    def test_sending_without_specify_url(self):
        self.assertEqual(slack_reporter().send_message(LOREM_IPSUM_TEST_MSG),0,
            'testing sending english, the sending API only')

    def test_sending_with_specify_url(self):
        self.assertEqual(slack_reporter(SLACK_WEBHOOK_URL).send_message(LOREM_IPSUM_TEST_MSG),0,
            'testing sending english, the sending API only')

    def test_sending_with_specify_channel(self):

        self.assertEqual(slack_reporter(channel='sandbox').send_message(LOREM_IPSUM_TEST_MSG),0,
            'testing sending english, the sending API only')

    def test_sending_with_specify_username(self):
        self.assertEqual(slack_reporter(slack_username='123321').send_message(LOREM_IPSUM_TEST_MSG),0,
            'testing sending english, the sending API only')


if __name__ == '__main__':
    unittest.main(verbosity=2)
