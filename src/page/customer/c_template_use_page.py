"""
@author: DT_testing
@file:   c_template_use_page.py
@desc:  【】
@step：  
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from common.base import Base


class C_TemplateUsePage(Base):
    '''
    page
    '''
    # ----------------工单模板选择---------------
    # # 流程名称
    # process_name_loc = (By.CSS_SELECTOR, ".create-ticket-template-content > h4")
    # # 模板 1 名称（收藏的模板）[0]
    # template1_name_loc = (By.CSS_SELECTOR, ".create-ticket-template-content > span")
    # # 模板 2 名称（未收藏的模板）[1]
    # # template2_name_loc = (By.CSS_SELECTOR, ".create-ticket-template-content > span")
    #
    # # 选择第一个工单模板点击（收藏的那个模板）
    # template01choose_loc = (By.CSS_SELECTOR, '[class="create-ticket-template-content"]')
    #
    # # 收藏的模板颜色
    # template1_color_loc = (By.CSS_SELECTOR, ".create-ticket-template-icon")
    # # 收藏的模板图标--现在 bug 不能显示出图标
    # template1_img_loc = (By.CSS_SELECTOR,'#ticketTemplate1 > div > span > fa-icon > svg')
    #
    # # 模板 2---未收藏的第一个 名称
    # template2_name_loc = (By.CSS_SELECTOR, "#ticketTemplate3 > div > div > span")
    # 收藏的模板 [0] 、第一个工单模板(非收藏) [1]
    template01choose_loc = (By.CSS_SELECTOR, '[class="create-ticket-template-content"]')

    # 流程名称
    process_name_loc = (By.CSS_SELECTOR, '[class="create-ticket-template-title ellipsis-row"]')
    # 模板 1 名称
    # template1_name_loc = (By.CSS_SELECTOR, ".create-ticket-template-content > span")
    # 模板 1 颜色
    template1_color_loc = (By.CSS_SELECTOR, ".create-ticket-template-icon")
    # 模板 1  图标
    template1_img_loc = (By.CSS_SELECTOR, '#ticketTemplate1 > div > span > fa-icon > svg')

    # 模板名称
    template_name_loc = (By.CSS_SELECTOR, '[class="create-ticket-template-desc"]')

    # 客户 A-1 使用的模板2
    template22_name_loc = (By.ID, "ticketTemplate44")


    # ----------------工单模板创单页面------------
    type_loc = (By.ID, 'TypeID')  # 类型
    customeruser_loc = (By.ID, "CustomerUser")  # 客户用户
    # 客户名称
    company_loc = (By.ID, "CustomerID")
    # 资产
    cmdbbtn_loc = (By.CSS_SELECTOR, '.search-content-btn')
    customernocmdbtips_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-content>div')
    cmdbtips_ntb_loc = (By.CSS_SELECTOR, '.ant-btn.ant-btn-primary.ng-star-inserted')

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

    # dynamic_field 省市区
    province_loc = (By.ID, "DynamicField_province")
    city_loc = (By.ID, "DynamicField_city")
    qu_loc = (By.ID, "DynamicField_qu")
    qu_readonly_loc = (By.ID, "DynamicField_qu")

    province1_loc = (By.ID, "DynamicField_sheng1")
    city1_loc = (By.ID, "DynamicField_city1")
    # 价格、数量
    price_loc = (By.ID, 'DynamicField_ziduanzu1_price')
    amount_loc = (By.ID, 'DynamicField_ziduanzu1_amount')

    # 再添加一组
    addGroupField_loc = (By.ID, 'addGroupField')
    price2_loc = (By.ID, 'DynamicField_ziduanzu1_price1')
    amount2_loc = (By.ID, 'DynamicField_ziduanzu1_amount1')

    # 删除第三个组
    remove_2_loc = (By.ID, 'remove_2')
    price3_loc = (By.ID, 'DynamicField_ziduanzu1_price2')
    amount3_loc = (By.ID, 'DynamicField_ziduanzu1_amount2')

    # 提交按钮
    submitbtn_loc = (By.ID, "submit")

    # 提交并完成
    submitandcontinue_loc = (By.ID, "submitContinue")   # 20200909 用户元素更新为 submitContinue

    # 提交并完成后的路径
    road_submitandcontinue_loc = (By.CSS_SELECTOR, '[class ="ant-breadcrumb"]')

    # 文本字段
    wenben1_loc = (By.ID, "DynamicField_wenben")


    '''
    flow
    '''
    # 进入收藏的模板
    def templatefavoritechoose(self):
        self.find_elements(self.template01choose_loc)[0].click()
        time.sleep(2)

    # 进入第一个未收藏的工单模板
    def template01choose(self):
        self.find_elements(self.template01choose_loc)[1].click()
        time.sleep(2)

    # 进入第二个未收藏的工单模板
    def template02choose(self):
        self.find_elements(self.template01choose_loc)[2].click()
        time.sleep(2)

    def template03choose(self):
        self.find_elements(self.template01choose_loc)[3].click()
        time.sleep(2)

    # 客户 A-1 使用的模板1
    def templateforA1(self):
        self.find_element(self.template01choose_loc).click()
        time.sleep(2)

    # 客户 A-1 使用的模板2
    def templateforA2(self):
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
        self.driver.find_element(*self.cmdbtips_ntb).click()


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
        ActionChains(self.driver).send_keys(province).perform()
        time.sleep(2)
        self.driver.find_element_by_id(province).click()
        time.sleep(2)

    def city(self, city):
        self.driver.find_element(*self.city_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(city).perform()
        time.sleep(2)
        self.driver.find_element_by_id(city).click()
        time.sleep(2)

    def sendprice(self, price):
        self.driver.find_element(*self.price_loc).send_keys(price)
    def sendamount(self, amount):
        self.driver.find_element(*self.amount_loc).send_keys(amount)

    # 第二组
    def sendprice2(self, price):
        self.driver.find_element(*self.price2_loc).send_keys(price)
    def sendamount2(self, amount):
        self.driver.find_element(*self.amount2_loc).send_keys(amount)

    # 第三组
    def sendprice3(self, price):
        self.driver.find_element(*self.price3_loc).send_keys(price)

    def sendamount3(self, amount):
        self.driver.find_element(*self.amount3_loc).send_keys(amount)



    def addGroupField(self):
        self.driver.find_element(*self.addGroupField_loc).click()

    # 删除第三个组
    def remove_2(self):
        self.driver.find_element(*self.remove_2_loc).click()

    # 只读字段及字段值
    def company_readonly(self):
        return self.driver.find_element(*self.company_loc).get_attribute('class')

    def qu_readonly(self):
        return self.driver.find_element(*self.qu_readonly_loc).get_attribute('class')

    def wenben1_readonly(self):
        return self.driver.find_element(*self.wenben1_loc).get_attribute('class')

    def company_readonly_value(self):
        return self.driver.find_element(*self.company_loc).get_attribute('testvalue')

    def qu_readonly_value(self):
        return self.driver.find_element(*self.qu_loc).get_attribute('testvalue')

    def wenben1_readonly_value(self):
        return self.driver.find_element(*self.wenben1_loc).get_attribute('testvalue')



    # process_name
    def process_name(self):
        return self.driver.find_elements(*self.process_name_loc)[0].text

    # template1_name
    def template1_name(self):
        # return self.driver.find_element(*self.template1_name_loc).text
        return self.driver.find_elements(*self.template_name_loc)[0].text
    # template1_color
    def template1_color(self):
        return self.driver.find_elements(*self.template1_color_loc)[0].get_attribute('style')

    # template1_img
    def template1_img(self):
        return self.driver.find_element(*self.template1_img_loc).get_attribute('data-icon')


    # template2_name
    def template2_name(self):
       # return self.driver.find_element(*self.template2_name_loc).text
       return self.driver.find_elements(*self.template_name_loc)[1].text

    # ----------------工单模板创单页面_点击---------------
    def typeclick(self):
        self.driver.find_element(*self.type_loc).click()

    def stateclick(self):
        self.driver.find_element(*self.state_loc).click()

    def priorityclick(self):
        self.driver.find_element(*self.priority_loc).click()

    # 点击省 、市 字段检查下拉选
    def provinceclick(self):
        self.driver.find_element(*self.province_loc).click()

    def cityclick(self):
        self.driver.find_element(*self.city_loc).click()
    # 点击省1 、市1 字段检查下拉选
    def province1click(self):
        self.driver.find_element(*self.province1_loc).click()
    def city1click(self):
        self.driver.find_element(*self.city1_loc).click()

    # ------------------下拉选的值-------
    # 下拉选值的检查
    def selectorvalues(self):
        return self.driver.find_element(*self.selectorvalues_loc).text
    # 下拉选值的选中
    def chooseselectorvalues(self,value):
        self.driver.find_element_by_css_selector('[testvalue="' + value + '"]').click()



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

