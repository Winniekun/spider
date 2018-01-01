'''
@author：KongWeiKun
@file: wordcloud.py
@time: 18-1-1 下午9:42
@contact: 836242657@qq.com
'''
'''
签名词云
'''
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import numpy as np
import jieba
with open('signature.txt','rb') as f:
    text=f.read()
    f.close()
wordlist_jieba = jieba.cut(text, cut_all=True)
wl_space_split = " ".join(wordlist_jieba)

# wordcloud词云



d = os.path.dirname(__file__)
alice_coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))
# 这里要选择字体存放路径，这里是Mac的，win的字体在windows／Fonts中
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         max_font_size=40, random_state=42,
                         mask=alice_coloring,
                         font_path='/home/kongweikun/PycharmProjects/spider/weixin/font/simsun.ttc').generate(wl_space_split)

plt.imshow(my_wordcloud)
image_colors = ImageColorGenerator(alice_coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.axis("off")
plt.show()
my_wordcloud.to_file(os.path.join(d, 'signature_cloud.png'))