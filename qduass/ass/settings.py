# -*- coding:utf-8 -*-
SAE_APPID = 'qduass'


APP_KEY = '801326924'
APP_SECRET = 'd28a69bf9e6e9509730e55c5aae71421'

AUTH_URL = 'http://{0}.sinaapp.com/auth'.format(SAE_APPID)

CODE_REQ_URL = 'https://open.t.qq.com/cgi-bin/oauth2/authorize?client_id={0}&response_type=code&redirect_uri={1}'
	
ACCESSTOKEN_REQ_URL = 'https://open.t.qq.com/cgi-bin/oauth2/access_token?client_id={0}&client_secret={1}&redirect_uri={2}&grant_type=authorization_code&code={3}'

REFRESH_ACCESSTOKEN = 'https://open.t.qq.com/cgi-bin/oauth2/access_token?client_id={0}&grant_type={1}&refresh_token={2}'

XINHUA_RSS = 'http://www.xinhuanet.com/politics/news_politics.xml'
