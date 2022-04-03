"""
@author: QianJingjing
@file:   template_page.py
@desc:  【工单模板】
@step：
"""
from selenium.webdriver.common.by import By

from common.base import Base
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class TemplatePage(Base):
    '''
    page
    '''
    # ----------------工单模板配置页面，列表----------------
    # 路径
    road_loc = (By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    # 增加模板按钮
    addbtn_loc = (By.ID, "addTemplate")
    import_loc = (By.ID, 'import')
    # 按客户过滤 第一个class
    searchcustomer_loc = (By.CSS_SELECTOR, "[class='ant-select-selection__rendered']")
    # 按角色过滤 第二个class
    searchrole_loc = (By.CSS_SELECTOR, "[class='ant-select-selection__rendered']")
    # 过滤框 第二个class
    search_loc = (By.ID, "Search-input")
    tabtitle_loc = (By.CSS_SELECTOR, '.nav-horizontal-active [class="nav-horizontal-title ellipsis-row"]')
    # 工单模板数量显示
    tmpnumber_loc = (By.CSS_SELECTOR, ".flex-space-between.list-tabList-detail>[class='ng-star-inserted']")
    # 搜索框为空的描述信息
    emptydescribe_loc = (By.CSS_SELECTOR, '[class="empty-text ng-star-inserted"]')
    # 搜索结果
    searchresult_loc = (By.CSS_SELECTOR, '.cursor.ant-table-row.ng-star-inserted')
    searchresulttd_loc = (By.CSS_SELECTOR, '.cursor.ant-table-row.ng-star-inserted td')
    # 列表表头字段
    #
    tableth_loc = (By.CSS_SELECTOR, '.ant-table-thead th')


    # 复制 Copy
    copy_loc = (By.ID, 'Copy')

    # 导出  Export
    export_loc = (By.ID, "Export")
    # 删除  删除提示语  取消  确认
    delete_loc = (By.ID, "Delete")
    # deletetitle_loc = (By.CSS_SELECTOR, "div [class='ant-modal-confirm-title']")
    deletetitle_loc = (By.CSS_SELECTOR, "div .ant-modal-confirm-title")
    cancle_loc = (By.CSS_SELECTOR, 'button.ant-btn.ng-star-inserted:nth-child(1)')
    # confirm_loc = (By.CSS_SELECTOR, 'button.ant-btn.ng-star-inserted:nth-child(2)')
    confirm_loc = (By.CSS_SELECTOR, 'button.ant-btn.ant-btn-danger.ng-star-inserted')

    # --------------工单模板配置页面，新增页面---------------
    # 提交
    commitbtn_loc = (By.ID, 'submit')
    # 返回列表
    backlist_loc = (By.ID, 'goBack')
    # 左上角标题栏
    titlebar_loc = (By.CSS_SELECTOR, '[class="breadcrumb-overflow"]')
    # 名称 名称重复信息
    name_loc = (By.ID, 'Name')
    rename_loc = (By.CSS_SELECTOR, '.ng-trigger.ng-trigger-helpMotion')
    # 在以下界面可用（服务人员、用户）
    agent_loc = (By.ID, 'Agent')
    customer_loc = (By.CSS_SELECTOR, 'div #Customer')
    # 角色 Role  客户
    role_loc = (By.ID, 'Role')
    Company_loc = (By.ID, 'FilterCompany')
    # 取客户/角色输入框前的字段名称
    # rolecompany_lable_loc = (By.CSS_SELECTOR, 'div [class="ng-untouched ng-dirty ng-invalid"] label')
    rolecompany_lable_loc = (By.CSS_SELECTOR, 'nz-form-label[class="ant-form-item-label ant-col ant-col-8"]>label')
    # 角色为空的提示语
    emptyrole_loc = (By.CSS_SELECTOR,'[class="ant-empty-description ng-star-inserted"]')

    # 提示信息
    message_loc = (By.CSS_SELECTOR, '[class="prompt-message-text font12 relative '
                                    'ant-col ant-col-offset-8 ng-star-inserted"]')
    # 显示位置
    showLocation_loc = (By.ID, 'ShowLocation')
    # 选择全部 、清除所有、反选、确定Select
    selectall_loc = (By.ID, 'Select')
    clear_loc = (By.ID, 'Clear')
    reverse_loc = (By.ID, 'Reverse')
    closeOption_loc = (By.ID, 'closeOption')
    # 显示位置：移动端、网页web端、windwos端
    mobile_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(1)')
    web_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(3)')
    windows_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(4)')
    # 类型:创建工单、处理工单、工单详情展示
    templateType_loc = (By.ID, 'TemplateType')
    createticket_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(1)')
    process_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(2)')
    details_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(3)')
    # 显示类型： 普通表单、快捷操作
    displayType_loc = (By.ID, 'TemplateDisplayType')
    commonform_loc = (By.CSS_SELECTOR, 'div.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(1)')
    quickoperation_loc = (By.CSS_SELECTOR, 'div.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(2)')
    # 描述
    describe_loc = (By.ID, 'Describe')
    # 关联知识库类型 、类别、关键字
    relationFaqType_loc = (By.ID, 'RelationFaqType')
    category_loc = (By.CSS_SELECTOR, 'div.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(1)')
    keyword_loc = (By.CSS_SELECTOR, 'div.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(2)')
    # 关联知识库内容,Misc 事故报告
    relationFaqContent_loc = (By.ID ,'RelationFaqContent')
    Misc_loc = (By.CSS_SELECTOR, '[title="Misc"]')
    accidentreport_loc = (By.CSS_SELECTOR, '[title="事故报告"]')
    # 模板颜色
    ticketColor_loc = (By.ID, 'TicketColor')
    # 模板图片
    defaultimg_loc = (By.ID, 'award')
    img_loc = (By.ID, 'cannabis')
    # 有效性  有效、无效
    validinput_loc = (By.ID, 'ValidID')
    valid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(1)')
    invalid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(2)')
    # 工单模板过滤信息
    # -------工单模板显示信息
    # 取该模块的显示字段
    temshowfield_loc = (By.CSS_SELECTOR, '.ant-form-item.ant-row.ng-star-inserted>.ant-form-item-label>label')

    # 类型 隐藏 显示 必填 只读
    type_loc = (By.ID,'TypeID')
    hiddentype_loc = (By.ID,'hidden_fieldsTypeID')
    showntype_loc = (By.ID, 'shown_fieldsTypeID')
    requiredtype_loc = (By.ID, 'required_fieldsTypeID')
    readonlytype_loc = (By.ID, 'readonly_fieldsTypeID')

    # 类型
    chosetype_loc = (By.CSS_SELECTOR, '[class="cdk-virtual-scroll-content-wrapper"] nz-option-item:nth-child(5)')

    # 客户用户
    # 删除客户用户
    delCustomerUser_loc = (By.ID, 'delete_fieldsCustomerUser')
    # 客户名称
    # 删除客户用户名称
    delCustomerID_loc = (By.ID, 'delete_fieldsCustomerID')
    # 客户用户资产
    # 删除客户用户资产
    delConfigItems_loc = (By.ID, 'delete_fieldsConfigItems')
    # 角色 隐藏 显示 必填 只读
    queue_loc = (By.ID, 'QueueID')
    hiddenqueue_loc = (By.ID, 'hidden_fieldsQueueID')
    shownqueue_loc = (By.ID, 'shown_fieldsQueueID')
    requiredqueue_loc = (By.ID, 'required_fieldsQueueID')
    readonlyqueue_loc = (By.ID, 'readonly_fieldsQueueID')
    # 指定处理人  OwnerID
    owner_loc = (By.ID, 'OwnerID')
    # 删除指定处理人
    delOwner_loc = (By.ID, 'delete_fieldsOwnerID')
    # 负责人
    # 删除负责人
    delresponsibleID_loc = (By.ID, 'delete_fieldsResponsibleID')
    # 主题 隐藏 显示 必填 只读
    subject_loc = (By.ID, 'Subject')
    hiddensubject_loc = (By.ID, 'hidden_fieldsSubject')
    shownsubject_loc = (By.ID, 'shown_fieldsSubject')
    requiredsubject_loc = (By.ID, 'required_fieldsSubject')
    readonlysubject_loc = (By.ID, 'readonly_fieldsSubject')

    # 删除按钮---类型、角色、主题、内容、状态、优先级
    delete_type_loc = (By.ID, 'delete_fieldsTypeID')
    delete_queue_loc = (By.ID, 'delete_fieldsQueueID')
    delete_subject_loc = (By.ID, 'delete_fieldsSubject')
    delete_body_loc = (By.ID, 'delete_fieldsBody')
    delete_state_loc = (By.ID, 'delete_fieldsStateID')
    delete_priority_loc = (By.ID, 'delete_fieldsPriorityID')
    # 内容 隐藏 显示 必填 只读
    hiddenbody_loc = (By.ID, 'hidden_fieldsBody')
    shownbody_loc = (By.ID, 'shown_fieldsBody')
    requiredbody_loc = (By.ID, 'required_fieldsBody')
    readonlybody_loc = (By.ID, 'readonly_fieldsBody')
    # 内容iframe 框
    iframe_loc =(By.CSS_SELECTOR, '[class="cke_wysiwyg_frame cke_reset"]')
    iframe_body_loc = (By.CSS_SELECTOR, '[class="cke_editable cke_editable_themed cke_contents_ltr cke_show_borders"]')
    content_loc = (By.CSS_SELECTOR,'[role="textbox"]')
    # 状态 隐藏 显示 必填 只读
    state_loc = (By.ID, 'StateID')
    hiddenstate_loc = (By.ID, 'hidden_fieldsStateID')
    shownstate_loc = (By.ID, 'shown_fieldsStateID')
    requiredstate_loc = (By.ID, 'required_fieldsStateID')
    readonlystate_loc = (By.ID, 'readonly_fieldsStateID')
    pedingstate_loc = (By.CSS_SELECTOR, '[class="cdk-virtual-scroll-content-wrapper"] nz-option-item:nth-child(8)')
    # 状态黑色小三角
    down_fieldsState_loc = (By.ID, 'down_fieldsStateID')
    Stateoptions_loc = (By.ID, 'StateID_optionsShowValue')
    # 主题黑色小三角
    down_fieldsSubject_loc = (By.ID,'down_fieldsSubject')
    # 主题说明提示类型
    Subject_explain_type_loc = (By.CSS_SELECTOR, '#promptDisplaySubject .ant-select-show-arrow')
    #
    Subject_explain_type_text_loc = (By.CSS_SELECTOR, '#promptDisplaySubject .ant-select-show-arrow input')
    # 
    Subject_explain_option_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item')
    # 主题说明提示内容
    Subject_explain_Content_loc = (By.ID, 'Subject_ConfigFieldHintContent')

    # 状态选项中选择新建
    Stateoptions_new_loc = (By.CSS_SELECTOR, '[class="cdk-virtual-scroll-content-wrapper"] nz-option-item:nth-child(1)')
    # 优先级 隐藏 显示 必填 只读
    priority_loc = (By.ID, 'PriorityID')
    hiddenpriority_loc = (By.ID, 'hidden_fieldsPriorityID')
    shownpriority_loc = (By.ID, 'shown_fieldsPriorityID')
    requiredpriority_loc = (By.ID, 'required_fieldsPriorityID')
    readonlypriority_loc = (By.ID, 'readonly_fieldsPriorityID')
    chosepriority_loc =(By.CSS_SELECTOR, '[class="cdk-virtual-scroll-content-wrapper"] nz-option-item:nth-child(5)')
    # 挂起时间 隐藏 显示 必填 只读 ，挂起时间选择框
    Pending_loc = (By.ID, 'fieldsPendingTime')
    hiddenPending_loc = (By.ID, 'hidden_fieldsPendingTime')
    shownPending_loc = (By.ID, 'shown_fieldsPendingTime')
    requiredPending_loc = (By.ID, 'required_fieldsPendingTime')
    readonlyPending_loc = (By.ID, 'readonly_fieldsPendingTime')

    Pendingmonth_loc = (By.ID, 'PendingTime_month')
    chosemonth_loc =(By.CSS_SELECTOR,'[class="cdk-virtual-scroll-content-wrapper"] nz-option-item:nth-child(3)')
    Pendingdate_loc =(By.ID, 'PendingTime_date')
    chosedate_loc = (By.CSS_SELECTOR, '[class="cdk-virtual-scroll-content-wrapper"] nz-option-item:nth-child(3)')
    # 选择要显示的字段
    dynamicFieldSelect_loc = (By.ID, 'DynamicFieldSelect_Search2')

    # 指定处理人，必填
    required_fieldsOwner_loc = (By.ID, 'required_fieldsOwnerID')



    # 添加字段
    # 添加字段组
    '''
            工单模板添加自定义字段页面
    '''
    # addfield_loc = (By.CSS_SELECTOR, '[class="cursor absolute template-add-icon"]')  #addIcon
    addfield_loc = (By.ID, 'addIcon')  # addIcon
    # 字段显示类型
    fieldType_loc = (By.ID, 'FieldType')
    textType_loc = (By.ID, 'Text')  # 文本
    selectType_loc = (By.ID, 'Dropdown')  # 下拉选c择框
    # dateType_loc = (By.ID, 'Date')  # 日期
    dateType_loc = (By.CSS_SELECTOR, '[title="日期（年-月-日）"]')  # 日期
    # datetimeType_loc = (By.ID, 'DateTime')  # 日期时间

    datetimeType_loc = (By.CSS_SELECTOR, '[title="日期（年-月-日 时:分:秒）"]')
    # checkboxType_loc = (By.ID, 'Checkbox')  # 复选框
    checkboxType_loc = (By.CSS_SELECTOR, '[title="复选框"]')  # 复选框

    # 系统字段
    sysfield_loc = (By.ID, 'FieldID')

    # 字段名称
    fieldname_loc = (By.ID, 'FieldName')

    fieldvalid_loc = (By.ID, 'Valid')

    # 添加选项值
    addFieldBtn_loc = (By.ID, 'addFieldBtn')

    # 添加第一个选项值
    fileTypeKey0_loc = (By.ID, 'FileTypeKey0')
    fileTypeValue0_loc = (By.ID, 'FileTypeValue0')
    # 删除
    removeField0_loc = (By.ID, 'removeField0')

    # 添加第二个选项值
    fileTypeKey1_loc = (By.ID, 'FileTypeKey1')
    fileTypeValue1_loc = (By.ID, 'FileTypeValue1')

    # 添加第三个选项值
    fileTypeKey2_loc = (By.ID, 'FileTypeKey2')
    fileTypeValue2_loc = (By.ID, 'FileTypeValue2')
    # 提交
    fieldsubmi_loc = (By.ID, 'Submit2')

    # 自定义日期字段，时间控件的确认按钮
    dateconfirm_loc = (By.CSS_SELECTOR, '.ant-btn-sm')

    # 客户用户
    CustomerUser_loc = (By.ID, 'CustomerUser')

    def chose_customer_user(self, customer_user):
        self.find_element(self.CustomerUser_loc).click()
        ActionChains(self.driver).send_keys(customer_user).perform()
        title = '[title="' + customer_user + '"]'

        elem = (By.CSS_SELECTOR, title)
        self.find_element(elem).click()

    def get_customer_user(self):
        return self.find_element(self.CustomerUser_loc).text

    # 等待表头元素出现  tableth_loc
    def wait_tableth(self):
        self.find_element(self.tableth_loc)



    '''
        页面操作
    '''

    # 取页面gettabTitle
    def gettabTitle(self):
        return self.find_element(self.tabtitle_loc).text

    # 取road路径标题
    def getroadText(self):
        return self.find_element(self.road_loc).text

    # # 获取工单模板数量
    # def gettemnuber(self):
    #     return self.find_element(self.tmpnumber_loc).text

    # 取当前显示的记录条数
    def gettemnuber(self):
        elem = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr.cursor")
        return len(elem)

    def addtemplate(self):
        self.find_element(self.addbtn_loc).click()
        # 此时强制等待必须有
        time.sleep(4)

    def importtem(self):
        self.clickButton(self.import_loc)
        time.sleep(2)

    # 添加页面点击提交按钮
    def commit(self):
        self.find_element(self.commitbtn_loc).click()
        time.sleep(3)

    # 判断提交按钮是否可以点击
    def commi_clickable(self):
        return self.find_element(self.commitbtn_loc).is_enabled()
        # return self.find_element(self.commitbtn_loc)
    # def getcommiColor(self):
    #     return self.find_element(self.commitbtn_loc).get_attribute('style')

    # 检查提交按钮是否存在
    def check_sumbit(self):
        self.find_element(self.commitbtn_loc)

    # 添加页面点击返回列表按钮
    def backlist(self):
        self.clickButton(self.backlist_loc)

    # 第三个过滤框输入内容
    def search(self, text):
        time.sleep(2)  # 20210315,工单模板列表数据较多提交立即搜索不能搜到正确值，需要列表返回完毕后再搜索
        self.clickButton(self.search_loc)
        self.find_element(self.search_loc).clear()
        # time.sleep(2)
        self.send_keys(self.search_loc, text)
        time.sleep(2)

    # 取描述信息为空的描述
    def getemptydescribe(self):
        return self.find_element(self.emptydescribe_loc).text

    # 点击搜索结果
    def clicksearchresult(self):
        self.clickButton(self.searchresult_loc)
        time.sleep(1)

    # 搜索并点击
    def searchclick(self, text):
        TemplatePage(self.driver).search(text)
        time.sleep(1)
        TemplatePage(self.driver).clicksearchresult()
        time.sleep(3)

    # 取列表表头字段
    def gettableth(self):
        return self.find_elements(self.tableth_loc)

    def getearchresult(self):
        return self.find_elements(self.searchresulttd_loc)

    # 点击删除，点击取消  点击确认 取删除弹框的提示信息
    def clickdete(self):
        self.clickButton(self.delete_loc)
        time.sleep(1)

    def clickcancledete(self):
        self.clickButton(self.cancle_loc)

    def clickconfirmdete(self):
        self.clickButton(self.confirm_loc)
        time.sleep(1)

    def getdetetitle(self):
        return self.find_element(self.deletetitle_loc).text
    # 点击复制
    def clickcopy(self):
        self.clickButton(self.copy_loc)
        # self.find_element(self.copy_loc).click()




    # 添加、编辑页面的标题
    def gettitlebar(self):
        return str.replace(self.find_element(self.titlebar_loc).get_attribute('textContent'), ' ', '')

    # 查找输入框
    def check_name_input(self):
        self.find_element(self.name_loc)

    # 输入名称 取名称的值  取名称重复提示
    def inputname(self, text):
        self.clearInput(self.name_loc)
        self.send_keys(self.name_loc, text)
        time.sleep(2)

    def getname(self):
        return self.find_element(self.name_loc).get_attribute('textContent')
    def getrename(self):
        return self.find_element(self.rename_loc).text

    # 点击服务人员、用户
    def clickagent(self):
        self.clickButton(self.agent_loc)

    def clickcustomer(self):
        self.clickButton(self.customer_loc)

    # 角色：取角色值，点击角色输入框,选择指定角色 ,往角色框输入值
    def getrole(self):
        return str.replace(self.find_element(self.role_loc).text,"\n",'')

    def clickrole(self):
        self.clickButton(self.role_loc)

    def choserole(self, text):
        ele = '[title = "' + text + '"]'
        # print(ele)
        self.find_element(self.role_loc).click()
        # time.sleep(2)
        self.driver.find_element_by_css_selector(ele).click()
        # time.sleep(2)
        # self.find_element(self.role_loc).click()

    def inputrole(self, text):
        self.find_element(self.role_loc).click()
        # time.sleep(1)
        self.send_keys(self.role_loc, text)

    # 取角色为空的描述信息
    def getemptyrole(self):
        return self.find_element(self.emptyrole_loc).text

    # 取服务人员/用户切换时，下方字段
    def getrolecompany(self):
        return self.find_elements(self.rolecompany_lable_loc)[3].text

    # 取角色/用户下方提示信息
    def getmessage(self):
        return self.find_elements(self.message_loc)[1].text

    # 选择显示位置，全选，确认,取显示位置值
    def clickshowLocation(self):

        # self.find_element(self.showLocation_loc).click()
        self.clickButton(self.showLocation_loc)


    def clickselectall(self):
        self.clickButton(self.selectall_loc)

    def clickcloseOption(self):
        self.clickButton(self.closeOption_loc)
        # time.sleep(1)

    def getshowLocation(self):
        return str.replace(self.find_element(self.showLocation_loc).text,"\n",'')

    # 显示位置下拉：（1）清除所有 (2)点击移动端 （3）点击网页、web端 （4）点击windows端
    def clickclear(self):
        self.clickButton(self.clear_loc)

    def clickmobile(self):
        self.clickButton(self.showLocation_loc)
        # time.sleep(1)
        self.clickButton(self.clear_loc)
        self.clickButton(self.mobile_loc)
        self.clickButton(self.closeOption_loc)

    def clickweb(self):
        self.clickButton(self.showLocation_loc)
        # time.sleep(1)
        self.clickButton(self.clear_loc)
        self.clickButton(self.web_loc)
        self.clickButton(self.closeOption_loc)

    def clickwindows(self):
        self.clickButton(self.showLocation_loc)
        # time.sleep(1)
        self.clickButton(self.clear_loc)
        self.clickButton(self.windows_loc)
        self.clickButton(self.closeOption_loc)

    # 选择类型:创建工单  ,处理工单 ，工单详情展示，取类型值
    def chosecreateticket(self):
        self.clickButton(self.templateType_loc)
        # time.sleep(2)
        self.clickButton(self.createticket_loc)

    def choseprocessticket(self):
        self.clickButton(self.templateType_loc)
        # 此处等待必须
        time.sleep(1)
        self.clickButton(self.process_loc)

    def chosedetailsticket(self):
        self.clickButton(self.templateType_loc)
        # time.sleep(2)
        self.clickButton(self.details_loc)

    def gettemplatetype(self):
        return  self.find_element(self.templateType_loc).text

    # 显示类型取值、选择普通表单、选择快捷方式
    def getdisplaytype(self):
        return self.find_element(self.displayType_loc).text

    def chosecommonform(self):
        self.clickButton(self.displayType_loc)
        # time.sleep(2)
        self.clickButton(self.commonform_loc)

    def chosequickoperation(self):
        self.clickButton(self.displayType_loc)
        # time.sleep(2)
        self.clickButton(self.quickoperation_loc)

    # 描述取值 ，输入描述值
    def getdescribe(self):
        return self.find_element(self.describe_loc).text

    def inputdescribe(self, text):
        self.send_keys(self.describe_loc, text)

    # 关联知识库类型取值, 选择类别、选择关键字
    def getrelationfaqtype(self):
        return self.find_element(self.relationFaqType_loc).text

    def chosecategory(self):
        self.clickButton(self.relationFaqType_loc)
        # time.sleep(2)
        self.clickButton(self.category_loc)

    def chosekeyword(self):
        self.clickButton(self.relationFaqType_loc)
        # time.sleep(2)
        self.clickButton(self.keyword_loc)

    # 关联知识库内容取值,选择Misc，选择事故报告
    def getrelationfaqcontent(self):
        return str.replace(self.find_element(self.relationFaqContent_loc).text, "\n", '')

    def chosemisc(self):
        self.clickButton(self.relationFaqContent_loc)
        # time.sleep(2)
        self.clickButton(self.Misc_loc)

    def choseaccidentreport(self):
        self.clickButton(self.relationFaqContent_loc)
        # time.sleep(2)
        self.clickButton(self.accidentreport_loc)

    # 模板颜色取值, 往颜色框中输入颜色值
    def getticketcolor(self):
        return self.find_element(self.ticketColor_loc).get_attribute('style')

    def inputcolor(self, text):
        self.send_keys(self.ticketColor_loc, text)

    # 取默认图片的样式
    def getimgstyle(self):
        return self.find_element(self.defaultimg_loc).get_attribute('class')

    # 取选择图片的样式
    def getchoseimgstyle(self):
        return self.find_element(self.img_loc).get_attribute('class')

    # 点击一个图片
    def clickimg(self):
        self.find_element(self.img_loc).click()

    # 有效、无效、有效性取值
    def chosevaild(self):
        self.clickButton(self.validinput_loc)
        # time.sleep(1)
        self.clickButton(self.valid_loc)

    def choseinvaild(self):
        self.clickButton(self.validinput_loc)
        # time.sleep(1)
        self.clickButton(self.invalid_loc)

    def getvalid(self):
        return self.find_element(self.validinput_loc).text

    # -----工单模板显示信息部分事件--------------
    # 取工单模板的显示字段
    def gettemshowfidld(self):
        return self.find_elements(self.temshowfield_loc)

    # 删除客户用户、客户名称、客户用户资产、owner_loc、负责人
    def clickdelCustomerUser(self):
        self.clickButton(self.delCustomerUser_loc)

    def clickdelCustomerID(self):
        self.clickButton(self.delCustomerID_loc)

    def clickdelConfigItems(self):
        self.clickButton(self.delConfigItems_loc)

    def clickdelOwner(self):
        self.clickButton(self.delOwner_loc)

    def clickdelresponsible(self):
        self.clickButton(self.delresponsibleID_loc)

    # 删除 必填字段-类型、角色、主题、内容、状态、优先级
    def delete_type(self):
        self.clickButton(self.delete_type_loc)
        # 必须的强制等待，否则删除无效
        time.sleep(0.5)

    def delete_queue(self):
        self.clickButton(self.delete_queue_loc)
        # 必须的强制等待，否则删除无效
        time.sleep(0.5)

    def delete_subject(self):
        self.clickButton(self.delete_subject_loc)
        # 必须的强制等待，否则删除无效
        time.sleep(0.5)

    def delete_body(self):
        self.clickButton(self.delete_body_loc)
        # 必须的强制等待，否则删除无效
        time.sleep(0.5)

    def delete_state(self):
        self.clickButton(self.delete_state_loc)
        # 必须的强制等待，否则删除无效
        time.sleep(0.5)

    def delete_priority(self):
        self.clickButton(self.delete_priority_loc)
        # 必须的强制等待，否则删除无效
        time.sleep(0.5)

    # 类型点击隐藏、显示、必填、只读 同时取按钮的颜色
    def clicktypehidden(self):
        self.clickButton(self.hiddentype_loc)

    def gettypehiddencolor(self):
        return self.find_element(self.hiddentype_loc).get_attribute('style')

    def clicktypeshown(self):
        self.clickButton(self.showntype_loc)

    def gettypeshowncolor(self):
        return self.find_element(self.showntype_loc).get_attribute('style')

    def clicktyperequired(self):
        self.clickButton(self.requiredtype_loc)

    def gettyperequiredcolor(self):
        return self.find_element(self.requiredtype_loc).get_attribute('style')

    def clicktypereadonly(self):
        self.clickButton(self.readonlytype_loc)

    def gettypereadonlycolor(self):
        return self.find_element(self.readonlytype_loc).get_attribute('style')

    # 选择问题类型
    def chosetype(self):
        self.clickButton(self.type_loc)
        self.clickButton(self.chosetype_loc)

        # 状态选择挂起

    def chosetype2(self, text):
        self.find_element(self.type_loc).click()
        # 输入值
        ActionChains(self.driver).send_keys(text).perform()
        # 点击
        title = '[title="' + text + '"]'
        title_loc = (By.CSS_SELECTOR, title)
        self.find_element(title_loc).click()

    # 获取类型的输入值
    def gettypetext(self):
        return self.find_element(self.type_loc).text

    # 角色点击隐藏、显示、必填、只读 ，同时取四个按钮颜色
    def clickqueuehidden(self):
        self.clickButton(self.hiddenqueue_loc)

    def getqueuehiddencolor(self):
        return self.find_element(self.hiddenqueue_loc).get_attribute('style')

    def clickqueueshown(self):
        self.clickButton(self.shownqueue_loc)

    def getqueueshowncolor(self):
        return self.find_element(self.shownqueue_loc).get_attribute('style')

    def clickqueuerequired(self):
        self.clickButton(self.requiredqueue_loc)

    def getqueuerequiredcolor(self):
        return self.find_element(self.requiredqueue_loc).get_attribute('style')

    def clickqueuereadonly(self):
        self.clickButton(self.readonlyqueue_loc)

    def getqueuereadonlycolor(self):
        return self.find_element(self.readonlyqueue_loc).get_attribute('style')
    # 主题点击隐藏、显示、必填、只读,同时取四个按钮的颜色
    def clicksubjecthidden(self):
        self.clickButton(self.hiddensubject_loc)

    def clicksubjectshown(self):
        self.clickButton(self.shownsubject_loc)

    def clicksubjectrequired(self):
        self.clickButton(self.requiredsubject_loc)

    def clicksubjectreadonly(self):
        self.clickButton(self.readonlysubject_loc)

    def getsubjecthiddencolor(self):
        return self.find_element(self.hiddensubject_loc).get_attribute('style')

    def getsubjectshowncolor(self):
        return self.find_element(self.shownsubject_loc).get_attribute('style')

    def getsubjectrequiredcolor(self):
        return self.find_element(self.requiredsubject_loc).get_attribute('style')

    def getsubjectreadonlycolor(self):
        return self.find_element(self.readonlysubject_loc).get_attribute('style')

    # 主题传值
    def inputsubject(self, text):
        self.send_keys(self.subject_loc, text)

    # 取主题值
    def getsubject(self):
        return self.find_element(self.subject_loc).get_attribute('value')

    # 状态点击隐藏、显示、必填、只读,取四个按钮颜色
    def clickstatehidden(self):
        self.clickButton(self.hiddenstate_loc)

    def clickstateshown(self):
        self.clickButton(self.shownstate_loc)

    def clickstaterequired(self):
        self.clickButton(self.requiredstate_loc)

    def clickstatereadonly(self):
        self.clickButton(self.readonlystate_loc)

    def getstatehiddencolor(self):
        return self.find_element(self.hiddenstate_loc).get_attribute('style')

    def getstateshowncolor(self):
        return self.find_element(self.shownstate_loc).get_attribute('style')

    def getstaterequiredcolor(self):
        return self.find_element(self.requiredstate_loc).get_attribute('style')

    def getstatereadonlycolor(self):
        return self.find_element(self.readonlystate_loc).get_attribute('style')

    # 状态选择挂起
    def chosepeding(self, text):
        self.find_element(self.state_loc).click()
        # 输入值
        ActionChains(self.driver).send_keys(text).perform()
        # 点击
        title = '[title="' + text + '"]'
        title_loc = (By.CSS_SELECTOR, title)
        self.find_element(title_loc).click()

    # 获取状态值
    def getstatetext(self):
        return self.find_element(self.state_loc).text

    # 工单模板显示信息，选择角色
    def clickrole1(self):
        self.clickButton(self.queue_loc)

    def inputrole1(self, text):
        # self.clickButton(self.queue_loc)
        self.send_keys(self.queue_loc, text)

    def getroletext(self):
        return self.find_element(self.queue_loc).text


    # 优先级点击隐藏、显示、必填、只读
    def clickpriorityhidden(self):
        self.clickButton(self.hiddenpriority_loc)

    def clickpriorityshown(self):
        self.clickButton(self.shownpriority_loc)

    def clickpriorityrequired(self):
        self.clickButton(self.requiredpriority_loc)

    def clickpriorityreadonly(self):
        self.clickButton(self.readonlypriority_loc)

    def getpriorityhiddencolor(self):
        return self.find_element(self.hiddenpriority_loc).get_attribute('style')

    def getpriorityshowncolor(self):
        return self.find_element(self.shownpriority_loc).get_attribute('style')

    def getpriorityrequiredcolor(self):
        return self.find_element(self.requiredpriority_loc).get_attribute('style')

    def getpriorityreadonlycolor(self):
        return self.find_element(self.readonlypriority_loc).get_attribute('style')

    # 选择非常高优先级
    def chosepriority(self, text):
        # self.clickButton(self.priority_loc)
        # self.clickButton(self.chosepriority_loc)

        self.find_element(self.priority_loc).click()
        # 输入值
        ActionChains(self.driver).send_keys(text).perform()
        # 点击
        title = '[title="' + text + '"]'
        title_loc = (By.CSS_SELECTOR, title)
        self.find_element(title_loc).click()

    # 取优先级值
    def getPrioritytext(self):
        return self.find_element(self.priority_loc).text

    # 内容点击隐藏、显示、必填、只读
    def clickbodyhidden(self):
        self.clickButton(self.hiddenbody_loc)

    def clickbodyshown(self):
        self.clickButton(self.shownbody_loc)

    def clickbodyrequired(self):
        self.clickButton(self.requiredbody_loc)

    def clickbodyreadonly(self):
        self.clickButton(self.readonlybody_loc)

    def getbodyhiddencolor(self):
        return self.find_element(self.hiddenbody_loc).get_attribute('style')

    def getbodyshowncolor(self):
        return self.find_element(self.shownbody_loc).get_attribute('style')

    def getbodyrequiredcolor(self):
        return self.find_element(self.requiredbody_loc).get_attribute('style')

    def getbodyreadonlycolor(self):
        return self.find_element(self.readonlybody_loc).get_attribute('style')

    # 进入内容框，在内容中输入值
    def enteriframe(self):
        #iframe = self.driver.find_element_by_css_selector('[class="cke_wysiwyg_frame cke_reset"]')
        iframe = self.driver.find_elements_by_tag_name('iframe')[0]
        self.driver.switch_to.frame(iframe)

    def inputcontent(self, text):
        self.send_keys(self.iframe_body_loc, text)

    def getiframe(self):
        return self.find_element(self.iframe_body_loc).text

    # 富文本框样式变更修改
    def inputcontent2(self, text):
        self.clickButton(self.content_loc)
        time.sleep(1)
        self.send_keys(self.content_loc, text)

    def getcontent(self):
        return self.find_element(self.content_loc).text


    # 挂起时间点击收藏、并获取按钮颜色 ，选择挂起时间这里选择3天
    def clickpendinghidden(self):
        self.clickButton(self.hiddenPending_loc)

    def getpendinghiddencolor(self):
        return self.find_element(self.hiddenPending_loc).get_attribute('style')

    def chosependingmonth(self):
        self.clickButton(self.Pendingmonth_loc)
        self.clickButton(self.chosemonth_loc )

    def chosependingdate(self):
        self.clickButton(self.Pendingdate_loc)
        self.clickButton(self.chosedate_loc)

    def choseField(self, Fieldname, sysField):
        self.clickButton(self.dynamicFieldSelect_loc)
        time.sleep(2)
        ActionChains(self.driver).send_keys(Fieldname).perform()
        time.sleep(3)
        title = str(Fieldname + ' ( DynamicField_' + sysField + ' )')
        self.driver.find_element_by_css_selector('[title="' + title + '"]').click()


        # self.clickButton(self.dynamicFieldSelect_loc)
        # res = 0
        # resulut = ''
        # titl = '[title="' + text + '"]'
        # # 一开始还需要做一次判断。
        # # 此时必须使用滚动下拉框的滚动条操作
        # try:
        #     resulut = self.driver.find_element_by_css_selector(titl)
        # except:
        #     pass
        # while res < 15 and resulut == '':
        #     js = 'document.getElementsByClassName' \
        #          '("cdk-virtual-scroll-viewport cdk-virtual-scroll-orientation-vertical")[0].scrollBy(0,544)'
        #     self.driver.execute_script(js)
        #     try:
        #         resulut = self.driver.find_element_by_css_selector(titl)
        #     except:
        #         pass
        #     res = res+1
        #
        #
        # time.sleep(1)
        # self.driver.find_element_by_css_selector(titl).click()

    # 检查工单转派规则字段，是否在页面中
    def check_TransferRule(self):
        return len(self.driver.find_elements_by_id("fieldsDynamicField_TransferRuleID"))

    def clickStateoptions(self):
        self.find_element(self.Stateoptions_loc).click()
        # self.clickButton(self.Stateoptions_loc)
        time.sleep(1)

    def sendesc(self):
        self.clickButton(self.Stateoptions_loc)
        # self.send_keys(self.Stateoptions_loc, Keys.ESCAPE)
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    # 获取状态选项的值
    def getStateoptionstext(self):
        return self.find_element(self.Stateoptions_loc).text

    # 点击状态后的黑色小三角
    def clickdownState(self):
        # self.clickButton(self.down_fieldsState_loc)
        self.find_element(self.down_fieldsState_loc).click()
        # self.clickButton(self.down_fieldsState_loc)
        time.sleep(2)

    # 状态选项中选择新建
    def chosestatenew(self):
        self.find_element(self.Stateoptions_new_loc).click()
        # self.clickButton(self.Stateoptions_new_loc)
        # ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        ActionChains(self.driver).move_to_element(self.find_element(
            self.Stateoptions_loc)).send_keys(Keys.ESCAPE).perform()


    # 删除遮罩层
    def delete_backdrop_showing(self):
        js = 'document.getElementsByClassName("cdk-virtual-scroll-viewport cdk-virtual-scroll-orientation-vertical")[0].remove()'
        self.driver.execute_script(js)



    '''
        工单模板页面添加自定义字段操作
    '''
    # 点击添加自定义字段
    def clickaddfield(self):
        self.find_element(self.addfield_loc).click()
        # self.clickButton(self.addfield_loc)

    # 定位到添加自定义字段位置
    def move_to_addfield(self):
        """定位到添加字段这个位置"""
        self.find_element(self.addfield_loc)

    def fieldType(self):
        self.clickButton(self.fieldType_loc)

    def selectType(self):
        self.find_element(self.selectType_loc).click()

    def dateType(self):
        self.find_element(self.dateType_loc).click()

    def datetimeType(self):
        self.find_element(self.datetimeType_loc).click()

    def checkboxType(self):
        self.find_element(self.checkboxType_loc).click()

    def sysField(self, sysField):
        self.send_keys(self.sysfield_loc, sysField)

    def fieldName(self, fieldName):
        self.send_keys(self.fieldname_loc, fieldName)

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

    def fieldsubmi(self):
        return self.clickButton(self.fieldsubmi_loc)

    # 自定义字段点击隐藏
    def hiddenfield(self, name):
        ele = 'hidden_fieldsDynamicField_' + name
        self.driver.find_element_by_id(ele).click()

    # 自定义字段输入框  DynamicField_sheng
    def chosefielddefault(self, name):
        ele = 'DynamicField_' + name
        self.driver.find_element_by_id(ele).click()
        self.driver.find_elements_by_css_selector('[class="ant-select-item-option-content"]')[0].click()
        # 点击下拉的项

    def gethiddenfieldcolor(self, name):
        ele = 'hidden_fieldsDynamicField_' + name
        ele_loc = (By.ID, ele)
        return self.find_element(ele_loc).get_attribute('style')
        # return self.driver.find_element_by_id(ele).get_attribute('style')

    # 取自定义字段值
    def getfieldtext(self, name):
        # value0
        ele = 'DynamicField_' + name
        return self.driver.find_element_by_id(ele).text

    # 点击自定义字段后面的黑色展开图标
    def clickfielddown(self, name):
        ele = 'down_fieldsDynamicField_' + name
        self.driver.find_element_by_id(ele).click()

    # 自定义字段点击黑色图标后，点击选项输入框，并选择第一项
    # DynamicField_sheng_optionsShowValue
    def clickfieldoptions(self, name):
        ele = 'DynamicField_' + name + '_optionsShowValue'
        self.driver.find_element_by_id(ele).click()
        self.driver.find_elements_by_css_selector('[class="ant-select-item-option-content"]')[0].click()
        # [class="ant-select-item-option-content"]
        # time.sleep(1)

        # ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
        # self.driver.find_element(*self.Permission_loc).click()
        # time.sleep(2)


    # 取自定义字段点击黑色图标后，选项中显示的值
    def getfieldoptions(self, name):
        ele = 'DynamicField_' + name + '_optionsShowValue'
        return self.driver.find_element_by_id(ele).text

    # 自定义字段日期时间输入指定日期
    def chose_datetime(self, num, text):
        self.driver.find_elements_by_css_selector("[placeholder='请选择日期']")[num].clear()
        self.driver.find_elements_by_css_selector("[placeholder='请选择日期']")[num].click()
        time.sleep(0.5)
        self.driver.find_elements_by_css_selector("[placeholder='请选择日期']")[num].send_keys(text)
        self.find_element(self.dateconfirm_loc).click()

    # 自定义字段日期输入今日日期
    def chose_data(self, num):
        self.driver.find_elements_by_css_selector("[placeholder='请选择日期']")[num].clear()
        self.driver.find_elements_by_css_selector("[placeholder='请选择日期']")[num].click()
        time.sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR,".ant-picker-today-btn").click()


    # 自定义的复选框字段勾选
    def chose_checkbox(self, num):
        self.driver.find_elements_by_css_selector("[type='checkbox']")[num].click()

    # 返回当前自定义复选的项
    def checkboxnum(self):
        return len(self.driver.find_elements_by_css_selector("label [class='ant-checkbox ant-checkbox-checked']"))

    # 取自定义日期字段的值
    def get_data(self, num):
        return self.driver.find_elements_by_css_selector("[placeholder='请选择日期']")[num].get_attribute("value")

    # 点击主题黑色三角
    def down_fieldssubject(self):
        self.find_element(self.down_fieldsSubject_loc).click()
        time.sleep(1)

    # 选择主题说明类型
    def subject_explain_type(self, num):
        self.find_element(self.Subject_explain_type_loc).click()
        self.find_elements(self.Subject_explain_option_loc)[num].click()

    # 取类型的值
    def get_subject_explain_type(self):
        # ele000 = self.driver.find_element_by_css_selector("#promptDisplaySubject .ant-select-show-arrow nz-select-item").\
        #     get_attribute("innerHTML")
        # ele001 = self.driver.find_element_by_css_selector(
        #     "#promptDisplaySubject .ant-select-show-arrow nz-select-item"). \
        #     get_attribute("outerHTML")

        # ele002 = self.driver.find_element_by_css_selector(
        #     "#promptDisplaySubject .ant-select-show-arrow nz-select-item").text
        ele = self.driver.find_element_by_css_selector(
            "#promptDisplaySubject .ant-form-item-control-input input").get_attribute("textContent")

        # print(ele002, 2)
        # print(ele003, 3)

        # ele = self.driver.find_element_by_css_selector("#promptDisplaySubject .ant-select-show-arrow input")
        # # return self.find_element(self.Subject_explain_type_text_loc).get_attribute("value")
        return ele

    # 填写主题说明内容
    def subject_explain_content(self, text):
        self.send_keys(self.Subject_explain_Content_loc, text)

    # 清空主题说明：
    def subject_explain_content_clear(self):
        ele = self.find_element(self.Subject_explain_Content_loc)
        ele.send_keys(Keys.CONTROL + 'a')
        ele.send_keys(Keys.DELETE)

    def get_subject_explain_content(self):
        return self.find_element(self.Subject_explain_Content_loc).get_attribute("value")
        # return self.find_element(self.Subject_explain_Content_loc).text

    # 指定处理人字段，点击必填按钮
    def required_fields_Owner(self):
        self.find_element(self.required_fieldsOwner_loc).click()







