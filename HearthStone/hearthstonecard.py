# -*- coding: UTF-8 -*-

import json
import requests
import re
from bs4 import BeautifulSoup

def getJson():
    f = open('hearthstone_data.json.backup')
    line = f.readline()
    json_str = line
    while line:
        line = f.readline()
        json_str += line
    js = json.loads(json_str)
    return js

def getUrl(image, name):
    return "http://db.h.163.com/card/%s/%s" % (image, name)

def handleCard(item):
    card_url = getUrl(item['image'], item['name'])
    req = requests.get(card_url)
    content = req.text
    soup = BeautifulSoup(content, 'lxml')
    card_attr = soup.find_all('div',class_='card-attribute')[0]
    name = re.compile('\s*(.*)\s*').findall(card_attr.h2.a.string)[0]
    item['name_zh'] = name
    # print item['id']
    print name
    # print '-----------'
    # print name
    if not 'class' in card_attr.p.attrs:
            text_str = str(card_attr.p)
            text_str = unicode(text_str, 'utf-8')
            text_str = re.sub('<[^>]*>|', '', text_str)
            # print type(text_str)
            item['text_zh'] = text_str
            print text_str
            # print type(text_str)
            # print text_str
    # print item
    # print type(card_attr)

    # print card_attr + "\n"

def jsonWrite(js):
    print js
    json_str = json.dumps(js)
    f = open('hearthstone_data_zh.json', 'wb')
    json_str = json_str
    # print type(json_str)
    # print json_str
    f.write(json_str)

def main():
    js = getJson()
    for i in js:
        item = js[i]
        handleCard(item)
    jsonWrite(js)

if __name__ == '__main__':
    main();
