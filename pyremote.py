import sys
from datetime import datetime
import requests
import traceback
import warnings

class connection(object):
    _debug = False

    def check_user_id(self, user_id):
        message = {'check_user_id': user_id}
        response = requests.post(url= self.server, json = message)
        if self._debug:
             print(f'Response from server: {response.content}')
        if response.status_code != 200:
            #Couldn't reach the server server
            raise ConnectionError(f"Couldn't reach the server! Server response: {response}. Please check your internet connection and try again.")
        elif response.content != b'OK':
            # Invalid user_id
            raise ValueError(f"Invalid user_id: {user_id}. Please go to t.me/PyRemoteBot to get your user_id.")

    def __init__(self, user_id):
        """ """
        self.user_id = user_id
        self.server = "https://www.MahbodNouri.com/python/PyRemote/"
        self.check_user_id(user_id)
        if self._debug:
            warnings.filterwarnings('always')

    def _post_text(self, message, message_type):
        assert message_type in ['data', 'json'], "message_type must be 'data' or 'json'"
        if message_type == 'data':
            response = requests.post(url= self.server, data = message)
        if message_type == 'json':
            response = requests.post(url= self.server, json = message)

        if response.status_code != 200:
            #Couldn't reach the server server
             warnings.warn(f"WARMIMG: Couldn't reach the server! Server response: {response}. Please check your internet connection and try again.")

        elif response.content != b'OK':
            #Telegram couldn't deliver the message
            warnings.warn(f"WARMIMG: Sending message to telegram bot wasn't successful.{f' Error: {response.content}' if self._debug else ''}")
        
        if self._debug:
             print(f'Response from server: {response.content}')

    def send(self, msg, show_file_name=True):
        """ """
        try:
            json_msg = {"user_id": self.user_id, "content" : msg}
            if show_file_name:
                json_msg['file'] = sys.argv[0]

            self._post_text(json_msg, 'json')

        except Exception as e:
            warnings.warn(f"WARMIMG: Sending message to telegram bot wasn't successful. Error: {e}")
            if self._debug:
                warnings.warn(traceback.format_exc())