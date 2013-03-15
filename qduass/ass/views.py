# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from url import ACCESSTOKEN_REQ_URL,
                MY_URL,
                CODE_REQ_URL,
                REFRESH_ACCESSTOKEN

from key import APP_KEY, APP_SECRET

from urllib2

def index(request):
    valid_url = CODE_REQ_URL.format(APP_KEY, MY_URL)

    print valid_url
    
	return HttpResponseRedirect(valid_url)

def authorization(request):
	if 'code' in request.GET:
		code =  request.GET['code']
		openid =  request.GET['openid']
		openkey =  request.GET['openkey']
'''	else:
		print request.GET['access_token']
		print request.GET['expires_in']
		print request.GET['refresh_token']
'''
    
    print code
    print openid
    print openkey

    url = ACCESSTOKEN_REQ_URL.format(APP_KEY, APP_SECRET, MY_URL, code)

    response = urllib2.urlopen(url).read()

    print response

	return HttpResponse()
