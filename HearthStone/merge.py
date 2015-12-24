# -*- coding: UTF-8 -*-
import json
import os
import sys

__author__ = 'PurpleK'


def get_json(filename):
    f = open(filename)
    line = f.readline()
    json_str = line
    while line:
        line = f.readline()
        json_str += line
    js = json.loads(json_str)
    return js


def open_json():
    path = sys.path[0]
    files = os.listdir(path)
    array = []
    for f in files:
        if "zh_" in f:
            print f
            content = get_json(f)
            array.append(content)
    return array


def start_merge(array):
    result_dict = {}
    for item in array:
        for key in item.keys():
            if not result_dict.has_key(key):
                result_dict[key] = item[key]
    print len(result_dict)
    print json.dumps(result_dict)


def main():
    start_merge(open_json())

if __name__ == '__main__':
    main()
