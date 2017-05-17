#-*- coding:utf-8 -*-
from  selenium import webdriver
from time import sleep


def insert_img(driver,file_name):
    driver.get_screenshot_as_file('../screen_shot/%s' % file_name)

if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get('https://dockyard.gobindo.com/')
    sleep(5)
    insert_img(driver,'bindo.jpg')
    driver.quit()