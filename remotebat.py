

# encoding:utf-8
import sys
import wmi
import time

bat_name = "D:\\%s_%s.bat" % (sys.argv[1],sys.argv[2])


# logfile = 'logs_%s.txt' % time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())


class RemoteUtil:
	def __init__(self):
		pass

	@staticmethod
	def call_remote_bat(ip="172.19.7.1", user="administrator", pwd="Za888888", date=None):
		try:
			conn = wmi.WMI(computer=ip, user=user, password=pwd)
			cmd_call_bat = "cmd /c call %s %s" % (bat_name, date)
			conn.Win32_Process.Create(CommandLine=cmd_call_bat)
			print (u"执行成功!")
			return True
		except Exception, e:
			print(e.message)
		# log = open(logfile, 'a')
		# log.write('%s, call bat Failed!\r\n' % ipaddress)
		# log.close()
		return False


if __name__ == "__main__":
	RemoteUtil.call_remote_bat()
