# -*- coding:utf-8 -*-
'''
    作者：zhongan_TestTerm
    创建日期：2017.08.15
    功能：生成手机号
'''
__author__ = 'zhongan_TestTerm'
__version__ = '1.0'


import random, time



class makephone():
    @staticmethod
    def makemphone():
        global mphone
        '''
        生成手机号码
        '''
        mphone = '1444' + '%3d' % (random.randint(100, 800)) + '%4d' % (random.randint(5000, 9999))
        #print mphone
        return mphone
    def makenphone(self):
        return mphone

if __name__ == "__main__":
    makephone().makemphone()

