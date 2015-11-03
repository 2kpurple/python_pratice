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
    # print card_attr.p
    text_str = str(card_attr.p)
    text_str = re.sub('<.>|<\/.>', '', text_str)
    # print type(text_str)
    print text_str
    # card_text = re.compile()
    # print name
    item['name_zh'] = name
    item['text_zh'] = text_str
    # print type(card_attr)

    # print card_attr + "\n"

def main():
    js = getJson()
    for i in js:
        item = js[i]
        handleCard(item)
    # print js

if __name__ == '__main__':
    main();
