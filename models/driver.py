#-*- coding:utf-8 -*-
from  selenium import webdriver
from selenium.webdriver import Remote
from time import sleep


def browser():
    driver=webdriver.Chrome()
    return driver


if __name__=='__main__':
    dr=browser()
    dr.get('https://dockyard.gobindo.com/')
    sleep(5)
    dr.quit()