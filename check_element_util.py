# -*- coding:utf-8 _*-
""" 
@author:Administrator 
@file: element_util.py 
@time: 2018/06/15 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait_for_clickable(driver, ky):
    try:
        result = WebDriverWait(driver, 30, 2).until(ec.element_to_be_clickable(ky))
        if result:
            flag = True
    except Exception as e:
        print e.message
        flag = False
    return flag


def wait_for_disappear(driver, ky):
    try:
        result = WebDriverWait(driver, 30, 0.5).until_not(lambda x: x.find_element(ky).is_displayed())
        if not result:
            return True
    except Exception as e:
        print e.message
        return False


def wait_for_element(driver, ky):
    try:
        element = WebDriverWait(driver, 30).until(lambda x: x.find_element(ky))
        if element:
            return True
    except:
        return False


if __name__ == "__main__":
    # dr = webdriver.Chrome()
    # dr.get("http://172.21.2.3:8009/account/login")
    # assert wait_for_clickable(dr, (By.CSS_SELECTOR, "input[value='登 录']"))
    # print "element is clickable"
    pass
