"""
@author: DT_testing
@file:   import_common.py
@desc:  【】
@step：  
"""
import win32gui
import win32con
import time
from selenium.webdriver.common.by import By
from common.base import Base

class ImportCommon(Base):
    def importCommon(self,filePath):
        # 找到打开的windows弹窗
        dialog=win32gui.FindWindow('#32770', u'打开')

        # 依次寻找对象，直到找到输入框Edit对象的句柄
        ComboBoxEx32=win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox=win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit=win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)

        # 找到windows弹窗上的确定按钮句柄
        button=win32gui.FindWindowEx(dialog, 0, 'Button', None)

        # 需要上传的文件地址输入，使用绝对地址
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filePath)

        # 点击windows弹窗确定按钮
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        time.sleep(3)

    def checkImport(self):
        # 上传文件
        agentImport_loc=(By.CSS_SELECTOR, '[class="margin-R20 ant-btn ant-btn-primary"]')
        # 获取导出结果
        uploadResult_loc=(By.CSS_SELECTOR, '[class="flex-start analysis-process font10"]')
        # 分析按钮
        analysis_loc=(By.ID, 'Analysis')

        # 导入进度
        speed_loc=(By.CSS_SELECTOR, '[class="ant-progress-text ng-star-inserted"]')
        # 错误提示
        errorText_loc=(By.CSS_SELECTOR, '.analysis-result-error-text')
        #---------------------------------------------------------------------

        analysisColor=self.find_element(analysis_loc).get_attribute('style')
        # 上传文件后会loading，等待页面loading完成，页面loading完成的结果是导入按钮变为蓝色
        while (analysisColor == 'background-color: rgb(191, 191, 191);'):

            analysisColor=self.find_element(analysis_loc).get_attribute('style')
        # 点击导入按钮
        self.find_elements(agentImport_loc)[1].click()
        time.sleep(1)
        # 需要等待导入进度条完成之后才关闭页面，并且给出提示
        speed=self.find_element(speed_loc).get_attribute('textContent')
        while (speed != ''):
            time.sleep(2)
            print('导入进度:' + speed)

            speed=self.find_element(speed_loc).get_attribute('textContent')
            try:
                errorText=self.find_element(errorText_loc).get_attribute('textContent')
                if errorText == '请求失败':
                    break
            except Exception as msg:
                print(msg)
        assert speed == '', '导入失败'
        print('导入成功')
