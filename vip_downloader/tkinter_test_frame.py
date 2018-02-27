'''
@author：KongWeiKun
@file: tkinter_test_frame.py
@time: 18-2-27 下午12:34
@contact: 836242657@qq.com
'''
import tkinter as tk

root = tk.Tk(className='Frame测试')
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame1.pack()
frame2.pack()
root.mainloop()