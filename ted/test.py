'''
@author：KongWeiKun
@file: test.py
@time: 18-3-26 下午9:28
@contact: 836242657@qq.com
'''
import re

target = {"id":12459,"talk":"rei_my_mama_black_banana","tag":"guitar,live music,music,performance,singer","year":"2017","event":"TEDNYC"}
print(str(target))
pattern = re.compile("'id':(\d+)",re.S)
video_id = re.findall(pattern, str(target))[0]
video_tags = re.findall("'tag':\s*'(.*?)'", str(target))
print(video_id)
print(video_tags)