# -*- coding:utf-8 _*-
""" 
@author:Administrator 
@file: pip_test.py 
@time: 2018/07/09 
"""
"""
解决：.whl is not support wheel on this platform
找到本机支持的格式，将下载的包名修改成支持的格式
win32:
    import pip; print(pip.pep425tags.get_supported())
win64:
    import pip._internal;print(pip._internal.pep425tags.get_supported())
such as:
    opencv_python-3.4.1.15-cp27-cp27m-win_amd64.wheel-->opencv_python-3.4.1.15-cp27-cp27m-win32.wheel
"""
import pip._internal

print(pip._internal.pep425tags.get_supported())

if __name__ == "__main__":
    pass
