"""
@author: DT_testing
@file:   customer_user_page.py
@desc:  【客户用户管理】
@step：
"""
from selenium.webdriver.common.by import By
from common.base import Base
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class CustomerUserPage(Base):

    # 路径
    road_loc = (By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    # 页内title(小title)
    tabtitle_loc = (By.CSS_SELECTOR,'.cursor.ng-star-inserted.nav-horizontal-active.relative div span')
    # 添加客户按钮
    # AddCompanybtn_loc = (By.ID,'AddSubCompany')
    AddCompanybtn_loc = (By.CSS_SELECTOR, '.company-action li#AddSubCompany')
    # 编辑客户按钮
    EditCompanybtn_loc = (By.ID, 'EditCompany')
    # 设置客户主管按钮
    SetManagerbtn_loc = (By.ID, 'SetCompanyManager')
    # 关联服务按钮
    AssociateServicebtn_loc = (By.ID, 'AssociateService')
    # 关联角色按钮
    AssociateQueuebtn_loc = (By.ID, 'AssociateQueue')
    # 搜索用户
    Searchuserbtn_loc = (By.ID,'Search-input')
    # 搜索到的第一条用户数据
    Searchfirstuser_loc = (By.CSS_SELECTOR, 'tbody>tr.ant-table-row.ng-star-inserted')
    # 取用户列表-有效tab的标题
    # Valid_usesrnumber_loc =(By.CSS_SELECTOR,'#Valid>span')  # 0810修改
    Valid_usesrnumber_loc = (By.ID, 'Valid')  # 0810修改
    # 搜索客户
    SearchCompanybtn_loc = (By.ID, 'Search-tree')
    SearchCompanybtn2_loc = (By.CSS_SELECTOR, '#CustomerCompanyMainTree .ant-input')

    # 搜索客户后数据,按属性去元素
    # SearchresultCom_loc = (By.CSS_SELECTOR, '[class ="tree-dom-element-hover active-tree ng-star-inserted"]')
    SearchresultCom_loc = (By.CSS_SELECTOR, '.ant-tree-node-content-wrapper.ant-tree-node-selected')
    # 用户为空时列表提示语言
    userempty_loc =  (By.CSS_SELECTOR, '.empty-text.ng-star-inserted span')

    # ----------------------start  添加客户页面字段----------------------------.active-tree>span>span
    # 添加/编辑页面的左上角页面标题,添加用户页面同样共用
    left_title_loc = (By.CSS_SELECTOR,'#main-title>h4')
    # 客户编号
    CustomerID_loc = (By.ID,'CustomerID')
    # 客户编号下的重复提示信息
    repeat_CustomerID_loc = (By.ID,'CustomerID_errorServeMessage')
    # 负责人
    Responsible_loc = (By.ID, 'DepartmentResponsible')
    # 负责人-选择全部
    Responsible_Select_loc = ( By.ID,'Select')
    # 负责人-确定
    Responsible_closeOption_loc = (By.ID, 'closeOption')
    # 负责人-反选
    Responsible_Reverse_loc = (By.ID, 'Reverse')
    # 负责人-清除所有
    Responsible_Clear_loc = (By.ID, 'Clear')
    # 负责人-查看选中
    Responsible_checkOption_loc = (By.CSS_SELECTOR, '.check-box-no.margin-R5.ng-star-inserted')
    # 负责人-删除
    Responsible_dele_loc = (By.CSS_SELECTOR, '#DepartmentResponsible [nztype="close"]')

    #Responsible_dele_loc = (By.CSS_SELECTOR, '[style = "user-select: none;"]')



    # 客户名称
    CompanyName_loc = (By.ID,'CustomerCompanyName')
    # 客户名称的重复提示信息
    repeat_CompanyName_loc = (By.ID,'CustomerCompanyName_errorServeMessage')
    # 父部门  父部门的输入框值
    ParentCustomer_loc = (By.ID, 'ParentCustomerID')
    # 父部门 输入框后的删除
    ParentCustomer_dele_loc = (By.CSS_SELECTOR, '#ParentCustomerID [nztype="close-circle"]')
    # 区域、区域的输入框值
    CompanyDistrict_loc = (By.ID, 'CustomerCompanyDistrict')
    # 街道
    CompanyStreet_loc = (By.ID, 'CustomerCompanyStreet')
    # 邮编
    CompanyZIP_loc = (By.ID, 'CustomerCompanyZIP')
    # 城市
    CompanyCity_loc = (By.ID, 'CustomerCompanyCity')

    # 国家 ，取第一个国家  ，取国家输入框的值
    CompanyCountry_loc = (By.ID, 'CustomerCompanyCountry')
    Afghanistan_loc = (By.ID, '.ant-select-dropdown-menu-vertical>li>div')
    # 网址
    CompanyURL_loc = (By.ID, 'CustomerCompanyURL')
    # 备注
    CompanyComment_loc = (By.ID, 'CustomerCompanyComment')
    # 有效性父元素、 #有效 、#无效、有效性输入框内的值
    companyValidID_loc = (By.ID,'ValidID')
    # companyValid_loc = (By.CSS_SELECTOR, '.ant-select-dropdown-menu-item.ng-star-inserted:nth-child(1)')
    # companyinvalid_loc = (By.CSS_SELECTOR, '.ant-select-dropdown-menu-item.ng-star-inserted:nth-child(2)')
    companyValid_loc = (By.CSS_SELECTOR, 'nz-option-item:nth-child(1)')
    companyinvalid_loc = (By.CSS_SELECTOR, 'nz-option-item:nth-child(2)')

    #valid_text_loc = (By.CSS_SELECTOR, '#ValidID>div>div>div')
    # 有效性将鼠标放上去后，的“×”元素
    # valid_del_loc = (By.CSS_SELECTOR, 'i.anticon.ant-select-close-icon')
    valid_del_loc = (By.CSS_SELECTOR, '#ValidID i.anticon.ant-select-close-icon')

    # 提交按钮
    Submit1btn_loc = (By.ID,'Submit1')
    # 添加，编辑页面的返回列表按钮
    Goback1btn_loc = (By.ID, 'Goback1')
    # -------------------------end  添加客户页面字段----------------------------------------

    # ----------设置关联项页面-----------------

    associate_manager_loc = (By.CSS_SELECTOR,'.item-img.associate-manager')
    # .item-img.associate-service
    associate_service_loc = (By.CSS_SELECTOR, '.item-img.associate-service')

    # 上一步
    Previous_loc = (By.ID, 'Previous')
    # 返回列表
    GoBackbtn_loc = (By.ID, 'GoBack')

    # 设置部门关联服务
    # 提交
    Submit_server_loc = (By.ID,'Submit2')
    # 返回关联项
    ReturnAssocia_server_loc = (By.ID,'ReturnAssociation2')
    # 返回列表GoBack3
    server_back_loc = (By.ID, 'GoBack3')
    # 服务框 CompanyLinkService
    CompanyLink_server_loc = (By.ID, 'CompanyLinkService')

    # ##-------------设置客户主管页面----------
    # 确定按钮
    Submit_manager_loc = (By.ID, 'Ok1')
    # 返回关联项
    ReturnAssocia_manager_loc = (By.ID, 'ReturnAssociation1')
    # 返回列表  Goback2
    # GoBack2_manager_loc = (By.ID, 'GoBack2')
    GoBack2_manager_loc = (By.CSS_SELECTOR, 'button#Goback2')
    # 继续设置关联信息
    ContinueSetting_loc = (By.ID, 'ContinueSetting')

    # 添加用户
    AddCustomerUser_loc = (By.ID, 'AddCustomerUser')
    # 转移客户
    MoveToDepartment_loc = (By.ID, 'MoveToDepartment')
    # 导入导出
    ImportExport_loc = (By.ID, 'ImportExport')
    # 导出当前
    ExportSelected_loc = (By.ID,'ExportSelected')
    # 有效用户列表
    user_valid_loc =  (By.ID,'valid')
    # 无效用户列表
    user_invalid_loc   = (By.ID,'Invalid')
    # 用户右上角的设置图标
    preferenceset_loc = (By.ID,'preferenceset')

    # # ----start添加用户页面元素---
    UserTitle_loc = (By.CSS_SELECTOR, 'input#UserTitle')
    UserFullname_loc = (By.ID, 'UserFullname')
    UserLastname_loc = (By.ID, 'UserLastname')
    UserFirstname_loc = (By.ID, 'UserFirstname')
    UserLogin_loc = (By.ID, 'UserLogin')
    repeat_userlogin_loc = (By.ID,'UserLogin_errorServeMessage')
    UserPassword_loc = (By.ID, 'UserPassword')
    # 密码后面的可见与隐藏图标
    UserPassword_eyeicon_loc = (By.ID, 'eye-icon')

    UserEmail_loc = (By.ID, 'UserEmail')
    # 邮箱的重复提示信息
    repeat_UserEmail_loc = (By.ID, 'UserEmail_errorServeMessage')
    UserCustomerID_loc = (By.ID, 'UserCustomerID')
    # 选择客户编号（取搜索命中的）
    UserCustomer_select_loc = (By.CSS_SELECTOR, '[class ="font-highlight"]')
    # 客户编号后面的叉×
    UserCustomer_dele_loc = (By.CSS_SELECTOR, '.ant-select-clear-icon.anticon-close-circle')
    # 客户编号的第一条
    Userfirstcustomer_loc = (By.CSS_SELECTOR, '.ant-select-tree-dropdown>nz-tree>ul>nz-tree-node:nth-child(1)>li')
    UserDistrict_loc = (By.ID, 'UserDistrict')
    UserPhone_loc = (By.ID, 'UserPhone')
    UserFax_loc = (By.ID, 'UserFax')
    UserMobile_loc = (By.ID, 'UserMobile')
    UserStreet_loc = (By.ID, 'UserStreet')
    UserZip_loc = (By.ID, 'UserZip')
    UserCity_loc = (By.ID, 'UserCity')
    UserCountry_loc = (By.ID, 'UserCountry')
    UserComment_loc = (By.ID, 'UserComment')
    # 有效框、有效、无效
    UserValidID_loc = (By.ID, 'ValidID')
    UserValid_loc = (By.CSS_SELECTOR, 'nz-option-item:nth-child(1)')
    Userinvalid_loc = (By.CSS_SELECTOR, 'nz-option-item:nth-child(2)')
    # 有效性将鼠标放上去后，的“×”元素
    user_valid_del_loc = (By.CSS_SELECTOR, '#ValidID i.anticon.ant-select-close-icon')
    # 提交
    adduser_Submit_loc = (By.ID, 'Submit')
    # 返回列表
    adduser_back_loc = (By.ID, 'GoBack')
    # 左上角标题 ,与客户页面共用
    # ----导入导出页面元素
    # 返回
    ImportExportback_loc = (By.ID,'GoBack')
    # 左侧导入按钮  li#Import
    Importbtn_loc = (By.CSS_SELECTOR, 'li#Import')
    # 左侧导出按钮
    Exportbtn_loc = (By.CSS_SELECTOR, 'li#Export')

    # # ----end添加用户页面元素---

    # 获取路径内容
    def road(self):
        return self.find_element(self.road_loc).text

    # 获取tab title
    def tabtitle(self):
        return  self.find_element(self.tabtitle_loc).text

    # 往搜索用户框输入信息
    def Searchuser(self, text):
        self.clickButton(self.Searchuserbtn_loc)
        time.sleep(2)
        self.send_keys(self.Searchuserbtn_loc, text)
    # 点击搜索到的用户，第一条
    # tbody>tr.ant-table-row.ng-star-inserted

    def  click_Searchfirstuser(self):
        self.clickButton(self.Searchfirstuser_loc)

    # 取有效用户的有效tab的标题
    def getValidusesrnumber(self):
        return self.find_element(self.Valid_usesrnumber_loc).get_attribute("title")



    def userempty(self):
        return  self.find_element(self.userempty_loc).text

    # 往搜索客户框输入信息
    def SearchCompany(self, text):
        self.find_element(self.SearchCompanybtn_loc).clear()
        self.send_keys(self.SearchCompanybtn_loc, text)



    # 点击搜索结果
    def Searchresultcom_click(self):
        # self.find_element(self.SearchresultCom_loc).click()
        self.clickButton(self.SearchresultCom_loc)

    def Searchresultcom2_click(self, text):
        self.find_element(self.SearchCompanybtn2_loc).clear()
        self.send_keys(self.SearchCompanybtn2_loc, text)
        time.sleep(2)
        title = '[title="'+ text +'"]'
        self.driver.find_element_by_css_selector(title).click()
        time.sleep(1)

    # 获取客户的搜索结果文本
    def Searchresultcom_text(self):
        return self.find_element(self.SearchresultCom_loc)

    # 添加客户
    def AddCompany(self):
        # self.find_element(self.AddCompanybtn_loc).click()

        self.clickButton(self.AddCompanybtn_loc)
        time.sleep(8)

    # 获取添加和编辑客户页面的标题
    def Edit_title(self):
        return  self.find_element(self.left_title_loc).text

    # 添加客户提交
    def Companysub(self):
        self.clickButton(self.Submit1btn_loc)
        # self.find_element(self.Submit1btn_loc).click()

    # 判断提交按钮是否可触发
    def submit_enabled(self):
        return  self.find_element(self.Submit1btn_loc).is_enabled()


    #添加客户-返回列表
    def Companyback(self):
        # self.find_element(self.Goback1btn_loc).click()
        self.clickButton(self.Goback1btn_loc)


    #填写客户编号
    def CustomerID(self,text):
        elem = self.find_element(self.CustomerID_loc)
        elem.clear()
        elem.send_keys(text)
        time.sleep(5)
        elem.send_keys(Keys.ENTER)

    #取客户编号输入框的值
    def CustomerID_text(self):
      return  self.find_element(self.CustomerID_loc).get_attribute("testvalue")
    # 清空客户编号的输入
    def clear_CustomerID(self):
      self.find_element(self.CustomerID_loc).clear()

    #判断客户编号提示信息是否存在
    def repeat_CustomerID(self):
        return self.find_element(self.repeat_CustomerID_loc).text

    # 填写客户名称
    def CompanyName(self, text):
        self.send_keys(self.CompanyName_loc,text)
    #  取客户名称输入框内的值
    def CompanyName_text(self):
      return  self.find_element(self.CompanyName_loc).get_attribute("testvalue")
    # 清空客户名称的输入
    def clear_CompanyName(self):
      self.find_element(self.CompanyName_loc).clear()

    # 判断客户名称提示信息是否存在
    def repeat_CompanyName(self):
        return self.find_element(self.repeat_CompanyName_loc).text
    # 点击负责人下拉框
    def click_Responsible(self):
        self.clickButton(self.Responsible_loc)
        time.sleep(2)
    # 负责人-选择全部
    def click_Responsible_Select(self):
        self.clickButton(self.Responsible_Select_loc)
    # 负责人-确定
    def click_Responsible_closeOption(self):
        self.clickButton(self.Responsible_closeOption_loc )
    # 负责人-反选
    def click_Responsible_Reverse(self):
        self.clickButton(self.Responsible_Reverse_loc)
    # 负责人-清除所有
    def click_Responsible_Clear(self):
        self.clickButton(self.Responsible_Clear_loc )
    # 负责人-查看选中
    def click_Responsible_checkOption(self):
        self.clickButton(self.Responsible_checkOption_loc)
    # 负责人-删除
    def click_Responsible_dele(self):

        self.clickButton(self.Responsible_dele_loc)


    # 取负责人输入框内的值
    def Responsible_text(self):
      return self.find_element(self.Responsible_loc).get_attribute("testvalue")

    # 点击父部门
    def click_ParentCustomer(self):
        self.clickButton(self.ParentCustomer_loc)
    # 点击父部门并选择指定父部门
    def select_ParentCustomer(self,ele):
        self.clickButton(self.ParentCustomer_loc)
        time.sleep(2)
        elm = ".ant-select-tree-node-content-wrapper[title =" + "'" + ele + "'" + "]"
        self.driver.find_element_by_css_selector(elm).click()


    # 取父部门输入框内的值
    def ParentCustomer_text(self):
      return self.find_element(self.ParentCustomer_loc).text
    # 删除父部门  ParentCustomer_dele_loc
    def ParentCustomer_dele(self):
        ele = self.find_element(self.ParentCustomer_loc)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(1)
        self.clickButton(self.ParentCustomer_dele_loc)
    # 填写区域
    # 取区域内的值
    def CompanyDistrict_text(self):
      return self.find_element(self.CompanyDistrict_loc).text

    # 填写街道
    def CompanyStreet(self, text):
        self.send_keys(self.CompanyStreet_loc, text)

    # 取街道输入框的值
    def CompanyStreet_text(self):
      return self.find_element(self.CompanyStreet_loc).get_attribute("testvalue")

    # 填写邮编
    def CompanyZIP(self,text):
        self.send_keys(self.CompanyZIP_loc,text)

    # 取邮编输入框的值
    def CompanyZIP_text(self):
      return  self.find_element(self.CompanyZIP_loc).get_attribute("testvalue")

    # 填写城市
    def CompanyCity(self,text):
        self.send_keys(self.CompanyCity_loc, text)

    # 取城市输入框的值
    def CompanyCity_text(self):
      return self.find_element(self.CompanyCity_loc).get_attribute("testvalue")

    # 选择国家
    def CompanyCountry(self):
        self.clickButton(self.CompanyCountry_loc)
        # self.find_element(self.CompanyCountry_loc).click()
        time.sleep(1)
        self.find_element(self.Afghanistan_loc).click()

    # 取国家输入框内的值
    def CompanyCountry_text(self):
      return  self.find_element(self.CompanyCountry_loc).get_attribute("testvalue")

    # 填写网址
    def CompanyURL(self,text):
        self.send_keys(self.CompanyURL_loc, text)

    # 取网址输入框的值
    def CompanyURL_text(self):
      return self.find_element(self.CompanyURL_loc).get_attribute("testvalue")

    # 填写备注
    def CompanyComment(self,text):
        self.send_keys(self.CompanyComment_loc,text)

    # 取备注输入框的值
    def CompanyComment_text(self):
      return  self.find_element(self.CompanyComment_loc).get_attribute("testvalue")

    # 点击有效性-选择有效
    def valid(self):
        self.clickButton(self.companyValidID_loc)
        # self.find_element(self.companyValidID_loc).click()
        time.sleep(2)
        self.clickButton(self.companyValid_loc)
        # self.find_element(self.companyValid_loc).click()

    # 点击有效性-选择无效

    def invalid(self):
        self.clickButton(self.companyValidID_loc)
        # self.find_element(self.companyValidID_loc).click()
        time.sleep(3)
        self.clickButton(self.companyinvalid_loc)
        # self.find_element(self.companyinvalid_loc ).click()

    # 取有效性输入框的值
    def valid_text(self):
      return self.find_element(self.companyValidID_loc).text

    # 将鼠标移动到有效性上
    def move_valid(self):
        elm = self.find_element(self.companyValidID_loc)
        ActionChains(self.driver).move_to_element(elm).perform()

    # 点击有效性输入框后的删除“×”
    def vaild_dete(self):
        self.clickButton(self.valid_del_loc)
        # self.find_element(self.valid_del_loc).click()

    # 进入编辑客户
    def EditCompany(self):
        time.sleep(1)
        self.clickButton(self.EditCompanybtn_loc)
        time.sleep(1)
        # 等待提交按钮到可点击的状态再取值
        Base(self.driver).waitclickable(self.Submit1btn_loc)

    # 点击设置客户主管按钮
    def SetManager(self):
        self.clickButton(self.SetManagerbtn_loc)

    # 点击关联服务按钮
    def AssociateService(self):
        self.clickButton(self.AssociateServicebtn_loc)

    # 点击导入导出按钮
    def ImportExport(self):
        self.clickButton(self.ImportExport_loc)

    # 设置关联项页面，点击设置主管
    def associate_manager(self):
        # self.find_element(self.associate_manager_loc).click()
        self.clickButton(self.associate_manager_loc)
    # 设置关联项页面，点击关联服务

    def associate_service(self):
        # self.find_element(self.associate_service_loc).click()
        self.clickButton(self.associate_service_loc)

    # 设置关联项页面 点击上一步

    def Previous(self):
        # self.find_element(self.Previous_loc).click()
        self.clickButton(self.Previous_loc)

    # 设置关联项页面 点击返回列表
    def associate_GoBack(self):
        # self.find_element(self.GoBackbtn_loc).click()
        self.clickButton(self.GoBackbtn_loc)

    # 关联信息--设置客户主管-返回关联项
    def ReturnAssocia_manager(self):
        self.clickButton(self.ReturnAssocia_manager_loc)

    # 关联信息-设置客户主管-返回列表
    def manager_backlist(self):
        self.find_element(self.GoBack2_manager_loc).click()
        # self.clickButton(self.GoBack2_manager_loc)


    # 设置部门关联服务页面，提交
    def Submit_server(self):
        # self.find_element(self.Submit_server_loc).click()
        self.clickButton(self.Submit_server_loc)

    # 设置部门关联服务页面，返回关联项
    def ReturnAssocia_server(self):
        # self.find_element(self.ReturnAssocia_server_loc).click()
        self.clickButton(self.ReturnAssocia_server_loc)

    # 设置部门关联服务页面，返回列表
    def server_back(self):
        self.find_element(self.server_back_loc).click()
        # self.clickButton(self.server_back_loc)
    # 设置部门关联服务页面，取服务框中的值

    def server_text(self):
        return  self.find_element(self.CompanyLink_server_loc).text
    # 点击继续设置关联信息按钮

    def ContinueSetting(self):
        # self.find_element(self.ContinueSetting_loc).click()
        self.clickButton(self.ContinueSetting_loc)


    # 添加用户
    def adduser(self):
        # self.find_element(self.AddCustomerUser_loc).click()
        self.clickButton(self.AddCustomerUser_loc)

    # 点击用户的无效列表
    def click_invaliduser(self):
        # self.find_element(self.user_invalid_loc).click()
        self.clickButton(self.user_invalid_loc)


    # #-------start 添加用户页面----------
    def usertitle(self, text):
        self.find_element(self.UserTitle_loc).clear()
        self.send_keys(self.UserTitle_loc, text)

    # 获取用户标题或问候语
    def usertitle_text(self):
        return self.find_element(self.UserTitle_loc).get_attribute('testvalue')

    def userfullname(self, text):
        self.find_element(self.UserFullname_loc).clear()
        self.send_keys(self.UserFullname_loc, text)
    # 获取全名
    def userfullname_text(self):
        return self.find_element(self.UserFullname_loc).get_attribute('testvalue')

    # 姓
    def userlastname(self, text):
        self.find_element(self.UserLastname_loc).clear()
        self.send_keys(self.UserLastname_loc, text)

    def userlastname_text(self):
        return self.find_element(self.UserLastname_loc).get_attribute('testvalue')

    # 名
    def userfirstname(self, text):
        self.find_element(self.UserFirstname_loc).clear()
        self.send_keys(self.UserFirstname_loc, text)

    def userfirstname_text(self):
        return self.find_element(self.UserFirstname_loc).get_attribute('testvalue')

    # 账号
    def userlogin(self, text):
        self.find_element(self.UserLogin_loc).clear()
        self.send_keys(self.UserLogin_loc, text)
    # 输入账户后输入回车
    def userlogin_enter(self, text):
        elem = self.find_element(self.UserLogin_loc)
        elem.clear()
        elem.send_keys(text)
        time.sleep(5)
        elem.send_keys(Keys.ENTER)

    def userlogin_text(self):
        return self.find_element(self.UserLogin_loc).get_attribute('testvalue')




    # 判断用户账户的重复提示信息是否存在
    def repeat_userlogin(self):
        return  self.find_element(self.repeat_userlogin_loc).text

    # 清空账号账号
    def clear_userlogin(self):
        self.find_element(self.UserLogin_loc).clear()

  # 密码
    def userpwd(self, text):
        self.find_element(self.UserPassword_loc).clear()
        self.send_keys(self.UserPassword_loc, text)

    def userpwd_text(self):
        return self.find_element(self.UserPassword_loc).text

    def click_userpwd_eyeicon(self):
        # self.find_element(self.UserPassword_eyeicon_loc).click()
        self.clickButton(self.UserPassword_eyeicon_loc)

    # 取用户密码框的显示类型  UserPassword_loc
    def userpwd_type(self):
        return self.find_element(self.UserPassword_loc).get_attribute('type')

    # 邮件地址
    def useremail(self, text):
        self.find_element(self.UserEmail_loc).clear()
        self.send_keys(self.UserEmail_loc, text)

    # 输入邮件地址，并输入回车
    def useremail_enter(self, text):
        elem = self.find_element(self.UserEmail_loc)
        elem.clear()
        elem.send_keys(text)
        time.sleep(5)
        elem.send_keys(Keys.ENTER)


    def useremail_text(self):
        return self.find_element(self.UserEmail_loc).get_attribute('testvalue')
    # 邮件重复的提示信息
    def repeat_UserEmail(self):
        return self.find_element(self.repeat_UserEmail_loc).text

    def click_usercustomerid(self):
        # self.find_element(self.UserCustomerID_loc).click()
        self.clickButton(self.UserCustomerID_loc)

    # 选择客户编号
    def selectcustomer(self, ele):
        elm = "[title ="+"'" + ele + "'"+"]"
        self.driver.find_element_by_css_selector(elm).click()

    # 选择第一条客户编号
    def selectfirstcustomer(self):
        # self.find_element(self.UserCustomerID_loc).click()
        self.clickButton(self.UserCustomerID_loc)
        time.sleep(7)
        element = self.find_element(self.Userfirstcustomer_loc)
        # self.driver.execute_script("arguments[0].click();", element)
        ActionChains(self.driver).move_to_element(element).click(element).perform()



        # time.sleep(4)
        # self.find_element(self.Userfirstcustomer_loc).click()

    def usercustomerid_text(self):
        return self.find_element(self.UserCustomerID_loc).get_attribute('testvalue')

    # 鼠标移动到客户编号，然后点击后面的叉删除
    def user_customerid_dele(self):
        elm = self.find_element(self.UserCustomerID_loc)
        ActionChains(self.driver).move_to_element(elm).perform()
        self.find_element(self.UserCustomer_dele_loc).click()

    # 获取区域
    def userdistrict(self, text):
        self.find_element(self.UserDistrict_loc).clear()
        self.send_keys(self.UserDistrict_loc, text)

    def userdistrict_text(self):
        return self.find_element(self.UserDistrict_loc).get_attribute('testvalue')

    # 获取电话
    def userphone(self, text):
        self.find_element(self.UserPhone_loc).clear()
        self.send_keys(self.UserPhone_loc, text)

    def userphone_text(self):
        return self.find_element(self.UserPhone_loc).get_attribute('testvalue')

    # 获取传真
    def userfax(self, text):
        self.find_element(self.UserFax_loc).clear()
        self.send_keys(self.UserFax_loc, text)

    def userfax_text(self):
        return self.find_element(self.UserFax_loc).get_attribute('testvalue')

    # 获取手机
    def usermobile(self, text):
        self.find_element(self.UserMobile_loc).clear()
        self.send_keys(self.UserMobile_loc, text)

    def usermobile_text(self):
        return self.find_element(self.UserMobile_loc).get_attribute('testvalue')

    # 获取街道
    def userstreet(self, text):
        self.find_element(self.UserStreet_loc).clear()
        self.send_keys(self.UserStreet_loc, text)

    def userstreet_text(self):
        return self.find_element(self.UserStreet_loc).get_attribute('testvalue')

    # 获取邮编
    def userzip(self, text):
        self.find_element(self.UserZip_loc).clear()
        self.send_keys(self.UserZip_loc, text)

    def userzip_text(self):
        return self.find_element(self.UserZip_loc).get_attribute('testvalue')

    # 获取城市
    def usercity(self, text):
        self.find_element(self.UserCity_loc).clear()
        self.send_keys(self.UserCity_loc, text)

    def usercity_text(self):
        return self.find_element(self.UserCity_loc).get_attribute('testvalue')

    # 获取国家
    def usercountry(self, text):
        self.find_element(self.UserCountry_loc).clear()
        self.send_keys(self.UserCountry_loc, text)

    def usercountry_text(self):
        return self.find_element(self.UserCountry_loc).get_attribute('testvalue')

    # 获取备注
    def usercommom(self, text):
        self.find_element(self.UserComment_loc).clear()
        self.send_keys(self.UserComment_loc, text)

    def usercommom_text(self):
        return self.find_element(self.UserComment_loc).get_attribute('testvalue')

    # 有效
    def uservaild(self):
        # self.find_element(self.UserValidID_loc).click()
        self.clickButton(self.UserValidID_loc)
        time.sleep(4)
        self.clickButton(self.UserValid_loc)
        # self.find_element(self.UserValid_loc).click()

    # 无效
    def userinvaild(self):
        self.clickButton(self.UserValidID_loc)
        # self.find_element(self.UserValidID_loc).click()
        time.sleep(3)
        self.clickButton(self.Userinvalid_loc)
        # self.find_element(self.Userinvalid_loc).click()

    def uservaild_text(self):
        return self.find_element(self.UserValidID_loc).get_attribute('testvalue')

    # 将鼠标移动到有效性上
    def user_move_valid(self):
        elm = self.find_element(self.UserValidID_loc)
        ActionChains(self.driver).move_to_element(elm).perform()

    # 点击有效性输入框后的删除“×”
    def user_vaild_dete(self):
        elm = self.find_element(self.UserValidID_loc)
        time.sleep(2)
        ActionChains(self.driver).move_to_element(elm).perform()
        # self.find_element(self.user_valid_del_loc).click()
        self.clickButton(self.user_valid_del_loc)

    def click_adduser_Submit(self):
        if self.find_element(self.adduser_Submit_loc).is_enabled():
            self.clickButton(self.adduser_Submit_loc)
        else:
            print("提交按钮不可点击")

    def adduser_Submit_enabled(self):
        return self.find_element(self.adduser_Submit_loc).is_enabled()

    def click_adduser_back(self):
        self.clickButton(self.adduser_back_loc)
    # -------end 添加用户页面----------

    # -----导入导出页面--
    # 点击返回按钮
    def ImportExportback(self):
        self.clickButton(self.ImportExportback_loc)

    # 点击左侧导入
    def Importleft(self):
        self.clickButton(self.Importbtn_loc)

    # 点击左侧导出
    def Exportleft(self):
        self.clickButton(self.Exportbtn_loc)