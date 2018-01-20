'''
@author：KongWeiKun
@file: wang_spider.py
@time: 18-1-19 下午9:19
@contact: 836242657@qq.com
'''
import random

'''
网易云音乐评论爬取
'''
from wangyiMusic.data_to_mysql import Mysql
from wangyiMusic.EncryptUtil import *
import json
import requests
import logger

logger = logger.logger

class Spider(object):

    def __init__(self,id):
        self.musicId = id
        self.baseurl = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_418603077?csrf_token=%d'%int(id)
        self.params = get_params()
        self.encSecKey = get_encSecKey()
        # self.taskSchedule = taskSchedule
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
        jsonData = self.get_json(self.baseurl,self.params,self.encSecKey)
        jsonDict = json.loads(jsonData)
        # print(jsonData['total'])
        self.dataSave(jsonDict)
        # self.taskSchedule.trigger(self.musicId,offset)
        # time.sleep(random.random() * 5)
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
            off += 10
            self.getComment(off)
        # self.taskSchedule.trigger(self.musicId, "-1")

def main():
    s = Spider(418603077)
    s.process(1)


if __name__ == '__main__':
    main()