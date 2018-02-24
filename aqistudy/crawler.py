'''
@author：KongWeiKun
@file: crawler.py
@time: 18-2-24 下午8:31
@contact: 836242657@qq.com
'''
import requests
import execjs
import json

# Init environment
node = execjs.get()

# Params
method = 'GETCITYWEATHER'
city = '北京'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'

# Compile javascript
file = 'encryption.js'
ctx = node.compile(open(file).read())

# Get params
js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)

# Get encrypted response text
api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})

# Decode data
js = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(js)
data = json.loads(decrypted_data)
print(data)