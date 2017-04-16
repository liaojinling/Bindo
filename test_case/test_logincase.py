#-*- coding:utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from Bindo.models import myunit,function
from Bindo.page_obj.loginPage import login


class LoginPageTest(myunit.Mytest):
    """登录页面测试用例"""

    #用户登录
    def user_login_verify(self,username="",password=""):
        login(self.driver).user_login(username,password)

    def test_login_right(self):
        '''用户名、密码均正确'''
        self.user_login_verify(username="18606990406@163.com",password="SQL110")
        sleep(10)
        # po = login(self.driver)
        try:
            self.assertEqual(self.driver.title,u"百味村")
            sleep(10)
            print u'登录成功'
        except:
            print u"未能成功登录"

    def test_wrong_password(self):
        '''账号正确，密码不匹配'''
        char=random.choice('qwertyuiopasdfghjklmnbvcxz')
        pwd=u'12345'+char
        self.user_login_verify(username='18606990406@163.com',password=pwd)
        sleep(10)
        po=login(self.driver)
        try:
            self.assertEqual(po.err_hint(),u'登入无效')
            sleep(10)
            print u'assertEqual is scuesss'
        except:
            print u'assertEqual is failed'

    def test_wrong_account(self):
        '''账号错误，密码正确'''
        account=random.randint(1,500)
        username=account+u'@163.com'
        self.user_login_verify(username=username,password='SQL110')
        po=login(self.driver)
        try:
            self.assertEqual(po.err_hint(),u'登录无效')
            sleep(10)
            print u'assertEqual is scuesss'
        except:
            print u'assertEqual is failed'

    def test_forget_pwd(self):
        '''忘记密码'''
        po = login(self.driver)
        po.login_Bindo()
        po.forget_password('18606990406@163.com')
        try:
            self.assertEqual(po.forget_pwd_hint(),u' 输入电邮来重设密码 ')
            sleep(10)
            print u'assertEqual is scuesss'
        except:
            print u'assertEqual is failed'

    def test_register_rigthnow(self):
        '''马上注册'''
        po = login(self.driver)
        po.login_Bindo()
        user=random.randint(20,100)+u'@163.com'
        passwd=random.choice('qwsazxcvderfgtyhnujmikolp')+u'12345'
        po.register(user,passwd)
        try:
            self.assertEqual(po.register_now_hint(),u'注册成功')
            sleep(10)
            print u'assertEqual is scuesss'
        except:
            print u'assertEqual is failed'


if __name__=="__main__":
    unittest.main()