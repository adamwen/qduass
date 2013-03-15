AUTH_URL = 'http://www.darkof.com:4321/auth'

CODE_REQ_URL = 'https://open.t.qq.com/cgi-bin/oauth2/authorize?client_id={0}&response_type=code&redirect_uri={1}'
	
ACCESSTOKEN_REQ_URL = 'https://open.t.qq.com/cgi-bin/oauth2/access_token?client_id={0}&client_secret={1}&redirect_uri={2}&grant_type=authorization_code&code={3}'

REFRESH_ACCESSTOKEN = 'https://open.t.qq.com/cgi-bin/oauth2/access_token?client_id={0}&grant_type=refresh_token&refresh_token={1}'

XINHUA_RSS = 'http://www.xinhuanet.com/politics/news_politics.xml'
