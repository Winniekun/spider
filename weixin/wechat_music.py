'''
@author：KongWeiKun
@file: wechat_music.py
@time: 18-1-2 上午11:22
@contact: 836242657@qq.com
'''
'''
通过微信调用网易
'''
import sys,subprocess
import itchat
from NetEaseMusicApi import interact_select_song
# 第三方包通过该命令安装：pip install itchat, NetEaseMusicApi

HELP_MSG = u'''\
欢迎使用微信网易云音乐
帮助： 显示帮助
关闭： 关闭歌曲
歌名： 按照引导播放音乐\
'''
music = './music/somedreams.mp3'

with open(music, 'w') as f: pass
def close_music():
    subprocess.call(["open",music])

@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper': return
    if msg['Text'] == u'关闭':
        close_music()
        itchat.send(u'音乐已关闭', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(HELP_MSG, 'filehelper')
    else:
        itchat.send(interact_select_song(msg['Text']), 'filehelper')

itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run()