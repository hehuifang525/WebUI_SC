"""
@author: DT_testing
@file:   field_page.py
@desc:  【字段库】
@step：
"""
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from common.base import Base
import time


class FieldPage(Base):
    '''
    page
    '''
    # 页面路径显示
    road_loc=(By.CSS_SELECTOR, '.ant-breadcrumb')

    # 筛选的几个按钮  全部、信件、合同、客户、客户用户、知识库、配置项、工单
    all_loc=(By.ID, 'All')
    ticket_loc=(By.ID, 'Ticket')
    article_loc=(By.ID, 'Article')
    contract_loc=(By.ID, 'Contract')
    customerCompany_loc=(By.ID, 'CustomerCompany')
    customerUser_loc=(By.ID, 'CustomerUser')
    #faq_loc=(By.CSS_SELECTOR, '[class="margin-R10 ant-btn ng-star-inserted ant-btn-default"]')#0715 修改
    faq_loc = (By.CSS_SELECTOR, '[class="margin-R10 ant-btn ng-star-inserted"]#FAQ')  # 0715 修改
    # faqAfter_loc=(By.CSS_SELECTOR,'[class="margin-R10 ant-btn ng-star-inserted ant-btn-default admin-ticket-template-btn"]')
    faqAfter_loc = (By.CSS_SELECTOR, '[class="margin-R10 ant-btn ng-star-inserted admin-ticket-template-btn"]')  # 0715修改

    ITSMConfigItem_loc=(By.ID, 'ITSMConfigItem')

    # 搜索
    SearchInput_loc=(By.CSS_SELECTOR, 'input#Search-input')

    # 添加按钮
    addbtn_loc=(By.ID, 'CreateButton')

    # 字段显示类型
    fieldType_loc=(By.ID, 'FieldType')

    # 文本类型   #Text
    # textType_loc=(By.CSS_SELECTOR, '[unselectable="unselectable"]')  # 0723修改
    # textType_loc = (By.ID, 'Text')   # 0723修改
    textType_loc = (By.CSS_SELECTOR, '[title="文本"]')  # 210823修改
    # 多文本
    # TextAreaType_loc = (By.ID, 'TextArea')
    TextAreaType_loc = (By.CSS_SELECTOR, '[title="多文本类型"]')
    # 字段组
    FieldGroupType_loc = (By.CSS_SELECTOR, '[title="字段组"]')
    # 复选框
    # CheckboxType_loc = (By.ID, 'Checkbox')
    CheckboxType_loc = (By.CSS_SELECTOR, '[title="复选框"]')
    #下拉类型
    # selectType_loc=(By.CSS_SELECTOR,'ul > li:nth-child(6) > div')    # 0723 修改
    selectType_loc = (By.CSS_SELECTOR, '[title="下拉选择框"]')  # 下拉选择框
    # 系统字段对象--工单
    objectType_loc=(By.ID, 'ObjectType')

    # 对象--工单
    # ticketFieldObject_loc=(By.CSS_SELECTOR, 'ul > li:nth-child(7) > div')  # 0723 修改
    # ticketFieldObject_loc = (By.ID, 'Ticket')   # 0723 增加
    # 210820修改
    ticketFieldObject_loc = (By.CSS_SELECTOR, '.ant-select-dropdown [title="工单"]')
    # 对象--配置项   ITSMConfigItem
    # itsmFieldObject_loc=(By.CSS_SELECTOR, 'ul > li:nth-child(6) > div')   # 0723 修改
    # itsmFieldObject_loc = (By.ID, 'ITSMConfigItem')    # 0723 增加
    itsmFieldObject_loc = (By.CSS_SELECTOR, '[title="配置项"]')
    # 对象--知识库#Text  FAQ
    # faqFieldObject_loc=(By.CSS_SELECTOR, 'ul > li:nth-child(5) > div') # 0723 修改
    faqFieldObject_loc = (By.CSS_SELECTOR, '[title="知识库"]')
    # 对象--客户用户  CustomerUser
    # comuserFieldObject_loc=(By.CSS_SELECTOR, '.ant-select-dropdown-menu-item') # 0723 修改
    # comuserFieldObject_loc = (By.ID, 'CustomerUser')  # 0723 增加
    comuserFieldObject_loc = (By.CSS_SELECTOR, '[title="客户用户"]')
    # 对象--客户  CustomerCompany
    # customerFieldObject_loc=(By.CSS_SELECTOR, '.ant-select-dropdown-menu-item') # 0723 修改
    # customerFieldObject_loc = (By.ID, 'CustomerCompany')   # 0723 增加
    customerFieldObject_loc = (By.CSS_SELECTOR, '[title="客户"]')
    # 对象--合同
    contractFieldObject_loc=(By.CSS_SELECTOR, '.ant-select-dropdown-menu-item')
    # 对象--信件   Article
    # articleFieldObject_loc=(By.CSS_SELECTOR, 'ul > li:nth-child(1) > div') # 0723 修改
    # articleFieldObject_loc = (By.ID, 'Article')   # 0723 增加
    articleFieldObject_loc = (By.CSS_SELECTOR, '[title="信件"]')

    # 表格-一行记录的td FiledList01  FiledList01
    FiledList_loc = (By.CSS_SELECTOR, 'table .ant-table-tbody>tr td')

    # 系统字段
    sysfield_loc=(By.ID, 'FieldID')

    # 字段名称
    fieldname_loc=(By.ID, 'FieldName')

    # 用户不可见
    userInvisible_loc=(By.ID, '2-invisible')

    # 用户可见
    userVisible_loc=(By.ID, '1-visible')

    # 只读

    # 读写

    # 用户是否可见

    # 有效性
    valid_loc=(By.ID, 'Valid')

    # 正则表达式
    regex_loc=(By.ID, 'Regex')
    # 正则错误提示
    regexHint_loc=(By.ID, 'RegexHint')
    # 页面字段说明提示类型
    hintType_loc=(By.ID, 'HintType')

    # 选择提示在目标栏中、下方、右侧、下方
    # hintTypeValue_loc=(By.CSS_SELECTOR, '.ant-select-dropdown-menu-item') # 0723修改
    hintTypeValue01_loc = (By.CSS_SELECTOR, '[title="提示在目标栏中"]')
    hintTypeValue02_loc = (By.CSS_SELECTOR, '[title="提示在目标栏下方"]')
    hintTypeValue03_loc = (By.CSS_SELECTOR, '[title="提示在目标栏右侧的提示图标中"]')
    hintTypeValue04_loc = (By.CSS_SELECTOR, '[title="信息提示在目标栏下方，信息字体为红色"]')
    # 页面字段说明提示内容
    hintContent_loc=(By.ID, 'HintContent')
    # 计算方式
    formula_loc=(By.ID, 'Formula')
    # 提交按钮
    submit1_loc=(By.ID, 'Submit1')
    # 再添加一条
    addAnother_loc=(By.ID, 'AddAnother')
    # 返回列表
    goBack_loc=(By.ID, 'GoBack')

    # 添加选项值
    addFieldBtn_loc=(By.ID, 'addFieldBtn')

    # 添加第一个选项值
    fileTypeKey0_loc=(By.ID, 'FileTypeKey0')
    fileTypeValue0_loc=(By.ID, 'FileTypeValue0')
    # 删除
    removeField0_loc=(By.ID, 'removeField0')

    # 添加第二个选项值
    fileTypeKey1_loc=(By.ID, 'FileTypeKey1')
    fileTypeValue1_loc=(By.ID, 'FileTypeValue1')
    # 删除
    removeField1_loc=(By.ID, 'removeField1')

    # 添加第三个选项值
    fileTypeKey2_loc=(By.ID, 'FileTypeKey2')
    fileTypeValue2_loc=(By.ID, 'FileTypeValue2')
    # 删除
    removeField2_loc=(By.ID, 'removeField2')

    # 删除后查看选项数
    selectOptions_loc=(By.ID, 'SelectOptions')
    # 点击进入编辑
    # edit_loc=(By.CSS_SELECTOR, '.ant-table-td-left-sticky')    # 0723修改
    edit_loc = (By.CSS_SELECTOR, 'table .ant-table-tbody>tr td')
    # 获取系统字段提示语
    # fieldIDMessage_loc=(By.ID, 'FieldID_message')
    fieldIDMessage_loc = (By.CSS_SELECTOR, '.ng-trigger-helpMotion')
    # 获取字段名称提示语
    fieldNameMessage_loc=(By.ID, 'FieldName_message')
    # 系统字段填写错误提示语
    fieldIDError_loc=(By.CSS_SELECTOR, '.ng-trigger-helpMotion')

    #进入导入导出页面
    import_loc=(By.ID,'Import/Export')

    #导入导出页面返回按钮
    importGoBack_loc=(By.ID,'GoBack')

    #上传文件按钮
    uploadFile_loc=(By.ID,'file')

    #导入按钮
    importFile_loc=((By.CSS_SELECTOR,'[class="margin-R20 ant-btn ant-btn-primary"]'))

    #分析按钮
    analysis_loc=(By.ID,'Analysis')
    #导入页面提示语
    tips_loc=(By.CSS_SELECTOR,'.import-weight-content-desc')

    #导入进度
    speed_loc=(By.CSS_SELECTOR,'[class="ant-progress-text ng-star-inserted"]')

    #错误提示
    errorText_loc=(By.CSS_SELECTOR,'.analysis-result-error-text')
    # 左侧导出按钮
    left_Export_loc = (By.CSS_SELECTOR, 'li#Export')

    # 添加/编辑页面，选择字段库字段  FieldLibraryList
    FieldLibraryList_loc = (By.ID, 'FieldLibraryList')


    '''
    flow
    '''

    # 获取页面路径
    def getRoad(self):
        return self.find_element(self.road_loc).text

    # 点击“工单”按钮
    def clickTicket(self):
        self.clickButton(self.ticket_loc)

    def clickAll(self):
        self.clickButton(self.all_loc)

    def clickArticle(self):
        self.clickButton(self.article_loc)

    def clickContract(self):
        self.clickButton(self.contract_loc)

    def clickCompany(self):
        self.clickButton(self.customerCompany_loc)

    def clickCustomerUser(self):
        self.clickButton(self.customerUser_loc)

    def clickFAQ(self):
        self.clickButton(self.faq_loc)  # 0723修改
        # self.find_elements(self.faq_loc)[4].click()

    def clickFAQForGet(self):
        self.clickButton(self.faq_loc)
        # self.find_elements(self.faq_loc)[3].click()   # 0723 修改
        time.sleep(2)

    def clickITSM(self):
        self.clickButton(self.ITSMConfigItem_loc)

    # ----判断有没有被选中-----
    def getAllClass(self):
        return self.find_element(self.all_loc).get_attribute('class')

    def getArticleClass(self):
        return self.find_element(self.article_loc).get_attribute('class')

    def getContractClass(self):
        return self.find_element(self.contract_loc).get_attribute('class')

    def getCompanyClass(self):
        return self.find_element(self.customerCompany_loc).get_attribute('class')

    def getCustomerUserClass(self):
        return self.find_element(self.customerUser_loc).get_attribute('class')

    def getFAQClass(self):
        return self.find_element(self.faqAfter_loc).get_attribute('class')

    def getITSMClass(self):
        return self.find_element(self.ITSMConfigItem_loc).get_attribute('class')

    def getTicketClass(self):
        return self.find_element(self.ticket_loc).get_attribute('class')

    # 表格，取表格列表一行中的各个列值 FiledList_loc
    def get_filedlist_td(self, num):
        return self.find_elements(self.FiledList_loc)[num].text

    # 进入字段添加页面
    def add(self):
        self.clickButton(self.addbtn_loc)

    # 获取添加按钮文字
    def getAdd(self):
        return self.find_element(self.addbtn_loc).text

    # 返回列表
    def returnList(self):
        self.clickButton(self.goBack_loc)

    # 字段显示类型
    def fieldType(self):
        self.clickButton(self.fieldType_loc)

    # 字段显示类型----选择文本  0723
    def textType(self):
        # ele=self.find_elements(self.textType_loc)[11]
        # self.driver.execute_script('arguments[0].scrollIntoView();', ele)
        # self.driver.execute_script('arguments[0].click()', ele)
        self.clickButton(self.textType_loc)   # 0723 修改

    # 选择多文本
    def  TextArea(self):
        self.clickButton(self.fieldType_loc)
        self.clickButton(self.TextAreaType_loc)

    # 选择字段组
    def FieldGroup(self):
        self.clickButton(self.fieldType_loc)
        self.clickButton(self.FieldGroupType_loc)

    # 选择复选框
    def Checkbox(self):
        self.clickButton(self.fieldType_loc)
        self.clickButton(self.CheckboxType_loc)

    def choiceTextType(self):
        self.find_elements(self.textType_loc)[11].click()

    def selectType(self):
        self.find_element(self.selectType_loc).click()

    def objectType(self):
        self.clickButton(self.objectType_loc)

    # 对象--工单
    def objectTicket(self):
        self.clickButton(self.ticketFieldObject_loc)

    # 对象--知识库
    def objectFAQ(self):
        self.clickButton(self.faqFieldObject_loc)

    # 对象--配置项
    def objectITSM(self):
        self.clickButton(self.itsmFieldObject_loc)

    # 对象--客户用户
    def objectComuser(self):
        # self.find_elements(self.comuserFieldObject_loc)[3].click()
        self.clickButton(self.comuserFieldObject_loc)  # 0723 修改

    # 对象--客户
    def objectCompany(self):
        # self.find_elements(self.customerFieldObject_loc)[2].click()
        self.clickButton(self.customerFieldObject_loc)  # 0723 修改

    # 对象--合同
    def objectContract(self):
        self.find_elements(self.contractFieldObject_loc)[1].click()

    # 对象--信件
    def objectArticle(self):
        self.clickButton(self.articleFieldObject_loc)

    def sysField(self, sysField):
        self.send_keys(self.sysfield_loc, sysField)

    def fieldName(self, fieldName):
        self.send_keys(self.fieldname_loc, fieldName)

    def submit(self):
        self.clickButton(self.submit1_loc)
        time.sleep(15)

    def addAnother(self):
        self.clickButton(self.addAnother_loc)

    # 获取添加按钮的颜色
    def submitColor(self):
        return self.find_element(self.submit1_loc).get_attribute('disabled')

    def addAnotherColor(self):
        return self.find_element(self.addAnother_loc).get_attribute('disabled')

    def search(self, text):
        self.send_keys(self.SearchInput_loc, text)

    # 点击用户不可见
    def userInvisible(self):
        self.clickButton(self.userInvisible_loc)

    # 点击用户可见
    def userVisible(self):
        self.clickButton(self.userVisible_loc)

    # 填写正则表达式
    def regex(self, regex):
        self.send_keys(self.regex_loc, regex)

    # 清空填写的值
    def clearRegex(self):
        self.clearInput(self.regex_loc)

    # 填写正则错误提示
    def regexHint(self, regexHint):
        self.send_keys(self.regexHint_loc, regexHint)

    # 清空
    def clearRegexHint(self):
        self.clearInput(self.regexHint_loc)

    # 页面字段说明提示类型
    def hintType(self):
        self.clickButton(self.hintType_loc)

    # 选择提示在目标栏中
    def hintTypeValue01(self):
        # self.find_elements(self.hintTypeValue_loc)[0].click() #0723修改
        self.find_element(self.hintTypeValue01_loc).click()

        # 选择提示在目标栏下方
    def hintTypeValue02(self):
        # self.find_elements(self.hintTypeValue_loc)[1].click()
        self.find_element(self.hintTypeValue02_loc).click()

    # 选择提示在目标栏右侧
    def hintTypeValue03(self):
        # self.clickButton(self.hintTypeValue03_loc)
        # self.find_elements(self.hintTypeValue_loc)[2].click()
        self.find_element(self.hintTypeValue03_loc).click()

    # 选择提示在目标栏下方，字体为红色
    def hintTypeValue04(self):
        # self.find_elements(self.hintTypeValue_loc)[3].click()
        self.find_element(self.hintTypeValue04_loc).click()

    # 填写页面提示内容
    def hintContent(self, hintContent):
        self.send_keys(self.hintContent_loc, hintContent)

    # 清空填写的页面提示内容
    def clearHintContent(self):
        self.clearInput(self.hintContent_loc)

    # 计算方式
    def formula(self, formula):
        self.send_keys(self.formula_loc, formula)

    def clearFormula(self):
        self.clearInput(self.formula_loc)

    def edit(self):
        self.find_elements(self.edit_loc)[2].click()
        # self.clickButton(self.edit_loc)

    # ----------获取编辑页面的值---------
    def getFieldTypeValue(self):
        # 等待提交按钮显示后再继续操作
        self.find_element(self.submit1_loc)
        return self.find_element(self.fieldType_loc).get_attribute('testvalue')

    def getObjectTypeValue(self):
        return self.find_element(self.objectType_loc).get_attribute('testvalue')

    def getFieldIDValue(self):
        return self.find_element(self.sysfield_loc).get_attribute('testvalue')

    def getFieldNameValue(self):
        return self.find_element(self.fieldname_loc).get_attribute('testvalue')

    def getInvisibleValue(self):
        return self.find_element(self.userInvisible_loc).get_attribute('class')

    def getVisibleValue(self):
        return self.find_element(self.userVisible_loc).get_attribute('class')

    def getValidValue(self):
        return self.find_element(self.valid_loc).get_attribute('testvalue')

    def getRegexValue(self):
        return self.find_element(self.regex_loc).get_attribute('value')

    def getRegexHintValue(self):
        return self.find_element(self.regexHint_loc).get_attribute('value')

    def getHintTypeValue(self):
        return self.find_element(self.hintType_loc).get_attribute('textContent')

    def getHintContentValue(self):
        return self.find_element(self.hintContent_loc).get_attribute('testvalue')

    def getFormulaValue(self):
        return self.find_element(self.formula_loc).get_attribute('value')

    # 下拉框添加按钮
    def addFieldBtn(self):
        return self.clickButton(self.addFieldBtn_loc)

    def fileTypeKey0(self, fileTypeKey0):
        self.send_keys(self.fileTypeKey0_loc, fileTypeKey0)

    def fileTypeValue0(self, fileTypeValue0):
        self.send_keys(self.fileTypeValue0_loc, fileTypeValue0)

    def fileTypeKey1(self, fileTypeKey1):
        self.send_keys(self.fileTypeKey1_loc, fileTypeKey1)

    def fileTypeValue1(self, fileTypeValue1):
        self.send_keys(self.fileTypeValue1_loc, fileTypeValue1)

    def fileTypeKey2(self, fileTypeKey2):
        self.send_keys(self.fileTypeKey2_loc, fileTypeKey2)

    def fileTypeValue2(self, fileTypeValue2):
        self.send_keys(self.fileTypeValue2_loc, fileTypeValue2)

    def removeField0(self):
        self.clickButton(self.removeField0_loc)

    def removeField1(self):
        self.clickButton(self.removeField1_loc)

    def removeField2(self):
        self.clickButton(self.removeField2_loc)

    # 删除后选项数为0
    def getSelectOptions(self):
        return self.find_element(self.selectOptions_loc).text

    # 当类型为下拉框时，获取下拉框中填写的值
    def getFileTypeKey0Value(self):
        return self.find_element(self.fileTypeKey0_loc).get_attribute('value')

    def getFileTypeValue0Value(self):
        return self.find_element(self.fileTypeValue0_loc).get_attribute('value')

    def getFileTypeKey1Value(self):
        return self.find_element(self.fileTypeKey1_loc).get_attribute('value')

    def getFileTypeValue1Value(self):
        return self.find_element(self.fileTypeValue1_loc).get_attribute('value')

    def getFileTypeKey2Value(self):
        return self.find_element(self.fileTypeKey2_loc).get_attribute('value')

    def getFileTypeValue2Value(self):
        return self.find_element(self.fileTypeValue2_loc).get_attribute('value')

    # 获取提示语
    def getFieldIDMessage(self):
        return self.find_element(self.fieldIDMessage_loc).text

    def getFieldNameMessage(self):
        return self.find_element(self.fieldNameMessage_loc).text

    def getFieldError(self):
        return self.find_element(self.fieldIDError_loc).text

    #进入导入导出页面
    def import_export(self):
        self.clickButton(self.import_loc)

    #导入导出页面返回按钮
    def importGoBack(self):
        self.clickButton(self.importGoBack_loc)

    #上传文件按钮
    def uploadFile(self):
        ele=self.driver.find_element_by_id('file')
        self.driver.execute_script('arguments[0].click()', ele)
        time.sleep(3)

    #导入按钮
    def importFile(self):
        self.find_elements(self.importFile_loc)[1].click()

    def getTips(self):
       return self.find_element(self.tips_loc).get_attribute('innerText')

    #获取导入按钮颜色
    def getImportColor(self):
        return self.find_elements(self.importFile_loc)[1].get_attribute('style')
    def getSpeed(self):
        return self.find_element(self.speed_loc).get_attribute('textContent')
    def getErrorText(self):
        return self.find_element(self.errorText_loc).get_attribute('textContent')

    # 点击左侧导出按钮
    def left_Export(self):
        self.clickButton(self.left_Export_loc)

    # 选择字段库字段
    def chose_field(self,field):
        title = '[title="'+ field +'"]'
        self.find_element(self.FieldLibraryList_loc ).click()
        ActionChains(self.driver).send_keys(field).perform()
        # print(title)
        elm = (By.CSS_SELECTOR, title)
        self.find_element(elm).click()

    # 取字段组中显示的字段, 以系统字段字段参数
    def get_group_field(self, loc):
        title = '[id="'+"fields" + loc + '"] label'
        # print(title)
        elm = (By.CSS_SELECTOR, title)
        return self.find_element(elm).text



