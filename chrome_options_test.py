# encoding:utf-8

"""
@version: python27
@author: fafa
@site: http://www.phpgao.com
@software: PyCharm Community Edition
@file: chromeoptions.py
@time: 2018/7/29 0029 上午 10:34
"""
# 如果设置的参数不生效，请下载最新的chromedriver
from selenium import webdriver


option = webdriver.ChromeOptions()
# 设置字符编码
option.add_argument("lang=zh_CN.UTF-8")
# 窗口最大化
option.add_argument("start-maximized")
# 隐身模式
# option.add_argument("incognito")
# 阻止弹出框
option.add_argument('disable-infobars')
print(option.arguments)
# option.add_argument("user-data-dir=/path/to/your/custom/profile")
# prefs = {"profile.managed_default_content_settings.disable-infobars": 2}
# option.add_experimental_option('pref', prefs)
driver = webdriver.Chrome(chrome_options=option)
# driver.set_window_size(configure.)
driver.get("http://www.baidu.com")


if __name__ == '__main__':
	pass
