#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    """用户登录页面"""

    url = ''

    login_username_loc = (By.XPATH,".//div[@class='input-wrapper']/ion-input/input")
    password_path=".//*[@id='loginForm']/div[2]/div/form/ion-list/ion-item[2]/div[1]/div/ion-input/input"
    login_password_loc = (By.XPATH,password_path)
    login_button_loc = (By.ID,'loginFormSubmit')

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)
        sleep(5)

    #密码登录
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)
        sleep(5)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()
        sleep(5)

    #忘记密码流程
    forget_pwd=(By.LINK_TEXT,'忘记密码?')
    new_email_path="html/body/ion-app/ion-modal[2]/div/ng-component/ion-content/div[2]/div/form/ion-list/ion-item/div[1]/div/ion-input/input"
    new_emali_input=(By.XPATH,new_email_path)
    button = "html/body/ion-app/ion-modal[2]/div/ng-component/ion-content/div[2]/div/form/div"
    email_button=(By.XPATH,button)
    login_button1 = "html/body/ion-app/ion-modal[3]/div/ng-component/ion-content/div[2]/div/div/button"
    go_login_button=(By.XPATH,login_button1)

    def forget_password(self,email_adr):
        self.find_element(*self.forget_pwd).click()
        sleep(5)
        self.find_element(*self.new_emali_input).send_keys(email_adr)
        sleep(5)
        self.find_element(*self.email_button).click()
        sleep(15)
        self.find_element(*self.go_login_button).click()
        sleep(5)

    #马上去注册
    register_now=(By.LINK_TEXT,'马上注册')
    register_account=(By.ID,'email')
    register_password=(By.ID,'password')
    register_repassword=(By.ID,'repeatPassword')
    path = "html/body/ion-app/ion-modal[2]/div/ng-component/ion-content/div[2]/div/form/div"
    register_button=(By.XPATH,path)

    def register(self,account,reg_password):
        self.find_element(*self.register_now).click()
        sleep(5)
        self.find_element(*self.register_account).send_keys(account)
        sleep(5)
        self.find_element(*self.register_password).send_keys(reg_password)
        sleep(5)
        self.find_element(*self.register_repassword).send_keys(reg_password)
        sleep(5)
        self.find_element(*self.register_button).click()
        sleep(5)



    #定义统一登录入口
    def user_login(self,username='18606990406@163.com',password='SQL110'):
        self.open()
        self.login_username(username)
        sleep(10)
        self.login_password(password)
        sleep(10)
        self.login_button()
        sleep(5)

    #打开登录界面
    def login_Bindo(self):
        self.open()
        sleep(10)

    error_hint_loc= (By.XPATH,".//div[@class='alert-wrapper']/div/h2")
    path1 = "html/body/ion-app/ion-modal[2]/div/ng-component/ion-content/div[2]/div/p"
    forget_pwd_hint_loc=(By.XPATH,path1)
    path2="html/body/ion-app/ion-modal[2]/div/ng-component/ion-header/ion-navbar/div[2]/ion-title/div"
    register_now_hint_loc=(By.XPATH,path2)


    #用户名错误提示
    def err_hint(self):
        return self.find_element(*self.err_hint_loc).text

    #忘记密码提示
    def forget_pwd_hint(self):
        return self.find_element(*self.forget_pwd_hint_loc).text

    #马上去注册提示
    def register_now_hint(self):
        return self.find_element(*self.register_now_hint_loc).text

    #登录成功提示






