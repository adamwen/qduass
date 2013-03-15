from tencent_settings import TEXT, HEADERS, TWEET_SEND_URL
import requests

class Microblog:
    def __init__(self, app_key, access_token, openid):
        self.app_key = app_key
        self.access_token = access_token
        self.openid = openid

    def send(self, text, ip):
        text = str(text)
        data = TEXT.format(text, self.app_key, self.access_token, self.openid, ip)
        url = TWEET_SEND_URL
        headers = HEADERS

        response = requests.post(url, data=data, headers=headers)

        return response.ok





