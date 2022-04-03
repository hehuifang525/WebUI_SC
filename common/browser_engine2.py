
"""
@author: DT_testing
@file:   browser_engine2.py
@desc:  【封装浏览器驱动（引擎）类--登录customer页面】
@step：  主要目前常用的Chrome、Firefox和IE三大浏览器引擎的封装
"""
# 导入模块
import configparser
import os.path
from selenium import webdriver

from common.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine2(object):
    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    chrome_driver_path = dir + '/drivers/chromedriver.exe'

    # print(chrome_driver_path)

    def __init__(self, driver):
        self.driver = driver

    # Read the browser type from config.ini file, return the driver
    def open_customerbrowser(self):
        # 设置url
        # URL1 = 'https://ctitest1.otrs365.cn/customer/login'
        rc = readconfig()
        test1 = rc.readconfig()
        URL1 = test1.get('url', 'url1')
        # url = self.get(URL1) #获取测试的 OTRS URL 地址1
        logger.info("The test server url is: %s" % URL1)  # 日志打印测试的URL地址

        # 选择谷歌浏览器
        chrome_driver_path = os.path.join("chromedriver.exe")
        driver = webdriver.Chrome(chrome_driver_path)  # 初始化一个实例
        driver.get(URL1)  # 访问URL

        driver.maximize_window()  # 窗口最大化

        driver.implicitly_wait(10)
        # logger.info("Set implicitly wait 10 seconds.")
        # print(driver)
        return driver

    # 关闭浏览器
    def quit_browser(self):
        # logger.info("Now, close and quit the browser.")
        self.driver.quit()


class BrowserEngine22(object):
    # dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    # chrome_driver_path = dir + '/drivers/chromedriver.exe'

    # print(chrome_driver_path)

    def __init__(self, driver):
        self.driver = driver

    # Read the browser type from config.ini file, return the driver
    def open_customerbrowser22(self):
        # 设置url
        URL11 = 'http://192.168.123.231/customer/login'
        # URL1 = 'http://192.168.123.56:4300//user/login' # 徐敏
        # 获取测试的 OTRS URL 地址1
        # logger.info("The test server url is: %s" % URL1) #日志打印测试的URL地址

        # 选择谷歌浏览器
        chrome_driver_path = os.path.join("chromedriver.exe")
        driver = webdriver.Chrome(chrome_driver_path)  # 初始化一个实例
        driver.get(URL11)  # 访问URL

        driver.maximize_window()  # 窗口最大化

        driver.implicitly_wait(10)
        # logger.info("Set implicitly wait 10 seconds.")
        # print(driver)
        return driver

    # 关闭浏览器
    def quit_browser(self):
        # logger.info("Now, close and quit the browser.")
        self.driver.quit()
