'''
@author：KongWeiKun
@file: wechat_spider.py
@time: 18-1-1 下午9:18
@contact: 836242657@qq.com
'''
import re

import itchat
from echarts import Echart, Legend, Pie


itchat.login()


# itchat.send(u'你好','filehelper') #以文件传输的方式发送文件
#获取好友列表
friends = itchat.get_friends(update=True)[0:]
for i in friends:
# 获取个性签名
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
# 正则匹配过滤掉emoji表情，例如emoji1f3c3等
    rep = re.compile("1f\d.+")
    signature = rep.sub("", signature)
    print(signature)
# male = female = other = 0
#
# # 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# # 1表示男性，2女性
# for i in friends[1:]:
#     sex = i["Sex"]
#     if sex == 1:
#         male += 1
#     elif sex == 2:
#         female += 1
#     else:
#         other += 1
#
# # 总数算上，好计算比例
# total = len(friends[1:])
# man = float(male) / total * 100
# women = float(female) / total * 100
# others = float(other) / total * 100
# 打印结果
# print(u"男性好友：%.2f%"%man)
# print (u"女性好友：%.2f%%"%women)
# print (u"未填性别：%.2f%%"%others)
# chart = Echart(u'%s的微信好友性别比例' % (friends[0]['NickName']), 'from WeChat')
# chart.use(Pie('WeChat',
#               [{'value': male, 'name': u'男性 %.2f%%' % (float(male) / total * 100)},
#                {'value': female, 'name': u'女性 %.2f%%' % (float(female) / total * 100)},
#                {'value': other, 'name': u'其他 %.2f%%' % (float(other) / total * 100)}],
#               radius=["50%", "70%"]))
# chart.use(Legend(["male", "female", "other"]))
# del chart.json["xAxis"]
# del chart.json["yAxis"]
# chart.plot()
