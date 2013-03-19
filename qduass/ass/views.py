# -*- coding: utf-8 -*-
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from ass.settings import ACCESSTOKEN_REQ_URL, \
                AUTH_URL,\
                CODE_REQ_URL,\
                REFRESH_ACCESSTOKEN,\
                XINHUA_RSS,\
                APP_KEY, \
                APP_SECRET


from ass.models import User
from ass.tencent import Microblog
from ass.utils import filter_accesstoken, get_news


import urllib2
import time

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



def send(reqeust):

    user = User.objects.all()[0]
    microblog = Microblog(APP_KEY, user.accesstoken, user.openid)

    text = get_news(XINHUA_RSS)
    microblog.send(text, '184.82.244.128')

    return HttpResponse(text)
    

def refresh_accesstoken(request):
    user = User.objects.all()[0]

    client_id = APP_KEY
    grant_type = 'refresh_token' 
    refresh_token = user.refresh_key

    url = REFRESH_ACCESSTOKEN.format(client_id, grant_type, refresh_token)

    response = urllib2.urlopen(url).read()
    params = filter_accesstoken(response)

    user.accesstoken = params['access_token']
    user.expires_in = params['expires_in']
    user.refresh_key = params['refresh_token']

    user.save()

    return HttpResponse()

