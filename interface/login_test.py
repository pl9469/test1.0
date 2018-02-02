import  unittest
import  common_func
import  config_init
import  requests
import  json




class Login(unittest.TestCase):
    def setUp(self):
       self.msg=common_func.Common()
       for row in self.msg:
           self.uname=row[0]
           self.passwords=row[1]
       c=config_init.Config().Config_set()
       self.url=c['url']
       self.code=c['status']


    def test_login(self):
        data1={
            'username':self.uname,
            'password':self.passwords,
            'verify':'',
            'remember':'1',
            'pwencode':'1',
            'browser_key':'a2195e87ffa284cd8dd91948aa04f255',
            'referer': 'referer'
             }
        result=requests.post(self.url,data=data1)
        r=json.loads(result.text)
        print(r)
        self.assertEqual(r['status'],int(self.code))





    def tearDown(self):
        print('test,over!')
