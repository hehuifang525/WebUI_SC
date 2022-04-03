"""
@author: DT_testing
@file:   ticketcreate_handle_case.py
@desc:  【工单创建及处理】  A/C 使用 231 机器（完毕后将此机器备份，作为测试镜像）
@step：  登录root 账户，使用“TESTBED_测试流程” 进行验证
"""
import time
import traceback

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from common.base import Base
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.template_use_page import TemplateUsePage
from src.testcase.testcase_base.basecase_user import BaseCaseUser, BaseCaseUserForTestBed


class TestBed(BaseCaseUserForTestBed, Base):  # TESTBed
# class TestBed(BaseCaseUser, Base):    # 徐敏

    # 1.SC_Template_140  SC_Template_141  SC_Template_142  SC_Template_143
    def test_1_ticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None

        EntranceAgentPage(self.driver).enter_templateuse()

        # # 检查模板
        # process_name =  TemplateUsePage(self.driver).process_name()
        # # print('process_name 是' + process_name)  # 这块有 bug
        #
        # try:
        #     self.assertEqual(process_name, '测试模拟客户场景_测试使用的流程（+）')
        # except AssertionError as msg:
        #     print('流程名称显示不正确！正确显示是：' + process_name + str(msg))
        #     res = True

        #template1_name = self.driver.find_element_by_css_selector('.create-ticket-template-content > span').text
        template1_name = TemplateUsePage(self.driver).template1_name()
        # print(template1_name)
        try:
            self.assertEqual(template1_name, str('服务人员模板创单-TEMplate'))
        except AssertionError as msg:
            print('模板1名称显示不正确！正确显示是：' + str(msg))
            res = True

        # template2_name = self.driver.find_element_by_css_selector('#ticketTemplate2 > div > div > span').text
        template2_name = TemplateUsePage(self.driver).template2_name()
        # print(template2_name)
        try:
            self.assertEqual(template2_name, str('服务人员创单（+）'))
        except AssertionError as msg:
            print('模板2名称显示不正确！正确显示是：' + str(msg))
            res = True



        # # 进入工单1---提交并继续创建
        TemplateUsePage(self.driver).template01choose()
        # self.driver.find_elements_by_css_selector('[class="create-ticket-template-content"]')[0].click()
        time.sleep(3)

        # # 检查所有显示的字段   （徐敏代码更新后可使用）
        #         # # 页面字段检查及值检查
        #         # for fields in ["#OrderField label"]:
        #         #     for i in range(0, 14):
        #         #         text = self.driver.find_elements_by_css_selector(fields)[i].text
        #         #         print(text)
        #                 # if text != '名称' and text != '角色所属区域' and text != '默认所有者' and text != '默认负责人' \
        #                 #         and text != '角色管理者' and text != '备注' and text != '有效性' and text != '修改时间' \
        #                 #         and text != '修改人':
        #                 #     print("角色列表显示不正确！正确显示是：" + text)
        #
        #
        # 填值,点击继续创单
        # 主题
        self.driver.find_element_by_id('Subject').send_keys('TEST1')
        self.driver.find_elements_by_css_selector('.ant-btn-primary')[2].click()  # （徐敏会增加 id）
        time.sleep(3)

        #-------------继续创单---------
        # 再次新增 用户是鲁班七号，检查右侧客户显示

        # 01. 检查显示的字段（徐敏代码更新可使用）
        #         # # 页面字段检查及值检查
        #         # for fields in ["#OrderField label"]:
        #         #     for i in range(0, 14):
        #         #         text = self.driver.find_elements_by_css_selector(fields)[i].text
        #         #         print(text)
        #                 # if text != '名称' and text != '角色所属区域' and text != '默认所有者' and text != '默认负责人' \
        #                 #         and text != '角色管理者' and text != '备注' and text != '有效性' and text != '修改时间' \
        #                 #         and text != '修改人':
        #                 #     print("角色列表显示不正确！正确显示是：" + text)

        # 02. 检查已填写值的字段
        # 检查类型/等模板设置的字段
        typevalue = TemplateUsePage(self.driver).typevalue()
        #print(typevalue)
        try:
            self.assertEqual(typevalue, str('Problem'))
        except AssertionError as msg:
            print('模板已设置的类型显示不正确！正确显示是：' +  str(msg))
            res = True

        # 填值创单
        customerusername ='鲁班七号'
        customeruserlogin='lubanqihao'
        TemplateUsePage(self.driver).customeruser(customerusername, customeruserlogin)

        # 检查客户单位显示
        companyvalue =  TemplateUsePage(self.driver).companyvalue()
        # print(company)
        try:
            self.assertEqual(companyvalue, str('测试客户'))
        except AssertionError as msg:
            print('选择用户后自动带出的客户单位显示不正确！正确显示是：'+ str(msg))
            res = True

        # 检查右侧显示
        list1 = ['C001', 'lubanqihao', '鲁班 七号', '区域: 陕西区域', '手机: 13289356543', '电话:', '邮箱: testqihao@163.com']
        for fields in [".Narrow p"]:
            for i in range(0, 1):
                text2 = self.driver.find_elements_by_css_selector(fields)[i].text
                # print(text2)

                # if 'C001' and 'lubanqihao' and '鲁班 七号' and '区域: 陕西区域' and '城市: 陕西西安' and '手机: 13289356543' \
                #           and '电话:' and '邮箱: testqihao@163.com' not in text2:
                #     print("显示不正确！ 正确显示是：" + text2)
                try:
                    assert text2 not in list1[i]
                except AssertionError as msg:
                    print('选择用户后自动带出的表单右侧信息显示不正确！正确显示是：' + text2 + str(msg))
                    res = True
        # 角色
        queuevalue = TemplateUsePage(self.driver).queuevalue()
        #print(queuevalue)
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
        #print(subjectvalue)
        try:
            self.assertEqual(subjectvalue, str('主题'))
        except AssertionError as msg:
            print('工单主题显示不正确！正确显示是：' + str(msg))
            res = True

        # 内容
        # 文本
        # 鼠标点击一下文本内部
        self.driver.find_element_by_id("cke_1_contents").click()
        # 写入文字：先定位到div-iframe的xpath，然后再输入内容
        self.driver.switch_to.frame(
            self.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe'))
        actions = ActionChains(self.driver)
        actions.send_keys("文本必填").perform()

        # 切出执行其他操作
        self.driver.switch_to.default_content()

        # ---重新选择指定人和负责人
        TemplateUsePage(self.driver).owner('韦艳霞')
        TemplateUsePage(self.driver).responsible('卢志尧')
        # 填写主题
        self.driver.find_element_by_id('Subject').send_keys('TEST2')

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
            print('工单主题显示不正确！正确显示是：' +str(msg))
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
        self.driver.find_elements_by_css_selector('.ant-btn-primary')[1].click()
        time.sleep(3)

        # 等待工单详情部分更新后，需要增加详情的判断

        # 最后断言res的值
        assert res is None




# class TestBed(BaseCaseUser, Base):    # 徐敏

    # 1.
    def test_2_customerticketcreate(self):
        # 这里捕获了这里的异常，初始res为None
        res = None

        # EntranceAgentPage(self.driver).enter_templateuse()








