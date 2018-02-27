'''
@author：KongWeiKun
@file: tkinter_test02.py
@time: 18-2-27 下午12:02
@contact: 836242657@qq.com
'''
from tkinter import *
import tkinter as tk

root = Tk(className="dsf")
li = ['C','Python','php','html','SQL','java']
movie = ['css','jquery','bootstrap']
listb = Listbox(root)   #  创建两个列表组件
listb2 = Listbox(root)
for item in li:   # 第一个小部件插入数据
    listb.insert(0,item)
for item in movie:   # 第一个小部件插入数据
    listb2.insert(0,item)

listb.pack()    # 将小部件放置到主窗口中
listb2.pack()
root.mainloop()     # 进入消息循环