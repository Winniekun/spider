'''
@author：KongWeiKun
@file: douyinCrawler.py
@time: 18-3-1 下午8:11
@contact: 836242657@qq.com
'''
from bs4 import BeautifulSoup
from contextlib import closing
import requests, json, time, re, os, sys, time
from requests.exceptions import  RequestException


class DouYin:

    def __init__(self):
        pass

    def get_video_urls(self,user_id):
        video_names = []
        video_urls = []
        unique_id = ''
        while unique_id != user_id:
            serch_url = 'https://aweme.snssdk.com/aweme/v1/discover/search/?iid=27107052549&device_id=46724623936&os_api=18&app_name=aweme&channel=App%20Store&idfa=27A02899-57FC-4215-9A22-E23B35586609&device_platform=iphone&build_number=17502&vid=9BAC598A-CE7C-4561-9F57-BE103E368C06&openudid=42dd301bd6fd8051135bc01cc03146eeb58da1a4&device_type=iPhone6,2&app_version=1.7.5&version_code=1.7.5&os_version=11.2.5&screen_width=640&aid=1128&ac=WIFI&count=20&cursor=0&keyword={}&search_source=discover&type=1&mas=0088e1ffec4e20b6872aac69456ca4c9ec62e7bbf4078bb6c9d0c8&as=a1256e291b9cfad8170178&ts=1519904971'.format(user_id)
            response = requests.get(serch_url,verify=False)#SSL认证False
            html = json.loads(response.text)
            aweme_count = html['user_list'][0]['user_info']['aweme_count']
            uid = html['user_list'][0]['user_info']['uid']
            nickname = html['user_list'][0]['user_info']['nickname']
            unique_id = html['user_list'][0]['user_info']['unique_id']
        user_url = 'https://www.douyin.com/aweme/v1/aweme/post/?user_id=%s&max_cursor=0&count=%s' % (uid, aweme_count)
        req = requests.get(url=user_url, verify=False)
        html = json.loads(req.text)
        i = 1
        for each in html['aweme_list']:
            share_desc = each['share_info']['share_desc']
            if '抖音-原创音乐短视频社区' == share_desc:
                video_names.append(str(i) + '.mp4')
                i += 1
            else:
                video_names.append(share_desc + '.mp4')
            video_urls.append(each['share_info']['share_url'])
        print(len(video_urls))
        return video_names, video_urls, nickname

    def get_download_url(self, video_url):
        """
        获得视频播放地址
        Parameters:
            video_url：视频播放地址
        Returns:
            download_url: 视频下载地址
        """
        req = requests.get(url=video_url, verify=False)
        bf = BeautifulSoup(req.text, 'lxml')
        script = bf.find_all('script')[-1]
        video_url_js = re.findall('var data = \[(.+)\];', str(script))[0]
        video_html = json.loads(video_url_js)
        download_url = video_html['video']['play_addr']['url_list'][0]
        return download_url

    def video_downloader(self, video_url, video_name):
        """
        视频下载
        Parameters:
            None
        Returns:
            None
        """
        size = 0
        with closing(requests.get(video_url, stream=True, verify=False)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                sys.stdout.write('  [文件大小]:%0.2f MB\n' % (content_size / chunk_size / 1024))

                with open(video_name, "wb") as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
                        size += len(data)
                        file.flush()

                    sys.stdout.write('    [下载进度]:%.2f%%' % float(size / content_size * 100))
                    sys.stdout.flush()
        time.sleep(1)

    def run(self):
        """
        运行函数
        Parameters:
            None
        Returns:
            None
        """
        self.hello()
        user_id = 'Fengtimo1219'
        video_names, video_urls, nickname = self.get_video_urls(user_id)
        if nickname not in os.listdir():
            os.mkdir(nickname)
        sys.stdout.write('视频下载中:\n')
        for num in range(len(video_urls)):
            print('  %s\n' % video_urls[num])
            video_url = self.get_download_url(video_urls[num])
            if '\\' in video_names[num]:
                video_name = video_names[num].replace('\\', '')
            elif '/' in video_names[num]:
                video_name = video_names[num].replace('/', '')
            else:
                video_name = video_names[num]
            self.video_downloader(video_url, os.path.join(nickname, video_name))
            print('')

    def hello(self):
        print('**********抖音视频下载助手**********')
        print('**********************************')
        print('**********************************')

if __name__ == '__main__':
    douyin = DouYin()
    douyin.run()