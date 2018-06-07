# -*- coding: utf-8 -*-
import sys, os

sys.path.append('d:\\auto_test\\python_auto')
from public_method import WebDriver
from selenium import webdriver
from time import sleep

# mobileEmulation = {'deviceName': 'Apple iPhone 6'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)
# driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
#
# driver.get('http://xxxxx')
# driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/a").click()
#
# sleep(3)

# sys.path.append('C:\\Python27\\Lib\\site-packages')
os.chdir('C:\\Python27\\Lib\\site-packages\\PIL')
# os.chdir('C:\Python27\Lib\site-packages\pytesser')
from PIL import Image

import PIL.Image
import PIL
import pytesseract
from selenium import webdriver


class Code():
    def __init__(self, dr):
        self.dr = dr

    @property
    def TextCode(self):
        code = self.dr.find_element_by_id('Amounts')
        # dr.execute_script("var element=document.getElementById('Amounts');element.scrollIntoView(true);"
        self.dr.execute_script("arguments[0].scrollIntoView();", code)
        self.dr.save_screenshot('D://a.png')  # 截取当前网页需要的验证码
        imgelement = self.dr.find_element_by_xpath('//*[@id="imgSendCaptcha"]')  # 定位验证码
        type(imgelement)
        # js = "$('.salary').parent().parent('.listingBox_content').find('input.btn-primary').click()"
        y = "$('#imgSendCaptcha')[0].getBoundingClientRect().top"
        print  self.dr.execute_script(y)
        print imgelement
        x = "$('#imgSendCaptcha')[0].getBoundingClientRect().left"
        print  self.dr.execute_script(x)
        location = imgelement.location  # 获取验证码x,y轴坐标
        print location
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = PIL.Image.open("D://a.png")  # 打开截图
        frame5 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame5.load()
        frame5.save('D://aa.jpg')
        qq = PIL.Image.open('D://aa.jpg')
        text = pytesseract.image_to_string(qq)  # .strip() #使用image_to_string识别验证码
        text = text[0:4]
        print text
        return text

    def Code(self):
        # code = self.dr.find_element_by_id('Amounts')
        # self.dr.execute_script("arguments[0].scrollIntoView();", code)
        self.dr.save_screenshot(
            'D://a.png')  # 截取当前网页需要的验证码   /html/body/div[6]/div/div[2]/div/div/div[2]/div/form/div[1]/img
        imgelement = self.dr.find_element_by_xpath(
            '/html/body/div[6]/div/div[2]/div/div/div[2]/div/form/div[1]/img')  # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = PIL.Image.open("D://a.png")  # 打开截图
        frame5 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame5.save('D://aa.jpg')
        # qq = PIL.Image.open('E://aa.jpg')
        # text = pytesseract.image_to_string(qq)  # .strip() #使用image_to_string识别验证码
        # text = text[0:4]
        # print text
        # return text

    def Imege(self):
        self.dr.save_screenshot('D://Img.png')  # 截取当前网页需要的验证码
        imgelement = self.dr.find_element_by_id('imgSendCaptcha')  # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = PIL.Image.open("D://Img.png")  # 打开截图
        frame5 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame5.save('D://captchaImg.jpg')
        qq = PIL.Image.open('D://captchaImg.jpg')
        text = pytesseract.image_to_string(qq)  # .strip() #使用image_to_string识别验证码
        text = text[0:4]
        print text
        return text

    def CaptchaImg(self):
        self.dr.save_screenshot('D://Img.png')  # 截取当前网页需要的验证码
        imgelement = self.dr.find_element_by_id('captchaImg')  # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = PIL.Image.open("D://Img.png")  # 打开截图
        frame5 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame5.save('D://captchaImg.jpg')
        qq = PIL.Image.open('D://captchaImg.jpg')
        text = pytesseract.image_to_string(qq)  # .strip() #使用image_to_string识别验证码
        text = text[0:4]
        print text
        return text

    def Image1(self):
        qq = PIL.Image.open('D://a.png')
        text = pytesseract.image_to_string(qq)  # .strip() #使用image_to_string识别验证码
        text = text[0:4]
        print text
        return text
        # def Code(self):
        #     # code = self.dr.find_element_by_id('Amounts')
        #     # self.dr.execute_script("arguments[0].scrollIntoView();", code)
        #     self.dr.save_screenshot('E://a.png')  # 截取当前网页需要的验证码   /html/body/div[6]/div/div[2]/div/div/div[2]/div/form/div[1]/img   /html/body/div[6]/div/div[2]/div/div/div[2]/div/form/div[1]/img
        #     imgelement = self.dr.find_element_by_xpath('/html/body/div[6]/div/div[2]/div/div/div[2]/div/form/div[1]/img')  # 定位验证码
        #     location = imgelement.location  # 获取验证码x,y轴坐标
        #     size = imgelement.size  # 获取验证码的长宽
        #     rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
        #               int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        #     i = PIL.Image.open("E://a.png")  # 打开截图
        #     frame5 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        #     frame5.save('E://aa.jpg')
        #     qq = PIL.Image.open('E://aa.jpg')
        #     text = pytesseract.image_to_string(qq)  # .strip() #使用image_to_string识别验证码
        #     text = text[0:4]
        #     print text
        #     return text


if __name__ == '__main__':
    # driver = WebDriver.GetWebdriver()
    # dr = driver.GetdriverO()
    image = Code('')
    image.Image1()
