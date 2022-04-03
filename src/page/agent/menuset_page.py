"""
@author: DT_testing
@file:   menuset_page.py
@desc:  【】
@step：
"""

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base import Base


class MenusetPage(Base):
    '''
    page
    '''
    # --------列表页面---------
    # 路径
    road_loc = (By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    # 列表--服务人员/客户用户
    # invalidlist_loc = (By.CSS_SELECTOR, ".list-tabList-item-text.flex-start")

    # 增加按钮
    addbtn_loc = (By.ID, "Add")

    # 过滤框
    searchtab_loc = (By.ID, "Search-input")
    # 搜索结果检查
    # searchresult_loc = (By.CLASS_NAME, 'ant-table-td-left-sticky')  # 0729修改
    searchresult_loc = (By.CSS_SELECTOR, 'td.ant-table-cell-fix-left')
    searchresultrow_loc = (By.CSS_SELECTOR, 'td.ant-table-cell')
    # 搜索不存在的显示“空空如也”
    searchnotext_loc = (By.CLASS_NAME, 'ant-empty-description')
    # 服务人员 、客户tab
    Customertab_loc = (By.ID, "Customer user")
    Usertab_loc = (By.ID, "User")
    # 列表为空
    emptylist_loc = (By.CSS_SELECTOR,'[class="ant-empty-description ng-star-inserted"]')

    # --------增加页面---------
    # 权限标志      权限标记校验提示
    permission_loc = (By.ID, "PermissionID")
    Permissiontip_loc = (By.ID, 'PermissionID_errorServeMessage')
    # 名称   名称校验提示
    name_loc = (By.ID, "Name")
    Nametip_loc = (By.ID, 'Name_errorServeMessage')
    # 类型
    Type_loc = (By.ID, 'Type')
    # 0922修改
    # TypeAgent_loc = (By.ID, 'Agent')
    # TypeCustomer_loc = (By.ID, 'Customer')
    TypeAgent_loc = (By.CSS_SELECTOR, 'nz-option-item[title="服务人员"]')
    TypeCustomer_loc = (By.CSS_SELECTOR, 'nz-option-item[title="用户"]')
    closetype_loc = (By.CSS_SELECTOR, '#Type .ant-select-close-icon')
    # 父权限
    Parent_loc = (By.ID, 'ParentID')

    Parent2_loc = (By.CSS_SELECTOR, '#ParentID input')

    # 备注
    Comment_loc = (By.ID, 'Comment')
    # 菜单权限
    PermissionMenu_loc = (By.ID, 'PermissionMenu')
    Permissioncheckbox_loc = (By.CSS_SELECTOR, '.ant-select-tree-checkbox-inner')
    # 所属角色 所属单位
    PermissionQueue_loc = (By.ID, 'PermissionQueue')
    PermissionQueue2_loc = (By.CSS_SELECTOR, '#PermissionQueue input')
    PermissionCompany_loc =(By.ID, 'PermissionCompany')

    # 提交按钮
    submit_loc = (By.ID, "Submit")


    # 有效性（选择有效/无效）
    clickvalid_loc = (By.ID, 'ValidID')
    # choosevalid_loc = (By.CSS_SELECTOR, '.ant-select-dropdown-menu-item-active.ng-star-inserted')  # 无效的改为有效也可使用  # 0716修改

    choosevalid_loc = (By.CSS_SELECTOR, 'nz-option-item[title="有效"]')
    chooseinvalid_loc = (By.CSS_SELECTOR, 'nz-option-item[title="无效"]')
    closevalid_loc = (By.CSS_SELECTOR, '#ValidID .ant-select-close-icon')

    # 返回按钮
    returnlist_loc = (By.ID, 'GoBack')

    '''
    flow
    '''
    # ---------列表-------------
    def road(self):
        return self.find_element(self.road_loc).text

    def addmenu(self):
        self.find_element(self.addbtn_loc).click()

    def getaddmenu(self):
        return  self.find_element(self.addbtn_loc).text

    def clickusertab(self):
        self.clickButton(self.Usertab_loc)

    def clickcustomertab(self):
        self.clickButton(self.Customertab_loc)
        time.sleep(3)

    def getemptylist(self):
        return self.find_element(self.emptylist_loc).text

    def getsearchresultrow(self):
        return self.find_elements(self.searchresultrow_loc)


    # --------新增页面----------
    def permission(self, name):
        self.send_keys(self.permission_loc, name)

    def getpermissiontip(self):
        return self.find_element(self.Permissiontip_loc).text

    def menuname(self, name):
        self.send_keys(self.name_loc, name)

    def getmenunametip(self):
        return self.find_element(self.Nametip_loc).text

    def chosetypeagent(self):
        self.clickButton(self.Type_loc)
        time.sleep(1)
        self.clickButton(self.TypeAgent_loc)

    def chosetypeustomer(self):
        self.clickButton(self.Type_loc)
        self.clickButton(self.TypeCustomer_loc)

    def dele_type(self):
        ele = self.find_element(self.Type_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.clickButton(self.closetype_loc)


    def submit(self):
        self.find_element(self.submit_loc).click()
        time.sleep(10)

    def getsubmitcolor(self):
        return self.find_element(self.submit_loc).get_attribute('disabled')

    def returnlist(self):
        self.find_element(self.returnlist_loc).click()

    def searchtab(self, text):
        self.clickButton(self.searchtab_loc)
        self.send_keys(self.searchtab_loc, text)

    # 搜索后页面loading时间长
    def searchresult(self):
        # Base(self.driver).waitclickable(self.searchresult_loc)
        return self.find_element(self.searchresult_loc).text

    def clicksearchresult(self):
        self.clickButton(self.searchresult_loc)
        time.sleep(1)

    # 取编辑菜单页面各个值
    def getname(self):
        return self.find_element(self.name_loc).get_attribute('testvalue')

    def getparentper(self):
        return self.find_element(self.Parent_loc).get_attribute('testvalue')

    def gettype(self):
        return self.find_element(self.Type_loc).text

    def getcommon(self):
        return self.find_element(self.Comment_loc).get_attribute('testvalue')

    def getvalid(self):
        return self.find_element(self.clickvalid_loc).text

    def getmenupermission(self):
        return self.find_element(self.PermissionMenu_loc).text

    def getPermissionQueue(self):
        return self.find_element(self.PermissionQueue_loc).text

    def getPermissionCompany(self):
        return self.find_element(self.PermissionCompany_loc).text

    # 搜索列表显示空空如也
    def searchnotext(self):
        return self.find_element(self.searchnotext_loc).text

    # 有效性：选择无效
    def clickchooseinvalid(self):
        self.driver.find_element(*self.clickvalid_loc).click()
        time.sleep(2)
        self.driver.find_element(*self.chooseinvalid_loc).click()  #0716修改
        # ActionChains(self.driver).send_keys("无效").perform()   0716修改

    def chooseinvalid(self):
        self.driver.find_element(*self.choosevalid_loc).click()

    # 选择有效
    def clickchoosevalid(self):
        self.driver.find_element(*self.clickvalid_loc).click()
        time.sleep(2)
        self.driver.find_element(*self.choosevalid_loc).click()  #0716修改
        # ActionChains(self.driver).send_keys("有效").perform()   0716修改

    def dele_valid(self):
        ele = self.find_element(self.clickvalid_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(2)
        self.clickButton(self.closevalid_loc)

    # 点击菜单权限
    def clickPermissionMenu(self):
        self.clickButton(self.PermissionMenu_loc)
        #self.driver.find_element(*self.PermissionMenu_loc).click()
        time.sleep(2)
        # ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    # 服务人员类菜单选择：第一个菜单--cmdb
    def clickPermissionjc(self):
        self.clickButton(self.PermissionMenu_loc)
        # self.find_element(self.PermissionMenu_loc).click()
        self.find_elements(self.Permissioncheckbox_loc)[0].click()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.find_element(
            self.PermissionMenu_loc)).send_keys(Keys.ESCAPE).perform()

    # 服务人员选择权限菜单
    def chosePermissionjc(self, number=0):
        '''
            0-集成，1-主页，2-cmdb，3-系统管理，4-工单，5-知识库
        '''
        self.clickButton(self.PermissionMenu_loc)
        self.find_elements(self.Permissioncheckbox_loc)[number].click()
        time.sleep(2)

        ActionChains(self.driver).move_to_element(self.find_element(
            self.PermissionMenu_loc)).send_keys(Keys.ESCAPE).perform()



    # 服务人员类菜单选择：主页
    def clickhome(self):
        self.clickButton(self.PermissionMenu_loc)
        self.find_elements(self.Permissioncheckbox_loc)[1].click()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(
            self.PermissionMenu_loc)).send_keys(Keys.ESCAPE).perform()

    # 客户用户类菜单选择：工单
    def clicktikect(self):
        self.clickButton(self.PermissionMenu_loc)
        self.find_elements(self.Permissioncheckbox_loc)[0].click()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(
            self.PermissionMenu_loc)).send_keys(Keys.ESCAPE).perform()

    # 客户用户类菜单选择：知识库
    def clickfaq(self):
        self.clickButton(self.PermissionMenu_loc)
        self.find_elements(self.Permissioncheckbox_loc)[2].click()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.find_element(
            self.PermissionMenu_loc)).send_keys(Keys.ESCAPE).perform()

    # 选择父权限
    def choseParent(self, text):
        self.driver.find_element_by_css_selector('#ParentID').click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(text).perform()
        # 必须加等待，等待遮罩层消失
        time.sleep(3)
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()

    # 选择角色
    def choserole(self, text):
        self.driver.find_element_by_css_selector('#PermissionQueue').click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(5)  # 必须加等待，等待遮罩层消失
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    # 选择客户
    def choseCompany(self, text):
        self.driver.find_element_by_css_selector('#PermissionCompany').click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(5)  # 必须加等待，等待遮罩层消失
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def sendcommon(self, text):
        self.send_keys(self.Comment_loc, text)

    # 删除遮罩层
    def delete_backdrop_showing(self):
        js = 'document.getElementsByClassName("cdk-overlay-backdrop nz-overlay-transparent-' \
             'backdrop cdk-overlay-backdrop-showing")[0].remove()'
        self.driver.execute_script(js)
