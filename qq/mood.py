'''
@author：KongWeiKun
@file: mood.py
@time: 17-11-21 下午1:47
@contact: 836242657@qq.com
'''
import re
import requests
import datetime
import pymysql
import csv
from . getFriends import getFriends



def get_qq():
    friends=getFriends()
    for qq in friends:
        return qq

def parse_mood(i):
    '''从返回的json中，提取我们想要的字段'''
    qq=get_qq()
    text = re.sub('"commentlist":.*?"conlist":', '', i)
    if text:
        myMood = {}
        myMood["isTransfered"] = False
        tid = re.findall('"t1_termtype":.*?"tid":"(.*?)"', text)[0]  # 获取说说ID
        tid = qq + '_' + tid
        myMood['id'] = tid
        myMood['pos_y'] = 0
        myMood['pos_x'] = 0
        mood_cont = re.findall('\],"content":"(.*?)"', text)
        if re.findall('},"name":"(.*?)",', text):
            name = re.findall('},"name":"(.*?)",', text)[0]
            myMood['name'] = name
        if len(mood_cont) == 2:  # 如果长度为2则判断为属于转载
            myMood["Mood_cont"] = "评语:" + mood_cont[0] + "--------->转载内容:" + mood_cont[1]  # 说说内容
            myMood["isTransfered"] = True
        elif len(mood_cont) == 1:
            myMood["Mood_cont"] = mood_cont[0]
        else:
            myMood["Mood_cont"] = ""
        if re.findall('"created_time":(\d+)', text):
            created_time = re.findall('"created_time":(\d+)', text)[0]
            temp_pubTime = datetime.datetime.fromtimestamp(int(created_time))
            temp_pubTime = temp_pubTime.strftime("%Y-%m-%d %H:%M:%S")
            dt = temp_pubTime.split(' ')
            time = dt[1]
            myMood['time'] = time
            date = dt[0]
            myMood['date'] = date
        if re.findall('"source_name":"(.*?)"', text):
            source_name = re.findall('"source_name":"(.*?)"', text)[0]  # 获取发表的工具（如某手机）
            myMood['tool'] = source_name
        if re.findall('"pos_x":"(.*?)"', text):
            pos_x = re.findall('"pos_x":"(.*?)"', text)[0]
            pos_y = re.findall('"pos_y":"(.*?)"', text)[0]
            if pos_x:
                myMood['pos_x'] = pos_x
            if pos_y:
                myMood['pos_y'] = pos_y
            idname = re.findall('"idname":"(.*?)"', text)[0]
            myMood['idneme'] = idname
            cmtnum = re.findall('"cmtnum":(.*?),', text)[0]
            myMood['cmtnum'] = cmtnum
        return myMood


