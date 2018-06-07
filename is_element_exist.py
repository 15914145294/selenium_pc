# -*- coding:utf-8 -*-
'''
    作者：zhongan_TestTerm
    创建日期：2017.08.15
    功能：生成手机号
'''
__author__ = 'zhongan_TestTerm'
__version__ = '1.0'


import random, time
from selenium import webdriver
import string
import win32gui
import win32con
import  win32api
import sys
sys.path.append('D:\\auto_test\\python_auto')
from public_method import WebDriver


class iselementexist():
    def __init__(self,dr):
        self.dr=dr
    def Driver(self):
        global dr
        dri = WebDriver.GetWebdriver()
        dr = dri.Getdriver()
    @staticmethod
    def is_element_exist(path,name):
        # chromedriver = "C:\Python27\Scripts\chromedriver.exe"
        # # os.environ["webdriver.chrome.driver"] = chromedriver
        # dr = webdriver.Chrome(chromedriver)
        #s = dr.find_elements_by_xpath(path)
        s = win32gui.FindWindow(path,name)
        #print type(s)
        ss=str(s)
        #print ss
        if len(ss) == 1:
            print "元素未显示:%s" % path
            return False
        elif len(ss) > 1:
            return True
        else:
            print "找到%s个元素：%s" % (len(ss), path)
            return False

    def IsElementExist(self, css):
        s = self.dr.find_elements_by_xpath(css)
        if len(s) == 0:
            print "元素未显示:%s" % css
            return False
        elif len(s) == 1:
            return True
        else:
            print "找到%s个元素：%s" % (len(s), css)
            return False

if __name__ == "__main__":
    iselementexist().is_element_exist(path, name)

