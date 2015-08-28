#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import cookielib

username = ''
password = ''
host = 'v2ex.com'
login_url = 'http://v2ex.com/signin'
mission_url = 'http://v2ex.com/mission/daily'

def login():
    cj = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cj)

    req = urllib2.Request(url = login_url)
    opener = urllib2.build_opener(cookie_handler)
    urllib2.install_opener(opener)
    contents = opener.open(req).read()

    reg = 'value="(.*)" name="once"'
    once = re.compile(reg).findall(contents)[0]

    post_data = {
        'u': username,
        'p': password,
        'once': once,
        'next': '/'
    }

    post_data = urllib.urlencode(post_data)
    req = urllib2.Request(url = login_url, data = post_data)
    opener = urllib2.build_opener(cookie_handler)
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'),
        ('Referer', login_url),
        ('Host', 'v2ex.com')
    ]
    resp = opener.open(req)
    page = resp.read()
    # print page
    # print_cookie(cj)


def sign():
    mission = urllib2.urlopen(url = mission_url)
    print mission.read()


def print_cookie(cookie):
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value

if __name__ == '__main__':
    login()
    sign()
