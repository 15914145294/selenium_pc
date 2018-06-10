# encoding:utf-8
import os
import time
import logging




class Logger():

    def __init__(self, logname='./logger.log', loglevel=logging.DEBUG):
        """
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        """

        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(loglevel)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logname)
        fh.setLevel(loglevel)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d  - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

if __name__ == "__main__":
    logger = Logger().getlog()
    logger.info("aaaa")
    logger.warn("bbb")
    logging.info("cccc")
    
    logging.error("this is an error.")
