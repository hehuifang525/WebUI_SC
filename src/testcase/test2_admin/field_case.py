"""
@author: testing
@file:   field_case.py
@desc:  【】
@step： 001.检查字段库页面路径（SC_Field_9）
        002.切换各tab，查看是否被选中(SC_Field_2，)
        003.检查添加页面返回按钮（SC_Field_3，SC_Field_19）
        004.只填写必填项保存后搜索查看(SC_Field_5，SC_Field_22)
        005.带特殊字符搜索（SC_Field_8）
        006.不填写必填项，查看提交按钮显示（SC_Field_20，SC_Field_21）
        007.点击再添加一条按钮（SC_Field_23,SC_Field_25）
        008.填写全部字段--文本
        009.填写字段--下拉框
        010.二次编辑后进入查看（SC_Field_26，SC_Field_27）
        011.二次编辑清空非必填字段查看（SC_Field_28）
        012.填写全部字段后不提交，更换字段类型（SC_Field_29）
        013.填写全部字段后不提交，更换字段对象（SC_Field_30）
        014.系统字段的重复性检验(SC_Field_31,SC_Field_33,SC_Field_35)
        015.必填项输入空格检验(SC_Field_36)
        016.添加字段对象---配置项
        017.添加字段对象--知识库
        018.添加字段对象--客户用户
        019.添加字段对象--客户
        020.添加字段对象--合同
        021.添加系统字段对象--信件
        022.
        023.导入导出页面的返回按钮，查看导入页面显示的描述提示语（SC_Field_50,SC_Field_51）
        024.
        025.添加字段组（字段组字段有文本，下拉单选框）
"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.field_page import FieldPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from src.page.pagecommon.field_common import FieldCommon
import unittest


class Field(BaseCaseUser, Base):

    # 1.检查字段库页面路径  ok
    def test_001_field(self):
        EntranceAgentPage(self.driver).enter_filed()
        time.sleep(3)
        # 检查页面路径
        roadText=FieldPage(self.driver).getRoad()
        time.sleep(3)
        # 检查页面title
        titleText=FieldPage(self.driver).get_title()
        # 检查列表表头
        fieldlist_info = [ '', '系统字段', '字段名称', '字段显示类型', '系统字段对象', '有效性']   #0723增加

        # 20210918修改
        for listheader01 in ['.ant-table-thead th']:
            for i in range(0, 6):
                text = self.driver.find_elements_by_css_selector(listheader01)[i].text
                self.assertEqual(text, fieldlist_info[i], msg='字段库列表表头显示不正确！')
        assert roadText == '/ 系统管理 / 字段库', '字段库列表路径显示不正确'
        assert titleText == '字段库', '字段库列表当前窗口 title 显示不正确'

    # 2.切换各tab，查看是否被选中   ok
    def test_002_field(self):
        EntranceAgentPage(self.driver).enter_filed()
        time.sleep(5)
        FieldPage(self.driver).clickAll()
        time.sleep(3)
        allClass = FieldPage(self.driver).getAllClass()
        time.sleep(3)
        # assert allClass == 'margin-R10 ant-btn admin-ticket-template-btn ant-btn-default' or \
        #        allClass == 'margin-R10 ant-btn ant-btn-default admin-ticket-template-btn', '切换至全部tab失败'  #0715修改

        self.assertIn( 'admin-ticket-template-btn', allClass, '切换至全部tab失败')
        time.sleep(2)
        FieldPage(self.driver).clickArticle()
        articleClass = FieldPage(self.driver).getArticleClass()
        # assert articleClass == 'margin-R10 ant-btn ng-star-inserted ant-btn-default admin-ticket-template-btn', '切换至信件tab失败'  #0715修改
        self.assertIn('admin-ticket-template-btn' , articleClass , '切换至信件tab失败')
        # 0715合同分类被取消，注释该分类
        # time.sleep(2)
        # FieldPage(self.driver).clickContract()
        # contractClass=FieldPage(self.driver).getContractClass()
        # assert contractClass == 'margin-R10 ant-btn ng-star-inserted admin-ticket-template-btn', '切换至合同tab失败'
        time.sleep(2)
        FieldPage(self.driver).clickCompany()
        companyClass = FieldPage(self.driver).getCompanyClass()
        # assert companyClass == 'margin-R10 ant-btn ng-star-inserted admin-ticket-template-btn', '切换至客户tab失败'
        self.assertIn('admin-ticket-template-btn', companyClass, '切换至客户tab失败')
        time.sleep(2)
        FieldPage(self.driver).clickCustomerUser()
        cutomerUserClass = FieldPage(self.driver).getCustomerUserClass()
        self.assertIn( 'admin-ticket-template-btn', cutomerUserClass,'切换至客户tab失败')
        # assert cutomerUserClass == 'margin-R10 ant-btn ng-star-inserted admin-ticket-template-btn', '切换至客户用户tab失败'
        time.sleep(2)
        FieldPage(self.driver).clickFAQForGet()
        FAQClass = FieldPage(self.driver).getFAQClass()
        self.assertIn('admin-ticket-template-btn',FAQClass,  '切换至FAQtab失败')
        # assert FAQClass == 'margin-R10 ant-btn ng-star-inserted admin-ticket-template-btn', '切换至FAQ tab失败'
        time.sleep(2)
        FieldPage(self.driver).clickITSM()
        ITSMClass = FieldPage(self.driver).getITSMClass()
        self.assertIn( 'admin-ticket-template-btn', ITSMClass,'切换至配置项tab失败')
        # assert ITSMClass == 'margin-R10 ant-btn ng-star-inserted admin-ticket-template-btn', '切换至配置项tab失效'
        time.sleep(2)
        FieldPage(self.driver).clickTicket()
        ticketClass = FieldPage(self.driver).getTicketClass()
        self.assertIn( 'admin-ticket-template-btn',ticketClass,'切换至工单tab失败')
        # assert ticketClass == 'margin-R10 ant-btn ng-star-inserted admin-ticket-template-btn', '切换至工单tab失败'

    # 3.检查添加页面返回按钮  ok
    def test_003_field(self):
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).returnList()
        roadText=FieldPage(self.driver).getRoad()
        assert roadText == '/ 系统管理 / 字段库', '返回字段库列表页面失败'

    # 4.只填写必填项  0723修改ok
    # 20220119 已知bug，列表有效错误显示为1
    @unittest.expectedFailure     # 预期失败标记，列表中“有效”错误显示为1
    def test_004_field(self):
        fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('Ticket')
        FieldPage(self.driver).clickTicket()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        fieldlist_info =['', '', fieldInfo.get('sysField'), fieldInfo.get('name'), '文本', '工单', '有效']

        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            print(text_zoom_01, fieldlist_info[i],i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )  # 0723修改

        FieldPage(self.driver).clickAll()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))

        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )

    # 5.带特殊字符搜索   # 0723 修改 ok
    # 20220119 已知bug，列表有效错误显示为1
    @unittest.expectedFailure  # 预期失败标记，列表中“有效”错误显示为1
    def test_005_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber + '!@#$%^&*[}=')
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()  # 0723 修改
        FieldPage(self.driver).objectType()
        time.sleep(2)
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        FieldPage(self.driver).submit()
        FieldPage(self.driver).clickTicket()
        FieldPage(self.driver).search(sysField)
        fieldlist_info = ['','', sysField, name, '文本', '工单', '有效']  # 0723增加
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )


    # 6.不填写必填项，必填按钮显示   0723修改ok
    def test_006_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber + '!@#$%^&*[}=')
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        submitColor=FieldPage(self.driver).submitColor()
        addAnotherColor=FieldPage(self.driver).addAnotherColor()
        self.assertEqual(submitColor, 'true', msg='不选择字段显示类型时，提交按钮可点击')
        self.assertEqual(addAnotherColor, 'true', msg='不选择字段显示类型时，再添加一条按钮可点击')
        # assert submitColor == 'background-color: rgb(191, 191, 191);', '不选择字段显示类型时，提交按钮可点击'   # 0723 修改
        # assert addAnotherColor == 'background-color: rgb(191, 191, 191);', '不选择字段显示类型时，再添加一条按钮可点击'
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()   # 0723修改
        submitColor01=FieldPage(self.driver).submitColor()
        addAnotherColor01=FieldPage(self.driver).addAnotherColor()
        self.assertEqual(submitColor01, 'true', msg='不选择系统字段对象时，提交按钮可点击')
        self.assertEqual(addAnotherColor01, 'true', msg='不选择系统字段对象时，再添加一条按钮可点击')
        # assert submitColor01 == 'background-color: rgb(191, 191, 191);', '不选择系统字段对象时，提交按钮可点击'  # 0723修改
        # assert addAnotherColor01 == 'background-color: rgb(191, 191, 191);', '不选择系统字段对象时，再添加一条按钮可点击'
        FieldPage(self.driver).objectType()
        time.sleep(2)
        FieldPage(self.driver).objectTicket()
        submitColor02 = FieldPage(self.driver).submitColor()
        addAnotherColor02 = FieldPage(self.driver).addAnotherColor()
        self.assertEqual(submitColor02, 'true', msg='不填写系统字段时，提交按钮可点击')
        self.assertEqual(addAnotherColor02, 'true', msg='不填写系统字段时，再添加一条按钮可点击')
        # assert submitColor02 == 'background-color: rgb(191, 191, 191);', '不填写系统字段时，提交按钮可点击'  # 0723 修改
        # assert addAnotherColor02 == 'background-color: rgb(191, 191, 191);', '不填写系统字段时，再添加一条按钮可点击'
        FieldPage(self.driver).sysField(sysField)
        submitColor03 = FieldPage(self.driver).submitColor()
        addAnotherColor03 = FieldPage(self.driver).addAnotherColor()
        self.assertEqual(submitColor03, 'true', msg='不填写字段名称时，提交按钮可点击')
        self.assertEqual(addAnotherColor03, 'true', msg='不填写字段名称时，再添加一条按钮可点击')
        # assert submitColor03 == 'background-color: rgb(191, 191, 191);', '不填写字段名称时，提交按钮可点击'   # 0723 修改
        # assert addAnotherColor03 == 'background-color: rgb(191, 191, 191);', '不填写字段名称时，再添加一条按钮可点击'

    # 7.点击再添加一条按钮   0723修改  ok
    # 20220119 已知bug，列表有效错误显示为1
    @unittest.expectedFailure  # 预期失败标记，列表中“有效”错误显示为1
    def test_007_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType() # 0723 修改
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        FieldPage(self.driver).addAnother()
        time.sleep(2)
        roadText = str.replace(FieldPage(self.driver).getRoad(),' ','')
        self.assertEqual(roadText, '/系统管理/字段库/字段库添加',msg='点击再添加一条后，页面路径显示不正确')
        # assert roadText == '/ 系统管理 / 字段库 / 字段库添加', '点击再添加一条后，页面路径显示不正确'  0723 修改
        time.sleep(3)
        FieldPage(self.driver).returnList()
        time.sleep(3)
        FieldPage(self.driver).search(sysField)
        time.sleep(3)
        fieldlist_info = ['','', sysField, name, '文本', '工单', '有效']
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )



    # 0809 用户可见功能修改，屏蔽用例  0819修改恢复
    # 8.填写全部字段--文本
    def test_008_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()  # 0723修改
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        # FieldPage(self.driver).userInvisible()
        FieldPage(self.driver).regex('^[0-9]*$')
        FieldPage(self.driver).regexHint('只能输入数字')
        FieldPage(self.driver).hintType()
        FieldPage(self.driver).hintTypeValue03()
        FieldPage(self.driver).hintContent('请填写')
        FieldPage(self.driver).formula('12')
        FieldPage(self.driver).submit()
        FieldPage(self.driver).search(sysField)
        FieldPage(self.driver).edit()
        fieldType=FieldPage(self.driver).getFieldTypeValue()
        objectType=FieldPage(self.driver).getObjectTypeValue()
        fieldID=FieldPage(self.driver).getFieldIDValue()
        fieldName=FieldPage(self.driver).getFieldNameValue()
        invisible=FieldPage(self.driver).getInvisibleValue()
        valid=FieldPage(self.driver).getValidValue()
        regex=FieldPage(self.driver).getRegexValue()
        regexHint=FieldPage(self.driver).getRegexHintValue()
        hintType=FieldPage(self.driver).getHintTypeValue()
        hintContent=FieldPage(self.driver).getHintContentValue()
        formula=FieldPage(self.driver).getFormulaValue()
        fieldValue01=[fieldType, objectType, fieldID, fieldName, invisible, valid, regex, regexHint, hintType,
                      hintContent, formula]
        # fieldValue02=['Text', 'Ticket', sysField, name, 'ant-radio-wrapper ng-star-inserted ant-radio-wrapper-checked', 'valid',
        #               '^[0-9]*$', '只能输入数字', '提示在目标栏右侧的提示图标中', '请填写', '12']   # 0723 修改
        fieldValue02 = ['Text', 'Ticket', sysField, name,
                        'ant-radio-wrapper ng-star-inserted', 'valid',
                        '^[0-9]*$', '只能输入数字', '提示在目标栏右侧的提示图标中', '请填写', '12']
        # assert fieldValue01 == fieldValue02, '文本类型，填写全部字段提交后，二次进入查看，显示不正确'   # 0724修改
        self.assertEqual(fieldValue01, fieldValue02, msg='错误：文本类型，填写全部字段提交后，二次进入查看，显示不正确')  # 0723修改


    # 0809 用户可见功能修改，屏蔽用例 0819 修复恢复
    # 0819 检查发现下拉类型字段无用户可见不可见
    # 9.填写字段--下拉框
    def test_009_field(self):
        fieldInfo=FieldCommon(self.driver).fullSelectFieldCommon()
        time.sleep(5)
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        FieldPage(self.driver).edit()
        fieldType=FieldPage(self.driver).getFieldTypeValue()
        objectType=FieldPage(self.driver).getObjectTypeValue()
        fieldID=FieldPage(self.driver).getFieldIDValue()
        fieldName=FieldPage(self.driver).getFieldNameValue()
        # invisible=FieldPage(self.driver).getInvisibleValue()
        valid=FieldPage(self.driver).getValidValue()
        key0=FieldPage(self.driver).getFileTypeKey0Value()
        value0=FieldPage(self.driver).getFileTypeValue0Value()
        key1=FieldPage(self.driver).getFileTypeKey1Value()
        value1=FieldPage(self.driver).getFileTypeValue1Value()
        key2=FieldPage(self.driver).getFileTypeKey2Value()
        value2=FieldPage(self.driver).getFileTypeValue2Value()
        # fieldValue01=[fieldType, objectType, fieldID, fieldName, invisible, valid, key0, value0, key1, value1, key2,
        #               value2]
        fieldValue01 = [fieldType, objectType, fieldID, fieldName,  valid, key0, value0, key1, value1, key2,
                        value2]

        fieldValue02=['Dropdown', 'Ticket', fieldInfo.get('sysField'), fieldInfo.get('name'),
                      'valid', 'key2', 'value2', 'key1', 'value1', 'key0', 'value0']
        self.assertEqual(fieldValue01, fieldValue02, msg='错误：文本类型，填写全部字段提交后，二次进入查看，显示不正确')  # 0723修改

        assert fieldValue01 == fieldValue02, '下拉框类型，填写全部字段提交后，二次进入查看，显示不正确'  # 0723修改

    # 0809 用户可见功能修改，屏蔽用例  0819修复恢复 屏蔽用户可见的判断
    # 10.二次编辑后进入查看  ok
    def test_010_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        fieldInfo=FieldCommon(self.driver).fullTextFieldCommon()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        FieldPage(self.driver).edit()
        FieldPage(self.driver).fieldName(name + 'edit')
        FieldPage(self.driver).userVisible()
        FieldPage(self.driver).regex('^[0-9]*$edit')
        FieldPage(self.driver).regexHint('只能输入数字edit')
        FieldPage(self.driver).hintType()
        FieldPage(self.driver).hintTypeValue01()
        FieldPage(self.driver).hintContent('请填写edit')
        FieldPage(self.driver).formula('12edit')
        FieldPage(self.driver).submit()
        FieldPage(self.driver).search(sysField)
        FieldPage(self.driver).edit()
        fieldType=FieldPage(self.driver).getFieldTypeValue()
        objectType=FieldPage(self.driver).getObjectTypeValue()
        fieldID=FieldPage(self.driver).getFieldIDValue()
        fieldName=FieldPage(self.driver).getFieldNameValue()
        visible=FieldPage(self.driver).getVisibleValue()
        valid=FieldPage(self.driver).getValidValue()
        regex=FieldPage(self.driver).getRegexValue()
        regexHint=FieldPage(self.driver).getRegexHintValue()
        hintType=FieldPage(self.driver).getHintTypeValue()
        hintContent=FieldPage(self.driver).getHintContentValue()
        formula=FieldPage(self.driver).getFormulaValue()
        # 0819 用户可见功能有问题，屏蔽其判断
        # fieldValue01=[fieldType, objectType, fieldID, fieldName, visible, valid, regex, regexHint, hintType,
        #               hintContent, formula]
        # fieldValue02=['Text', 'Ticket', sysField, name + 'edit',
        #               'ant-radio-wrapper ng-star-inserted', 'valid',
        #               '^[0-9]*$edit', '只能输入数字edit', '提示在目标栏中', '请填写edit', '12edit']
        fieldValue01 = [fieldType, objectType, fieldID, fieldName,  valid, regex, regexHint, hintType,
                        hintContent, formula]
        fieldValue02 = ['Text', 'Ticket', sysField, name + 'edit', 'valid',
                        '^[0-9]*$edit', '只能输入数字edit', '提示在目标栏中', '请填写edit', '12edit']
        # print(fieldValue01, fieldValue02)
        self.assertEqual(fieldValue01, fieldValue02, msg='错误：文本类型，编辑字段后，二次进入查看，显示不正确')  # 0723修改
        # assert fieldValue01 == fieldValue02, '文本类型，编辑字段后，二次进入查看，显示不正确'

    # 0809 用户可见功能修改，屏蔽用例   0819 修复恢复
    # 11.二次编辑清空非必填字段查看 ok
    def test_011_field(self):
        fieldInfo=FieldCommon(self.driver).fullSelectFieldCommon()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        FieldPage(self.driver).edit()
        FieldPage(self.driver).removeField0()
        FieldPage(self.driver).removeField1()
        FieldPage(self.driver).removeField2()
        # 0819 修改 文本类字段才有正则
        # FieldPage(self.driver).regex(' ')
        # FieldPage(self.driver).regexHint(' ')
        # FieldPage(self.driver).hintContent(' ')
        # FieldPage(self.driver).formula(' ')
        FieldPage(self.driver).submit()
        # 必须加强制等待
        time.sleep(3)
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        FieldPage(self.driver).edit()
        selectOptions=FieldPage(self.driver).getSelectOptions()
        # regex=FieldPage(self.driver).getRegexValue()
        # regexHint=FieldPage(self.driver).getRegexHintValue()
        # hintContent=FieldPage(self.driver).getHintContentValue()
        # formula=FieldPage(self.driver).getFormulaValue()
        # fieldValue01 = [selectOptions, regex, regexHint, hintContent, formula]
        # fieldValue02 = ['选项数 : 0', ' ', ' ', ' ', ' ']
        fieldValue01=[selectOptions]
        fieldValue02=['选项数 : 0']
        # assert fieldValue01 == fieldValue02, '二次编辑清空非必填字段不正确'  # 0723修改
        self.assertEqual(fieldValue01, fieldValue02, msg='错误：二次编辑清空非必填字段不正确')  # 0723修改

    # 0809 用户可见功能修改，屏蔽用例  0819 修复恢复
    # 0819 文本类字段才有正则填写
    # 12.填写全部字段后不提交，更换字段类型   从文本更改下拉
    def test_012_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        # FieldPage(self.driver).userInvisible()
        FieldPage(self.driver).regex('^[0-9]*$')
        FieldPage(self.driver).regexHint('只能输入数字')
        FieldPage(self.driver).hintType()
        time.sleep(2)
        FieldPage(self.driver).hintTypeValue03()
        FieldPage(self.driver).hintContent('请填写')
        FieldPage(self.driver).formula('12')
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).selectType()
        fieldType=FieldPage(self.driver).getFieldTypeValue()
        objectType=FieldPage(self.driver).getObjectTypeValue()
        fieldID=FieldPage(self.driver).getFieldIDValue()
        fieldName=FieldPage(self.driver).getFieldNameValue()
        # invisible=FieldPage(self.driver).getInvisibleValue()
        valid=FieldPage(self.driver).getValidValue()
        # regex=FieldPage(self.driver).getRegexValue()
        # regexHint=FieldPage(self.driver).getRegexHintValue()
        # hintType=FieldPage(self.driver).getHintTypeValue()
        # hintContent=FieldPage(self.driver).getHintContentValue()
        # formula=FieldPage(self.driver).getFormulaValue()
        # 0819 屏蔽用户可见的判断
        # fieldValue01=[fieldType, objectType, fieldID, fieldName, invisible, valid, regex, regexHint, hintType,
        #               hintContent, formula]
        #
        # fieldValue02=['Dropdown', 'Ticket', None, None, 'ant-radio-wrapper ng-star-inserted', 'valid',
        #               '^[0-9]*$', '只能输入数字', '提示在目标栏右侧的提示图标中', None, '12']
        fieldValue01 = [fieldType, objectType, fieldID, fieldName,  valid]

        # fieldValue02 = ['Dropdown', 'Ticket', None, None, 'valid']
        fieldValue02 = ['Dropdown', None, "", "", 'valid']
        # assert fieldValue01 == fieldValue02, '填写全部字段后不提交，更换字段类型，填写的字段显示不正确' # 0723修改
        self.assertEqual(fieldValue01, fieldValue02, msg='错误：填写全部字段后不提交，更换字段类型，填写的字段显示不正确')

    # 0809 用户可见功能修改，屏蔽用例   0819修复恢复
    # 13.填写全部字段后不提交，更换字段对象   工单--切换到知识库
    def test_013_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType() #0723修改
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        # FieldPage(self.driver).userInvisible()
        FieldPage(self.driver).regex('^[0-9]*$')
        FieldPage(self.driver).regexHint('只能输入数字')
        FieldPage(self.driver).hintType()
        time.sleep(2)
        FieldPage(self.driver).hintTypeValue03()
        FieldPage(self.driver).hintContent('请填写')
        FieldPage(self.driver).formula('12')
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectFAQ()
        fieldType=FieldPage(self.driver).getFieldTypeValue()
        objectType=FieldPage(self.driver).getObjectTypeValue()
        fieldID=FieldPage(self.driver).getFieldIDValue()
        fieldName=FieldPage(self.driver).getFieldNameValue()
        # invisible=FieldPage(self.driver).getInvisibleValue()
        valid=FieldPage(self.driver).getValidValue()
        regex=FieldPage(self.driver).getRegexValue()
        regexHint=FieldPage(self.driver).getRegexHintValue()
        hintType=FieldPage(self.driver).getHintTypeValue()
        hintContent=FieldPage(self.driver).getHintContentValue()
        formula=FieldPage(self.driver).getFormulaValue()
        # 0819 屏蔽用户可见的判断
        # fieldValue01=[fieldType, objectType, fieldID, fieldName, invisible, valid, regex, regexHint, hintType,
        #               hintContent, formula]
        #
        # fieldValue02=['Text', 'FAQ', None, None, 'ant-radio-wrapper ng-star-inserted',
        #               'valid','^[0-9]*$', '只能输入数字', '提示在目标栏右侧的提示图标中',None, '12']
        fieldValue01 = [fieldType, objectType, fieldID, fieldName, valid, regex, regexHint, hintType,
                        hintContent, formula]

        fieldValue02 = ['Text', 'FAQ', "", "",
                        'valid', '^[0-9]*$', '只能输入数字', '提示在目标栏右侧的提示图标中', "", '12']
        # print(fieldValue01, fieldValue02)
        # assert fieldValue01 == fieldValue02, '填写全部字段后不提交，更换字段类型，填写的字段显示不正确'  # 0723 修改
        self.assertEqual(fieldValue01, fieldValue02, msg='错误：填写全部字段后不提交，更换字段类型，填写的字段显示不正确')

    # 14.系统字段的重复性检验   # 0731 2020072128000019
    def test_014_field(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber + '666')
        name=str('name' + strnumber + '101')
        fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('Ticket')
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()
        FieldPage(self.driver).objectType()
        time.sleep(2)
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(fieldInfo.get('sysField'))
        FieldPage(self.driver).fieldName(name)
        time.sleep(3)
        fieldIDMessage=FieldPage(self.driver).getFieldIDMessage()
        submitColor=FieldPage(self.driver).submitColor()
        addAnotherColor=FieldPage(self.driver).addAnotherColor()

        self.assertEqual(fieldIDMessage, '当前字段已存在或是系统字段!', msg='系统字段重复性检验功能错误')
        self.assertEqual(submitColor, 'true', msg='不选择字段显示类型时，提交按钮可点击')
        self.assertEqual(addAnotherColor, 'true', msg='不选择字段显示类型时，再添加一条按钮可点击')
        FieldPage(self.driver).sysField('系统字段')
        time.sleep(3)

        submitColor001 = FieldPage(self.driver).submitColor()
        self.assertEqual(submitColor001, 'true', msg='错误：系统字段输入中文提交按钮可提交')
        fieldIDMessage=FieldPage(self.driver).getFieldError()
        self.assertEqual(fieldIDMessage, '您当前输入值不符合要求，请检查', msg='系统字段输入汉字检验错误')

        FieldPage(self.driver).sysField('!@#$%^&*_{]')
        submitColor002 = FieldPage(self.driver).submitColor()
        self.assertEqual(submitColor002, 'true', msg='错误：系统字段输入特殊只读提交按钮可提交')
        time.sleep(2)
        fieldIDMessage02=FieldPage(self.driver).getFieldError()
        self.assertEqual(fieldIDMessage02, '您当前输入值不符合要求，请检查', msg='错误:系统字段输入特殊检验错误')

        # 系统字段名称不做重名校验
        # FieldPage(self.driver).sysField(sysField)
        # FieldPage(self.driver).fieldName(fieldInfo.get('name'))
        # time.sleep(3)
        # fieldNameMessage=FieldPage(self.driver).getFieldNameMessage()
        # submitColor02=FieldPage(self.driver).submitColor()
        # addAnotherColor02=FieldPage(self.driver).addAnotherColor()
        # self.assertEqual(fieldNameMessage, '当前字段名称已存在或是系统字段名称!', msg='字段名称重复性检验功能错误')
        # self.assertEqual(submitColor02, 'background-color: rgb(191, 191, 191);', msg='不选择字段显示类型时，提交按钮可点击')
        # self.assertEqual(addAnotherColor02, 'background-color: rgb(191, 191, 191);', msg='不选择字段显示类型时，再添加一条按钮可点击')

    # 15.必填项输入空格检验   ok
    def test_015_field(self):
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()

        FieldPage(self.driver).sysField('        ')
        FieldPage(self.driver).fieldName('       ')
        submitColor=FieldPage(self.driver).submitColor()
        addAnotherColor=FieldPage(self.driver).addAnotherColor()
        # assert submitColor == 'background-color: rgb(191, 191, 191);', '不选择字段显示类型时，提交按钮可点击'
        # assert addAnotherColor == 'background-color: rgb(191, 191, 191);', '不选择字段显示类型时，再添加一条按钮可点击'
        self.assertEqual(submitColor, 'true', msg='不选择字段显示类型时，提交按钮可点击')
        self.assertEqual(addAnotherColor, 'true', msg='不选择字段显示类型时，再添加一条按钮可点击')

    # 16.添加字段对象---配置项  ok
    @unittest.expectedFailure  # 预期失败标记，列表中“有效”错误显示为1
    def test_016_field(self):
        fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('ITSM')
        FieldPage(self.driver).clickITSM()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        # for FiledList01 in ['.ant-table-tbody  td']:  0723修改
        fieldlist_info = ['','', fieldInfo.get('sysField'), fieldInfo.get('name'), '文本', '配置项', '有效']
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )

        FieldPage(self.driver).clickAll()
        # print('2121')
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误2：添加字段数据列表显示错误'+text_zoom_01 )

    # 17.添加字段对象--知识库  ok
    # 20220119 已知bug，列表有效错误显示为1
    @unittest.expectedFailure  # 预期失败标记，列表中“有效”错误显示为1
    def test_17_field(self):
        fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('FAQ')
        time.sleep(2)

        FieldPage(self.driver).clickFAQ()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))

        fieldlist_info = ['','', fieldInfo.get('sysField'), fieldInfo.get('name'), '文本', '知识库', '有效']  # 0723修改
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )

        FieldPage(self.driver).clickAll()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误2：添加字段数据列表显示错误'+text_zoom_01 )

    # 18.添加字段对象--客户用户  OK
    # 20220119 已知bug，列表有效错误显示为1
    @unittest.expectedFailure  # 预期失败标记，列表中“有效”错误显示为1
    def test_18_field(self):
        fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('CustomerUser')
        FieldPage(self.driver).clickCustomerUser()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        fieldlist_info = ['','', fieldInfo.get('sysField'), fieldInfo.get('name'), '文本', '客户用户', '有效']  # 0723修改
        #for FiledList01 in ['.ant-table-tbody  td']:  # 0723 修改
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )

        FieldPage(self.driver).clickAll()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        # for FiledList01 in ['.ant-table-tbody  td']: #0723修改
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误2：添加字段数据列表显示错误'+text_zoom_01 )

    # 19.添加字段对象--客户  ok
    # 20220119 已知bug，列表有效错误显示为1
    @unittest.expectedFailure  # 预期失败标记，列表中“有效”错误显示为1
    def test_19_field(self):
        fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('Customer')
        FieldPage(self.driver).clickCompany()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        fieldlist_info = ['', '',fieldInfo.get('sysField'), fieldInfo.get('name'), '文本', '客户', '有效']  # 0723修改
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误'+text_zoom_01 )

        FieldPage(self.driver).clickAll()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误2：添加字段数据列表显示错误'+text_zoom_01 )

    # # 20.添加字段对象--合同    # 0723修改 合同部分暂时取消
    # def test_20_field(self):
    #     fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('Contract')
    #     FieldPage(self.driver).clickContract()
    #     FieldPage(self.driver).search(fieldInfo.get('sysField'))
    #     fieldlist_info = ['', fieldInfo.get('sysField'), fieldInfo.get('name'), '文本', '合同', '有效']
    #     for FiledList01 in ['.cursor.ant-table-row.ng-star-inserted td']:
    #         for i in range(0, 6):
    #             text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
    #             self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误：添加字段数据列表展示不正确' + text_zoom_01)  # 0723修改
    #
    #
    #     FieldPage(self.driver).clickAll()
    #     FieldPage(self.driver).search(fieldInfo.get('sysField'))
    #     for FiledList01 in ['.cursor.ant-table-row.ng-star-inserted td']:
    #         for i in range(0, 6):
    #             text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
    #             self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误：添加字段数据列表展示不正确' + text_zoom_01)  # 0723修改
    #

    # 21.添加系统字段对象--信件
    # 添加字段对象-信件  ok
    # 20220119 已知bug，列表有效错误显示为1
    @unittest.expectedFailure  # 预期失败标记，列表中“有效”错误显示为1
    def test_21_field(self):
        fieldInfo=FieldCommon(self.driver).fieldRequiredCommon('Article')
        FieldPage(self.driver).clickArticle()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))

        fieldlist_info = ['', '',fieldInfo.get('sysField'), fieldInfo.get('name'), '文本', '信件', '有效']
        # for FiledList01 in ['.cursor.ant-table-row.ng-star-inserted td']:   # 0723 修改

        for i in range(0, 7):
            text_zoom_01 = FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误1：添加字段数据列表显示错误' + text_zoom_01)
            # for i in range(0, 7):
            #     text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
            #     self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误：添加字段数据列表展示不正确' + text_zoom_01)  # 0723修改


        FieldPage(self.driver).clickAll()
        FieldPage(self.driver).search(fieldInfo.get('sysField'))
        # for FiledList01 in ['.cursor.ant-table-row.ng-star-inserted td']:
        for i in range(0, 7):
            text_zoom_01=FieldPage(self.driver).get_filedlist_td(i)
            self.assertEqual(text_zoom_01, fieldlist_info[i], msg='错误2：添加字段数据列表显示错误'+text_zoom_01 )
    # 22.添加自定义字段，在工单模板页面搜索添加

    # 23.导入导出页面的返回按钮，查看导入页面显示的描述提示语  ok
    def test_23_field(self):
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).import_export()
        time.sleep(3)
        tips=FieldPage(self.driver).getTips()
        time.sleep(3)
        FieldPage(self.driver).importGoBack()
        add=FieldPage(self.driver).getAdd()

        assert tips == 'Import itsm config item data required field : Name, Label, FieldOrder, FieldType, ObjectType, ' \
                       'Config, ValidID, UserID.', '字段库导入页面提示语不正确'
        assert add == '添加', '字段库从导入页面返回至列表页面失败'

    def test_24_field(self):
        # EntranceAgentPage(self.driver).enter_filed()
        # fieldInfo={'sysField': "sys202110251243", 'name': "name202110251243"}
        # fieldInfo2 = {'sysField': "sys2110251309", 'name': "name2110251309"}
        # Field_group = {'sysField': "sys2110255759", 'name': "name2110255759"}
        # time.sleep(10)
        #
        # # 搜索点击检查
        # FieldPage(self.driver).search("name202110251243")
        # time.sleep(5)
        # FieldPage(self.driver).edit()

        # 添加文本类型字段
        fieldInfo = FieldCommon(self.driver).fieldRequiredCommon('Ticket')

        # 添加下拉选择框类型字段
        fieldInfo2 = FieldCommon(self.driver).fullSelectFieldCommon()

        # 添加字段组

        Field_group = FieldCommon(self.driver).createFieldCommon('字段组')
        # 选择字段1
        FieldPage(self.driver).chose_field(fieldInfo.get("name"))
        # 选择字段2
        FieldPage(self.driver).chose_field(fieldInfo2.get("name"))
        # 提交
        FieldPage(self.driver).submit()
        time.sleep(5)
        # 搜索二次进入
        # print(Field_group.get('name'))
        FieldPage(self.driver).search(Field_group.get('name'))
        time.sleep(2)
        FieldPage(self.driver).edit()
        time.sleep(4)
        # 断言
        label1= FieldPage(self.driver).get_group_field(fieldInfo.get("sysField"))
        label2= FieldPage(self.driver).get_group_field(fieldInfo2.get("sysField"))

        # 取当前
        self.assertEqual(label1,  fieldInfo.get("name"),msg='错误：字段组添加文本字段失败')
        self.assertEqual(label2,  fieldInfo2.get("name"), msg='错误：字段组添加下拉选择框字段失败')



