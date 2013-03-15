# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from ass.url import ACCESSTOKEN_REQ_URL, \
                AUTH_URL,\
                CODE_REQ_URL,\
                REFRESH_ACCESSTOKEN\

from ass.key import APP_KEY, APP_SECRET

from urllib import quote
import urllib2

from utils import filter_accesstoken

from ass.models import User

def index(request):
    valid_url = CODE_REQ_URL.format(APP_KEY, AUTH_URL)

    print valid_url
    
    return HttpResponseRedirect(valid_url)

def authorization(request):

    if 'code' in request.GET:
        code =  request.GET['code']
        openid =  request.GET['openid']
        openkey =  request.GET['openkey']

    url = ACCESSTOKEN_REQ_URL.format(APP_KEY, APP_SECRET, AUTH_URL, code)

    response = urllib2.urlopen(url).read()
    params = filter_accesstoken(response)

    user = User(openid=openid, 
                openkey=openkey,
                accesstoken=params['access_token'],
                expires_in=params['expires_in'],
                refresh_key=params['refresh_token'],
                nickname=params['nick'],
                name=params['name']
                )
    user.save()

    return HttpResponse('You Got It')



