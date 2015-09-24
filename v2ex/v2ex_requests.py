# coding: utf-8
import re
import requests
from requests import Session
from bs4 import BeautifulSoup
from datetime import datetime
import sys

username = ''
password = ''
v2ex_url = 'http://v2ex.com'
v2ex_host = 'v2ex.com'
v2ex_login = 'http://v2ex.com/signin'
mission_url = 'http://v2ex.com/mission/daily'
session = Session()

def login():
    r = requests.get(v2ex_login)
    # print r.text
    reg = 'value="(.*)" name="once"'
    once = re.compile(reg).findall(r.text)[0]

    post_data = {
        'u': username,
        'p': password,
        'once': once,
        'next': '/'
    }

    session.post(v2ex_login, post_data, headers = get_header(), cookies = r.cookies)

    # print s.get(mission_url).text
    # s = Session()
    # req = Request('POST', v2ex_login,
    #     data = post_data,
    #     headers = header)

    # prepare = req.prepare()
    # resp = s.send(prepare)

def get_header():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Referer': v2ex_login,
        'Host': 'v2ex.com'
    }
    return header

def get_result(contents):
    # print contents
    soup = BeautifulSoup(contents, 'lxml')
    result = soup.find(class_='fa fa-ok-sign')
    return result

#签到
def sign():
    r = session.get(mission_url)
    soup = BeautifulSoup(r.text, "lxml")
    btn = soup.find('input', class_='super normal button');
    onclick = btn.get('onclick')
    href = re.compile('\'(.*)\'').findall(onclick)[0]
    session.get(v2ex_url + href, headers = get_header())
    result = get_result(session.get(mission_url).text)
    now = datetime.now()
    path = sys.path[0]
    f = open(path + '/v2ex.log', 'a')
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    if result:
        f.write(time + ' Sign Success!')
    else:
        f.write(time + ' Wrong!!!')

if __name__ == '__main__':
    login()
    sign()
