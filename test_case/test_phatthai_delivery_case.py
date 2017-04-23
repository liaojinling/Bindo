#-*- coding:utf-8 -*-
import unittest,random
from time import sleep
from Bindo.page_obj.loginPage import login
from Bindo.page_obj.menuPage import PhatThai
from Bindo.models import myunit


class Delivery(myunit.Mytest):
    '''测试送外卖的流程步骤'''

    def test_delivery(self):
        lg=login(self.driver)
        lg.user_login()
        sleep(20)
        pt=PhatThai(self.driver)
        cvv="111"
        tips=random.randint(1,20)
        pt.delivery(cvv,tips)
        sleep(10)
        try:
            self.assertEqual(pt.order_complete_clues(),u'订单提交成功')
            sleep(10)
            print u'your order scuessful'
        except:
            print u'your order failed'


if __name__=='__main__':
    unittest.main()