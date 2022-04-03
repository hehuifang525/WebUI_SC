"""
@author: DT_testing
@file:   agent_page.py
@desc:  【】
@step：
"""

from selenium.webdriver.common.by import By
from common.base import Base
import time
from selenium.webdriver import ActionChains


class AgentPage(Base):
    time.sleep(2)
    # 页面路径
    road_loc=(By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    # 添加按钮
    addbtn_loc=(By.ID, 'Add')

    # ------------------基本信息----------------------
    # 添加页面的字段 姓名，密码，邮箱，备注......等
    position_loc=(By.ID, 'UserTitle')
    fullname_loc=(By.ID, 'UserFullname')
    lastname_loc=(By.ID, 'UserLastname')
    firstname_loc=(By.ID, 'UserFirstname')
    jobnumber_loc=(By.ID, 'JobNumber')
    userlogin_loc=(By.ID, 'UserLogin')
    userpw_loc=(By.ID, 'UserPw')
    usermobile_loc=(By.ID, 'UserMobile')
    useremail_loc=(By.ID, 'UserEmail')
    usercity_loc=(By.ID, 'UserCity')
    vaild_loc=(By.ID, 'ValidID')
    # invaild_loc=(By.CSS_SELECTOR, '[class="ant-select-dropdown-menu-item ng-star-inserted"]') #0715修改
    invaild_loc = (By.CSS_SELECTOR, '[title="无效"]')
    yvaild_loc = (By.CSS_SELECTOR, '[title="有效"]')
    relevancebtn_loc=(By.CSS_SELECTOR, '[class="ant-steps-icon ng-star-inserted"]')
    # 下一步按钮
    nextbtn_loc=(By.ID, 'Next')
    # 提交并返回
    comandre_loc=(By.ID, 'SubmitReturn')
    # 返回列表
    returnAg_loc=(By.ID, 'GoBack1')
    # ------------------关联信息----------------------
    # 关联角色
    group_loc=(By.ID, 'UserQueue')
    groupValue_loc=(By.CSS_SELECTOR, '[class="ant-tree-title"]')
    # 完成
    commitbtn_loc=(By.ID, 'Finished')
    # 完成再添加一条
    comanother_loc=(By.ID, 'Finish and add another one')
    # 上一步
    previous_loc=(By.ID, 'se')
    # 返回列表
    returnlist_loc=(By.ID, 'GoBack2')
    relatedbtn_loc=(
        By.CSS_SELECTOR, '#step1 > form > nz-form-item > nz-form-control > div > span > div > button:nth-child(2)')

    # --------------------列表-------------------------
    # 列表表头
    list_loc=(By.CSS_SELECTOR, 'theadtr > th')
    # 切换有效列表
    validList_loc=(By.ID, 'Valid')
    # 切换无效列表
    invalidList_loc=(By.ID, 'Invalid')
    # 过滤服务人员
    search_loc=(By.ID, 'Search-input')

    # 表格td
    list_td_loc = (By.CSS_SELECTOR, ".ant-table-row.ng-star-inserted td")

    # 搜索结果检查
    searchresult_loc=(By.CSS_SELECTOR, '[nowrap="nowrap"]')
    # 过滤左侧角色
    searchrole_loc=(By.ID, 'Search-tree')
    role_loc = (By.CSS_SELECTOR, '//*[@id="tree-dom-element-nodes1"]/span/span/span[2]')
    # role_loc=(By.CSS_SELECTOR, '.tree-dom-node-text')
    # 点击进入详情
    #details_loc=(By.CSS_SELECTOR, '[class="ant-table-td-left-sticky ng-star-inserted"]') #0715修改
    details_loc = (By.CSS_SELECTOR, '#baseTableTbody tr.cursor')
    step_loc=(By.CSS_SELECTOR, '[class="ant-steps-item-icon"]')

    # 获取组中填写的值
    groupText_loc=(By.CSS_SELECTOR, '[class="ant-select-selection__choice__content"]')

    # 重复提示语
    loginMessage_loc=(By.ID, 'UserLogin_errorServeMessage')
    emailMessage_loc=(By.ID, 'UserEmail_errorServeMessage')
    mobileMessage_loc=(By.ID, 'UserMobile_errorServeMessage')
    jobnumberMessage_loc=(By.ID, 'JobNumber_errorServeMessage')
    # 带倒计时的返回列表按钮
    goback_loc=(By.ID, 'GoBack3')

    # 密码眼睛
    pwdEye_loc=(By.ID, 'eye-icon')

    # 列表页面导入导出
    imEx_loc=(By.ID, 'Import/Export')

    # 左侧导出按钮  1021

    Exportbtn_loc = (By.CSS_SELECTOR, 'li#Export')

    # 上传文件
    uploadFile_loc=(By.ID, 'file')

    # 导入
    # agentImport_loc=(By.ID, 'Import')
    agentImport_loc=(By.CSS_SELECTOR,'[class="margin-R20 ant-btn ant-btn-primary"]')
    # 获取导出结果
    uploadResult_loc=(By.CSS_SELECTOR, '[class="flex-start analysis-process font10"]')
    #分析按钮
    analysis_loc=(By.ID, 'Analysis')

    #导入进度
    speed_loc=(By.CSS_SELECTOR,'[class="ant-progress-text ng-star-inserted"]')

    # 错误提示
    errorText_loc=(By.CSS_SELECTOR, '.analysis-result-error-text')

    # 导入导出点击左侧导出按钮  1021
    def Export(self):
        self.clickButton(self.Exportbtn_loc)

    # 关联信息中的返回列表
    def returnlist2(self):
        self.clickButton(self.returnlist_loc)


    def road(self):
        return self.find_element(self.road_loc).text

    def goback(self):

        self.clickButton(self.goback_loc)

    def validList(self):
        self.clickButton(self.validList_loc)

    def invalidList(self):
        self.clickButton(self.invalidList_loc)

    def addagent(self):
        self.clickButton(self.addbtn_loc)
        time.sleep(3)

    def getAdd(self):
        addValue=self.find_element(self.addbtn_loc).get_attribute('textContent')
        return addValue

    def position(self, position):
        self.send_keys(self.position_loc, position)

    # 获取职位中填写的值
    def getPosition(self):
        return self.find_element(self.position_loc).text

    def fullname(self, fullname):
        self.clickButton(self.fullname_loc)
        self.send_keys(self.fullname_loc, fullname)

    def getFullname(self):
        return self.find_element(self.fullname_loc).get_attribute('testvalue')

    def lastname(self, lastname):
        self.send_keys(self.lastname_loc, lastname)

    def getLastname(self):
        return self.find_element(self.lastname_loc).get_attribute('testvalue')

    def firstname(self, firstname):
        self.send_keys(self.firstname_loc, firstname)

    def getFirstname(self):
        return self.find_element(self.firstname_loc).get_attribute('testvalue')

    def jobnumber(self, jobnumber):
        self.send_keys(self.jobnumber_loc, jobnumber)

    # 获取工号中填写的值
    def getJobnumber(self):
        return self.find_element(self.jobnumber_loc).text

    def userlogin(self, userlogin):
        self.send_keys(self.userlogin_loc, userlogin)
        time.sleep(4)

    def getUserLogin(self):
        return self.find_element(self.userlogin_loc).get_attribute('testvalue')

    def userpw(self, userpw):
        self.send_keys(self.userpw_loc, userpw)
        time.sleep(3)

    def getUserPw(self):
        return self.find_element(self.userpw_loc).text

    # 点击密码眼睛的样式
    def pwdEye(self):
        self.clickButton(self.pwdEye_loc)

    def usermobile(self, usermobile):
        self.send_keys(self.usermobile_loc, usermobile)

    def getUsermobile(self):
        return self.find_element(self.usermobile_loc).get_attribute('testvalue')

    def useremail(self, useremail):
        self.send_keys(self.useremail_loc, useremail)
        time.sleep(3)

    # 清空邮箱
    def clearEmail(self):
        self.clearInput(self.useremail_loc)

    # 清空密码
    def clearPassWord(self):
        self.clearInput(self.userpw_loc)

    def getUsermail(self):
        return self.find_element(self.useremail_loc).get_attribute('testvalue')

    def usercity(self, usercity):
        self.send_keys(self.usercity_loc, usercity)

    # 获取城市中填写的值
    def getCity(self):
        return self.find_element(self.usercity_loc).text

    def vaild(self):
        self.clickButton(self.vaild_loc)

    def selectInvaild(self):
        self.clickButton(self.invaild_loc)
        #self.driver.find_element(self.vaild_loc).click()
        # self.clickButton(self.vaild_loc)
        # time.sleep(2)
        # ActionChains(self.driver).send_keys("无效").perform()
    def selectvaild(self):
        self.clickButton(self.vaild_loc)
        self.clickButton(self.yvaild_loc)

    # 下一步按钮
    def next01(self):
        self.clickButton(self.nextbtn_loc)

    # 获取下一步按钮的颜色
    def getNextColor(self):
        return self.find_element(self.nextbtn_loc).get_attribute('disabled')

    # 提交并返回列表
    def comandre(self):
        self.find_element(self.comandre_loc).click()
        # self.clickButton(self.comandre_loc)

    # 获取 提交并返回列表 按钮的颜色
    def getComColor(self):
        return self.find_element(self.comandre_loc).get_attribute('disabled')

    # 返回服务人员列表
    def returnAg(self):
        self.clickButton(self.returnAg_loc)

    def group01(self):
        self.clickButton(self.group_loc)

    def regruop01(self):

        self.find_element(self.commitbtn_loc).click()

    def groupValue01(self):
        self.find_elements(self.groupValue_loc)[0].click()

    def groupValue02(self):
        self.find_elements(self.groupValue_loc)[1].click()

    def commit(self):
        self.clickButton(self.commitbtn_loc)

    def relatedbtn(self):
        self.find_elements(self.relatedbtn_loc)[1].click()

    def relevance(self):
        self.clickButton(self.relevancebtn_loc)

    def search(self, text):
        self.clickButton(self.search_loc)
        self.send_keys(self.search_loc, text)

    def searchplaceholder(self):
        se=self.driver.find_element_by_id(self.search_loc)
        # print(se)
        se.get_attribute('placeholder')
        # print(se)
        # return placeholder

    def listheader(self):
        list_header_01=[]
        for listheader01 in ['.ant-table-thead th']:
            for i in range(0, 8):
                list_header_01=self.driver.find_elements_by_css_selector(listheader01)[i].text
        return list_header_01

    def list_td(self):
        """
         返回列表记录td中值,除表头
        """
        return self.find_elements(self.list_td_loc)

    # 点击进入详情
    def details(self):
        self.clickButton(self.details_loc)

    def step2(self):
        self.find_elements(self.step_loc)[1].click()

    # 获取组中填写的值
    def groupText(self):
        return self.find_element(self.groupText_loc).text

    # 获取页面路径
    def getroadText(self):
        return self.find_element(self.road_loc).text

    # 获取页面提示语
    def getLoginMessage(self):
        return self.find_element(self.loginMessage_loc).text

    def getMobileMessage(self):
        return self.find_element(self.mobileMessage_loc).text

    def getEmailMessage(self):
        return self.find_element(self.emailMessage_loc).text

    def getJobNumMessage(self):
        return self.find_element(self.jobnumberMessage_loc).text

    def upload(self):
        self.clickButton(self.imEx_loc)

    def uploadFile(self):
        # 点击导入按钮
        ele=self.driver.find_element_by_id('file')
        self.driver.execute_script('arguments[0].click()', ele)
        time.sleep(3)

    def agentImport(self):
        # ele=self.driver.find_element_by_id('Import')
        # self.driver.execute_script('arguments[0].click()', ele)
        # self.clickButton(self.agentImport_loc)
        self.find_elements(self.agentImport_loc)[1].click()
        time.sleep(5)

    def analysis(self):
        self.clickButton(self.analysis_loc)
    def getAnalysisColor(self):
        return self.find_element(self.analysis_loc).get_attribute('style')

    def getUploadResult(self):
        return self.find_element(self.uploadResult_loc).text

    def getSpeed(self):
        return self.find_element(self.speed_loc).get_attribute('textContent')
    #获取错误提示
    def getErrorText(self):
        return self.find_element(self.errorText_loc).get_attribute('textContent')

    #过滤左侧角色
    def searchRole(self,role):
        self.send_keys(self.searchrole_loc,role)
    #获取搜索后的角色
    def getSearchRole(self ,text ):
        # [title="测试0001"] span.tree-dom-node-text
        elm = '[title="' + text + '"]'+' span.tree-dom-node-text'
        # print(elm)
        return self.driver.find_element_by_css_selector(elm).get_attribute('textContent')
        # return  self.find_element(self.role_loc).get_attribute('textContent')