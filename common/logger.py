# _*_ coding:utf-8 _*_
"""
@author: DT_testing
@file:   logger.py
@desc:  【封装日志类】
@step：
"""
# 导入模块
import logging
import logging.handlers
import os.path
import time


class Logger(object):
    def __init__(self,  logger):
        '''''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个日志器logger，并设置其日志级别为DEBUG
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #log_path = os.path.dirname(os.getcwd()) + '/logs/'  # 项目根目录下/logs 保存日志
        #log_path = os.path.dirname(os.path.abspath('.')) + '/logs/'  # E:\\New-demoOtrs\\otrs_test\\logs\
        # 获取项目路径 E:\New-demoOtrs
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # 日志需要存放的路径是E:\New-demoOtrs/logs/
        log_path = project_path + '/logs/'
        #print(log_path)
        # 如果case组织结构式 /testsuit/featuremodel/xxx.py ， 那么得到的相对路径的父路径就是项目根目录
        log_name = log_path + rq + '.log'
        # 创建一个文件处理器handler并设置其日志级别为INFO
        #fh = logging.FileHandler(log_name, maxBytes=1024 * 1024, backupCount=5,encoding='utf-8')

        fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024, backupCount=5,
                                                         encoding='utf-8')  # 实例化handler

        #fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        '''
        创建一个流处理器handler并设置其日志级别为INFO
        '''
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        #handler = logging.handlers.RotatingFileHandler(fh, maxBytes=1024 * 1024, backupCount=5,
        #                                                 encoding='utf-8')  # 实例化handler
        '''
        创建一个格式器formatter并将
        '''
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给日志处理器logger添加上面创建的handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger