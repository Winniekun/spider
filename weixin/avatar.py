'''
@author：KongWeiKun
@file: avatar.py
@time: 18-1-13 上午11:38
@contact: 836242657@qq.com
'''
import re
import os

import itchat
from PIL import Image


# 获取好友信息并取出图片
def get_friend_imgs(save_path, get_img_nums=160):
    # 创建存储图片路径
    if os.path.exists(save_path):
        save_path = input(u'该路径已存在，请输入其他目录路径: ')
    os.mkdir(save_path)
    # 获取好友列表
    friends = itchat.get_friends()
    if get_img_nums > len(friends):
        get_img_nums = len(friends)
        print(u'需要获取的图片数量大于好友数量，取好友数量： %s' % len(friends))
    for num, friend in enumerate(friends):
        friend_name = friend['NickName'] or friend['UserName']
        # 好友名字中带空格的用下划线替代
        friend_name = re.sub(r'[\s+]', '_', friend_name)
        friend_img = itchat.get_head_img(userName=friend['UserName'])
        with open(save_path + '/' + friend_name + str(num+1).zfill(3) + '.jpg', 'wb') as f:
            print(u'正在写入 %s 的图像, 还要写入 %s 个' % (friend_name, get_img_nums-num))
            f.write(friend_img)
        if num > get_img_nums:
            print(u'%s 个图片写入完毕' % get_img_nums)
            break


def generate_image(path, gen_filename='multi_img', row_num=10):
    # 确定文件中可用的拼接图片数量
    images = os.listdir(path)
    # 图片缩略尺寸
    slide_size = int(640/row_num)
    thum_size = (slide_size, slide_size)
    # 创建画布
    toImage = Image.new('RGB', (640, 768))
    # 创建画布游标
    x = 0; y = 0
    # 未写入的图片
    invilid_imgs = []
    for num, img in enumerate(images):
        if img.endswith('.jpg'):
            print(u'写入第 {} 个图片; 图片名为: {}'.format(num, img))
            img = path + '/' + img
            try:
                im = Image.open(img)
                im = im.convert('RGB')

            except OSError:
                print(u'%s 未写入' % img)
                invilid_imgs.append(img)
                continue
            # 每行放`row_num`数量图片后，每个图片的尺寸
            if im.size != thum_size:
                thum_im = im.resize(thum_size, Image.ANTIALIAS)
            else:
                thum_im = im
            toImage.paste(thum_im, (x * slide_size, y * slide_size))
            x += 1
            if x == row_num:
                x = 0
                y += 1
    print(u'未写入的图片有: {}'.format(' --|-- '.join(invilid_imgs)))
    # 保存图片
    toImage.save(path + '/' + gen_filename + '.jpg')
    print(u'生成的文件位于: {}; 名为: {}'.format(path, gen_filename + '.jpg'))


if __name__ == '__main__':
    # itchat.auto_login()
    path = 'friend_avatar'
    # get_friend_imgs(path)
    generate_image(path)