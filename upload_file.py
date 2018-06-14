# -*- coding:utf-8 -*-
"""
@author:Administrator
@file: window_util.py
@time: 2018/06/08
"""
from window_util import *

__author__ = 'zhongan_TestTerm'
__version__ = '1.0'


class UploadFile(object):
    def __init__(self, path):
        """
        @:param path :传人文件的路径
        @usage:
            多个文件
                UploadFileApply('"d:/test/1.jpg" "d:/test/2.jpg"').upload_file()
            单个文件格式
                UploadFileApply('"d:/test/1.jpg"').upload_file()
           """
        self.path = path

    def uploadFile(self):
        """
        上传文件
        :return:
        """
        try:
            title = u"打开"
            classname = '#32770'
            hwnd = win32gui.FindWindow(classname, title)
            edit_handle = WindowUtil().find_subhandles(hwnd, [("ComboBoxEx32", 0), ("ComboBox", 0), ("Edit", 0)])
            button_handle = WindowUtil().find_subhandles(hwnd, [("Button", 0)])
            win32gui.SendMessage(edit_handle, win32con.WM_SETTEXT, 0, str(self.path))
            win32gui.SendMessage(hwnd, win32con.WM_COMMAND, 1, button_handle)
        except Exception as e:
            print e.message

        return True


if __name__ == "__main__":
    path = '"D:\\test\\1.jpg" "D:\\test\\2.jpg"'
    UploadFile(path).uploadFile()
