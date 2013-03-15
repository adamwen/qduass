# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from url import ACCESSTOKEN_REQ_URL, \
                AUTH_URL,\
                CODE_REQ_URL,\
                REFRESH_ACCESSTOKEN\

from key import APP_KEY, APP_SECRET

from urllib import quote
import urllib2

def index(request):
    valid_url = CODE_REQ_URL.format(APP_KEY, AUTH_URL)

    print valid_url
    
    return HttpResponseRedirect(valid_url)

def authorization(request):

    if 'code' in request.GET:
        code =  request.GET['code']
        openid =  request.GET['openid']
        openkey =  request.GET['openkey']

    print code
    print openid
    print openkey

    url = ACCESSTOKEN_REQ_URL.format(APP_KEY, APP_SECRET, AUTH_URL, code)

    response = urllib2.urlopen(url).read()

    print response

    return HttpResponse()
