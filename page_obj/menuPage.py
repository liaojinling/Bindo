#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class PhatThai(Page):
    url=''

    phat_thai_path = ".//ion-grid[@class='menu-grid grid']/ion-row/ion-col[2]/menu-cell/button"
    phat_thai_path_loc=(By.XPATH,phat_thai_path)

    # phat_thai点击
    def phat_thai_menu(self):
        self.find_element(*self.phat_thai_path_loc).click()
        sleep(5)

    plus_mask_loc=(By.CLASS_NAME,'minus-mask')

    #添加购物
    def plus_mask(self):
        self.find_element(*self.plus_mask_loc).click()
        sleep(5)


    cart_button_loc=(By.CLASS_NAME,'cart_button')

    #结账button1
    def cart_button1(self):
        self.find_element(*self.cart_button_loc).click()
        sleep(5)

    cart_button_path="html/body/ion-app/ng-component/ion-nav/ng-component[2]/ion-footer/button"
    cart_button_loc2=(By.XPATH,cart_button_path)

    #结账button2
    def cart_button2(self):
         self.find_element(*self.cart_button_loc2).click()
         sleep(5)


    take_out_path=".//div[@class='scroll-content']/div[2]/button/img"
    take_out_loc=(By.XPATH,take_out_path)

    #外卖元素
    def take_out(self):
         self.find_element(*self.take_out_loc).click()
         sleep(5)

    picker_opt=".//div[@class='picker-col']/div/button[2]"
    picker_opt_loc=(By.XPATH,picker_opt)

    #选择eastside(japanese counter)
    def eastside(self):
         self.find_element(*self.picker_opt_loc).click()
         sleep(5)

    button_inner=".//div[@class='picker-wrapper']/div/div[2]/button"
    button_inner_loc=(By.XPATH,button_inner)

    #下一步
    def choice_next(self):
         self.find_element(*self.button_inner_loc).click()
         sleep(5)

    picker_col=".//div[@class='picker-col']/div/button[3]"
    picker_col_loc=(By.XPATH,picker_col)

    #选择快递时间
    def Choose_delivery_time(self):
         self.find_element(*self.picker_col_loc).click()
         sleep(5)

    complete_button=".//div[@class='picker-toolbar']/div[2]/button"
    complete_button_loc=(By.XPATH,complete_button)

    #完成按钮
    def complete_butt(self):
         self.find_element(*self.complete_button_loc).click()
         sleep(5)

    payment_method=".//div[@class='payment-method__credit-cards']/ion-item/div/ion-radio/button"
    payment_method_loc=(By.XPATH,payment_method)

    #选择支付方式
    def choice_payment_method(self):
         self.find_element(*self.payment_method_loc).click()
         sleep(5)

    cvv_path=".//ion-grid[@class='theme-font grid']/ion-row/ion-col[3]/ion-item/div/div/ion-input/input"
    cvv_path_loc=(By.XPATH,cvv_path)

    #输入cvv码
    def input_cvv(self,cvv_code):
         self.find_element(*self.cvv_path_loc).send_keys(cvv_code)
         sleep(5)

    tips_path="html/body/ion-app/ng-component/ion-nav/ng-component[4]/ion-footer/ion-list/ion-item[2]/div[1]/div/ion-input/input"
    tips_path_loc=(By.XPATH,tips_path)

    #输入小费
    def input_tips(self,your_tip):
         self.find_element(*self.tips_path_loc).send_keys(your_tip)
         sleep(5)

    payment_button=".//div[@class='toolbar-content toolbar-content-md']/ion-grid/ion-row/ion-col/button"
    payment_button_loc=(By.XPATH,payment_button)

    #支付按钮
    def payment(self):
         self.find_element(*self.payment_button_loc).click()
         sleep(5)

    order_complete="html/body/ion-app/ng-component/ion-nav/ng-component[5]/ion-header/ion-navbar/div[2]/ion-title/div"
    order_complete_loc=(By.XPATH,order_complete)

    #订单完成提示
    def order_complete_clues(self):
         self.find_element(*self.order_complete_loc).text
         sleep(5)

    #定义phatthai外卖
    def delivery(self,cvv_code,your_tip):
        self.phat_thai_menu()
        sleep(5)
        self.plus_mask()
        sleep(5)
        self.cart_button1()
        sleep(5)
        self.cart_button2()
        sleep(5)
        self.take_out()
        sleep(5)
        self.eastside()
        sleep(5)
        self.choice_next()
        sleep(5)
        self.Choose_delivery_time()
        sleep(5)
        self.complete_butt()
        sleep(5)
        self.choice_payment_method()
        sleep(5)
        self.input_cvv(cvv_code)
        sleep(5)
        self.input_tips(your_tip)
        sleep(5)
        self.payment()
        sleep(5)



















