#
# """
# @author: DT_testing
# @file:   browser_engine1.py
# @desc:  【封装浏览器驱动（引擎）类--登录index页面】
# @step：  主要目前常用的Chrome、Firefox和IE三大浏览器引擎的封装
# """
# # 导入模块
# import os.path
# import sys
#
# from selenium import webdriver
#
# from common.logger import Logger
#
# logger = Logger(logger="BrowserEngine").getlog()
#
#
# class BrowserEngine1(object):
#     dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#     #chrome_driver_path = dir + '/drivers/chromedriver.exe'
#     # print(chrome_driver_path)
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # Read the browser type from config.ini file, return the driver
#     def open_agentbrowser(self):
#         # 设置url
#         # URL1 = 'https://ctitest1.otrs365.cn/user/login'
#         # 改为传参
#         URL1 = sys.argv[1] + "/user/login"
#
#         # 选择谷歌浏览器
#         driver = webdriver.ChromeOptions()
#         # 改为隐身模式
#         driver.add_argument('--headless')
#         driver.add_argument('--disable-gpu')
#         driver.add_argument('--no-sandbox')
#         # 重要
#         driver.add_argument('--disable-dev-shm-usage')
#         driver.add_argument('--disable-dev-shm-scrollbars')  # 隐藏滚动条
#         driver.add_argument('--window-size=1920,3000')
#         # driver.add_argument('--window-size=1366,768')
#         driver = webdriver.Chrome(options=driver)
#         # 获取测试的 OTRS URL 地址1
#         logger.info("The test server url is: %s" % URL1)  # 日志打印测试的URL地址
#         driver.get(URL1)  # 访问URL
#         # 智能等待
#         driver.implicitly_wait(10)
#
#         # print(driver)
#         return driver
#
#     # 关闭浏览器
#     def quit_browser(self):
#         # logger.info("Now, close and quit the browser.")
#         self.driver.quit()
#
#
# class BrowserEngine11(object):
#     dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
#     chrome_driver_path = dir + '/drivers/chromedriver.exe'
#     # print(chrome_driver_path)
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     # Read the browser type from config.ini file, return the driver
#     def open_agentbrowser11(self):
#         # 设置url
#         rc = readconfig()
#         test1 = rc.readconfig()
#         URL11 = test1.get('url', 'url11')
#         # URL1 = 'http://192.168.123.56:4300//user/login' # 徐敏
#         # 获取测试的 OTRS URL 地址1
#         # logger.info("The test server url is: %s" % URL1) #日志打印测试的URL地址
#
#         # 选择谷歌浏览器
#         chrome_driver_path = os.path.join("chromedriver.exe")
#         driver = webdriver.Chrome(chrome_driver_path)  # 初始化一个实例
#         driver.get(URL11)  # 访问URL
#
#         driver.maximize_window()  # 窗口最大化
#
#         driver.implicitly_wait(10)
#         # logger.info("Set implicitly wait 10 seconds.")
#         # print(driver)
#         return driver
#
#     # 关闭浏览器
#     def quit_browser(self):
#         # logger.info("Now, close and quit the browser.")
#         self.driver.quit()

"""
@author: DT_testing
@file:   browser_engine1.py
@desc:  【封装浏览器驱动（引擎）类--登录index页面】
@step：  主要目前常用的Chrome、Firefox和IE三大浏览器引擎的封装
"""
# 导入模块
import os.path
import sys

from selenium import webdriver

from common.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine1(object):
    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    chrome_driver_path = dir + '/drivers/chromedriver.exe'
    #print(chrome_driver_path)

    def __init__(self, driver):
        self.driver = driver

    # Read the browser type from config.ini file, return the driver
    def open_agentbrowser(self):
        # 设置url

        URL1 = '需要填写'


        # 改为传参
        #URL1 = sys.argv[1] + "/user/login"

        # 选择谷歌浏览器
        # driver = webdriver.ChromeOptions()
        # # 改为隐身模式
        # driver.add_argument('--headless')
        # driver.add_argument('--disable-gpu')
        # driver.add_argument('--no-sandbox')
        # # 重要
        # driver.add_argument('--disable-dev-shm-usage')
        # driver.add_argument('--disable-dev-shm-scrollbars') #隐藏滚动条
        # driver.add_argument('--window-size=1920,3000')
        # #driver.add_argument('--window-size=1366,768')
        # driver = webdriver.Chrome(self.chrome_driver_path, options=driver)
        driver = webdriver.Chrome(self.chrome_driver_path)
        # 获取测试的 OTRS URL 地址1
        logger.info("The test server url is: %s" % URL1)  # 日志打印测试的URL地址
        driver.get(URL1)  # 访问URL
        # 0722本地窗口最大化
        driver.maximize_window()
        # 智能等待
        # driver.implicitly_wait(10)

        # print(driver)
        return driver

    # 关闭浏览器
    def quit_browser(self):
        # logger.info("Now, close and quit the browser.")
        self.driver.quit()



class BrowserEngine11(object):
    dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    chrome_driver_path = dir + '/drivers/chromedriver.exe'
    #print(chrome_driver_path)

    def __init__(self, driver):
        self.driver = driver

    # Read the browser type from config.ini file, return the driver
    def open_agentbrowser11(self):
        # 设置url
        URL11 = '需要填写'
        # 获取测试的 OTRS URL 地址1
        #logger.info("The test server url is: %s" % URL1) #日志打印测试的URL地址

        # 选择谷歌浏览器
        chrome_driver_path = os.path.join("chromedriver.exe")
        driver = webdriver.Chrome(chrome_driver_path)# 初始化一个实例
        driver.get(URL11)#访问URL

        driver.maximize_window()  #窗口最大化

        # driver.implicitly_wait(10)
        # logger.info("Set implicitly wait 10 seconds.")
        # print(driver)
        return driver

    # 关闭浏览器
    def quit_browser(self):
        # logger.info("Now, close and quit the browser.")
        self.driver.quit()