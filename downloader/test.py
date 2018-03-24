'''
@author：KongWeiKun
@file: test.py
@time: 18-3-24 上午9:54
@contact: 836242657@qq.com
'''
# import re
# data = '/home/kongweikun/PycharmProjects/Data_Mining/data/PA_chapter3_data/wine.names'
# pattern = re.compile('.*[0-9]+\)\s?(\w+).*')
# with open(data) as f:
#     for l in f:
#         if pattern.findall(l.strip()):
#             print(pattern.findall(l.strip())[0])
import requests
from contextlib import closing
import sys

url = 'http://blog.topspeedsnail.com/wp-content/uploads/2016/05/bitcoin.pdf'
filename = url.split('/')[-1]
size = 0
with closing(requests.get(url, stream=True, verify=False)) as response:
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    if response.status_code == 200:
        sys.stdout.write('  [||%s||文件大小]:%0.2f MB\n' % ('songData', content_size / chunk_size / 1024))
        filesize = content_size
        with open(filename, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                print('  [下载进度]:%.2f%%' % float(size / content_size * 100))
                size += len(data)
                file.flush()

            sys.stdout.write('    [下载进度]:%.2f%%' % float(size / content_size * 100))
            sys.stdout.flush()