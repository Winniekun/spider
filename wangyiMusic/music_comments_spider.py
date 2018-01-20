'''
@author：KongWeiKun
@file: wang_spider.py
@time: 18-1-19 下午9:19
@contact: 836242657@qq.com
'''
import random

import time

'''
网易云音乐评论爬取
'''
from wangyiMusic.data_to_mysql import Mysql
from wangyiMusic.EncryptUtil import createSecretKey,timeStamp,aesEncrypt,rsaEncrypt
import json
import requests
import logger

logger = logger.logger

class Spider(object):

    def __init__(self,id):
        self.musicId = id
        modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        self.baseurl = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_418603077?csrf_token=%d'%int(id)
        self.secKey =createSecretKey(16)
        self.encSecKey = rsaEncrypt(self.secKey, pubKey, modulus)
        self.mysql = Mysql()
        self.headers = {
            'Cookie': 'appver=1.5.0.75771;',
            'Referer': 'http://music.163.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }

    def get_json(self,url, params, encSecKey):
        data = {
            "params": params,
            "encSecKey": encSecKey
        }
        response = requests.post(url, headers=self.headers, data=data)
        return response.text

    def getComment(self,offset):
        text = {
            'username': "",
            'password': "",
            'rememberLogin': 'true',
            'offset': offset
        }
        text = json.dumps(text)
        encText = aesEncrypt(aesEncrypt(text,self.nonce),self.secKey)
        jsonData = self.get_json(self.baseurl,encText,self.encSecKey)
        jsonDict = json.loads(jsonData)
        # print(jsonData['total'])
        self.dataSave(jsonDict)
        # self.taskSchedule.trigger(self.musicId,offset)
        time.sleep(random.random() * 5)
        return int(jsonDict['total'])

    def dataSave(self,jsonData):
        for comment in jsonData['comments']:
            commentData = {
                'id': str(comment["commentId"]),
                'user': str(comment["user"]["userId"]),
                'content': comment["content"],
                'likeCount': str(comment["likedCount"]),
                'commentTime': str(timeStamp(comment["time"])),
                'musicId': str(self.musicId)
            }
            if not comment["beReplied"] == []:
                commentData["reComment"] = str(comment["beReplied"][0]["user"]["userId"])

            if self.mysql.insertData("comments", commentData) >= 0:
                print("Comments %s Saved." % commentData["id"])

            userData = {
                'id': str(comment["user"]["userId"]),
                'username': comment["user"]["nickname"],
                'avatarUrl': comment["user"]["avatarUrl"]
            }
            if self.mysql.insertData("user", userData) >= 0:
                print("User %s Saved." % userData["id"])

    def process(self,offset):
        if offset == -1:
            return
        off = offset
        total = self.getComment(off)
        while off <total:
            print('正在爬取第%d页'%off)
            off += 10
            print('还有%d没爬完'%(int((total-off))))
            self.getComment(off)
        # self.taskSchedule.trigger(self.musicId, "-1")

def main():
    s = Spider(418603077)
    s.process(1)


if __name__ == '__main__':
    main()