import config_init
import pymysql
import requests
import json


def Common():
#初始化配置

   c=config_init.Config().Config_set()
   db_host=c['host']
   db_user=c['user']
   db_passwords=c['passwords']
   db_test_db=c['test_db']

#连接数据库

   conn=pymysql.connect(host=db_host,user=db_user,password=db_passwords,database=db_test_db)
   cursor=conn.cursor()
   sql='select name,passwords from userinfo'
   cursor.execute(sql)
   usr_result=cursor.fetchall()
   cursor.close()
   return usr_result
   print(usr_result)

# def Get_cookie():
#     c = config_init.Config.setup()
#     db_url=c['url']
#     for row in usr_result:
#         uname=row[0]
#         psd=row[1]
#         datalist={'username':uname,'passwords':psd}
#         head = {'Content-Type': 'application/Json'}
#         response = requests.post(db_url, data=datalist, headers=head)
#         uid=response.cookie.get('uid')
#         return=uid








