'''
@author：KongWeiKun
@file: wc.py
@time: 17-12-5 下午9:41
@contact: 836242657@qq.com
'''
import jieba
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import os
import PIL.Image as Image
import numpy as np

with open('/home/kongweikun/PycharmProjects/spider/douban/coco/coco_comments.txt','rb') as f:
    text=f.read()
    f.close()

wordlist=jieba.cut(text,cut_all=False)
#cut_all True 为全局模式 False为精准模式

wordlist_space_split=' '.join(wordlist)

d=os.path.dirname(__file__)

font='./font/simsun.ttc'
picture=np.array(Image.open(os.path.join(d,'picture.jpg')))
wordcloud=WordCloud(background_color='#F0F8FF',max_words=100,max_font_size=300,font_path=font,
                    mask=picture,random_state=42).generate(wordlist_space_split)

plt.imshow(wordcloud)            # 以图片的形式显示词云
plt.axis('off')                     # 关闭坐标轴
plt.show()

wordcloud.to_file(os.path.join(d, 'coico_movie_cloud.png'))