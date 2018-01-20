'''
@author：KongWeiKun
@file: data_to_mysql.py
@time: 18-1-20 下午1:44
@contact: 836242657@qq.com
'''
import pymysql
# import setting
import time
import logger

class Mysql:
    host = 'localhost'
    user = 'root'
    pwd = 'Hanhuan.0214'
    db = 'wangyi'

    #获取当前时间
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))

    #数据库初始化
    def __init__(self):

        try:
            self.con = pymysql.connect(self.host,
                                      self.user,
                                      self.pwd,
                                      self.db,
                                    use_unicode=True, charset="utf8")
            self.con.autocommit(True)
            self.cursor = self.con.cursor()
        except pymysql.Error as e :
            print('错误')

    #入库
    def insertData(self,table,my_dict):
        try:
            cols = ','.join(my_dict.keys())
            print(cols)
            values = '","'.join(my_dict.values())
            sql = "insert into %s (%s) values (%s)"%(table,cols,'"'+values+'"')

            try:
                result = self.cursor.execute(sql)
                insert_id = self.con.insert_id()
                #判断成功
                if result:
                    return insert_id
                else:
                    return 0
            except pymysql.Error as e:
                # 发生错误时回滚
                self.con.rollback()
                # 主键唯一，无法插入
                if "key 'PRIMARY'" in e.args[1]:
                    print('数据已存在')
                else:
                    print('数据已存在')
                return -1

        except pymysql.Error as e:
            print('链接错误')
            return -1

if __name__ == '__main__':
    d = Mysql()
    commentData = {
        'id': '1',
        'user': '1',
        'content': '你好',
        'likecount': '1'
    }
    # cols = ', '.join(commentData.keys())
    # print(cols)
    values = '","'.join(commentData.values())
    print(values)
    # d.insertData('comments', commentData)