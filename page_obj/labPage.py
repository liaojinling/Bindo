#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep
from Bindo.page_obj.menuPage import PhatThai


class LabPage(Page):

    lab_path=".//ion-grid[@class='menu-grid grid']/ion-row[4]/ion-col[2]/menu-cell/button"
    lab_path_loc=(By.XPATH,lab_path)

    #点击lab菜单
    def lab_menu(self):
        self.find_element(*self.lab_path_loc).click()
        sleep(5)

    lab_minus_mask_loc=(By.CLASS_NAME,'minus-mask')

    #添加lab购物车
    def lab_minus_mask(self):
        self.find_element(*self.lab_minus_mask_loc).click()
        sleep(5)

    temperature_path=".//ion-list[@class='modifier-selector__criterias list list-md']/ion-list/ion-item/div/div/ion-label/div"
    temperature_path_loc=(By.XPATH,temperature_path)

    #选择temperature
    def choose_temperature(self):
        self.find_element(*self.temperature_path_loc).click()
        sleep(5)

    Confirm_button_path =".//ion-header[@class='header header-md']/ion-navbar/ion-buttons[2]/button"
    Confirm_button_path_loc=(By.XPATH,Confirm_button_path)

    #选择temperature之后的确定按钮
    def Confirm_button(self):
        self.find_element(*self.Confirm_button_path_loc).click()
        sleep(5)

    # cart_button_loc=(By.CLASS_NAME,'cart_button')
    #
    # # #点击结账Button1
    # # def cart_button(self):
    # #     self.find_element(*self.cart_button_loc).click()
    # #
    # # cart_button2_path="html/body/ion-app/ng-component/ion-nav/ng-component[2]/ion-footer/button"
    # # cart_button2_loc=(By.XPATH,cart_button2_path)
    # #
    # # #点击结账Button2
    # # def cart_button2(self):
    # #     self.find_element(*self.cart_button2_loc)

    #定义lab外卖
    def lab_delivery(self,cvv,tips):
        self.lab_menu()
        sleep(5)
        self.lab_minus_mask()
        sleep(5)
        self.choose_temperature()
        sleep(5)
        self.Confirm_button()
        sleep(5)
        pht=PhatThai(self.driver)
        pht.cart_button1()
        sleep(5)
        pht.cart_button2()
        sleep(5)
        pht.take_out()
        sleep(5)
        pht.eastside()
        sleep(5)
        pht.choice_next()
        sleep(5)
        pht.Choose_delivery_time()
        sleep(5)
        pht.complete_butt()
        sleep(5)
        pht.choice_payment_method()
        sleep(5)
        pht.input_cvv(cvv)
        sleep(5)
        pht.input_tips(tips)
        sleep(5)
        pht.payment()
        sleep(5)







