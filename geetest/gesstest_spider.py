'''
@author：KongWeiKun
@file: gesstest_spider.py
@time: 17-12-26 下午1:47
@contact: 836242657@qq.com
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


EMAIL = 'kongwiki@163.com'
PASSWORD = 'kWK970214'

class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser,20)
        self.email = EMAIL
        self.password = PASSWORD

    def __del__(self):
        self.browser.close()

    def get_geetset_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        botton = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'geetest_radar_tip')))
        return botton

    def get_positon(self):
        """
        获取验证码的位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'')))

if __name__ == '__main__':
    crack = CrackGeetest()
    botton = crack.get_geetset_button()
    botton.click()