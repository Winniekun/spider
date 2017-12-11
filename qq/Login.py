'''
@author：KongWeiKun
@file: test.py
@time: 17-11-22 下午4:30
@contact: 836242657@qq.com
'''
from selenium import webdriver
import time
import re


#获取cookie,g_tk,g_qzontoken这三个数据
def Login_QQ():
    '''gtk解密'''
    def getGTK(cookie):
        """ 根据cookie得到GTK """
        hashes = 5381
        for letter in cookie['p_skey']:
            hashes += (hashes << 5) + ord(letter)
        gtk=hashes&0x7fffffff
        return gtk

    browser=webdriver.Chrome()
    url = "https://qzone.qq.com/"  # QQ登录网址
    browser.get(url)

    browser.switch_to.frame('login_frame')
    browser.find_element_by_id('switcher_plogin').click()

    browser.find_element_by_id('u').clear()
    browser.find_element_by_id('u').send_keys('')  # 这里填写你的QQ号
    browser.find_element_by_id('p').clear()
    browser.find_element_by_id('p').send_keys('')  # 这里填写你的QQ密码

    browser.find_element_by_id('login_button').click()
    time.sleep(1)
    print(browser.title)  # 打印网页标题
    # print(browser.get_cookies())
    cookie={}
    for element in browser.get_cookies():
        cookie[element['name']]=element['value']
    print('Get the cookie of QQlogin successfully!(共%d个键值对)' % (len(cookie)))
    print(cookie)
    html = browser.page_source  # 保存网页源码
    pattern = re.compile(r'window\.g_qzonetoken = \(function\(\)\{ try\{return "(.*?)";\}')
    g_qzonetoken=re.search(pattern,html)
    print(g_qzonetoken.group(1))
    gtk=getGTK(cookie)#通过getGTK函数计算gtk
    return (cookie,gtk,g_qzonetoken)


if __name__ == '__main__':
    Login_QQ()

