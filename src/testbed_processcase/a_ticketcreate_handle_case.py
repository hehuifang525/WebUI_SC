"""
@author: DT_testing
@file:   a_ticketcreate_handle_case.py
@desc:  【服务人员创单检查 -- 工单创建及处理】  A/C 使用 231 机器（完毕后将此机器备份，作为测试镜像）
@step：  登录root 账户，使用“TESTBED_测试流程” 进行验证

        1. 检查流程名、模板名称、模板颜色，提交并创建后检查路径、检查页面字段默认值、修改工单主题内容不会变化，提交检查详情的自定义字段、指定处理人
           SC_Template_140、SC_Template_141、SC_Template_142、SC_Template_143、SC_Template_144、SC_Template_146、
           SC_Template_147
        2. 检查字段组（字段组含有必填字段+字段组含有字段影响关系）、检查客户用户必填、检查必填项未填写提交俩按钮为灰色（SC_Template_155）

        3. 检查收藏的模板：服务人员创单 - 主题内容为空，资产必填，只读字段，不设置指定处理人
           SC_Template_145、SC_Template_148、SC_Template_149、SC_Template_150、SC_Template_156
        4. 模板下拉选可选及排除、处理模板中检查挂起状态和挂起时间的带入和下拉选值的排除可选、修改客户用户、处理模板主题内容联动
           SC_Template_151、SC_Template_154、SC_Template_154_1、SC_Template_158、SC_Template_170
           user：设置模板中角色下拉选有父子级，检查创建页面使用的下拉选值；创单重新选择角色在详情检查（SC_Template_156_1）

        5. 设置角色--管理员使用的模板，其他角色不能看到。BaseCaseUserForTestBed 登录默认服务人员： guan（SC_Template_153）
        6. user：检查自定义字段的流程跳转，修改模板指定处理人提交后是修改后的值（SC_Template_153_1）
        7. 模板下拉选可选对角色父子级的检查(SC_Template_156_1)
"""
import time
from selenium.webdriver import ActionChains

from common.base import Base
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.template_use_page import TemplateUsePage
from src.page.customer.c_template_use_page import C_TemplateUsePage
from src.page.pagecommon.agent_login_common import AgentLoginCommon

from src.testcase.testcase_base.basecase_user import BaseCaseUserForTestBed


class TestBedAgent(BaseCaseUserForTestBed, Base):  # TESTBed
    # OK1.SC_Template_140  SC_Template_141  SC_Template_142  SC_Template_143  SC_Template_144  SC_Template_146
    # SC_Template_147
    def test_1_ticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceAgentPage(self.driver).enter_templateuse()

        # # 检查模板
        # process_name = TemplateUsePage(self.driver).process_name()
        # # print('process_name 是' + process_name)  # 这块有 bug  Ticket#2020072328000104
        #
        # try:
        #     self.assertEqual(process_name, str(' 测试模拟客户场景_测试使用的流程（+） '))
        # except AssertionError as msg:
        #     print('流程名称显示不正确！正确显示是：' + str(msg))
        #     res = True

        template1_name = TemplateUsePage(self.driver).template1_name()
        # print(template1_name)
        try:
            self.assertEqual(template1_name, str('服务人员模板创单-TEMplate'))
        except AssertionError as msg:
            print('非收藏的模板 1 名称显示不正确！正确显示是：' + str(msg))
            res = True

        # 模板的图标和颜色检查
        template1_color = TemplateUsePage(self.driver).template1_color()
        # print(template1_color)
        try:
            self.assertEqual(template1_color, str('background: rgb(191, 65, 234);'))
        except AssertionError as msg:
            print('模板1颜色显示不正确！正确显示是：' + str(msg))
            res = True

        template1_img = TemplateUsePage(self.driver).template1_img()
        try:
            self.assertEqual(template1_img, str('wrench'))
        except AssertionError as msg:
            print('模板1图标显示不正确（不是钳子的图标）！正确显示是：' + str(msg))
            res = True

        # template2_name = self.driver.find_element_by_css_selector('#ticketTemplate2 > div > div > span').text
        template2_name = TemplateUsePage(self.driver).template2_name()
        # print(template2_name)
        try:
            self.assertEqual(template2_name, str('服务人员创单（+）字段组、客户用户必填、自定义状态'))
        except AssertionError as msg:
            print('非收藏的模板 2 名称显示不正确！正确显示是：' + str(msg))
            res = True

        # 进入工单1-'服务人员模板创单-TEMplate'--提交并继续创建
        TemplateUsePage(self.driver).template01choose()
        time.sleep(3)

        # 检查所有显示的字段
        # 1.检查路径显示
        load = TemplateUsePage(self.driver).road_submitandcontinue()
        try:
            self.assertEqual(load, str('/ 新建工单 ( 业务流程 ) / TESTBED_测试流程'))
        except AssertionError as msg:
            print('提交并完成后的路径显示不正确！正确显示是：' + str(msg))
            res = True

        # 2.页面字段检查及值检查
        list0 = ['类型', '客户用户', '客户名称', '客户用户资产', '角色', '指定处理人', '负责人', '主题', '内容', '', '附件', '状态',
                 '优先级', '省', '市']
        for fields in ["#OrderField label"]:
            for i in range(0, 15):
                text = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text)
                try:
                    assert text == list0[i]
                except AssertionError as msg:
                    print('页面字段显示不正确！字段显示是：' + text + str(msg))
                    res = True

        # 填值,点击继续创单
        # 主题
        TemplateUsePage(self.driver).subject('TEST1-创建工单，使用提交并继续按钮')

        # 检查工单模板已设置的内容不变化(工单内容检查)
        tickettextvalue = TemplateUsePage(self.driver).tickettextvalue()
        # print(tickettextvalue)
        try:
            self.assertEqual(tickettextvalue, str('问题描述：\n\n操作步骤：\n预期结果：\n实际结果'))

        except AssertionError as msg:
            print('工单内容显示不正确！正确显示是：' + str(msg))
            res = True

        # 点击“提交并继续”
        TemplateUsePage(self.driver).submitandcontinue()
        time.sleep(5)

        # -------------继续创单---------
        # 再次新增 用户是鲁班七号，检查右侧客户显示
        # 01. 检查显示的字段
        # 页面字段检查及值检查
        list00 = ['类型', '客户用户', '客户名称', '客户用户资产', '角色', '指定处理人', '负责人', '主题', '内容', '', '附件', '状态',
                  '优先级', '省', '市']
        for fields in ["#OrderField label"]:
            for i in range(0, 15):
                text0 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text0)
                try:
                    assert text0 == list00[i]
                except AssertionError as msg:
                    print('提交并完成后的页面字段显示不正确！字段显示是：' + text0 + str(msg))
                    res = True

        # 02. 检查已填写值的字段
        # 检查类型/等模板设置的字段
        typevalue = TemplateUsePage(self.driver).typevalue()
        # print(typevalue)
        try:
            self.assertEqual(typevalue, str('Problem'))
        except AssertionError as msg:
            print('模板已设置的类型显示不正确！正确显示是：' + str(msg))
            res = True

        # 填值创单
        customerusername = '鲁班七号'
        customeruserlogin = 'lubanqihao'
        TemplateUsePage(self.driver).customeruser(customerusername, customeruserlogin)
        time.sleep(2)  # 否则下方客户没有等到显示值会返回 None

        # 检查客户单位显示
        companyvalue = TemplateUsePage(self.driver).companyvalue()
        # print(companyvalue)
        try:
            self.assertEqual(companyvalue, str('测试客户'))
        except AssertionError as msg:
            print('选择用户后自动带出的客户单位显示不正确！正确显示是：' + str(msg))
            res = True

        # 检查右侧显示
        # list1 = ['C001', 'lubanqihao', '鲁班 七号', '区域: 陕西区域', '手机: 13289356543', '电话:', '邮箱: testqihao@163.com']
        list1 = str('C001\nlubanqihao\n鲁班七号\n\n区域: 陕西区域\n城市: 陕西西安\n手机: 13289356543\n电话:'
                    '\n邮箱: testqihao@163.com')
        for fields in [".Narrow p"]:
            for i in range(0, 1):
                text2 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text2)
                try:
                    self.assertEqual(text2, list1)
                except AssertionError as msg:
                    print('选择用户后自动带出的表单右侧信息显示不正确！正确显示是：' + text2 + str(msg))
                    res = True
        # 角色
        queuevalue = TemplateUsePage(self.driver).queuevalue()
        # print(queuevalue)
        try:
            self.assertEqual(queuevalue, str('信息科工程师'))
        except AssertionError as msg:
            print('角色显示不正确！正确显示是：' + str(msg))
            res = True

        # 指定处理人
        # ownervalue = TemplateUsePage(self.driver).ownervalue()
        try:
            ownervalue = TemplateUsePage(self.driver).ownervalue()
            self.assertEqual(ownervalue, str('李林'))
        except AssertionError as msg:
            print('指定处理人显示不正确！' + str(msg))
            res = True
        # 负责人
        responsiblevalue = TemplateUsePage(self.driver).responsiblevalue()
        try:
            self.assertEqual(responsiblevalue, str('管理'))
        except AssertionError as msg:
            print('负责人显示不正确！正确显示是：' + str(msg))
            res = True

        # 主题
        subjectvalue = TemplateUsePage(self.driver).subjectvalue()
        # print(subjectvalue)
        try:
            self.assertEqual(subjectvalue, str('主题'))
        except AssertionError as msg:
            print('工单主题显示不正确！正确显示是：' + str(msg))
            res = True

        # 内容
        # 文本
        TemplateUsePage(self.driver).tickettext('文本')

        # ---重新选择指定人和负责人
        TemplateUsePage(self.driver).owner('韦艳霞')
        TemplateUsePage(self.driver).responsible('卢志尧')

        # 填写主题
        TemplateUsePage(self.driver).subject('TEST2-使用提交并创建后的工单')

        # 滑动页面
        Base(self.driver).slide_bar('Subject')

        # 状态
        statevalue = TemplateUsePage(self.driver).statevalue()
        try:
            self.assertEqual(statevalue, str('自定义'))
        except AssertionError as msg:
            print('工单主题显示不正确！正确显示是：' + str(msg))
            res = True

        # 优先级
        priorityvalue = TemplateUsePage(self.driver).priorityvalue()
        try:
            self.assertEqual(priorityvalue, str('4 high'))
        except AssertionError as msg:
            print('工单优先级显示不正确！正确显示是：' + str(msg))
            res = True

        # 省
        provincevalue = TemplateUsePage(self.driver).provincevalue()
        try:
            self.assertEqual(provincevalue, str('陕西省'))
        except AssertionError as msg:
            print('省 显示不正确！正确显示是：' + str(msg))
            res = True
        # 市
        cityvalue = TemplateUsePage(self.driver).cityvalue()
        try:
            self.assertEqual(cityvalue, str('01西安'))
        except AssertionError as msg:
            print('市 显示不正确！正确显示是：' + str(msg))
            res = True

        # ---填写其他省市
        province = '四川省'
        city = '02绵阳'
        TemplateUsePage(self.driver).province(province)
        TemplateUsePage(self.driver).city(city)

        # 提交工单后，在处理页面检查处理按钮 SC_Template_141
        # self.driver.find_elements_by_css_selector('.ant-btn-primary')[1].click()
        TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)

        # 等待工单详情部分更新后，需要增加详情的判断

        # 最后断言res的值
        assert res is None

    # OK检查字段组及页面必填字段（字段组含有必填字段+字段组含有字段影响关系）、检查客户用户必填、检查必填项未填写提交俩按钮为灰色、检查流程不跳转模板依旧存在
    # SC_Template_155   SC_Template_168
    def test_2_agentticketcreate(self):

        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceAgentPage(self.driver).enter_templateuse()

        # 进入工单模板2--提交
        TemplateUsePage(self.driver).template02choose()
        time.sleep(3)

        #  检查客户用户字段是必填的--检查所有显示的字段
        # 页面字段检查及值检查
        list3 = ['类型', '客户用户', '客户名称', '客户用户资产', '角色', '指定处理人', '负责人', '主题', '内容', '', '附件', '状态',
                 '优先级', '数量', '价格', '总价', '一级分类', '二级分类']
        for fields in ["#OrderField label"]:
            for i in range(0, 18):
                text3 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text3)
                try:
                    assert text3 == list3[i]
                except AssertionError as msg:
                    print('页面字段显示不正确！这个显示是：' + text3 + str(msg))
                    res = True

        # 打印检查必填字段
        list4 = ['类型', '客户用户', '角色', '主题', '内容', '状态', '优先级', '数量', '价格']
        for fields in ["#OrderField .ant-form-item-required"]:
            for i in range(0, 9):
                text4 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text4)
                try:
                    assert text4 == list4[i]
                except AssertionError as msg:
                    print('页面带 * 的必填项显示不正确！带 * 的字段有：' + text4 + str(msg))
                    res = True
        time.sleep(2)
        # 检查提交俩按钮为灰色  background-color: rgb(52, 152, 166);
        color_submitbtn = TemplateUsePage(self.driver).color_submitbtn()
        try:
            self.assertEqual(color_submitbtn, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户必填项未填写值，提交按钮应该置灰！正确显示是：' + str(msg))
            res = True

        color_submitandcontinue = TemplateUsePage(self.driver).color_submitandcontinue()
        try:
            self.assertEqual(color_submitandcontinue, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户必填项未填写值，提交并完成按钮应该置灰！正确显示是：' + str(msg))
            res = True

        # 填写客户用户字段检查提交俩按钮
        customerusername = '鲁班'
        customeruserlogin = '鲁班'
        TemplateUsePage(self.driver).customeruser(customerusername, customeruserlogin)

        color_submitbtn1 = TemplateUsePage(self.driver).color_submitbtn()
        try:
            self.assertEqual(color_submitbtn1, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户必填项未填写值，提交按钮应该置灰！正确显示是：' + str(msg))
            res = True

        color_submitandcontinue1 = TemplateUsePage(self.driver).color_submitandcontinue()
        try:
            self.assertEqual(color_submitandcontinue1, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户必填项未填写值，提交并完成按钮应该置灰！正确显示是：' + str(msg))
            res = True

        # 主题
        TemplateUsePage(self.driver).subject('TEST字段组和客户用户必填')

        # 填写字段组必填值，填写数量、价格 （2020080328000015 徐敏在增加页面元素--已增加， 20200909 代码已更新）
        TemplateUsePage(self.driver).sendamount(2)
        TemplateUsePage(self.driver).sendprice(5)
        time.sleep(1)

        # 检查总计自动展示出  --没得元素、测试例未补充

        # 检查提交俩按钮为蓝色可点击  background-color: rgb(52, 152, 166);
        color_submitbtn2 = TemplateUsePage(self.driver).color_submitbtn()
        try:
            self.assertEqual(color_submitbtn2, str('background-color: rgb(52, 152, 166);'))
        except AssertionError as msg:
            print('客户用户和字段组必填项填写后，提交按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True

        color_submitandcontinue2 = TemplateUsePage(self.driver).color_submitandcontinue()
        try:
            self.assertEqual(color_submitandcontinue2, str('background-color: rgb(52, 152, 166);'))
        except AssertionError as msg:
            print('客户用户和字段组必填项填写后，提交并完成按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True
        # 再次添加字段组（可复制的字段组）
        # 点击添加按钮检查提交两按钮是灰色
        # 提交检查工单详情--检查字段组显示

        # 填写后继续点击添加复制字段组

        # 点击删除第三个字段组

        # 提交
        TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)
        # 检查工单详情--检查字段组显示、检查工单处理按钮（创建的模板依旧会显示，因为流程没有跳转）

        # 最后断言res的值
        assert res is None

    # OK3.检查收藏的模板：服务人员创单 - 主题内容为空，资产必填，只读字段，不设置指定处理人。提单检查详情资产的显示
    # SC_Template_145、SC_Template_148、SC_Template_149、SC_Template_150、
    # SC_Template_156 不设置指定处理人，则提交后指定人显示的是登录人员
    def test_3_agentticketcreate(self):

        # 这里捕获了这里的异常，初始res为NoneSC_Template_176
        res = None

        EntranceAgentPage(self.driver).enter_templateuse()
        # 进入收藏的工单模板
        TemplateUsePage(self.driver).templatefavoritechoose()

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

        # 设置链接的资产
        TemplateUsePage(self.driver).cmdbbtn()
        time.sleep(1)
        # 会提示请先选择客户用户
        # ll = self.driver.find_element_by_css_selector('.ant-modal-confirm-content>div').text
        # print(ll)
        customernocmdbtips = TemplateUsePage(self.driver).customernocmdbtips()
        try:
            self.assertEqual(customernocmdbtips, str('请先选择客户用户'))
        except AssertionError as msg:
            print('没有选择用户的时候点击资产弹框会有提示信息，提示信息展示不正确！正确显示是：' + str(msg))
            res = True
        time.sleep(1)
        # 点击资产弹框提示上的“确定”按钮
        TemplateUsePage(self.driver).cmdbtips_ntb()
        time.sleep(3)

        # 填写用户：鲁班
        customerusername = '鲁班'
        customeruserlogin = '鲁班'
        TemplateUsePage(self.driver).customeruser(customerusername, customeruserlogin)

        # 检查主题，文本联动，填写主题（除了资产字段未填写其他都已填写，检查提交按钮为灰色）
        # 主题
        TemplateUsePage(self.driver).subject('TEST主题填值则文本随之变化')

        tickettextvalue = TemplateUsePage(self.driver).tickettextvalue()
        # print(tickettextvalue)
        try:
            self.assertEqual(tickettextvalue, str('TEST主题填值则文本随之变化'))

        except AssertionError as msg:
            print('工单内容没有随着主题而变更！正确显示是：' + str(msg))
            res = True
        # 切出执行其他操作
        self.driver.switch_to.default_content()

        # 检查提交俩按钮为灰色不可点击
        color_submitbtn1 = TemplateUsePage(self.driver).color_submitbtn()
        try:
            self.assertEqual(color_submitbtn1, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户和字段组必填项填写后，提交按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True

        color_submitandcontinue = TemplateUsePage(self.driver).color_submitandcontinue()
        try:
            self.assertEqual(color_submitandcontinue, str('background-color: rgb(191, 191, 191);'))
        except AssertionError as msg:
            print('客户用户和字段组必填项填写后，提交并完成按钮应该蓝色可点击！正确显示是：' + str(msg))
            res = True

        # 只读字段检查
        qu_readonly = TemplateUsePage(self.driver).qu_readonly()

        # 判断“ant-select-disabled”   in 里面
        try:
            # self.assertIn(qu_readonly, str('ng-tns-c24-45 ant-select ant-select-sm ant-select-show-arrow '
            #                                'ant-select-disabled ant-select-show-search ant-select-allow-clear'
            #                                ' ant-select-single ng-untouched ng-pristine ng-star-inserted'))
            self.assertIn(str('ant-select-disabled'), qu_readonly)
        except AssertionError as msg:
            print('区字段应该是只读字段！正确显示是：' + str(msg))
            res = True

        qu_readonlyvalue = TemplateUsePage(self.driver).qu_readonly_value()
        try:
            self.assertEqual(qu_readonlyvalue, str('02雁塔区'))
        except AssertionError as msg:
            print('只读字段的默认值显示错误！正确显示是：' + str(msg))
            res = True

        # 选资产
        TemplateUsePage(self.driver).cmdbbtn()
        # 徐敏在增加页面元素（已增加 ， 20200909 已更新）
        self.driver.find_element_by_id('1').click()
        self.driver.find_element_by_id('save').click()

        # 提交，检查详情中指定人的显示
        TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)
        # 指定人显示的是登录人员


        # 最后断言res的值
        assert res is None

    # OK4.
    # SC_Template_151、SC_Template_154、SC_Template_158、SC_Template_170
    def test_4_agentticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceAgentPage(self.driver).enter_templateuse()

        # 进入工单模板3（未收藏的）
        TemplateUsePage(self.driver).template03choose()
        time.sleep(3)

        # 检查页面字段显示--不显示“挂起时间”
        # 页面字段检查及值检查
        list44 = ['类型', '角色', '指定处理人', '负责人', '主题', '内容', '', '附件', '状态', '', '优先级', '省1', '市1']
        for fields in ["#OrderField label"]:
            for i in range(0, 13):
                text44 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text44)
                try:
                    assert text44 == list44[i]
                except AssertionError as msg:
                    print('页面字段显示不正确！这个显示是：' + text44 + str(msg))
                    res = True

        # 类型下拉选只能选择 问题和其他  SC_Template_154
        TemplateUsePage(self.driver).typeclick()
        # 检查下拉选的值
        # ll = self.driver.find_element_by_class_name('cdk-virtual-scroll-content-wrapper').text
        types = TemplateUsePage(self.driver).selectorvalues()
        try:
            self.assertIn(types, '其他\n问题')
        except AssertionError as msg:
            print('类型下拉选值显示错误！类型下拉选只能选择 问题和其他' + str(msg))
            res = True
        # 选择其他
        TemplateUsePage(self.driver).chooseselectorvalues('其他')
        time.sleep(1)

        # 检查角色父子级（信息科人员+科长）可选的展示
        TemplateUsePage(self.driver).roleclick()
        roles = TemplateUsePage(self.driver).roleselectorvalue()
        try:
            self.assertIn(roles, '信息科工程师\n科长')
        except AssertionError as msg:
            print('角色下拉选值显示错误！类型下拉选只能选择父子级的信息科工程师和科长' + str(msg))
            res = True
        # 选择科长
        TemplateUsePage(self.driver).choosetitlevalues('科长')
        time.sleep(1)

        # 滑动页面
        Base(self.driver).slide_bar('Subject')
        Base(self.driver).slide_bar('StateID')

        # 优先级不可以选择 4高和5非常高
        TemplateUsePage(self.driver).priorityclick()
        priorities = TemplateUsePage(self.driver).selectorvalues()
        try:
            self.assertIn(priorities, '1-非常低\n2-低\n3-正常')
        except AssertionError as msg:
            print('优先级下拉选值显示错误！优先级不可以选择 4高和5非常高' + str(msg))
            res = True

        # 选中 1-非常低
        TemplateUsePage(self.driver).chooseselectorvalues('1-非常低')
        time.sleep(3)

        # # 省1 字段排除显示四川省（bug：2020081028000029 ）# province1click
        #
        # 市1 字段只可以选择西安、宝鸡、南宁
        TemplateUsePage(self.driver).city1click()
        city1 = TemplateUsePage(self.driver).selectorvalues()
        # print(city1)
        try:
            self.assertIn(city1, '南宁\n宝鸡\n西安')
        except AssertionError as msg:
            print('市1字段下拉选值显示错误！市1 字段只可以选择西安、宝鸡、南宁' + str(msg))
            res = True
        # 选中南宁
        TemplateUsePage(self.driver).chooseselectorvalues('南宁')
        time.sleep(3)

        # 提交
        TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)

        # --------- 工单详情 使用按钮“3处理模板”--------
        # 挂起的状态（创建的时候隐藏挂起时间这一字段，2h ），在处理页面会自动带入，依旧是 创建时候的挂起值
        # 01检查工单详情信息，不显示客户用户
        # 检查 挂起状态在处理模板中带入  SC_Template_151；检查详情中角色显示是科长SC_Template_156_1

        # 检查处理模板的下拉选值，可选/排除 （设置与创建的一致--需要增加模板的设置）SC_Template_154_1

        # 在处理模板设置选中客户用户--鲁班，提交后检查 SC_Template_170

        # 处理模板填写什么主题则显示出什么内容  SC_Template_158

        # 最后断言res的值
        assert res is None

# SC_Template_153：设置角色--管理员使用的模板，其他角色不能看到。BaseCaseUserForTestBed 登录默认服务人员： guan
# bug：2020090328000246
class TestBedAgent2(BaseCaseUserForTestBed, Base):
    def test_5_agentticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None
        # 模板是管理员的，登录普通角色--信息科人员lilin，不能看到这个模板
        # 可以使用流程“不同角色使用”enter_templateuse2，可以使用模板

        EntranceAgentPage(self.driver).enter_templateuse2()
        time.sleep(1)
        # 进入未收藏的工单模板1(使用 id 名称为11)
        TemplateUsePage(self.driver).template11choose()
        time.sleep(3)
        # 主题
        subjectvalue = TemplateUsePage(self.driver).subjectvalue()
        try:
            self.assertEqual(subjectvalue, str('主题'))
        except AssertionError as msg:
            print('模板已设置的主题显示不正确！正确显示是：' + str(msg))
            res = True

        # 退出系统
        AgentLoginPage(self.driver).logout_button()
        time.sleep(3)

        # 登录服务人员 李林（customerlogincommonforbed2），检查其页面不显示此菜单（不同角色使用）
        AgentLoginCommon(self.driver).customerlogincommonforbed2()

        # 点击开始按钮
        EntranceAgentPage(self.driver).openmenu()
        # 检查菜单不应显示"不同客户使用"
        menus = self.driver.find_element_by_xpath\
            ('//*[@id="newHeight"]/app-navigation/div/div[2]').get_attribute('textContent')
        # print(menus)
        try:
            self.assertNotIn(str('不同角色使用'), menus)
        except AssertionError as msg:
            print('信息科李林不应显示流程“不同角色使用”！正确显示是：' + str(msg))
            res = True

        # 合起菜单栏
        EntranceAgentPage(self.driver).closemenu()

        # 最后断言res的值
        assert res is None

    # SC_Template_153_1:user：检查自定义字段的流程跳转，修改模板指定处理人提交后是修改后的值
    def test_6_agentticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceAgentPage(self.driver).enter_templateuse2()

        # 进入工单模板1（未收藏的）
        TemplateUsePage(self.driver).template22choose()
        time.sleep(3)

        # 指定人选择李林
        TemplateUsePage(self.driver).owner('李林')
        # 滑动页面
        Base(self.driver).slide_bar('Subject')

        # 省下拉选选择“广西壮族自治区”
        TemplateUsePage(self.driver).province('广西壮族自治区')

        # 提交
        TemplateUsePage(self.driver).submitbtn()
        time.sleep(3)

        # --------- 工单详情 ，检查有操作按钮；检查工单指定处理人是李林------

        # 最后断言res的值
        assert res is None