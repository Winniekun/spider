'''
@author  : kongweikun
@file    : seleniumTest.py
@time    : 18-6-15 下午7:02
@contact : kongwiki@163.com
'''
"""
百度文库爬取
"""
import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("kongwiki")
driver.find_element_by_id("su").click()
