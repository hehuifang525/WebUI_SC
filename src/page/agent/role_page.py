"""
@author: QianJingjing
@file:   role_page.py
@desc:  【】
@step：  20200521 开发已提角色页面元素，更新元素获取
"""

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common.base import Base


class RolePage(Base):
    '''
    page
    '''
    # 路径
    road_loc = (By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    # 列表--有效无效按钮
    invalidlist_loc = (By.CSS_SELECTOR, ".list-tabList-item-text.flex-start")
    validbtn_loc = (By.ID, 'valid')
    invalidbtn_loc = (By.ID, 'invalid')
    # 增加按钮
    addbtn_loc = (By.ID, "AddQueue")
    ImportExport_loc = (By.ID, 'Import/Export')
    # 名称
    name_loc = (By.ID, "Name")
    # 父组(父角色)
    parentrole_loc = (By.ID, "ParentQueueID")

    # 系统邮件地址
    #systemadress_loc = (By.CSS_SELECTOR, '[class="ant-select-selection__rendered"]')
    #systemadress_loc = (By.CSS_SELECTOR, '[class="ant-form-item-children"]')
    systemadress_loc = (By.ID, "SystemAddressID")

    #choosesystemadress_loc = (By.CSS_SELECTOR, '.ant-select-dropdown-menu.ant-select-dropdown-menu-root') #20200521修改
    # choosesystemadress_loc = (By.CSS_SELECTOR, '.ant-select-dropdown-menu-item.ng-star-inserted') #0715修改
    choosesystemadress_loc = (By.CSS_SELECTOR, '.ant-select-item-option[title="otrs@localhost"]')

    # 有效性（选择有效/无效）
    clickvalid_loc = (By.ID, 'ValidID')
    choosevalid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(2)')
    chooseinvalid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper  nz-option-item:nth-child(1)')
    # choosevalid_loc = (By.CSS_SELECTOR, '[id="1"]')
    # chooseinvalid_loc = (By.CSS_SELECTOR,  '[id="2"]')
    # 备注
    comment_loc = (By.ID, 'Comment')

    # 返回列表（第一页的）
    # returnlist1_loc = (By.ID, 'BackList')
    returnlist1_loc = (By.ID, 'GoBack1')

    # 提交并返回列表
    savereturn_loc = (By.ID, 'Submit')

    # 下一步
    savenext_loc = (By.ID, 'Next')

    # 完成（下一步页面的按钮）
    savebtn_loc = (By.ID, 'Finished')

    # 完成并再次添加一条
    addagain_loc = (By.ID, 'Add')

    # 上一步
    backbtn_loc = (By.ID, 'Previous')

    # 返回列表（开发暂未加 id）第二页的
    # returnlist2_loc = (By.CSS_SELECTOR, '.ant-btn.ant-btn-primary')
    returnlist2_loc = (By.ID, 'GoBack2')
    # # 完成后的返回列表倒计时按钮
    # backlist_loc =(By.ID, 'BackList')

    # 搜索框
    searchtab_loc = (By.ID, 'Search-input')
    # 搜索结果检查
    # searchresult_loc = (By.CLASS_NAME, 'ant-table-td-left-sticky') # 0715修改
    searchresult_loc = (By.CSS_SELECTOR, '#baseTableTbody td.ant-table-cell-fix-left')
    # 搜索不存在的显示“空空如也”
    searchnotext_loc = (By.CLASS_NAME,'ant-empty-description')

    ### role 关联页面 ###
    # 角色所属区域
    district_loc = (By.ID, 'QueueDistrict')
    # 服务人员
    agent_loc = (By.ID, 'QueueAgent')
    # chooseagent_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-vertical")
    chooseagent_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-item.ng-star-inserted") #0615修改
    # 默认所有者
    defaultowner_loc = (By.ID, 'DefaultOwner')
    # chooseowner_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-vertical")
    # chooseowner_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-item.ng-star-inserted") #0615修改
    chooseowner_loc = (By.CSS_SELECTOR, ".ant-select-item-option-content")  # 0715修改
    # 默认负责人
    defaultresponsible_loc = (By.ID, 'DefaultResponsible')
    # chooseresponsible_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-vertical")
    # chooseresponsible_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-item.ng-star-inserted") #0615修改
    chooseresponsible_loc = (By.CSS_SELECTOR, ".ant-select-item-option-content")  # 0715修改
    # 角色管理者
    manager_loc = (By.ID, 'QueueManager')
    # choosemanager_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-vertical")
    # choosemanager_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-menu-item.ng-star-inserted") #0615修改
    choosemanager_loc = (By.CSS_SELECTOR, ".ant-select-item-option-content")  # 0715修改
    # 角色关联项按钮（小圆点2）
    #rolelinkbtn_loc = (By.CSS_SELECTOR, ".ant-steps-item-icon")
    rolelinkbtn_loc = (By.ID, "QueueAssociation")

    # 菜单权限01-请输入过滤信息框
    serachtree_loc = (By.ID, 'Search-tree')

    # 菜单权限02- 搜索后点击确定
    choosesearchtree_loc = (By.CSS_SELECTOR, '.tree-dom-element-nodes')
    # 右侧已有值的删除
    choosenotsearch_loc = (By.CSS_SELECTOR, '.ant-tree-icon-hide')

    # 检查权限选择的文本
    chooseserachtreeresult_loc = (By.CSS_SELECTOR, '.ant-tree-icon-hide')
    # chooseserachtreeresult_loc = (By.CSS_SELECTOR, '.tree-dom-node-text')
    emptyresult1 = (By.CSS_SELECTOR, '.ant-empty p')


    # 多选按钮
    # 01选择全部
    chooseallbtn_loc =   (By.ID, 'Select')

    # 02清除所有
    chooseclearbtn_loc = (By.ID, 'Clear')

    # 03反选
    chooseReversebtn_loc = (By.ID, 'Reverse')
    # 04查看选中

    # 05确定
    clickclosebtn_loc = (By.ID, 'closeOption')

    # 点击导入导出进入的页面
    # 01 左侧导入按钮
    Import_left_loc = (By.CSS_SELECTOR, 'li#Import')
    # 02 左侧导出按钮
    Export_left_loc = (By.CSS_SELECTOR, 'li#Export')

    '''
    flow
    '''

    def road(self):
        return self.find_element(self.road_loc).text

    def addrole(self):
        self.clickButton(self.addbtn_loc)
        # self.find_element(self.addbtn_loc).click()

    def importexport(self):
        self.clickButton(self.ImportExport_loc)
        # self.find_element(self.ImportExport_loc).click()

    def rolename(self, name):
        self.send_keys(self.name_loc, name)
    def nameresult(self):
        return self.find_element(self.name_loc).get_attribute('testvalue')

    def returnlist1(self):
        self.clickButton(self.returnlist1_loc)
        # 返回列表后等待元素才继续操作
        self.find_element(self.addbtn_loc)

    def savereturnbtn(self):
        self.find_element(self.savereturn_loc).click()

    def savenextbtn(self):
        self.clickButton(self.savenext_loc)
        # self.find_element(self.savenext_loc).click()

    def searchtab(self, text):
        self.clickButton(self.searchtab_loc)
        self.send_keys(self.searchtab_loc, text)

    def searchresult(self):
        # self.find_element(self.searchresult_loc)
        # return self.find_elements(self.searchresult_loc)[0].get_attribute('textContent')

        return self.find_elements(self.searchresult_loc)[0].text

    # 搜索列表显示空空如也
    def searchnotext(self):
        return self.find_element(self.searchnotext_loc).text

    # 父角色01（点击--填下拉值搜索）
    def parentrole(self,parentrole):
        self.driver.find_element(*self.parentrole_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(parentrole).perform()
    # 打印父角色中选中的值
    def parentresult(self):
        return self.find_element(self.parentrole_loc).text

    # 父角色02（选中）
    def chooseparentrole(self, parentrole):
        self.driver.find_element_by_css_selector('.ant-select-dropdown [title="' + parentrole + '"]').click()

    # 邮件地址01（点击）
    def systemadress(self):
        self.find_element(self.systemadress_loc).click()

    # 邮件地址02（选择）
    def choosesystemadress(self):
        self.find_element(self.choosesystemadress_loc).click()
    # 邮件地址 text 检查
    def systemadressresult(self):
        return self.find_element(self.systemadress_loc).text


    def comment(self, text):
        # self.find_element(self.comment_loc).sendkeys()
        self.send_keys(self.comment_loc, text)
    def commenttext(self):
        return self.find_element(self.comment_loc).get_attribute('testvalue')


    def clicksearchresult(self):
        self.find_element(self.searchresult_loc).click()


    # 上一步
    def backbtn(self):
        self.find_element(self.backbtn_loc).click()
    # 完成
    def savebtn(self):
        self.find_element(self.savebtn_loc).click()

    # 再次添加(完成并且再添加一条)
    def addagain(self):
        self.find_element(self.addagain_loc).click()
    # 返回列表
    def returnlist2(self):
        self.find_element(self.returnlist2_loc).click()

    # 有效性：选择无效
    def clickchooseinvalid(self):
        self.driver.find_element(*self.clickvalid_loc).click()
        time.sleep(2)
        # ActionChains(self.driver).send_keys("无效").perform()  # 0715修改
        self.driver.find_element(*self.chooseinvalid_loc).click()
    def chooseinvalid(self):
        self.driver.find_element(*self.choosevalid_loc).click()
    # 选择有效
    def clickchoosevalid(self):
        self.driver.find_element(*self.clickvalid_loc).click()
        time.sleep(2)
        # ActionChains(self.driver).send_keys("有效").perform() #0715修改
        self.driver.find_element(*self.choosevalid_loc).click()

    def choosevalid(self):
        self.driver.find_element(*self.choosevalid_loc).click()

    # 有效性的文本 text
    def validresult(self):
        return self.find_element(self.clickvalid_loc).text

    # 切换至无效列表
    def invalidlist(self):
        # 0806修改
        # self.find_elements(self.invalidlist_loc)[1].click()
        self.clickButton(self.invalidbtn_loc)
        # self.find_element(self.invalidbtn_loc).click()
    # # 完成后的返回列表倒计时按钮
    # def backlist(self):
    #     self.driver.find_element(self.backlist_loc).click()

    ### role 关联页面 ###
    # 点击角色所属区域
    def clickdistrict(self):
        self.driver.find_element(*self.district_loc).click()
        time.sleep(2)

    # 点击并输入选择服务人员
    # 01（点击并填值）
    def clickagent(self, agent):
        self.driver.find_element(*self.agent_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(agent).perform()


    # 打印服务人员中选中的值
    def agentresult(self):
        return self.find_element(self.agent_loc).text

    # 02（下拉选选择）
    def chooseagent(self):
        #self.driver.find_element_by_css_selector('[title="' + agent + '"]').click()
        self.driver.find_element(*self.chooseagent_loc).click()

    # 默认所有者
    # 01（点击）
    def clickdefaultowner(self, defaultowner):
        self.driver.find_element(*self.defaultowner_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(defaultowner).perform()

    # 打印服务人员中选中的值
    def defaultownerresult(self):
        return self.find_element(self.defaultowner_loc).text

    # 02（下拉选选择）
    def choosedefaultowner(self):
        self.driver.find_element(*self.chooseowner_loc).click()


    # 默认负责人
    # 01（点击）
    def clickdefaultresponsible(self, defaultresponsible):
        self.driver.find_element(*self.defaultresponsible_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(defaultresponsible).perform()

    # 打印服务人员中选中的值
    def defaultresponsibleresult(self):
        return self.find_element(self.chooseresponsible_loc).text

    # 02（下拉选选择）
    def choosedefaultresponsible(self):

        self.driver.find_element(*self.defaultresponsible_loc).click()
        # ele = self.driver.find_element(*self.defaultresponsible_loc)
        # self.driver.execute_script("arguments[0].click();", ele)


    # 角色管理者
    # 01（点击）
    def clickmanager(self, manager):
        self.driver.find_element(*self.manager_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(manager).perform()

    # 打印服务人员中选中的值
    def managerresult(self):
        return self.find_element(self.manager_loc).text

    # 02（下拉选选择）
    def choosemanager(self):
        self.driver.find_element(*self.choosemanager_loc).click()


    # 权限（左侧）
    def serachtree(self, menuname):
        self.driver.find_element(*self.serachtree_loc).click()
        self.send_keys(self.serachtree_loc, menuname)
    # 输入权限并点击权限
    def serach_choosetree(self, menuname):
        # 0715由于元素遮挡，不可直接点击
        self.send_keys(self.serachtree_loc, menuname)
        # ele = self.driver.find_element(*self.serachtree_loc)
        # self.driver.execute_script("arguments[0].click='menuname';", ele)
        self.driver.find_element_by_css_selector('[title="' + menuname + '"]').click()

    # 选中/删除
    def chooseserachtree(self):
        self.driver.find_element(*self.choosesearchtree_loc).click()

    # 二次检查已选中的值
    def chooseserachtreeresult(self):
        return self.find_elements(self.chooseserachtreeresult_loc)[1].text
    #

    # 检查左侧已有的值chooseserachtreeresult_loc
    def chooseserachtreeresult1(self):
        return self.find_elements(self.chooseserachtreeresult_loc)[0].text

    def choose_serach_emptyresult1(self):
        return self.find_element(self.emptyresult1).text

    # 权限（右侧）
    def clickserachtree2(self):
        self.driver.find_elements(*self.serachtree_loc)[1].click()

    def serachtreesendkey2(self, menuname):
        self.driver.find_elements(*self.serachtree_loc)[1].send_keys(menuname)

    # 取消选中(小删除按钮)
    def choosenotserach2(self):
        self.driver.find_elements(*self.choosenotsearch_loc)[1].click()

    # # 角色关联项按钮（小圆圈2）
    # def rolelinkbtn(self):
    #     self.driver.find_element(self.rolelinkbtn_loc).click()
    # 对选按钮 点击下拉后选择全部
    def clickallbtn(self):
        self.driver.find_element(*self.chooseallbtn_loc).click()


    # 多选按钮
    # 点击下拉选之后“确定”按钮
    def clickclosebtn(self):
        self.driver.find_element(*self.clickclosebtn_loc).click()

    # 导入导出页面---点击左侧导入按钮
    def click_Import_left(self):
        self.find_element(self.Import_left_loc).click()

    # 导入导出页面--点击左侧导出按钮
    def click_Export_left(self):
        self.find_element(self.Export_left_loc).click()
