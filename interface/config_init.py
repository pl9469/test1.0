from configparser import  *
import os


class Config():
    def __init__(self):
        self.config=ConfigParser()
        self.conf_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
        self.config.read(self.conf_path,encoding='utf-8-sig')
        self.conf = {'host':'','user':'','passwords':'','test_db':'','url':''}

    def Config_set(self):
        self.conf['host']=self.config.get('test_db','host')
        self.conf['user']=self.config.get('test_db','user')
        self.conf['passwords']=self.config.get('test_db','passwords')
        self.conf['test_db']=self.config.get('test_db','database')
        self.conf['url']=self.config.get('url','web')
        self.conf['status']=self.config.get('code','success')
        return self.conf



if __name__=='__main__':
    t=Config()
    print(t.Config_set())



