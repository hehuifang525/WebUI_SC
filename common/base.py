# _*_ coding:utf-8 _*_
"""
@author: QianJingjing
@file:   base.py
@desc:  【basepage.py封装对页面的基本操作。
          其中包含：查找元素、点击元素、输入、保存图片/下拉选择、切换iframe】
@step：  
"""
# 3.导入模块

import time

import os.path

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from common.logger import Logger
# Create a logger instance
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from functools import wraps
from selenium.webdriver.common.by import By



class Base(object):
    '''
    定义一个页面基类，所有页面都应当继承这个类
    封装一些常用的页面操作方法到这个类
    '''
    logger=Logger(logger="BasePage").getlog()
    def __init__(self, driver):
        self.driver = driver

    # logger=Logger(logname='log.txt', loglevel=1, logger="fox").getlog()
    # Quit browser and end testing
    def quit_browser(self):
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.driver.quit()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        #self.logger.info("wait for %d seconds." % seconds)

    # # 点击关闭当前窗口
    # def close(self):
    #     try:
    #         self.driver.close()
        #     logger.info("Closing and quit the browser.")
        # except NameError as e:
        #     logger.error("Failed to quit the browser with %s" % e)

    # 保存图片,截图，保存在根目录下的screenshots
    def get_windows_img(self):

        # 把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        # try:
        #     self.driver.get_screenshot_as_file(screen_name)
        #     print("已将截图保存到文件夹/screenshots")
        #     self.logger.info("Had take screenshot and save to folder : /screenshots")
        #
        # except NameError as e:
        #
        #     self.logger.error("Failed to take screenshot! %s" % e)
        #     print("截图保存失败! %s" % e)
        #     self.get_windows_img()
        self.driver.get_screenshot_as_file(screen_name)
        print("已将截图保存到文件夹/screenshots")
        self.logger.info("Had take screenshot and save to folder : /screenshots")
        raise

    # 创建用例执行失败装饰器
    def screenshot_about_case(func):
        # 把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        @wraps(func)
        # screen_name = file_path + rq + '.png'
        def get_screenshot_about_case(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except Exception as e:
                # 获取case_name的名称
                case_name = '{}-{}'.format(self.__class__.__name__, func.__name__)
                # 截屏的路径
                screenshotPath = os.path.join(file_path, case_name)
                # 获得现在的时间戳
                # time_now = datetime.now().strftime('%Y%m%d%H%M%S')
                # 名字的一部分
                screen_shot_name = ".png"
                # 组装图片需要传入的路径和推片名称
                screen_img = screenshotPath + '_' + rq + '_' + screen_shot_name
                # 截图并保存到相应的名称的路径
                self.driver.get_screenshot_as_file(screen_img)
                self.logger.info("Had take screenshot and save to folder : /screenshots")
                # print('截图成功')
                raise e
        return get_screenshot_about_case


    #     # 重新封装单个元素定位方法---可以填入登录名密码
    # def find_element(self, loc):
    #     try:
    #         WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
    #         return self.driver.find_element(*loc)
    #     except:
    #         print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 重写元素定位方法

    def find_element(self, loc):
        for i in range(5):
            try:
                a = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
                if a:
                    a = self.driver.find_element(*loc)
                    # 滚动到指定元素
                    js = "arguments[0].scrollIntoView(true);"
                    self.driver.execute_script(js, a)
                    return a
            except:
                pass
        else:
            raise Exception('time out:未找到元素，请重新定位')

    def find_element_10(self, loc):
        """
            封装元素定位，10秒内找不到元素就返回报错
        """
        try:
            a = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            if a:
                a = self.driver.find_element(*loc)
                return a
        except:
            raise Exception('time out:未找到元素，请重新定位')


    # 滑动页面滚动条,参数target为需要获取且被遮挡的的元素定位
    def slide_bar(self, target):
        # target = self.driver.find_element_by_id(target)
        loc = (By.ID, target)
        target = self.find_element(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # 重新封装一组元素定位方法
    def find_elements(self, loc):
        # try:
        #     # if len(self.driver.find_elements(*loc)):
        #     WebDriverWait(self.driver, 30).until(EC.visibility_of_any_elements_located(loc))
        #     return self.driver.find_elements(*loc)
        # except:
        #     print(u"%s 页面中未能找到 %s 元素" % (self, loc))
        #     raise
        # 0907 修改定位方式
        for i in range(5):
            try:
                a = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(loc))
                if a:
                    a = self.driver.find_elements(*loc)
                    return a
            except:
                pass
        else:
            raise Exception('time out:未找到元素，请重新定位')

    # 重新封装输入方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            # 0802 增加滚动
            # ele1 = self.find_element(loc)
            # self.driver.execute_script("arguments[0].scrollIntoView();", ele1)
            if click_first:
                # ActionChains(self.driver).move_to_element(self.find_element(loc)).click().perform()
                self.find_element(loc).click()
            if clear_first:
                # ActionChains(self.driver).move_to_element(self.find_element(loc)).perform()
                self.find_element(loc).clear()

            # ActionChains(self.driver).move_to_element(self.find_element(loc)).send_keys(value).perform()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print("%s 页面未能找到 %s 元素" % (self, loc))
            raise

    # 重新封装按钮点击方法
    def clickButton(self, loc, find_first=True):
        for i in range(5):
            try:
                elm = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
                if elm:
                    # 滚动到指定元素
                    js = "arguments[0].scrollIntoView(true);"
                    self.driver.execute_script(js,elm)
                    elm.click()
                    return
            except:
                pass

        else:
            raise Exception('time out:元素不是可点击的状态，请重新调整')

        # try:
        #     if find_first:
        #         WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(loc))
        #     elemnt = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(loc))
        #     ActionChains(self.driver).move_to_element(elemnt).click().perform()

        # except AttributeError:
        #     self.logger.error("%s 页面未能找到 %s 按钮" % (self, loc))
        #     print("%s 页面未能找到 %s 按钮" % (self, loc))
        #     raise

    # 封装判断元素是否为可点击状态
    def waitclickable(self, loc, find_first=True):

        for i in range(10):
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
                return
            except:
                pass
        else:
            raise Exception('time out:元素不是可点击的状态，请重新调整')



   #重新封装清空方法
    def clearInput(self,loc,find_first=True):
       try:
            if find_first:
               self.find_element(loc)
            self.find_element(loc).clear()
       except AttributeError:
           self.logger.error("%s 页面未能找到 %s 按钮" % (self, loc))
           print("%s 页面未能找到 %s 按钮" % (self, loc))


    def move_to_element(self, loc1, loc2):
        ''' 鼠标 悬停+点击 操作 '''
        try:
            ele1 = self.find_element(loc1)
            ele2 = self.find_element(loc2)
            # ActionChains(self.driver).move_to_element(menu).click(hidden_submenu).perform()
            ActionChains(self.driver).move_to_element(ele1).click(ele2).perform()
            # self.move_to_element(self.menu_loc).click(self.group_loc).perform()
        except:
            print("鼠标悬停操作失败")
            return False

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    def get_title(self):
        u"""获取当前窗口的title"""
        return self.driver.title

    def get_userLoginName(self):
        # 获取登录人右上角的名称
        return self.driver.find_element_by_css_selector('.padding-L10').get_attribute('textContent')

    # 移动到页面顶部
    def move_to_pagetop(self):
        js = "window.scrollTo(0,0);"
        self.driver.execute_script(js)
    # 移动到页面底部
    def move_to_pagebottom(self):
        # js = "window.scrollTo(0,document.body.scrollHeight);"
        js = "window.scrollTo(0,20000);"
        self.driver.execute_script(js)

    # 检查指定元素内的loading页面是否消失
    def check_loading(self):

        loc = (By.CSS_SELECTOR, '[class="ant-spin-dot ant-spin-dot-spin ng-star-inserted"]')
        for i in range(10):
            try:
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(loc))
                return
            except:
                pass
        else:
            raise Exception('time out:页面存在loading页，请重新调整')



