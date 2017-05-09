#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import logging
import os
logger = logging.getLogger('ROOT')

class Slack:
    def __init__(self, channel_url=os.environ['SLACK_CHANNEL_URL'],
                 channel="#dev", username="Username", icon_emoji=":one:"):
        self.channel_url = channel_url
        self.username = username
        self.channel = channel
        self.icon_emoji = icon_emoji

    def notify(self, message="No message was provided."):
        self.message = message
        self.__build_payload()
        self.__send()
        logger.info("Request for URL: {} responded: {}".format(self.channel_url, self.response_status))
        return self.response

    def __build_payload(self):
        self.payload = str({"channel": self.channel,
                            "username": self.username,
                            "text": str(self.message),
                            "icon_emoji": self.icon_emoji})

    def __send(self):
        self.response = requests.post(self.channel_url, data=self.payload)
        self.response_status = self.response.status_code

slack = Slack(channel="#data-alerts",
              username="Scoobydoo",
              icon_emoji=":beetle:")