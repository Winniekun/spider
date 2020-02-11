"""
@time : 2019/12/7下午8:17
@Author: kongwiki
@File: concurrSpider.py
@Email: kongwiki@163.com
"""
import csv
import requests
import urllib3
from bs4 import BeautifulSoup

imdbMovieBaseUrl = "https://www.imdb.com/title/tt"
timeoutInSeconds = 30

"""
获取封面图片地址
:imdbId movieId
"""


def fetchMoviePoster(imdbId):
	movieUrl = imdbMovieBaseUrl + str(imdbId)
	print("电影地址: " + movieUrl)
	http = urllib3.PoolManager()
	data = http.request('GET', movieUrl, timeout=timeoutInSeconds).data
	soup = BeautifulSoup(data, "html.parser")
	posterTag = soup.find("div", class_="poster")
	return posterTag.a.img['src']


if __name__ == '__main__':
	inputFile = open('links.csv')
	outputFile = open('records.csv', 'w')
	failedRecordFile = open("failed_records.csv", 'w')
	i = 0
	for line in inputFile:
		if i is 0:
			i = i + 1
			continue
		# 每行数据结构为：movieId,imdbId,tmdbId
		values = line.split(",")
		movieId = values[0]
		imdbId = values[1]
		print("开始获取电影的封面地址，电影id:" + movieId)
		try:
			imgUrl = fetchMoviePoster(imdbId)
			print(imgUrl)
			outputFile.write(movieId + "," + imgUrl + "\n")
		except BaseException as e:
			print('----获取电影封面地址失败:' + movieId, e)
			failedRecordFile.write(line)
			inputFile.close()
			outputFile.close()
			failedRecordFile.close()
		print("结束获取电影的封面地址，电影id::" + movieId)
	inputFile.close()
	outputFile.close()
	failedRecordFile.close()
