'''
@author：KongWeiKun
@file: another.py
@time: 18-3-24 下午3:45
@contact: 836242657@qq.com
'''
import sys
import requests
import threading
import datetime

# 传入的命令行参数，要下载文件的url
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00203/YearPredictionMSD.txt.zip'


def Handler(start, end, url, filename):
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    r = requests.get(url, headers=headers, stream=True)
    print("本次写入的大小为%.3f"%float(int(r.headers['content-length'])/1024/1024))
    # 写入文件对应位置
    with open(filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        for data in r.iter_content(chunk_size=1024):
            fp.write(data)



def download_file(url, num_thread=10):
    r = requests.head(url)
    try:
        file_name = url.split('/')[-1]
        file_size = int(
            r.headers['content-length'])  # Content-Length获得文件主体的大小，当http服务器使用Connection:keep-alive时，不支持Content-Length
    except:
        print("检查URL，或不支持对线程下载")
        return
    sys.stdout.write(' %s 文件大小为 :%0.2f MB\n' % (file_name, file_size / 1024 / 1024))
    # 创建一个和要下载文件一样大小的文件
    fp = open(file_name, "wb")
    #创建文件
    fp.truncate(file_size)
    fp.close()

    # 启动多线程写文件
    print("创建多线程写入文件")
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    print("共分为{}part".format(part))
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:  # 最后一块
            end = file_size
        else:
            end = start + part
        print("开始为{}结束为{}".format(start,end))
        t = threading.Thread(target=Handler, kwargs={'start': start, 'end': end, 'url': url, 'filename': file_name})
        t.setDaemon(True)
        t.start()

    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('%s 下载完成' % file_name)


if __name__ == '__main__':
    start = datetime.datetime.now().replace(microsecond=0)
    download_file(url)
    end = datetime.datetime.now().replace(microsecond=0)
    print("用时: ", end='')
    print(end - start)