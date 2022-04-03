"""
@author: DT_testing
@file:   c_ticketcreate_handle_case.py
@desc:  【用户创单检查】
@step：
    1.customer：字母大小写混合的流程名称在创建页面的展示 （ SC_Template_171）
      customer：设置工单模板所有值都填写，并设置有的值必填、有的值隐藏。使用按钮“提交并继续”后检查页面默认值的显示（SC_Template_173）
      customer：提交并继续创建，可以继续跳转到创单页面，检查页面字段检查右侧用户显示、检查工单详情显示（SC_Template_174）
      customer：设置自定义字段在用户模板，确保可以进行创单（SC_Template_178）
      customer：收藏模板--然后使用收藏的模板创单（SC_Template_180）
      customer：检查工单模板的图片和颜色（SC_Template_182）
    2.customer：设置字段组在服务人员创建模板，确保可以进行创单（字段组含有必填字段+字段组含有字段影响关系+提交按钮颜色检查）（SC_Template_183）
      customer：创单的时候选择失败关闭状态，流程不跳转，处理页面按钮依旧会显示创单那个模板（SC_Template_184 还需要补检查详情按钮）
    3.customer：主题文本联动：模板不设置主题文本的模板，使用时填写主题是什么，文本就是什么内容（SC_Template_176）
      customer：检查只读字段的值（客户单位、下拉选-区、文本字段）（SC_Template_177）
      customer：设置模板展示资产字段必填，创单（SC_Template_177_1）
      customer：不设置指定处理人，则提交后指定人显示的是 otrsadmin （SC_Template_177_2）
    4.customer：设置模板中的下拉选只能显示某几个值（可选+排除---自定义字段和固定字段），在使用模板页面检查（SC_Template_175）
      customer处理模板主题内容联动：不设置主题文本的模板，使用时填写主题是什么，文本就是什么内容（SC_Template_189）
    5.customer：设置客户A的模板，其他客户不能看到（SC_Template_181）
    6.customer：检查用户界面：自定义字段的流程跳转，修改模板指定处理人提交后是修改后的值（SC_Template_177_4）

"""

import time

import requests

from common.base import Base
from src.page.agent.template_use_page import TemplateUsePage
from src.page.customer.c_template_use_page import C_TemplateUsePage
from src.page.customer.customer_login_page import CustomerLoginPage
from src.page.customer.entrance_customer_page import EntranceCustomerPage
from src.page.pagecommon.customer_login_common import CustomerLoginCommon
from src.testcase.testcase_base.basecase_customer import BaseCaseCustomerForTestBed, BaseCaseCustomerForTestBed2


# BaseCaseCustomerForTestBed 默认登录用户：鲁班
class TestBedCustomer(BaseCaseCustomerForTestBed, Base):  # TESTBed

    # OK
    # 1.SC_Template_171、SC_Template_173、SC_Template_174、SC_Template_178、SC_Template_180、SC_Template_182
    def test_1_customerticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceCustomerPage(self.driver).enter_templateuse()
        time.sleep(8)
        # # 检查模板这块有 bug 不能正常显示 (+)
        # process_name =  TemplateUsePage(self.driver).process_name()
        # # print('process_name 是' + process_name)  # 这块有 bug
        #
        # try:
        #     self.assertEqual(process_name, '测试模拟客户场景_测试使用的流程（+）')
        # except AssertionError as msg:
        #     print('流程名称显示不正确！正确显示是：' + process_name + str(msg))
        #     res = True

        # 检查模板名称（收藏的模板）
        template1_name = C_TemplateUsePage(self.driver).template1_name()
        # print(template1_name)
        try:
            self.assertEqual(template1_name, str('0收藏：用户创单 + TEMplate'))
        except AssertionError as msg:
            print('用户收藏的模板名称显示不正确！正确显示是：' + str(msg))
            res = True

        # 非收藏的第一个模板
        template2_name = C_TemplateUsePage(self.driver).template2_name()
        # print(template2_name)
        try:
            self.assertEqual(template2_name, str('1用户模板创单，检查客户展示、字段组、失败关闭流程不跳转'))
        except AssertionError as msg:
            print('用户的模板1名称显示不正确！正确显示是：' + str(msg))
            res = True

        # 进入收藏的工单模板（1用户模板创单，检查代创单）---提交并继续创建
        C_TemplateUsePage(self.driver).templatefavoritechoose()
        time.sleep(3)

        # 页面字段检查及值检查
        list = ['类型', '客户用户资产', '主题', '角色', '优先级', '', '', '省', '内容', '', '附件']# BUG:2020081128000125 资产不应显示
        for fields in ["#OrderField label"]:
            for i in range(0, 11):
                text = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text)
                try:
                    assert text == list[i]
                except AssertionError as msg:
                    print('首次进入创单页面字段显示不正确！字段显示是：' + text + str(msg))
                    res = True

        # 填值,点击继续创单
        # 省
        C_TemplateUsePage(self.driver).provinceclick()
        C_TemplateUsePage(self.driver).chooseselectorvalues('陕西省')
        # 点击“提交并继续”

        # self.driver.find_elements_by_css_selector('.ant-btn-primary')[2].click()  # （研发增加 id, 20200909 测试已更新）
        C_TemplateUsePage(self.driver).submitandcontinue()
        time.sleep(3)

        # -------------继续创单---------
        # 01. 检查显示的字段（徐敏代码更新可使用） SC_Template_174
        # 页面字段检查及值检查
        list1 = ['类型', '客户用户资产', '主题', '角色', '优先级', '', '', '省', '内容', '', '附件']
        for fields in ["#OrderField label"]:
            for i in range(0, 11):
                text1 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text)
                try:
                    assert text1 == list1[i]
                except AssertionError as msg:
                    print('提交并继续-进入创单页面字段显示不正确！字段显示是：' + text1 + str(msg))
                    res = True

        # 02. 检查已填写值的字段 SC_Template_173
        # 检查类型/等模板设置的字段
        typevalue = C_TemplateUsePage(self.driver).typevalue()
        # print(typevalue)
        try:
            self.assertEqual(typevalue, str('ServiceRequest'))
        except AssertionError as msg:
            print('模板已设置的类型显示不正确！正确显示是：' + str(msg))
            res = True

        # 主题
        subjectvalue = C_TemplateUsePage(self.driver).subjectvalue()
        try:
            self.assertEqual(subjectvalue, str('用户提出服务请求'))
        except AssertionError as msg:
            print('模板已设置的主题显示不正确！正确显示是：' + str(msg))
            res = True
        # 03.用户是鲁班七号，检查右侧客户显示
        # 检查右侧显示
        list1 = ['C001', '鲁班', '鲁 班', '区域: 陕西区域', '城市', '手机', '电话:', '邮箱:']
        for fields in [".Narrow p"]:
            for i in range(0, 1):
                text2 = self.driver.find_elements_by_css_selector(fields)[i].text
                try:
                    assert text2 not in list1[i]
                except AssertionError as msg:
                    print('选择用户后自动带出的表单右侧信息显示不正确！正确显示是：' + text2 + str(msg))
                    res = True

        # 角色
        queuevalue = C_TemplateUsePage(self.driver).queuevalue()
        # print(queuevalue)
        try:
            self.assertEqual(queuevalue, str('信息科工程师'))
        except AssertionError as msg:
            print('角色显示不正确！正确显示是：' + str(msg))
            res = True
        # 优先级
        priorityvalue = C_TemplateUsePage(self.driver).priorityvalue()
        try:
            self.assertEqual(priorityvalue, str('5 very high'))
        except AssertionError as msg:
            print('工单优先级显示不正确！正确显示是：' + str(msg))
            res = True

        # 内容（内容框已变更，20200911 修改代码）
        # 文本检查
        tickettextvalue = C_TemplateUsePage(self.driver).tickettextvalue()
        # print(tickettextvalue)
        try:
            self.assertEqual(tickettextvalue, '隐藏了字段:  状态-新建、负责人-管理\n\n客户用户资产隐藏')
        except AssertionError as msg:
            print('工单内容显示不正确！正确显示是：' + str(msg))
            res = True

        # 跟进填写主题
        self.driver.find_element_by_id('Subject').send_keys('TEST2')

        # # --------------滑动页面
        # Base(self.driver).slide_bar('PriorityID')
        # 省
        # C_TemplateUsePage(self.driver).province('广西省')
        C_TemplateUsePage(self.driver).provinceclick()
        C_TemplateUsePage(self.driver).chooseselectorvalues('广西壮族自治区')

        # 提交工单后，在处理页面检查处理按钮 SC_Template_141
        TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)

        # 等待工单详情部分更新后，需要增加详情的判断

        # 最后断言res的值
        assert res is None


    # 2. 检查字段组及页面必填字段（字段组含有必填字段+字段组含有字段影响关系）、检查客户用户必填、检查必填项未填写提交俩按钮为灰色、
    # 检查流程不跳转模板依旧存在

    # SC_Template_183、SC_Template_184（需要检查工单详情的按钮）
    def test_2_customerticketcreate(self):

        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceCustomerPage(self.driver).enter_templateuse()

        # 进入工单模板1(未收藏的第一个模板：)--提交
        C_TemplateUsePage(self.driver).template01choose()
        time.sleep(3)

        #  检查客户用户字段是必填的--检查所有显示的字段
        # 页面字段检查及值检查
        list3 = ['类型', '', '客户名称', '客户用户资产', '角色', '指定处理人', '负责人', '主题', '内容', '', '附件',
                 '状态', '优先级', '数量', '价格', '总价', '一级分类', '二级分类', '000多选', '000多选1']
        for fields in ["#OrderField label"]:
            for i in range(0, 20):
                text3 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text3)
                try:
                    assert text3 == list3[i]
                except AssertionError as msg:
                    print('页面字段显示不正确！这个显示是：' + text3 + str(msg))
                    res = True

        # 打印检查必填字段
        list4 = ['类型', '角色', '主题', '内容', '状态', '优先级', '数量', '价格']
        for fields in ["#OrderField .ant-form-item-required"]:
            for i in range(0, 8):
                text4 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text4)
                try:
                    assert text4 == list4[i]
                except AssertionError as msg:
                    print('页面带 * 的必填项显示不正确！带 * 的字段有：' + text4 + str(msg))
                    res = True

        # 检查提交俩按钮为灰色
        color_submitbtn = C_TemplateUsePage(self.driver).color_submitbtn()
        try:
            self.assertEqual(color_submitbtn, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户必填项未填写值，提交按钮应该置灰！正确显示是：' + str(msg))
            res = True

        color_submitandcontinue = C_TemplateUsePage(self.driver).color_submitandcontinue()
        try:
            self.assertEqual(color_submitandcontinue, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户必填项未填写值，提交并完成按钮应该置灰！正确显示是：' + str(msg))
            res = True

        # # 填写客户用户字段检查提交俩按钮--客户用户模板已取消，代建单功能可用后再增加上来
        # customerusername = '鲁班'
        # customeruserlogin = '鲁班'
        # C_TemplateUsePage(self.driver).customeruser(customerusername, customeruserlogin)
        # color_submitbtn1 = TemplateUsePage(self.driver).color_submitbtn()
        # try:
        #     self.assertEqual(color_submitbtn1, str('background-color: rgb(191, 191, 191);'))
        # except AssertionError as msg:
        #     print('客户用户必填项未填写值，提交按钮应该置灰！正确显示是：' + str(msg))
        #     res = True
        #
        # color_submitandcontinue1 = C_TemplateUsePage(self.driver).color_submitandcontinue()
        # try:
        #     self.assertEqual(color_submitandcontinue1, str('background-color: rgb(191, 191, 191);'))
        # except AssertionError as msg:
        #     print('客户用户必填项未填写值，提交并完成按钮应该置灰！正确显示是：' + str(msg))
        #     res = True

        # 主题
        C_TemplateUsePage(self.driver).subject('TEST字段组和客户用户必填')

        # 填写字段组必填值，填写数量、价格 （2020080328000015 徐敏在增加页面元素--已增加， 20200910 代码已更新）
        C_TemplateUsePage(self.driver).sendamount(2)
        C_TemplateUsePage(self.driver).sendprice(5)
        time.sleep(1)

        # 检查提交俩按钮为蓝色可点击
        color_submitbtn2 = C_TemplateUsePage(self.driver).color_submitbtn()
        # print(color_submitbtn2)
        try:
            self.assertEqual(color_submitbtn2, str('background-color: rgb(52, 152, 166);'))
        except AssertionError as msg:
            print('字段组必填项填写后，提交按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True

        color_submitandcontinue2 = C_TemplateUsePage(self.driver).color_submitandcontinue()
        try:
            self.assertEqual(color_submitandcontinue2, str('background-color: rgb(52, 152, 166);'))
        except AssertionError as msg:
            print('字段组必填项填写后，提交并完成按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True

        # 第二次再次添加字段组（可复制的字段组）addGroupField
        C_TemplateUsePage(self.driver).addGroupField()
        C_TemplateUsePage(self.driver).sendamount2(999999999999)
        C_TemplateUsePage(self.driver).sendprice2(999999999999)
        time.sleep(1)

        # 第三次再次添加字段组（可复制的字段组）addGroupField
        C_TemplateUsePage(self.driver).addGroupField()
        C_TemplateUsePage(self.driver).sendamount3(1111)
        C_TemplateUsePage(self.driver).sendprice3(2222)
        time.sleep(1)

        # 删除第三次的字段组remove_2
        C_TemplateUsePage(self.driver).remove_2()
        time.sleep(1)
        # 提交
        C_TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)
        # 检查工单详情--检查字段组显示、检查工单处理按钮（创建的模板依旧会显示，因为流程没有跳转）



        # 最后断言res的值
        assert res is None

    # OK
    # SC_Template_176主题文本联动 ；SC_Template_177检查只读字段的值（客户单位、下拉选-区、文本字段）；
    # SC_Template_177_1设置模板展示资产字段必填，创单；SC_Template_177_2不设置指定处理人，则提交后指定人显示的是 otrsadmin
    def test_3_customerticketcreate(self):

        # 这里捕获了这里的异常，初始res为NoneSC_Template_176
        res = None

        EntranceCustomerPage(self.driver).enter_templateuse()
        # 进入未收藏的工单模板2
        C_TemplateUsePage(self.driver).template02choose()

        # 检查必填字段
        list5 = ['类型', '客户用户资产', '角色', '主题', '内容', '状态', '优先级']
        for fields in ["#OrderField .ant-form-item-required"]:
            for i in range(0, 7):
                text5 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text5)
                try:
                    assert text5 == list5[i]
                except AssertionError as msg:
                    print('页面带 * 的必填项显示不正确！带 * 的字段有：' + text5 + str(msg))
                    res = True


        # 检查右侧用户展示信息
        listc1 = ['C001', '鲁班', '鲁班', '区域: 陕西区域', '城市', '手机', '电话:', '邮箱:']
        for fields in [".Narrow p"]:
            for i in range(0, 1):
                textc1 = self.driver.find_elements_by_css_selector(fields)[i].text
                try:
                    assert textc1 not in listc1[i]
                except AssertionError as msg:
                    print('选择用户后自动带出的表单右侧信息显示不正确！正确显示是：' + textc1 + str(msg))
                    res = True

        # 检查只读字段的值（客户单位、下拉选-区、文本字段）
        # 01客户单位
        company_readonly = C_TemplateUsePage(self.driver).company_readonly()
        # print(company_readonly)
        try:
            self.assertIn(str('ant-select-disabled'), company_readonly)
        except AssertionError as msg:
            print('客户字段应该是只读字段！正确显示是：' + str(msg))
            res = True
        company_readonlyvalue = C_TemplateUsePage(self.driver).company_readonly_value()
        # print(company_readonlyvalue)
        try:
            self.assertEqual(company_readonlyvalue, '测试客户 - ( C001 ) - ( 陕西区域 ) ')
        except AssertionError as msg:
            print('工单内容显示不正确！正确显示是：' + str(msg))
            res = True

        # 02区字段检查
        qu_readonly = C_TemplateUsePage(self.driver).qu_readonly()

        # 判断“ant-select-disabled”   in 里面
        try:
            self.assertIn(str('ant-select-disabled'), qu_readonly)
        except AssertionError as msg:
            print('区字段应该是只读字段！正确显示是：' + str(msg))
            res = True

        qu_readonlyvalue = C_TemplateUsePage(self.driver).qu_readonly_value()
        try:
            self.assertEqual(qu_readonlyvalue, str('02雁塔区'))
        except AssertionError as msg:
            print('只读字段的默认值显示错误！正确显示是：' + str(msg))
            res = True

        # 03文本字段检查 ant-input-disabled
        wenben1_readonly = C_TemplateUsePage(self.driver).wenben1_readonly()
        # print(wenben1_readonly)
        try:
            self.assertIn(str('ant-input-disabled'), wenben1_readonly)
        except AssertionError as msg:
            print('文本字段应该是只读字段，不能填写值！正确显示是：' + str(msg))
            res = True

        wenben1_readonly_value = C_TemplateUsePage(self.driver).wenben1_readonly_value()
        # print(wenben1_readonly_value)
        try:
            self.assertEqual(wenben1_readonly_value, str('只读文本检查'))
        except AssertionError as msg:
            print('只读字段的默认值显示错误！正确显示是：' + str(msg))
            res = True

        # 检查主题，文本联动，填写主题（除了资产字段未填写其他都已填写，检查提交按钮为灰色）
        # 主题
        C_TemplateUsePage(self.driver).subject('TEST主题填值则文本随之变化')

        tickettextvalue = C_TemplateUsePage(self.driver).tickettextvalue()
        # print(tickettextvalue)
        try:
            self.assertEqual(tickettextvalue, str('TEST主题填值则文本随之变化'))

        except AssertionError as msg:
            print('工单内容没有随着主题而变更！正确显示是：' + str(msg))
            res = True
        # # 切出执行其他操作
        # self.driver.switch_to.default_content()

        # 检查提交俩按钮为灰色不可点击
        color_submitbtn1 = C_TemplateUsePage(self.driver).color_submitbtn()
        try:
            self.assertEqual(color_submitbtn1, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户和字段组必填项填写后，提交按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True

        color_submitandcontinue = C_TemplateUsePage(self.driver).color_submitandcontinue()
        try:
            self.assertEqual(color_submitandcontinue, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户和字段组必填项填写后，提交并完成按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True

        # 只读字段检查
        qu_readonly = C_TemplateUsePage(self.driver).qu_readonly()
        # 判断“ant-select-disabled”   in 里面
        try:
            self.assertIn(str('ant-select-disabled'), qu_readonly)
        except AssertionError as msg:
            print('区字段应该是只读字段！正确显示是：' + str(msg))
            res = True

        qu_readonlyvalue = C_TemplateUsePage(self.driver).qu_readonly_value()
        try:
            self.assertEqual(qu_readonlyvalue, str('02雁塔区'))
        except AssertionError as msg:
            print('只读字段的默认值显示错误！正确显示是：' + str(msg))
            res = True

        # 选资产
        C_TemplateUsePage(self.driver).cmdbbtn()
        # 徐敏在增加页面元素（已增加 ， 20200909 已更新）
        self.driver.find_element_by_id('1').click()
        self.driver.find_element_by_id('save').click()

        # 提交
        C_TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)
        # 检查详情中指定人的显示--需要在 user 界面查看


        # 最后断言res的值
        assert res is None


    # SC_Template_175 设置模板中的下拉选只能显示某几个值（可选+排除）
    # SC_Template_189 处理模板主题内容联动
    def test_4_customerticketcreate(self):

        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceCustomerPage(self.driver).enter_templateuse()
        # 进入未收藏的工单模板2
        C_TemplateUsePage(self.driver).template03choose()
        time.sleep(3)

        # 检查页面字段显示--不显示“挂起时间”
        # 页面字段检查及值检查
        list44 = ['类型', '角色', '指定处理人', '负责人', '主题', '内容', '', '附件', '状态', '优先级', '省1', '市1']
        for fields in ["#OrderField label"]:
            for i in range(0, 12):
                text44 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text44)
                try:
                    assert text44 == list44[i]
                except AssertionError as msg:
                    print('页面字段显示不正确！这个显示是：' + text44 + str(msg))
                    res = True

        # 类型下拉选只能选择 问题和其他  SC_Template_175
        C_TemplateUsePage(self.driver).typeclick()
        # 检查下拉选的值
        # ll = self.driver.find_element_by_class_name('cdk-virtual-scroll-content-wrapper').text
        types = C_TemplateUsePage(self.driver).selectorvalues()
        try:
            self.assertIn(types, '其他\n问题')
        except AssertionError as msg:
            print('类型下拉选值显示错误！类型下拉选只能选择 问题和其他' + str(msg))
            res = True

        # 任选一个
        C_TemplateUsePage(self.driver).chooseselectorvalues('其他')
        time.sleep(3)

        # 滑动页面
        Base(self.driver).slide_bar('Subject')
        Base(self.driver).slide_bar('StateID')

        # 优先级不可以选择 4高和5非常高
        C_TemplateUsePage(self.driver).priorityclick()
        priorities = C_TemplateUsePage(self.driver).selectorvalues()
        try:
            self.assertIn(priorities, '1-非常低\n2-低\n3-正常')
        except AssertionError as msg:
            print('优先级下拉选值显示错误！优先级不可以选择 4高和5非常高' + str(msg))
            res = True

        # 选中 1-非常低
        C_TemplateUsePage(self.driver).chooseselectorvalues('1-非常低')
        time.sleep(3)

        # # 省1 字段排除显示四川省（bug：2020081028000029 ）# province1click
        #
        # 市1 字段只可以选择西安、宝鸡、南宁
        C_TemplateUsePage(self.driver).city1click()
        city1 = C_TemplateUsePage(self.driver).selectorvalues()
        # print(city1)
        try:
            self.assertIn(city1, '南宁\n宝鸡\n西安')
        except AssertionError as msg:
            print('市1字段下拉选值显示错误！市1 字段只可以选择西安、宝鸡、南宁' + str(msg))
            res = True
        # 选中南宁
        C_TemplateUsePage(self.driver).chooseselectorvalues('南宁')
        time.sleep(3)

        # 提交
        C_TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)

        # 处理模板主题内容联动 SC_Template_189


        # 最后断言res的值
        assert res is None


# SC_Template_181：设置客户A的模板，其他客户不能看到。BaseCaseCustomer 默认登录用户： A-1
class TestBedCustomer2(BaseCaseCustomerForTestBed2, Base):
    def test_5_customerticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None
        # 模板是 A-1 的，登录 A-2，不能看到这个模板
        # 可以使用流程“不同客户使用”enter_templateuse2，可以使用模板

        EntranceCustomerPage(self.driver).enter_templateuse2()
        time.sleep(1)
        # 进入未收藏的工单模板2
        C_TemplateUsePage(self.driver).templateforA1()
        time.sleep(3)
        # 主题
        subjectvalue = C_TemplateUsePage(self.driver).subjectvalue()
        try:
            self.assertEqual(subjectvalue, str('模板使用者“A-1客户”'))
        except AssertionError as msg:
            print('模板已设置的主题显示不正确！正确显示是：' + str(msg))
            res = True

        #  用户A-1 退出系统
        CustomerLoginPage(self.driver).logout_button()
        time.sleep(3)

        # 登录用户 A-2（customerlogincommonforbed3），检查其页面不显示此菜单（不同客户使用）
        CustomerLoginCommon(self.driver).customerlogincommonforbed3()

        # 点击开始按钮
        EntranceCustomerPage(self.driver).openmenu()
        # 检查菜单不应显示"不同客户使用"
        menus = self.driver.find_element_by_xpath('/html/body/app-root/customer-root/div/div/app-navigation'
                                                       '/div/div[2]').get_attribute('textContent')
        # print(menus)
        try:
            self.assertNotIn(str('不同客户使用'), menus)
        except AssertionError as msg:
            print('a-2 用户不应显示流程“不同客户使用”！正确显示是：' + str(msg))
            res = True

        # 合起菜单栏
        EntranceCustomerPage(self.driver).closemenu()

        # 最后断言res的值
        assert res is None

# SC_Template_177_4 customer：检查用户界面：自定义字段的流程跳转，修改模板指定处理人提交后是修改后的值
class TestBedCustomer3(BaseCaseCustomerForTestBed2, Base):
    def test_6_customerticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceCustomerPage(self.driver).enter_templateuse2()

        # 进入工单模板1（A-1 使用的模板）
        C_TemplateUsePage(self.driver).templateforA2()
        time.sleep(3)

        # 指定人选择李林
        C_TemplateUsePage(self.driver).owner('李林')
        # 滑动页面
        Base(self.driver).slide_bar('Subject')

        # 省下拉选选择“广西壮族自治区”
        C_TemplateUsePage(self.driver).province('广西壮族自治区')

        # 提交
        TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)

        # --------- 工单详情 ，检查有用户的操作按钮

        # user 页面搜索检查工单指定处理人是李林------

        # 最后断言res的值
        assert res is None











