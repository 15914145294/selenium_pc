# encoding:utf-8

from time import sleep
from customThread import CustomThread

'''
运行三个线程，用于计算1..10的和
'''

def sum(n):
	sleep(1)
	print "sleep 1 seconde"
	if n < 2:
		return 1
	else:
		return n + sum(n - 1)


loops = range(3)

threads = []

for i in loops:
	# 产生线程对象
	t = CustomThread(sum, sum.__name__, 10)
	threads.append(t)

for t in threads:
	t.start()

for t in threads:
	# 挂起线程，直到线程结束运行
	t.join()
	print "the result is:",t.get_result()

if __name__ == '__main__':
	pass
