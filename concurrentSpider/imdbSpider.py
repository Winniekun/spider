"""
@time : 2019/12/8上午11:25
@Author: kongwiki
@File: imdbSpider.py
@Email: kongwiki@163.com
"""
import os
import csv
import time
import random
import pathlib

import requests
from lxml import etree
from requests import RequestException

imdb_movie_baseUrl = "https://www.imdb.com/title/tt"
timeoutInSeconds = 30
FILE = 'links.csv'
BASEPATH = pathlib.Path(".")


def get_page(imdb_id):
	"""
	target网页
	:param imdb_id:
	:return:
	"""
	try:
		"https://www.imdb.com/title/tt0114709"
		target_url = imdb_movie_baseUrl + str(imdb_id)
		print("正在爬取对应的url: " + target_url)
		response = requests.get(url=target_url)
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
	return url


def main(imdb_id):
	patterns = '//div[@class="poster"]/a/img/@src'
	html = get_page(imdb_id)
	imgurl = parse_page(html, patterns)
	return imgurl


if __name__ == '__main__':
	movieId = 1
	imdbId = '0114709'
	outputFile = open('records.csv', 'w')
	failedRecordFile = open("failed_records.csv", 'w')
	with open(FILE) as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			movieId = row[0]
			imdbId = row[1]
			print("开始获取电影的封面地址，电影id: {}, {}".format(movieId, imdbId))
			# print(main(imdbId))
			try:
				imgurl = main(imdbId)
				time.sleep(1 + float(random.randint(1, 20)) / 20)
				outputFile.write(movieId + "," + imgurl + "\n")
			except BaseException as e:
				print('----获取电影封面地址失败:{}, {}'.format(movieId, e))
				failedRecordFile.write(row)
	f.close()
	outputFile.close()
	failedRecordFile.close()
	print("结束获取电影的封面地址，电影id:: {}".format(movieId))
