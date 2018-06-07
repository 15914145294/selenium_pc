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
from data_create import data_idcard
from data_create import data_mobilephone
from data_create import data_QQorEmail
from file_operate import fileoperate
from public_method import is_element_exist
from public_method import WebDriver
from all_product_PC import ZacEsdAdmin

class Screen():
    def __init__(self,dr):
        self.dr=dr
    def dr(self):
        global dr
        screen = Screen()
        #dr=None
        dri=WebDriver.GetWebdriver()
        dr=dri.Getdriver()
        Screen.screenshot()
    def Screenshot(self):
        d = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # d=datetime.now()
        dd = str(d)
        ddd = dd[0:13] + dd[14:16] + dd[17:19]+"-PC"
        filename = "D:\\audofile\\" + str(ddd) + ".png"
        pictrue=self.dr.get_screenshot_as_file(filename)
        return pictrue
    def ScreenshotXDWeb(self):
        d = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # d=datetime.now()
        dd = str(d)
        ddd = dd[0:13] + dd[14:16] + dd[17:19]+"-XDWeb"
        filename = "D:\\audofile\\" + str(ddd) + ".png"
        pictrue=self.dr.get_screenshot_as_file(filename)
        return pictrue
    def ScreenshotWeb(self):
        d = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # d=datetime.now()
        dd = str(d)
        ddd = dd[0:13] + dd[14:16] + dd[17:19]+"-Web"
        filename = "D:\\audofile\\" + str(ddd) + ".png"
        pictrue=self.dr.get_screenshot_as_file(filename)
        return pictrue
    def ScreenshotEsdWeb(self):
        d = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # d=datetime.now()
        dd = str(d)
        ddd = dd[0:13] + dd[14:16] + dd[17:19]+"-EsdWeb"
        filename = "D:\\audofile\\" + str(ddd) + ".png"
        pictrue=self.dr.get_screenshot_as_file(filename)
        return pictrue

