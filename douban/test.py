'''
@author：KongWeiKun
@file: test.py
@time: 17-10-2 下午3:56
@contact: 836242657@qq.com
'''
import re
file='/home/kongweikun/PycharmProjects/spider/douban/starbucks_result.txt'
content=open(file)
    # url='https://movie.douban.com/subject/26759539/?from=tag_all'
    # html=get_page(url)
    # comment=get_comment(html)
    # for row in comment:
    #     print(row.strip())
for row in content:
    pattern = re.compile('[a-zA-z]+://[^\s,"]*')
    pattern1 = re.compile('https://movie.douban.com/subject/\d+.*?tag_all')
    url = re.findall(pattern, row)
