#coding=utf-8

import urllib2, urllib, re, cookielib

url = 'http://v2ex.com/signin'
v2ex = urllib2.urlopen(url)
contents = v2ex.read()

username = 'jz1206'
password = 'feng1206'

reg_once = 'value="(.*)" name="once"'
once = re.compile(reg_once).findall(contents)[0]

hdr = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36'}
post_data = {
	'username' : username,
	'password' : password,
	'once' : once,
	'next' : '/'
}

cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
dt = urllib.urlencode(post_data)

req = urllib2.Request(url, dt, hdr)
opener = urllib2.build_opener(cookie_handler)
urllib2.install_opener(opener)
response = opener.open(req)
page = response.read()

print(page)

reg_silver = '<a href="/balance" class="balance_area" style="">(.*)<img src="//cdn.v2ex.com/static/img/silver.png" alt="S" align="absmiddle" border="0" style="padding-bottom: 2px;"> (.*) <img src="//cdn.v2ex.com/static/img/bronze.png" alt="B" align="absmiddle" border="0"></a>'
coin = re.compile(reg_silver).findall(reg_silver)
for s in coin:
	print s


