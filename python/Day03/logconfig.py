# -*- coding: utf-8 -*-
'''
@Time    : 2023/3/24 0024 下午 3:37
@Author  : fengaijun
@File    : logconfig.py

'''

import logging


class logformat:
    def getlogger(self):
        # 创建日志器
        logger = logging.getLogger("logger")
        if not logger.handlers:
            # 设置日志记录最低级别（正对日志器所有处理器）
            logger.setLevel(logging.INFO)
            # 创建控制台处理器
            SH = logging.StreamHandler()
            # 设置处理器日志记录最低级别（仅限当前处理器）
            # SH.setLevel(logging.DEBUG)
            # 创建日志文件处理器
            FH = logging.FileHandler("log.txt")
            # 格式器
            formatter = logging.Formatter(fmt="[%(asctime)s] [%(filename)s] %(levelname)s :%(message)s",
                                          datefmt='%Y-%m-%d %H:%M:%S')
            # 日志器添加处理器
            logger.addHandler(SH)
            logger.addHandler(FH)
            # 处理器设置格式
            SH.setFormatter(formatter)
            FH.setFormatter(formatter)
        return logger

    def sum(self, *args):
        try:
            sum = 0
            for num in args:
                sum += num

            self.getlogger().info(f"计算多个数之和={sum}")
            return sum
        except Exception as error:
            self.getlogger().error("计算多个数之和有异常:\n" + str(error))

    def sum_two(self, x, y):
        try:
            sum = 0
            sum = x + y
            self.getlogger().info(f"计算2个数之和={sum}")
            return sum
        except Exception as error:
            self.getlogger().error("计算多个数之和有异常:\n" + str(error))

    def sum_three(self, x, y, z):
        try:
            sum = 0
            sum = x + y + z
            self.getlogger().info(f"计算3个数之和={sum}")
            return sum
        except Exception as error:
            self.getlogger().error("计算多个数之和有异常:\n" + str(error))


if __name__ == '__main__':
    logformat().sum(22, 3,2323,1)
    logformat().sum_two(2,12)
    logformat().sum_three(2324,351,9987)
    logformat().sum("werwer",1,12,77)
    logformat().sum_two("12",45)
    logformat().sum_three("sdsdf",10,23)
