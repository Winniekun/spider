'''
@author：KongWeiKun
@file: test.py
@time: 18-3-24 上午9:54
@contact: 836242657@qq.com
'''
import requests
from contextlib import closing
import sys
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip'
filename = url.split('/')[-1]
size = 0
count = 0
# with closing(requests.get(url, stream=True, verify=False)) as response:
#     chunk_size = 1024
#     # print(response.headers)
#     content_size = int(response.headers['content-length'])
#     if response.status_code == 200:
#         sys.stdout.write(' %s 文件大小为 :%0.2f MB\n' % (filename, content_size / chunk_size / 1024))
#         filesize = content_size
#         with open(filename, "wb") as file:
#             for data in response.iter_content(chunk_size=chunk_size):
#                 file.write(data)
#                 count += 1
#                 size += len(data)
#                 file.flush()#刷新缓存区
#                 if count%100 == 0:
#                     print('下载进度:%.3f%% 还有%.3f没下完' % (float(size / content_size * 100),(1-(float(size / content_size * 100)))))
