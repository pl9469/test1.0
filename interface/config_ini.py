from  configparser import *
#配置文件
config = ConfigParser()
'''写入参数'''
config.add_section('test_db')
config.set('test_db','host','192.168.181.128')
config.set('test_db','user','root')
config.set('test_db','passwords','root')
config.set('test_db','database','test_pl')

config.add_section('url')
config.set('url','web','https://www.imooc.com/passport/user/prelogin')


config.add_section('code')
config.set('code','success','10001')

'''写入文件'''
config.write(open('config.ini','w'))
