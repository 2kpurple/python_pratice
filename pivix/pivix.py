# coding: utf-8
import sys
import json
from requests import Session


class Pixiv:
    user = ''
    password = ''
    session = Session()
    login_url = 'https://www.secure.pixiv.net/login.php'

    def __init__(self):
        config = self._load_config()
        if config is not None:
            self.user = config['user']
            self.password = config['password']
            self._login()

    def _login(self):
        resp = self.session.get(self.login_url)
        post_data = {
            'mode': 'login',
            'pixiv_id': self.user,
            'pass': self.password,
            'skip': 1
        }
        login_resp = self.session.post(self.login_url, data=post_data, headers=self.get_header(), cookies=resp.cookies)
        print login_resp.text

    def get_header(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/44.0.2403.157 Safari/537.36',
            'Referer': self.login_url,
            'Host': 'www.secure.pixiv.net'
        }
        return header

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

p = Pixiv()

