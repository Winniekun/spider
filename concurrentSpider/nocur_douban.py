"""
@time : 2019/12/8下午4:39
@Author: kongwiki
@File: nocur_douban.py
@Email: kongwiki@163.com
"""
import time

import requests
import re
from threading import Thread
from bs4 import BeautifulSoup as bs


def fetch(url):
	s = requests.Session()
	s.headers.update({"user-agent": user_agent})
	return s.get(url)


def title_get(url):
	try:
		result = fetch(url)
	except requests.exceptions.RequestException:
		return False
	html = bs(result.text, 'lxml')
	title_list = html.select('div.pic > a > img')
	'''
   title_list中的元素格式如下 e.g: 
	<img alt="这个杀手不太冷" class="" src="https://img3.doubanio.com
	/view/movie_poster_cover/ipst/public/p511118051.jpg"/
   '''

	try:
		title = [re.findall(r'alt="(.*?)"', str(title))[0] for title in title_list]
	except IndexError:
		pass
	print(title)
	return title


def not_use_thread():
	for page in range(0, 250, 25):
		url = 'https://movie.douban.com/top250?start={}&filter='.format(page)
		title_get(url)


if __name__ == '__main__':
	user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
	start = time.time()
	not_use_thread()
	print("共耗时{}".format(time.time() - start))