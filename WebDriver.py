# - * -coding: utf - 8 - * -from selenium
# import webdriver
import os
import string
import time
import win32con
import win32gui
# 导入自定义库文件
import CustomLibrary
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random
import sys


class GetWebdriver():
    def Getdriver(self):
        chromedriver = "C:\Python27\Scripts\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        dr = webdriver.Chrome(chromedriver)
        dr.implicitly_wait(30)
        #dr.switch_to_frame('')
        #dr.find_element_by_xpath()
        #dr.maximize_window()
        return dr

    def GetdriverO(self):
        chromedriver = "D:\Python27\Scripts\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        dri = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
        return dri
    def Mobiledriver(self):
        # 把浏览器设置成为手机模式
        mobileEmulation = {'deviceName': 'Apple iPhone 6'}  # 设置手机型号
        options = webdriver.ChromeOptions()  # 进入浏览器设置
        options.add_experimental_option('mobileEmulation', mobileEmulation)  # 浏览器设置成手机模式
        dr = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)  # 调用浏览器自动化驱动
        return dr


    def Getdriver1111(self):
        chromedriver = "C:\Python27\Scripts\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        dr = webdriver.Chrome(chromedriver)
        dr.find_element_by_id().send_keys()




if __name__=='__main__':
    glo=GetWebdriver()
    glo.Getdriver()
