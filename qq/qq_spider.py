'''
@author：KongWeiKun
@file: qq_spider.py
@time: 17-11-23 上午11:06
@contact: 836242657@qq.com
'''
import pymysql
import re
import requests
import datetime
from qq.Login import Login_QQ
from qq.getFriends import getFriends
from qq.mood import parse_mood

host='localhost'
user=''
pwd=''
db=''

con=pymysql.connect(host,user,pwd,db,use_unicode=True, charset="utf8")#可中文入库
cursor=con.cursor()
con.autocommit(True)

# 伪造浏览器头
headers = {
    'Host': 'user.qzone.qq.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://user.qzone.qq.com/836242657',
    'Connection': 'keep-alive'
}

cookie,gtk,qzonetoken=Login_QQ()#通过登录函数取得cookies，gtk，qzonetoken
s=requests.session()#用requests初始化会话

friends=getFriends()

for qq in friends:#遍历qq号列表
    for p in range(0,1000):
        pos=p*20
        params={
        'uin':qq,
        'ftype':'0',
        'sort':'0',
        'pos':pos,
        'num':'20',
        'replynum':'100',
        'g_tk':gtk,
        'callback':'_preloadCallback',
        'code_version':'1',
        'format':'jsonp',
        'need_private_comment':'1',
        'qzonetoken':qzonetoken,
        'g_tk': gtk
        }

        response=s.request('GET','https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?',params=params,headers=headers,cookies=cookie)
        if response.status_code==200:
            text=response.text

            if not re.search('lbs',text):#通过lbs判断此qq的说说是否爬取完毕
                print("%s说说爬取完毕"%qq)
                break
            textlist=re.split('\{"certified"', text)[1:]
            for i in textlist:
                myMood=parse_mood(i)

                '''将提取的字段值插入mysql数据库，通过用异常处理防止个别的小bug中断爬虫，开始的时候可以先不用异常处理判断是否能正常插入数据库'''
                try:
                    # #去重
                    # same_sql = '''
                    #     select %s from mood
                    # '''
                    # cursor.execute(same_sql,myMood['id'])
                    # if  cursor.fetchall():
                    #     print("已经爬过该说说")
                    insert_sql = '''
                                          insert into mood(id,content,time,sitename,pox_x,pox_y,tool,comments_num,date,isTransfered,name)
                                          VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                                       '''
                    cursor.execute(insert_sql, (
                    myMood['id'], myMood["Mood_cont"], myMood['time'], myMood['idneme'], myMood['pos_x'],
                    myMood['pos_y'], myMood['tool'], myMood['cmtnum'], myMood['date'], myMood["isTransfered"],
                    myMood['name']))

                except:
                    pass

print('说说全部下载完成！')


