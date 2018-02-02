import os,sys
sys.path.append('E:/Project/interface')
import unittest
import HTMLTestRunner
import config_init
import time


test_dir='E:/Project/interface'

file=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

if  __name__=='__main__':
    config_init.Config().Config_set()
    now_time=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime(time.time()))
    path=os.path.dirname(os.path.abspath(sys.argv[0]))
    filename=path+'\\Report\\'+now_time+'report.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='接口测试报告',
        description='详细描述如下：'
    )
    runner.run(file)
    fp.close()

