"""
@author: DT_testing
@file:   template_use_page.py
@desc:  【】
@step：  
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common.base import Base


class TemplateUsePage(Base):
    '''
    page
    '''
    # ----------------工单模板选择---------------

    # 收藏的模板 [0]
    template01choose_loc = (By.CSS_SELECTOR, '[class="create-ticket-template-content"]')

    # 流程名称
    process_name_loc = (By.CSS_SELECTOR, '[class="create-ticket-template-title ellipsis-row"]')

    # 非收藏的模板 1 名称 -- #ticketTemplate1 > div > div > span  20200902 更新
    #template1_name_loc = (By.CSS_SELECTOR, ".create-ticket-template-content > span")
    template1_name_loc = (By.CSS_SELECTOR, "#ticketTemplate1 > div > div > span")

    # 模板 1 颜色
    template1_color_loc = (By.CSS_SELECTOR, ".create-ticket-template-icon")
    # 模板 1  图标
    template1_img_loc = (By.CSS_SELECTOR, '#ticketTemplate1 > div > span > fa-icon > svg')

    # 模板 2 名称
    template2_name_loc = (By.CSS_SELECTOR, "#ticketTemplate2 > div > div > span")

    # 模板 3 名称
    template3_name_loc = (By.CSS_SELECTOR, "#ticketTemplate25 > div > div > span")

    # 流程“不同角色可使用”
    template11_name_loc = (By.ID, "ticketTemplate1")
    template22_name_loc = (By.ID, "ticketTemplate43")

    # ----------------工单模板创单页面------------
    type_loc = (By.ID, 'TypeID')  # 类型
    customeruser_loc = (By.ID, "CustomerUser")  # 客户用户
    # 角色
    role_loc = (By.ID, "QueueID")

    # 客户名称
    company_loc = (By.ID, "CustomerID")
    # 资产
    cmdbbtn_loc = (By.CSS_SELECTOR, '.search-content-btn')
    customernocmdbtips_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-content>div')
    tips_ntb_loc = (By.CSS_SELECTOR, '.ant-btn.ant-btn-primary.ng-star-inserted')

    queue_loc = (By.CSS_SELECTOR, '#QueueID > div > nz-select-item')  # 角色
    owner_loc = (By.ID, 'OwnerID')   # 指定处理人
    responsible_loc = (By.ID, 'ResponsibleID')  # 负责人
    subject_loc = (By.ID, 'Subject')  # 主题
    # 文本
    # tickettext_loc =  (By.ID, 'cke_1_contents')
    tickettext_loc = (By.CSS_SELECTOR, '[role="textbox"]')

    # 状态
    state_loc = (By.ID, 'StateID')
    # 优先级
    priority_loc = (By.ID, 'PriorityID')

    # 下拉选值
    selectorvalues_loc = (By.CLASS_NAME, "cdk-virtual-scroll-content-wrapper")
    roleselectorvalue_loc =(By.CLASS_NAME, "cdk-overlay-pane")

    # dynamic_field 省市区
    province_loc = (By.ID, "DynamicField_province")
    city_loc = (By.ID, "DynamicField_city")
    qu_loc = (By.ID, "DynamicField_qu")
    # qu_readonly_loc = (By.CSS_SELECTOR, "#DynamicField_qu > nz-select-top-control > nz-select-search > input")
    qu_readonly_loc = (By.ID, "DynamicField_qu")
    province1_loc = (By.ID, "DynamicField_sheng1")
    city1_loc = (By.ID, "DynamicField_city1")

    # 价格、数量
    price_loc =  (By.ID,'DynamicField_ziduanzu1_price')
    amount_loc = (By.ID,'DynamicField_ziduanzu1_amount')


    # 提交按钮
    submitbtn_loc = (By.ID, "submit")

    # 提交并完成submitContinue
    submitandcontinue_loc = (By.ID, "submitAndContinue")

    # 提交并完成后的路径
    road_submitandcontinue_loc = (By.CSS_SELECTOR, '[class ="ant-breadcrumb"]')


    '''
    flow
    '''
    # 点击进入收藏的模板
    def templatefavoritechoose(self):
        self.find_elements(self.template01choose_loc)[0].click()
        time.sleep(2)


    # 点击进入第一个未收藏的工单模板
    def template01choose(self):
        self.find_element(self.template1_name_loc).click()
        time.sleep(2)


    # 点击进入第二个未收藏的工单模板
    def template02choose(self):
        self.find_element(self.template2_name_loc).click()
        time.sleep(2)

    # 点击进入第三个未收藏的工单模板
    def template03choose(self):
        self.find_element(self.template3_name_loc).click()
        time.sleep(2)

    # ---流程：不同角色可用
    # 第一个模板使用 id
    def template11choose(self):
        self.find_element(self.template11_name_loc).click()
        time.sleep(2)

    # 第二个模板使用 id
    def template22choose(self):
        self.find_element(self.template22_name_loc).click()
        time.sleep(2)

    # 工单模板内字段检查（1. 有隐藏的字段 2.有必填的 3. 有默认填值的  4. 有“显示”的）
    def customeruser(self,customerusername,customeruserlogin):
        self.driver.find_element(*self.customeruser_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(customerusername).perform()
        time.sleep(2)
        self.driver.find_element_by_id(customeruserlogin).click()

    def cmdbbtn(self):
        self.driver.find_element(*self.cmdbbtn_loc).click()
    # 未选择客户用户时，点击资产弹框的提示
    def customernocmdbtips(self):
        return self.driver.find_element(*self.customernocmdbtips_loc).text
    # 点击弹框的确定按钮
    def cmdbtips_ntb(self):
        # self.driver.find_element(*self.tips_ntb_loc).click()
        self.driver.find_elements(*self.tips_ntb_loc)[1].click() # 20201010更新

    def owner(self, owner):
        self.driver.find_element(*self.owner_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(owner).perform()
        self.driver.find_element_by_css_selector("[testvalue=" + owner + "]").click()
        time.sleep(2)

    def responsible(self, responsible):
        self.driver.find_element(*self.responsible_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(responsible).perform()
        self.driver.find_element_by_css_selector("[testvalue=" + responsible + "]").click()
        time.sleep(2)

    # 主题subject_loc
    def subject(self, subject):
        self.driver.find_element(*self.subject_loc).clear()
        time.sleep(2)
        self.driver.find_element(*self.subject_loc).send_keys(subject)

    # 文本 -- 更换内容编辑器之后调整代码
    def tickettext(self, text):
        # # 鼠标点击一下文本内部
        # self.driver.find_element(*self.tickettext_loc).click()
        # # 写入文字：先定位到div-iframe的xpath，然后再输入内容
        # self.driver.switch_to.frame(
        #     self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        # actions = ActionChains(self.driver)
        # actions.send_keys(text).perform()
        #
        # # 切出执行其他操作
        # self.driver.switch_to.default_content()
        self.driver.find_element(*self.tickettext_loc).click()

    # 文本内容 -- 更换内容编辑器之后调整代码
    def tickettextvalue(self):
        return self.driver.find_element(*self.tickettext_loc).text

        # # 鼠标点击一下文本内部
        # # 写入文字：先定位到div-iframe的xpath，然后再输入内容
        # self.driver.switch_to.frame(
        #     self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        #
        # return self.driver.find_element_by_xpath("/html/body").text

    # -------------------自定义字段-------------------------
    # print(context1)
    def province(self, province):
        self.driver.find_element(*self.province_loc).click()
        time.sleep(2)
        # ActionChains(self.driver).send_keys(province).perform()
        # time.sleep(2)
        # self.driver.find_element_by_id(province).click()
        # time.sleep(2)
        self.driver.find_element_by_id(province).click()
        time.sleep(2)

    def city(self, city):
        self.driver.find_element(*self.city_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(city).perform()
        time.sleep(2)
        self.driver.find_element_by_id(city).click()
        time.sleep(2)

    def sendamount(self, amount):
        self.driver.find_element(*self.amount_loc).send_keys(amount)

    def sendprice(self, price):
        self.driver.find_element(*self.price_loc).send_keys(price)



    def qu_readonly(self):
        return self.driver.find_element(*self.qu_readonly_loc).get_attribute('class')

    def qu_readonly_value(self):
        return self.driver.find_element(*self.qu_loc).get_attribute('testvalue')


    # process_name
    def process_name(self):
        return self.driver.find_elements(*self.process_name_loc)[0].text

    # template1_name
    def template1_name(self):
        return self.driver.find_element(*self.template1_name_loc).text

    # template1_color
    def template1_color(self):
        return self.driver.find_elements(*self.template1_color_loc)[0].get_attribute('style')

    # template1_img
    def template1_img(self):
        return self.driver.find_element(*self.template1_img_loc).get_attribute('data-icon')


    # template2_name
    def template2_name(self):
        return self.driver.find_element(*self.template2_name_loc).text

    # ----------------工单模板创单页面_点击---------------
    def roleclick(self):
        self.driver.find_element(*self.role_loc).click()

    def typeclick(self):
        self.driver.find_element(*self.type_loc).click()

    def stateclick(self):
        self.driver.find_element(*self.state_loc).click()

    def priorityclick(self):
        self.driver.find_element(*self.priority_loc).click()

    # 点击省1 、市1 字段检查下拉选
    def province1click(self):
        self.driver.find_element(*self.province1_loc).click()
    def city1click(self):
        self.driver.find_element(*self.city1_loc).click()

    # ------------------下拉选的值-------
    # 下拉选值的检查
    def selectorvalues(self):
        return self.driver.find_element(*self.selectorvalues_loc).text
    def roleselectorvalue(self):
        return self.driver.find_element(*self.roleselectorvalue_loc).text   # 角色父子级单独写


    # 下拉选值的选中
    def chooseselectorvalues(self,value):
        self.driver.find_element_by_css_selector('[testvalue="' + value + '"]').click()
    def choosetitlevalues(self,title):
        self.driver.find_element_by_css_selector('[title="' + title + '"]').click()  # 角色使用


    # ----------------工单模板创单页面_模板中默认设置的字段值在页面的显示情况------------
    def companyvalue(self):
        return self.driver.find_element(*self.company_loc).get_attribute('testvalue')

    def typevalue(self):
        return self.driver.find_element(*self.type_loc).get_attribute('testvalue')

    def queuevalue(self):
        return self.driver.find_element(*self.queue_loc).get_attribute('title')

    def ownervalue(self):
        return self.driver.find_element(*self.owner_loc).get_attribute('testvalue')

    def responsiblevalue(self):
        return self.driver.find_element(*self.responsible_loc).get_attribute('testvalue')

    def subjectvalue(self):
        return self.driver.find_element(*self.subject_loc).get_attribute('testvalue')


    def statevalue(self):
        return self.driver.find_element(*self.state_loc).get_attribute('testvalue')

    def priorityvalue(self):
        return self.driver.find_element(*self.priority_loc).get_attribute('testvalue')

    def provincevalue(self):
        return self.driver.find_element(*self.province_loc).get_attribute('testvalue')

    def cityvalue(self):
        return self.driver.find_element(*self.city_loc).get_attribute('testvalue')

    # 提交按钮
    def submitbtn(self):
        self.driver.find_element(*self.submitbtn_loc).click()

    # 提交并完成
    def submitandcontinue(self):
        self.driver.find_element(*self.submitandcontinue_loc).click()

    # 检查提交/提交并完成按钮是灰色
    def color_submitbtn(self):
        return self.driver.find_element(*self.submitbtn_loc).get_attribute('style')  # background-color: rgb(191, 191, 191);

    def color_submitandcontinue(self):
        return self.driver.find_element(*self.submitandcontinue_loc).get_attribute('style')  # background-color: rgb(191, 191, 191);

    # 提交并完成后的路径
    def road_submitandcontinue(self):
        return self.driver.find_element(*self.road_submitandcontinue_loc).text

