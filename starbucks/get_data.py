'''
@author：KongWeiKun
@file: get_data.py
@time: 18-1-2 下午1:08
@contact: 836242657@qq.com
'''
import codecs
import csv
import json
import random

import requests
import time

from starbucks.config import *
headers={
'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Connection':'keep-alive',
'Content-Length':'38',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'UM_distinctid=160b5353612722-01dcccf8ab9cbc-1d2a1f03-e1000-160b535361366c; captcha_key=a0989861109544a4a24862ce27e00cc6; token=oQ73eGlnjBaskDSjIUqFHmoA1z8nASSTwonFh1T0d1dll--q0tFA25rOhrEflqV3; gr_user_id=5cda758f-de6c-473b-8f13-4390fc9a1508; userId=20743; CNZZDATA1258752337=680637992-1514866514-https%253A%252F%252Fgeohey.com%252F%7C1514866514; gr_session_id_82de76b60c1512e9=99d5b69e-97b0-4152-b62d-b7fddfa35be0; _ga=GA1.2.1470358970.1514868656; _gid=GA1.2.1846825013.1514868656',
'Host':'geohey.com',
'Origin':'https://geohey.com',
'Referer':'https://geohey.com/public-data/gh3da25887a9995287942b5cce603f1e27/table',
'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
}
# base_url='http://geohey.com/s/public_data/'
# base_list='http://geohey.com/s/public_data/list'
# datauid='gh3da25887a9995287942b5cce603f1e27'
# ak='NGY5ZThlN2M5ZWU2NGJkNzhhMjRiYmNiMzJkNWJhMTM'
# url=base_url+datauid+'/query?ak='+ak
def get_page(url,data,timeOutRetry=5):
    try:
        response = requests.post(url,data=data,headers=headers)
        return response.text
    except Exception as e:
        if timeOutRetry > 0:
            get_page(url=url,data=data, timeOutRetry=(timeOutRetry - 1))
        print("失败")

# 获取页面的信息
def get_page_params(html):
    if not html:
        return False
    infomation = json.loads(html).get('data').get('features')# 获取json 数据
    return infomation


#写入csv
def writeCSV(filename,informations):
    info = {}
    csv_file = codecs.open(filename+'.csv','ab','utf-8','ignore')
    csv_writer=csv.writer(csv_file)
    for row  in informations:
        row = row['attrs']
        info['地址'] = row['address']
        info['品牌'] = row['brand']                        #职位城市
        info['城市'] = row['city']              #招聘职位
        info['倒闭时间'] = row['close_date']
        info['currentcy'] = row['currency']              #发布时间
        info['market'] = row['market']              #薪资待遇
        info['名字'] = row['name']              #经验要求
        info['开业时间'] = row['open_date']              #公司大小
        info['owner_type'] = row['owner_type']              #公司福利
        info['store_num'] = row['store_num']              #公司地址
        info['telephone'] = row['telephone']
        info['zipcode'] = row['zipcode']
        # print(info)

        csv_writer.writerow([row['address'],row['brand'] ,row['city'] ,row['close_date'],row['currency'],
                             row['market'],row['name'],row['open_date'] ,
                             row['owner_type'],row['store_num'],
                             row['telephone'],
                             row['zipcode']])

def main():
    url = 'https://geohey.com/s/public_data/gh3da25887a9995287942b5cce603f1e27/query'
    for i in range(995):
        data = {
            'page': i,
            'sortField': '',
            'sortType': 'DESC',
            'limit': '25',
            'offset': i*25,
            'returnGeometry': 'false'
        }
        page = get_page(url,data)
        informations = get_page_params(page)
        # for row in informations:
        time.sleep(random.random() * 5)
        print("开始爬取第%s页"%str(i+1))
        if informations ==None:
            break
        writeCSV('starbucks',informations)

if __name__ == '__main__':
    start = time.time()
    main()
    end=time.time()
    print("数据爬取完成 共用%s秒"%(end-start))
