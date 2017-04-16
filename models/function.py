#-*- coding:utf-8 -*-
from  selenium import webdriver
import os
from time import sleep


def insert_img(driver,file_name):
    base_dir=os.path.dirname(os.path.dirname(__file__))
    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    base=base_dir.split('/models')[0]
    file_path=base+"/report/image/"+file_name
    driver.get_screenshot_as_file(file_path)

if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get('https://dockyard.gobindo.com/')
    sleep(5)
    insert_img(driver,'bindo.jpg')
    driver.quit()