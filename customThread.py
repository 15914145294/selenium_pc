# encoding:utf-8

"""
继承于threading.Thread 用于实现多线程执行不同的函数
"""

import threading
from time import ctime


class CustomThread(threading.Thread):
	def __init__(self, func, name, *args):
		"""
		实例化一个多线程对象
		:param func: 多线程执行的函数对象
		:param name: 函数的名字
		:param args: 函数的参数
		"""
		threading.Thead.__init__(self)
		self.func = func
		self.name = name
		self.args = args
		self.res = None
		
	# override method run of threading.Thread
	def run(self):
		print "start {0} at:".format(self.name),ctime()
		self.res = apply(self.func,self.args)
		print "end {0} at:".format(self.name), ctime()

	def get_result(self):
		return self.res

