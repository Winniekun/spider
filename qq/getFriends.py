'''
@author：KongWeiKun
@file: getFriends.py
@time: 17-11-21 下午5:08
@contact: 836242657@qq.com
'''
import re

from PIL import Image

'''
获取qq好友的账号
'''
import selenium
import requests
from requests.exceptions import  RequestException
from selenium import webdriver
import time
import csv



def getFriends():
    file='./qq.csv'
    qq_reader=csv.reader(open(file))
    next(qq_reader)#去头部
    friend = []
    for row in qq_reader:
        friend.append(row[3])
    friends = []
    for f in friend:
        f = f[:-7]
        friends.append(f)
    # print(len(friends))
    return friends



if __name__ == '__main__':
    # getFriends()
    getFriends()