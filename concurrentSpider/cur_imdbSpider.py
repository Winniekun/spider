"""
@time : 2019/12/8下午4:56
@Author: kongwiki
@File: cur_imdbSpider.py
@Email: kongwiki@163.com
"""
import os
import csv
import time
import random
import pathlib

import threading
from threading import Thread
from multiprocessing.pool import ThreadPool

import requests
from requests import Session
from lxml import etree
from requests import RequestException

BASEURl = "https://www.imdb.com/title/tt"
FILE = 'links.csv'
BASEPATH = pathlib.Path(".")
PROXY_POOL_URL = 'http://localhost:5002/random'
lock = threading.Lock()



def get_proxy():
	"""
	从代理池获取代理
	:return:
	"""
	try:
		response = requests.get(PROXY_POOL_URL)
		if response.status_code == 200:
			print('Get Proxy', response.text)
			return response.text
		return None
	except requests.ConnectionError:
		return None


def get_page(imdb_id, proxy):
	"""
	target网页
	:param imdb_id:
	:return:
	"""
	try:
		session = Session()
		proxies = {
			'http': 'http://' + proxy,
			'https': 'https://' + proxy
		}
		target_url = BASEURl + str(imdb_id)
		print("正在爬取对应的url: " + target_url)
		response = session.get(url=target_url, proxies=proxies)
		if response.status_code == 200:
			return response.text
		return "被禁"
	except RequestException:
		return "网络问题"


def parse_page(content, patterns):
	"""
	抓取网页内容
	:param content: requests.content
	:param patterns: xpath对应的规则
	:return:
	"""
	tree = etree.HTML(content)
	url = tree.xpath(patterns)
	# print("图片地址 {}".format(url[0]))
	return url[0]


def write2file(filename, contents):
	with open(filename, 'w') as f:
		lock.acquire()
		print("写入内容为: {}".format(contents))
		f.write(contents + '\n')
		lock.release()
	f.close()


def main(imdb_id, id):
	print("开始获取电影的封面地址，电影id:{}, {}".format(id, imdb_id))
	# print(main(imdbId))
	try:
		proxy = get_proxy()
		patterns = '//div[@class="poster"]/a/img/@src'
		html = get_page(imdb_id, proxy)
		imgurl = parse_page(html, patterns)
		time.sleep(1 + float(random.randint(1, 20)) / 20)
		contents = id + "," + imgurl
		write2file("records.csv", contents)
	except BaseException as e:
		print('----获取电影封面地址失败:{}, {}'.format(id, e))
		contents = id + imdb_id
		write2file("failed_records.csv", contents)
	print("结束获取电影的封面地址，电影id:: {}".format(id))


def user_thread():
	threads = []
	with open(FILE) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			imdb_id = row[1]
			id = row[0]
			t = Thread(target=main, args=(imdb_id, id))
			t.setDaemon(True) # 守护线程
			threads.append(t)
			t.start()

		for t in threads:
			t.join()
	f.close()


if __name__ == '__main__':
	start = time.time()
	user_thread()
	print("共耗时: {}".format(time.time() - start))
# get_proxy()
