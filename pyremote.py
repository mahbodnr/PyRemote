import sys
from datetime import datetime
import requests

class connection(object):
    def __init__(self, chat_id, warning = False):
        """ """
        self.id = chat_id
        self.webhook = "https://www.MahbodNouri.com/python/PyRemote/bot"
        self.WARNING = warning

    def _post_text(self, message, message_type):
        assert message_type in ['data', 'json'], "message_type must be 'data' or 'json'"
        if message_type == 'data':
            response = requests.post(url= self.webhook, data = message)
        if message_type == 'json':
            response = requests.post(url= self.webhook, json = message)

        if response.status_code != 200 and self.WARNING:
            #Couldn't reach the Webhook server
            print(f"WARMIMG: Sending message to telegram bot wasn't successful. Site response: {response}. this has occurred because you couldn't reach the server. It may get disappear after trying again, if not, please inform me at: mahbodnouri@gmail.com")

        elif response.content != b'OK' and self.WARNING:
            #Telegram couldn't deliver the message
            print(f"WARMIMG: Sending message to telegram bot wasn't successful. Error: {response.content}")
        

    def send(self, msg, show_file_name=True):
        """ """
        try:
            json_msg = {"chat_id": self.id, "content" : msg}
            if show_file_name:
                json_msg['file'] = sys.argv[0]

            self._post_text(json_msg, 'json')

        except Exception as e:
            if self.WARNING:
                print(f"WARMIMG: Sending message to telegram bot wasn't successful. Error: {e}")