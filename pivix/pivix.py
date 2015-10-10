# coding: utf-8
import sys
import json
import requests
from requests import Session


class Pixiv:

    MODE_DAILY = 'daily'
    MODE_WEEK = 'week'
    MODE_MONTH = 'month'

    user = ''
    password = ''
    session = Session()
    login_url = 'https://www.secure.pixiv.net/login.php'
    rank_url = 'http://www.pixiv.net/ranking.php'

    def __init__(self):
        config = self._load_config()
        if config is not None:
            self.user = config['user']
            self.password = config['password']
            self._login()

    def _login(self):
        # resp = requests.get(self.login_url)
        post_data = {
            'mode': 'login',
            'pixiv_id': self.user,
            'pass': self.password,
            'skip': 1
        }
        self.session.post(self.login_url, data=post_data)

    def _get_header(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/45.0.2454.101 Safari/537.36',
            'Referer': self.login_url,
            'Host': 'www.secure.pixiv.net'
        }
        return header

    def get_daily_record(self, mode):
        resp = self.session.get(url='http://www.pixiv.net/ranking.php?mode=daily')
        print resp.text


    @staticmethod
    def _load_config():
        path = sys.path[0]
        try:
            f = open(path + '/config.json')
            line = f.readline()
            config_str = line
            while line:
                line = f.readline()
                config_str += line
            config = json.loads(config_str)
            if not config['user'] is None or not config['password'] is None:
                return config
        except IOError:
            print 'No config file!'
        except KeyError:
            print 'No user or password in config file!'
        return None

if __name__ == '__main__':
    p = Pixiv()
    p.get_daily_record(Pixiv.MODE_DAILY)
