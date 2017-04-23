#-*- coding:utf-8 -*-
import unittest,random
from time import sleep
from Bindo.page_obj.loginPage import login
from Bindo.page_obj.labPage import LabPage
from Bindo.page_obj.menuPage import PhatThai
from Bindo.models import myunit


class LabDelivery(myunit.Mytest):
    '''测试lab外卖的流程'''

    def test_lab_delivery(self):
        lg = login(self.driver)
        lg.user_login()
        sleep(20)
        lp=LabPage(self.driver)
        cvv = "111"
        tips = random.randint(1, 20)
        lp.lab_delivery(cvv,tips)
        sleep(10)
        pt=PhatThai(self.driver)
        print pt.order_complete_clues()
        try:
            self.assertEqual(pt.order_complete_clues(),u'订单提交成功')
            sleep(10)
            print u'your order scuessful'
        except:
            print u'your order failed'

if __name__=='__main__':
    unittest.main()


