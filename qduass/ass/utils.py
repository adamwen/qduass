from urlparse import urlparse, parse_qs
from settings import AUTH_URL

import random
import feedparser

def filter_accesstoken(string):
    string = AUTH_URL + '?' +string
    params = {}
    
    raw_params = parse_qs(urlparse(string).query)

    for k, v in raw_params.iteritems():
        params[k] = v[0]

    return params


if __name__ == '__main__':
    test_string = 'access_token=19e3762c1a89b810b5f3c3b6a2a78cf0&expires_in=604800&refresh_token=9bdf55a2049be1c47515d2c42341a691&openid=cd9588aa571d977bb4d3a9cb00a8cf23&name=adamwen829&nick=adamwen829&state='

    a = filter_accesstoken(test_string)

    print a



def get_news(rss_url):
    d = feedparser.parse(rss_url)

    num = random.randint(0, len(d.entries))

    return d.entries[num].title


    

