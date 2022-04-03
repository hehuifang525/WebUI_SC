"""
@author: DT_testing
@file:   user_search_case.py
@desc:  【界面元素检查】
@step： 001. 服务人员
        002. 客户用户管理
        003. 工作时间管理
        004. 邮件过滤器
        005.
        006.
"""
import sys
from common.base import Base
from common.OperationExcel import OperationExcel
from src.page.agent.district_page import DistrictPage
from src.page.agent.menuset_page import MenusetPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.agent_page import AgentPage
from src.page.agent.slacalender_page import SlacalenderPage
from src.page.agent.postmasterfilter_page import PostmasterFilter_Page
from src.page.agent.template_page import TemplatePage
from src.page.agent.role_page import RolePage
from src.page.agent.customer_user_page import CustomerUserPage
from src.page.agent.field_page import FieldPage
from src.page.agent.notification_page import NotificationPage
from src.page.agent.ticketgroup_page import TicketGroupPage
from src.page.agent.process_page import ProcessPage
from src.page.agent.generic_page import GenericPage
from src.page.agent.servicesla_page import ServiceSlaPage
from src.page.agent.fieldimpacts_page import FieldimpactsPage
from src.page.agent.faq_page import FaqPage
from src.page.agent.service_page import ServicePage
from src.page.agent.stats_page import StatsPage
from src.page.agent.statscombine_page import StatscombinePage
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.agent.agent_home_page import AgentHomePage
from src.page.agent.ticket_search_page import TicketSearchPage
from src.page.agent.mailmanagement_page import MmailmanagementPage
from src.page.agent.table_page import TablePage
from src.page.pagecommon.agent_common import AgentCommon
from src.page.pagecommon.menusetting_common import MenusetCommon
from src.page.pagecommon.role_common import RoleCommon
from src.page.pagecommon.tickettemplate_common import TicketTemplateCommon
from src.page.pagecommon.cmdb_overview_common import CmdbOverviewCommon
from src.page.pagecommon.notification_commom import NotificationCommon
from src.page.pagecommon.servicesla_common import ServiceSlaCommon
from src.page.pagecommon.faq_commom import FaqCommon
from src.page.pagecommon.stats_common import StatsCommon
import time
from selenium.webdriver.common.by import By




class check_element_whether_exists(BaseCaseUser, Base):

    # 服务人员模块
    def test_001(self):
        '''服务人员'''
        EntranceAgentPage(self.driver).enter_agent()
        # r'.\db\123.txt'
        userlist01 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '服务人员')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(userlist01,'默认页面')

        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 进入添加页面
        AgentPage(self.driver).addagent()
        time.sleep(3)
        # 1读取表格元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists(userlist01,'添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        # 输入必填值，点击下一步
        AgentCommon(self.driver).agentRequiredCommon2()
        AgentPage(self.driver).next01()
        time.sleep(3)
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists(userlist01,'添加下一步')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

        # 返回列表
        AgentPage(self.driver).returnlist2()
        time.sleep(3)

        # 导入页面
        AgentPage(self.driver).upload()
        time.sleep(3)
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists(userlist01,'导入页面')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)

        # 导出页面
        AgentPage(self.driver).Export()
        time.sleep(3)
        # userlist5 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '服务人员', '导出页面')
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists(userlist01,'导出页面')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)


    def test_002(self):
        '''客户用户管理'''
        EntranceAgentPage(self.driver).enter_customer_user()
        time.sleep(2)
        '''客户用户管理'''
        customeruserlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '客户用户管理')
        # EntranceAgentPage(self.driver).enter_customer_user()
        # time.sleep(2)
        # excel取值一次--默认页面
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        CustomerUserPage(self.driver).Searchresultcom2_click('默认客户')
        # 编辑客户
        CustomerUserPage(self.driver).EditCompany()
        # excel取值 --检查编辑客户页面
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '添加客户')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        # 提交
        CustomerUserPage(self.driver).Companysub()
        # excel取值 --检查关联信息页面
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '设置关联项')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

        # 关联信息页面元素  点击设置客户主管
        CustomerUserPage(self.driver).associate_manager()
        # excel取值--检查设置主管页
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '设置客户主管')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)

        # 返回关联项，点击关联服务
        CustomerUserPage(self.driver).ReturnAssocia_manager()
        CustomerUserPage(self.driver).associate_service()
        # excel取值 --检查关联服务
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '关联服务')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)

        # 返回列表
        CustomerUserPage(self.driver).server_back()
        # 设置客户主管按钮
        CustomerUserPage(self.driver).SetManager()
        time.sleep(2)
        # excel取值--检查从按钮入口进入的设置客户主管
        notexcitlist06,notexcitnum06= OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '设置客户主管')
        self.assertEqual(notexcitnum06, 0, notexcitlist06)
        # 返回列表
        CustomerUserPage(self.driver).manager_backlist()

        # 关联服务按钮
        CustomerUserPage(self.driver).AssociateService()
        # excel取值--检查从按钮入口进入的关联服务
        notexcitlist07,notexcitnum07= OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '关联服务')
        self.assertEqual(notexcitnum07, 0, notexcitlist07)

        # 返回列表
        time.sleep(1)
        CustomerUserPage(self.driver).server_back()
        # 导入导出按钮
        CustomerUserPage(self.driver).ImportExport()
        # 取excel --检查导入页面的值
        notexcitlist08,notexcitnum08= OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '导入页面')
        self.assertEqual(notexcitnum08, 0, notexcitlist08)

        # 点击导出
        CustomerUserPage(self.driver).Exportleft()
        # 取excel --检查导出页面的值
        notexcitlist09,notexcitnum09= OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '导出页面')
        self.assertEqual(notexcitnum09, 0, notexcitlist09)
        # 点击返回
        CustomerUserPage(self.driver).ImportExportback()

        # 添加用户按钮
        CustomerUserPage(self.driver).adduser()
        # 取excel --检查添加用户页面的值
        notexcitlist10,notexcitnum10= OperationExcel(self.driver).check_element_whether_exists (customeruserlist, '添加用户')
        self.assertEqual(notexcitnum10, 0, notexcitlist10)




    def test_003(self):
        '''工作时间管理'''
        EntranceAgentPage(self.driver).enter_slacalendar()
        time.sleep(2)
        userlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '工作时间管理')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(userlist1,'默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()

        # print(self.driver.current_url())
        # error_element = None
        # try:
        #     error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
        # except:
        #     pass
        #     # print('未出现请求出错报错')
        # self.assertIsNone(error_element, '错误，工作时间管理击后页面请求出错')

        # userlist2 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '工作时间管理', '添加页面')
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists(userlist1,'添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        # try:
        #     error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
        #     if len(error_element) > 0:
        #         print('error')
        # except:
        #     print('未出现请求出错报错')
    def test_004(self):
        '''邮件过滤器'''
        EntranceAgentPage(self.driver).enter_postmasterfilter()
        time.sleep(3)
        Postmasterlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '邮件过滤器')
        # 取excel 检查默认页面元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (Postmasterlist,'默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 点击添加
        PostmasterFilter_Page(self.driver).clickadd()
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "邮件过滤器点击添加请求出错")
        # 检查添加页面的元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (Postmasterlist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        # 返回列表
        PostmasterFilter_Page(self.driver).backlist()
        # 点击导入
        PostmasterFilter_Page(self.driver).clickImport()
        # 检查 url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "邮件过滤器点击导入请求出错")
        # 取excel 检查导入页面
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (Postmasterlist, '导入页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist03)

    def test_005(self):
        '''工单模板'''
        EntranceAgentPage(self.driver).enter_tickettemplate()
        time.sleep(3)
        userlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '工单模板')

        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (userlist, '默认页面')

        try:
            self.assertEqual(notexcitnum01, 0,notexcitlist01)
        except AssertionError as msg:
            print('工单模板默认页面不正确！' + str(msg))


        # 点击添加按钮
        TemplatePage(self.driver).addtemplate()
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "工单模板点击添加按钮后页面请求出错")

        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (userlist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        TemplatePage(self.driver).backlist()

        # 添加必填创建一个工单模板
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon3()
        time.sleep(3)
        # 搜索工单模板
        TemplatePage(self.driver).search(templateInfo.get('name'))
        # 取excel 检查操作按钮
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (userlist, '列表操作')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

        # 进入编辑页面，检查路径
        TemplatePage(self.driver).clicksearchresult()
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "工单模板进入编辑页面请求出错")
        # 取excel， 检查编辑页面
        time.sleep(5)
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (userlist, '编辑页面')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)

        # 返回列表
        TemplatePage(self.driver).backlist()
        TemplatePage(self.driver).search(templateInfo.get('name'))
        # 点击复制，判断是否报错
        time.sleep(3)
        TemplatePage(self.driver).clickcopy()
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "工单模板进入复制页面请求出错")

        # 取excel， 检查复制页面
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (userlist, '复制页面')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)

        # 返回列表
        TemplatePage(self.driver).backlist()
        time.sleep(3)
        # 点击导入
        TemplatePage(self.driver).importtem()
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "工单模板点击导入按钮后页面请求出错")

        notexcitlist06,notexcitnum06= OperationExcel(self.driver).check_element_whether_exists(userlist, '导入页面')
        self.assertEqual(notexcitnum06, 0, notexcitlist06)


    def test_006(self):
        '''工单通知'''
        notificationlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '工单通知')
        EntranceAgentPage(self.driver).enter_notificationevent()
        # 取excel检查页面默认元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(notificationlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加
        NotificationPage(self.driver).add()
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "工单通知点击添加按钮后页面请求出错")
        # 取excel2 检查添加页面元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (notificationlist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        # 提交遇到内容框无法输入，暂时屏蔽，后续修改
        # # 输入值，创建一个通知
        # Notificationinfo = NotificationCommon(self.driver).rquiredcommon()
        # # 点击提交
        # NotificationPage(self.driver).submit()
        # time.sleep(2)
        # # 搜索值
        # NotificationPage(self.driver).Search(Notificationinfo.get('name'))

        #点击返回
        NotificationPage(self.driver).backlist()

        # 取excel3 检查列表的操作按钮
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (notificationlist, '列表操作')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

        # 进入编辑页面
        NotificationPage(self.driver).searckresult()
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "工单通知进入编辑页面请求出错")
        # 取excel 检查编辑页面
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (notificationlist, '编辑页面')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)
        NotificationPage(self.driver).backlist()

        # 点击导入
        NotificationPage(self.driver).Import()
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "工单通知点击导入请求出错")
        # 取excel 检查导入页面
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (notificationlist, '导入页面')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)

    def test_007(self):
        '''字段库'''
        # 进入字段库
        # 进入初始页面，取excel判断页面元素
        EntranceAgentPage(self.driver).enter_filed()
        # time.sleep(3)
        filedlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '字段库')

        # 1 取excel，对进入的默认页面进行元素判断
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (filedlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加
        FieldPage(self.driver).add()
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "字段库点击添加按钮后页面请求出错")

        # 2 取excel，对下拉展开的 字段显示类型进行判断
        FieldPage(self.driver).fieldType()
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (filedlist, '字段类型下拉')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 选择文本
        FieldPage(self.driver).textType()
        # 点击系统对象
        FieldPage(self.driver).objectType()
        # 3 取excel，对下拉展开的 系统字段对象进行判断
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (filedlist, '系统字段对象下拉')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)
        # 选择工单
        FieldPage(self.driver).objectTicket()
        # 4 取excel，对工单-文本进行判断
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (filedlist, '工单-文本')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)

        # 切换多文本
        FieldPage(self.driver).TextArea()
        # 5 取excel，对工单-多文本进行判断
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (filedlist, '工单-多文本')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)

        # 切换复选框
        FieldPage(self.driver).Checkbox()
        # 点击点击值
        FieldPage(self.driver).addFieldBtn()
        # 6 取excel，对工单-复选框进行判断
        notexcitlist06,notexcitnum06= OperationExcel(self.driver).check_element_whether_exists (filedlist, '工单-复选框')
        self.assertEqual(notexcitnum06, 0, notexcitlist06)

        # 切换字段组
        FieldPage(self.driver).FieldGroup()
        # 7 取excel，对工单-字段组进行判断
        notexcitlist07,notexcitnum07= OperationExcel(self.driver).check_element_whether_exists (filedlist, '工单-字段组')
        self.assertEqual(notexcitnum07, 0, notexcitlist07)

        # 对象切换到配置项
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectITSM()
        # 8 取excel，对配置项-字段组进行判断
        notexcitlist08,notexcitnum08= OperationExcel(self.driver).check_element_whether_exists (filedlist, '配置项-字段组')
        self.assertEqual(notexcitnum08, 0, notexcitlist08)

        # 切换文本
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectITSM()
        # 9 取excel，对配置项-文本进行判断
        notexcitlist09,notexcitnum09= OperationExcel(self.driver).check_element_whether_exists (filedlist, '配置项-文本')
        self.assertEqual(notexcitnum09, 0, notexcitlist09)

        # 切换多文本
        FieldPage(self.driver).TextArea()
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectITSM()
        # 10 取excel，对配置项-多文本进行判断
        notexcitlist10,notexcitnum10= OperationExcel(self.driver).check_element_whether_exists (filedlist, '配置项-多文本')
        self.assertEqual(notexcitnum10, 0, notexcitlist10)
        # 切换复选框
        FieldPage(self.driver).Checkbox()
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectITSM()
        # 点击点击值
        # FieldPage(self.driver).addFieldBtn()
        # 11 取excel，对配置项-复选框进行判断
        notexcitlist11,notexcitnum11= OperationExcel(self.driver).check_element_whether_exists (filedlist, '配置项-复现框')
        self.assertEqual(notexcitnum11, 0, notexcitlist11)

        # 返回列表
        FieldPage(self.driver).returnList()
        # 点击导入导出
        FieldPage(self.driver).import_export()
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "字段库点击导入导出按钮后页面请求出错")
        # 12 取excel，判断导入页面
        notexcitlist12,notexcitnum12= OperationExcel(self.driver).check_element_whether_exists (filedlist, '导入页面')
        self.assertEqual(notexcitnum12, 0, notexcitlist12)

        # 点击导出
        FieldPage(self.driver).left_Export()
        # 13 取excel，判断导出页面
        notexcitlist13,notexcitnum13= OperationExcel(self.driver).check_element_whether_exists (filedlist, '导出页面')
        self.assertEqual(notexcitnum13, 0, notexcitlist13)


    def test_008(self):
        '''流程管理'''

        EntranceAgentPage(self.driver).enter_processmanagement()
        time.sleep(3)
        processlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '流程管理')

        # 检查默认页面
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (processlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击导入
        ProcessPage(self.driver).clickimport()
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "流程管理点击导入请求出错")
        # 取excel 检查导入页面
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (processlist, '导入页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist02)
        # 返回
        ProcessPage(self.driver).backlist()
        # 点击创建新的流程
        ProcessPage(self.driver).add()
        # 检查url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "流程管理打开新建流程页面请求出错")
        # 取excel 检查创建新的流程页面
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (processlist, '添加页面')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

        # 打开一个其他tab，以为cmdb概览为例
        EntranceAgentPage(self.driver).enter_cmdb_overview()
        # 关闭tab  close_edit_tab
        ProcessPage(self.driver).close_edit_tab()
        # 检查url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "其他tab切换到流程管理添加，页面提示权限不足")


    def test_009(self):
        '''9菜单权限管理'''
        EntranceAgentPage(self.driver).enter_menuset()
        time.sleep(3)
        rolemenulist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '9菜单权限管理')
        # 1 取excel 检查默认页面元素
        url0 = str(self.driver.current_url)
        self.assertEqual(url0.find('error'), -1, "进入菜单权限管理请求出错")
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (rolemenulist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮
        MenusetPage(self.driver).addmenu()
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "菜单权限点击添加按钮页面请求出错")
        # 2 取excel 检查添加页面
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (rolemenulist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 返回列表
        MenusetPage(self.driver).returnlist()
        time.sleep(4)

        # 搜索权限
        MenusetPage(self.driver).searchtab('系统超级权限')
        time.sleep(1)
        MenusetPage(self.driver).clicksearchresult()
        # 3 取excel 检查编辑页面
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "菜单权限进入编辑页面请求出错")
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (rolemenulist, '编辑页面')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)
        # 返回列表
        MenusetPage(self.driver).returnlist()

        # 切换到客户用户tab，检查页面
        MenusetPage(self.driver).clickcustomertab()
        time.sleep(1)
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "菜单权限切换到客户用户tab请求出错")

    def test_010(self):
        '''10角色'''
        # 进入角色管理，默认页面检查
        # 取excel--检查默认页面的元素
        userlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '10角色')

        EntranceAgentPage(self.driver).enter_role()
        time.sleep(3)
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (userlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加角色
        RolePage(self.driver).addrole()
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "角色点击添加按钮后页面请求出错")
        # 取excel --检查添加页面
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (userlist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 返回列表
        RolePage(self.driver).returnlist1()

        # 搜索系统默认角色--点击
        RolePage(self.driver).searchtab('系统默认角色')
        RolePage(self.driver).clicksearchresult()
        time.sleep(2)
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "角色点击搜索结果后页面请求出错")
        # 取excel --检查编辑页面
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (userlist, '添加页面')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

        # 点击下一步
        RolePage(self.driver).savenextbtn()
        time.sleep(2)
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "角色下一步后页面请求出错")

        # 取excel --检查角色关联项页面元素
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (userlist, '角色关联项')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)
        # 返回列表
        RolePage(self.driver).returnlist2()

        # 点击导入导出
        RolePage(self.driver).importexport()
        url4 = str(self.driver.current_url)
        self.assertEqual(url4.find('error'), -1, "角色点击导入导出按钮后页面请求出错")

        # 取excel元素--检查导入页面元素
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (userlist, '导入页面')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)

        # 切换到导出
        RolePage(self.driver).click_Export_left()
        # 取excel元素--检查导出页面元素
        notexcitlist06,notexcitnum06= OperationExcel(self.driver).check_element_whether_exists (userlist, '导出页面')
        self.assertEqual(notexcitnum06, 0, notexcitlist06)




    def test_011(self):
        '''11区域'''
        EntranceAgentPage(self.driver).enter_district()
        time.sleep(3)
        districtlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '11区域')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (districtlist,'默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮
        DistrictPage(self.driver).click_add()
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "区域点击添加按钮请求出错")

        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (districtlist, '添加页面')
        self.assertEqual(notexcitnum02, 0,  notexcitlist02)
        # 返回列表
        DistrictPage(self.driver).backlist()
        time.sleep(2)
        # 点击导入导出
        DistrictPage(self.driver).import_export()
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "区域点击导入导出按钮请求出错")
        # 取excel 检查导入
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (districtlist, '导入页面')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)
        # 点击导出
        DistrictPage(self.driver).left_export()
        # 取excel 检查导出
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (districtlist, '导出页面')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)

    def test_012(self):
        '''12cmdb概览'''
        EntranceAgentPage(self.driver).enter_cmdb_overview()
        time.sleep(3)
        cmdb1list = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls','12cmdb概览')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (cmdb1list, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 创建一个资产
        CmdbOverviewCommon(self.driver).CmdbOverview_requestCommon2()
        # 检查创建后返回列表页
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (cmdb1list, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist02)

    def test_013(self):
        '''13cmdb配置'''
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        time.sleep(3)
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "进入cmdb配置页面请求出错")

        cmdb2list = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '13cmdb配置')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (cmdb2list, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮
        self.driver.find_element_by_id('fieldCreateButton').click()
        time.sleep(3)
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "cmdb点击添加按钮页面请求出错")

        # 取excel值，检查填写类的基本信息
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (cmdb2list, '填写类的基本信息')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

    # 工单分组页面元素发生变化，屏幕该用例21-05-13
    def test_014(self):
        '''14工单分组'''
        EntranceAgentPage(self.driver).enter_ticketgroup()
        time.sleep(3)
        ticketgrouplist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '14工单分组')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (ticketgrouplist, '列表页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮
        TicketGroupPage(self.driver).add()
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "工单分组点击添加按钮页面请求出错")
        # 取excel 2 检查添加页面
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (ticketgrouplist, '分组基本信息')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 名称输入值
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "group" + strnumber
        TicketGroupPage(self.driver).send_name(name)
        # 点击下一步
        TicketGroupPage(self.driver).nextstep()
        # 校验筛选页
        notexcitlist02_1, notexcitnum02_1 = OperationExcel(self.driver).check_element_whether_exists(ticketgrouplist,
                                                                                                 '分组筛选信息')
        self.assertEqual(notexcitnum02_1, 0, notexcitlist02_1)
        # 点击下一步
        TicketGroupPage(self.driver).nextstep()
        # 校验标签配置页
        notexcitlist02_2, notexcitnum02_2 = OperationExcel(self.driver).check_element_whether_exists(ticketgrouplist,
                                                                                                 '配置标签')
        self.assertEqual(notexcitnum02_2, 0, notexcitlist02_2)
        # 点击返回列表
        TicketGroupPage(self.driver).backlist()
        time.sleep(2)

        # # 搜索默认数据
        # TicketGroupPage(self.driver).search('系统默认分组')
        # 点击进入编辑页面 --随意点击一个分组
        TicketGroupPage(self.driver).search_result()
        # 判断url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "工单分组进入编辑页面请求出错")
        # 取excel 3 检查编辑页面
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (ticketgrouplist, '编辑页面')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)
        # 点击返回列表
        TicketGroupPage(self.driver).backlist()
        time.sleep(2)

        # 点击导入
        TicketGroupPage(self.driver).clickimport()
        # 判断url
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "工单分组进入导入页面请求出错")
        # 取excel 4 检查导入页面
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (ticketgrouplist, '导入页面')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)

    def test_015(self):
        '''15自动任务列表'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(2)
        genericlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '15自动任务列表')

        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (genericlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 点击添加
        GenericPage(self.driver).add()
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "自动任务点击添加按钮页面报错")
        # 取excel 检查添加页面
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (genericlist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 添加必填提交
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "自动任务必填" + strnumber
        GenericPage(self.driver).inputname(name)
        GenericPage(self.driver).sumbit()

        # 搜索
        GenericPage(self.driver).search(name)
        # # 取excel 检查列表操作
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (genericlist, '列表操作')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

        # 点击进入编辑页面
        GenericPage(self.driver).search_result()
        # 检查url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "自动任务进入编辑页面，页面报错")
        # 取excel 检查编辑页面
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (genericlist, '编辑页面')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)

        # 返回
        GenericPage(self.driver).backlist()
        # 搜索 点击复制
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).copy()
        # 检查url
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "自动任务点击复制按钮页面报错")
        # 取excel 检查复制页面
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (genericlist, '编辑页面')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)

        # 返回
        GenericPage(self.driver).backlist()
        time.sleep(1)
        # 点击导入
        GenericPage(self.driver).clickimport()
        # 检查url
        url4 = str(self.driver.current_url)
        self.assertEqual(url4.find('error'), -1, "自动任务点击导入按钮页面报错")
        # 取excel 检查导入页面
        notexcitlist06,notexcitnum06= OperationExcel(self.driver).check_element_whether_exists (genericlist, '导入页面')
        self.assertEqual(notexcitnum06, 0, notexcitlist06)

        # # 返回列表
        # GenericPage(self.driver).importback()
        # # 搜索 点击运行
        # GenericPage(self.driver).search(name)
        # GenericPage(self.driver).runclick()
        # # 检查url
        # url5 = str(self.driver.current_url)
        # self.assertEqual(url5.find('error'), -1, "自动任务点击运行按钮页面报错")
        # # 取excel 检查导入页面
        # notexcitlist07,notexcitnum07= OperationExcel(self.driver).check_element_whether_exists(genericlist, '运行页面')
        # self.assertEqual(notexcitnum07, 0, notexcitlist07)

    # 打开三个图标失败，待修改
    def test_016(self):
        '''16主页'''
        EntranceAgentPage(self.driver).enter_home()
        time.sleep(3)
        homelist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '16主页')
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "进入主页页面报错")
        # 检查主页元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (homelist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # # 检查右侧设置按钮点开  AgentHomePage
        # AgentHomePage(self.driver).set_ico()
        # # 保存右侧设置
        # AgentHomePage(self.driver).sumbit_set()
        # time.sleep(6)
        # # 点击-未关闭的工单
        # AgentHomePage(self.driver).open_ticket()
        # time.sleep(5)
        # # 检查url
        # url2 = str(self.driver.current_url)
        # self.assertEqual(url2.find('error'), -1, "进入主页未关闭的工单页面报错")
        # # 取当前tab名称断言检查  active_tab
        # active_tab = AgentHomePage(self.driver).active_tab()
        # self.assertEqual(active_tab, '工单视图 - 未关闭的工单', msg='主页打开未关闭工单视图失败')
        # # 返回主页
        # AgentHomePage(self.driver).home()
        # # 检查-我参与的工单
        # AgentHomePage(self.driver).participate_ticket()
        # # 检查url
        # url3 = str(self.driver.current_url)
        # self.assertEqual(url3.find('error'), -1, "进入主页我参与的工单页面报错")
        # # 取当前tab名称断言检查
        # active_tab = AgentHomePage(self.driver).active_tab()
        # self.assertEqual(active_tab, '工单视图 - 我参与的工单', msg='主页打开我参与的工单视图失败')
        # # 返回主页
        # AgentHomePage(self.driver).home()
        # # 检查升级工单
        # AgentHomePage(self.driver).upgrade_ticket()
        # # 检查url
        # url4 = str(self.driver.current_url)
        # self.assertEqual(url4.find('error'), -1, "进入主页升级工单页面报错")
        # # 去当前tab名称断言检查
        # active_tab = AgentHomePage(self.driver).active_tab()
        # self.assertEqual(active_tab, '工单视图 - 升级工单', msg='主页打开升级工单视图失败')

    def test_017(self):
        '''17会话'''
        EntranceAgentPage(self.driver).enter_session()
        time.sleep(3)
        sessionlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '17会话')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(sessionlist1,"默认页面")
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

    def test_018(self):
        '''18知识库类别管理'''
        faqlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '18知识库类别管理')
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "知识库管理进入页面报错")
        # 检查默认页面元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (faqlist1, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 点击添加按钮
        FaqPage(self.driver).add()
        # 检查url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "知识库管理点击添加按钮报错")
        # 检查页面元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (faqlist1, '类别基本信息')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 填写必填
        faqinfo = FaqCommon(self.driver).Faqrequiredcommon()
        # 点击提交并返回按钮
        FaqPage(self.driver).submitreturn()
        time.sleep(6)
        # 搜索添加的数据
        FaqPage(self.driver).right_search(faqinfo.get('name'))
        # 删除
        FaqPage(self.driver).detele()
        FaqPage(self.driver).comfire_delete()
        time.sleep(5)
        # 删除后检查
        FaqPage(self.driver).right_search(faqinfo.get('name'))
        emptytext = FaqPage(self.driver).getempty()
        self.assertEqual(emptytext, '这里空空如也, 跟我的钱包一样', msg='删除知识库类别失败')

    def test_019(self):
        '''19邮箱'''
        maillist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '19邮箱')
        EntranceAgentPage(self.driver).enter_mailmanagement()
        time.sleep(3)
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "邮箱进入页面报错")

        # 点击添加发件服务器
        MmailmanagementPage(self.driver).add_SendHost()
        # 检查url2
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "点击添加发件服务器页面报错")
        MmailmanagementPage(self.driver).open_second_tab()

        # 检查元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (maillist, '发件服务器地址-添加')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 返回列表
        MmailmanagementPage(self.driver).backlist1()

        # 点击添加发件邮箱管理
        MmailmanagementPage(self.driver).add_Sendmail()
        time.sleep(1)

        # 检查url3
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "点击添加发件邮箱页面报错")
        # 检查元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (maillist, '发件邮件管理-添加')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 返回列表
        MmailmanagementPage(self.driver).backlist2()

        # 点击添加收件服务器
        MmailmanagementPage(self.driver).add_ReceiveHost()
        time.sleep(1)
        # 检查url4
        url4 = str(self.driver.current_url)
        self.assertEqual(url4.find('error'), -1, "点击添加收件服务器页面报错")
        MmailmanagementPage(self.driver).open_second_tab()
        time.sleep(2)
        MmailmanagementPage(self.driver).check_backlist1()
        # 检查元素
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (maillist, '收件服务器地址-添加')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

    def test_020(self):
        '''20工单搜索'''
        EntranceAgentPage(self.driver).enter_search()
        time.sleep(3)
        searchlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '20工单搜索')
        # 检查url1
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "进入工单搜索页面报错")
        time.sleep(2)

        # 检查默认页面元素 1
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (searchlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 点击添加模板按钮
        TicketSearchPage(self.driver).addtemp()
        time.sleep(2)
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (searchlist, '模板添加')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 输入模板名称
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        tempname = "搜索模板" + strnumber
        TicketSearchPage(self.driver).tempname(tempname)
        # 输入全文搜索条件
        TicketSearchPage(self.driver).fulltext('测试')
        # 点击保存模板
        TicketSearchPage(self.driver).savetemp()
        time.sleep(2)
        # 点击搜索
        TicketSearchPage(self.driver).search()

        # 使用模板搜索
        TicketSearchPage(self.driver).search_temp(tempname)
        TicketSearchPage(self.driver).search()
        # 检查url 2
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "工单搜索使用模板搜索页面报错")
        # 导航使用模板搜索
        # TicketSearchPage(self.driver).bar_temp_search(tempname)
        # # 检查url
        # url3 = str(self.driver.current_url)
        # self.assertEqual(url3.find('error'), -1, "工单搜索使用模板搜索页面报错")

        # 20211221导航元素变更，不可用，后续稳定再修改
        # # 导航搜索工单
        # TicketSearchPage(self.driver).bar_search_input('测试')
        # # TicketSearchPage(self.driver).search_ticket()
        # # 检查url
        # url4 = str(self.driver.current_url)
        # self.assertEqual(url4.find('error'), -1, "从导航栏搜索工单报错")
        #
        # # 导航搜索知识库
        # TicketSearchPage(self.driver).bar_search_input('测试')
        # TicketSearchPage(self.driver).search_faq()
        # # 检查url
        # url5 = str(self.driver.current_url)
        # self.assertEqual(url5.find('error'), -1, "从导航栏搜索知识库报错")

    # def test_021(self):
    #     '''21工单详情'''
    #     URL = sys.argv[1] + "/user/ticket/detail/1"
    #     self.driver.get(URL)
    #     time.sleep(3)
    #     zoomlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '21工单详情',
    #                                                         '默认页面')
    #     notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(zoomlist1)
    #     self.assertEqual(notexcitnum01, 0, notexcitlist01)

    # 2022-01-26 删除按钮定位不到搜索后的指定元素，删除失败影响下一次操作--未修改
    def test_022(self):
        '''22字段影响关系'''
        EntranceAgentPage(self.driver).enter_fieldimpact()
        time.sleep(2)

        fieldimpactlist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '22字段影响关系')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (fieldimpactlist, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 点击添加
        FieldimpactsPage(self.driver).add()
        time.sleep(1)
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "字段影响关系点击添加按钮页面报错")

        # 输入名称
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "字段影响关系必填" + strnumber
        FieldimpactsPage(self.driver).inputname(name)
        # 选择工单对象
        FieldimpactsPage(self.driver).obejctclick()
        FieldimpactsPage(self.driver).choose_tikect("工单")

        # 检查添加页面元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (fieldimpactlist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        # 点击选择字段
        FieldimpactsPage(self.driver).field_search('工单流转状态')
        # 选择一个字段
        FieldimpactsPage(self.driver).choose_field()
        # 选择流转状态的值
        FieldimpactsPage(self.driver).choose_FlowStats_all()
        # 点击添加
        FieldimpactsPage(self.driver).addfield()
        time.sleep(1)  # 添加后页面需要有刷新的动作，增加等待
        # 点击提交并返回列表
        FieldimpactsPage(self.driver).sumbit_return()
        time.sleep(1)

        # 取excel 检查列表元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (fieldimpactlist, '列表')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 20211223屏蔽进入编辑页面
        # # 搜索进入编辑页面
        # FieldimpactsPage(self.driver).search(name)
        # TablePage(self.driver).search_result()
        # # 检查url
        # url2 = str(self.driver.current_url)
        # self.assertEqual(url2.find('error'), -1, "字段影响关系进入编辑页面报错")
        # # 取excel 检查编辑页面
        # notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (fieldimpactlist, '编辑页面')
        # self.assertEqual(notexcitnum02, 0, notexcitlist03)
        # # 返回列表
        # FieldimpactsPage(self.driver).backlist()
        # time.sleep(2)
        # 删除关系，不影响下一次自动化
        FieldimpactsPage(self.driver).search(name)
        time.sleep(2)
        FieldimpactsPage(self.driver).detele()
        time.sleep(20)
        FieldimpactsPage(self.driver).detele_comfirm()

    def test_023(self):
        '''23知识库概览'''
        EntranceAgentPage(self.driver).enter_faq_overview()
        time.sleep(3)
        faqoverviewlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '23知识库概览')

        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "进入知识库概览页面报错")

        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (faqoverviewlist1, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮
        self.driver.find_element_by_css_selector('.ant-skeleton-active button ').click()
        # 检查ur2
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "知识库概览页面点击添加按钮页面报错")

        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (faqoverviewlist1, '新建知识库文章')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

    def test_024(self):
        '''24服务'''
        EntranceAgentPage(self.driver).enter_service()
        time.sleep(3)
        servicelist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '24服务')
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "服务进入页面报错")

        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (servicelist1, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 点击添加按钮
        ServicePage(self.driver).add()
        # 检查url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "服务添加按钮页面报错")
        # 检查添加页面元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (servicelist1, '服务基本信息')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "服务必填" + strnumber
        # 填写必填添加服务
        ServicePage(self.driver).inputname(name)
        # 下一步
        ServicePage(self.driver).next()

        # 检查下一步元素
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (servicelist1, '服务关联项')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)
        # 点击完成
        ServicePage(self.driver).complete()
        time.sleep(3)

        # 搜索后进入服务
        ServicePage(self.driver).right_search(name)
        time.sleep(2)
        # 进入编辑页面
        ServicePage(self.driver).search_result()
        # 检查url页面
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "服务进入编辑页面报错")
        time.sleep(8)
        # 点击返回列表
        ServicePage(self.driver).goBack1()
        time.sleep(4)

        # 点击导入/导出
        ServicePage(self.driver).ImportExport()
        # 检查url
        url4 = str(self.driver.current_url)
        self.assertEqual(url4.find('error'), -1, "服务进入导入导出页面报错")
        # 检查导入的元素
        notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (servicelist1, '导入页面')
        self.assertEqual(notexcitnum04, 0, notexcitlist04)
        # 点击导出
        ServicePage(self.driver).click_Export_left()
        # 检查导出页面元素
        notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (servicelist1, '导出页面')
        self.assertEqual(notexcitnum05, 0, notexcitlist05)

    # 20210220 协议创建需要必填工作时间，暂时屏蔽
    def test_026(self):
        '''26服务水平协议'''
        EntranceAgentPage(self.driver).enter_sla()

        time.sleep(3)
        slalist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '26服务水平协议')
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "服务水平协议进入页面报错")
        # 检查列表页面元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (slalist1, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)
        # 点击添加按钮
        ServiceSlaPage(self.driver).clickaddsla()
        time.sleep(1)

        # 检查url2
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "服务水平协议点击添加按钮页面报错")
        # 填写必填
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon3()
        # 点击下一步
        ServiceSlaPage(self.driver).clickslanext()
        # 点击指标度量管理
        ServiceSlaPage(self.driver).clicktarget()
        # 必须添加强制等待
        time.sleep(2)
        # 点击添加指标
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(2)

        # 检查指标度量管理-添加页面元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (slalist1, '指标度量管理-添加')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
        # 填写必填添加指标
        targetinfo = ServiceSlaCommon(self.driver).targetrequiredcommon()
        ServiceSlaPage(self.driver).clicksubmittar()
        # 关闭弹窗
        ServiceSlaPage(self.driver).closetar()
        # 点击创建指标
        ServiceSlaPage(self.driver).clicknewtarget()
        # 在下拉框中选择刚添加的指标

        ServiceSlaPage(self.driver).chosetargetname(targetinfo.get('name'))
        ServiceSlaPage(self.driver).inputtime('10')
        time.sleep(3)
        # 检查-设置指标信息-页面元素检查
        notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (slalist1, '设置指标信息')
        self.assertEqual(notexcitnum03, 0, notexcitlist03)

    # 20210220不稳定，暂时屏蔽；2021-12-23只验证简单元素，前置条件太多
    def test_027(self):
        '''27统计管理'''

    #
    #     # 创建一个服务人员
    #     # EntranceAgentPage(self.driver).enter_agent()
    #     userInfo=AgentCommon(self.driver).agentRequiredCommon3()
    #
    #     # 创建一个菜单--授权系统管理菜单
    #     menuname = MenusetCommon(self.driver).menurequiredcommon2()
    #     # MenusetPage(self.driver).searchtab(name)
    #     MenusetPage(self.driver).chosePermissionjc(3)
    #     MenusetPage(self.driver).submit()
    #
    #     # 创建一个角色--同时授权菜单、服务人员
    #     rolename = RoleCommon(self.driver).rolerequiredcommon()
    #     RolePage(self.driver).savenextbtn()
    #
    #     # 添加服务人员
    #     RolePage(self.driver).clickagent(userInfo.get('fullname'))
    #     RolePage(self.driver).clickallbtn()
    #     RolePage(self.driver).clickclosebtn()
    #     # 添加管理者
    #     RolePage(self.driver).clickmanager(userInfo.get('fullname'))
    #     RolePage(self.driver).clickallbtn()
    #     RolePage(self.driver).clickclosebtn()
    #     RolePage(self.driver).serach_choosetree(menuname)
    #     time.sleep(2)
    #
    #     # 完成
    #     RolePage(self.driver).savebtn()
    #     time.sleep(2)
    #
    #     # 退出当前系统，使用新创建的服务人员登录系统
    #     AgentLoginPage(self.driver).logout_button()
    #     AgentLoginPage(self.driver).input_username(userInfo.get('userlogin'))
    #     AgentLoginPage(self.driver).input_passwd('123456')
    #     AgentLoginPage(self.driver).login_button()
    #
    #     # 进入统计管理页面
    #     time.sleep(6)
        EntranceAgentPage(self.driver).enter_stats()
        time.sleep(2)
        # EntranceAgentPage(self.driver).enter_relust('统计管理')
        # time.sleep(5)
        slalist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '27统计管理')
        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "进入统计管理页面报错")
        # 检查添加页面元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (slalist1, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮  StatsPage
        StatsPage(self.driver).addstats()
        # 检查url
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "统计管理点击添加按钮页面报错")
        # 检查添加页面元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (slalist1, '添加页面-一般设定')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)
    #     # 添加一个统计，填写必填，点击提交并返回列表
    #     Statsinfo = StatsCommon(self.driver).statsrequiredcommon('动态列表', rolename, 'Excel')
    #     StatsPage(self.driver).submitlist()
    #     time.sleep(8)
    #     #检查列表，搜索进入编辑页面
    #     StatsPage(self.driver).search(Statsinfo.get('name'))
    #
    #     # StatsPage(self.driver).search('name202012022117')
    #     # 点击搜索结果
    #     StatsPage(self.driver).search_result()
    #     time.sleep(1)
    #
    #     # 检查url
    #     url3 = str(self.driver.current_url)
    #     self.assertEqual(url3.find('error'), -1, "统计管理进入编辑页面报错")
    #
    #     # 检查矩阵编辑页面-x轴
    #     notexcitlist03,notexcitnum03 = OperationExcel(self.driver).check_element_whether_exists (slalist1, '列表-统计预览')
    #     self.assertEqual(notexcitnum03, 0, notexcitlist03)
    #     time.sleep(3)
    #
    #
    #
    #     # 1202 未实现x轴选择数据
    #     # 滑动到页面底部
    #     # Base(self.driver).move_to_pagebottom()
    #     # # 点击x轴
    #     # StatsPage(self.driver).clickx()
    #     # # 选择类型字段  chosex_printfield
    #     # StatsPage(self.driver).chosex_printfield('类型')
    #     # # StatsPage(self.driver).chosex_field('类型')
    #     # # 选择类型字段的所有值
    #     # # StatsPage(self.driver).chosex_field_value()
    #     # # 点击保存
    #     # StatsPage(self.driver).closeSumit()
    #     # time.sleep(5)
    #     # # 点击提交并完成
    #     # StatsPage(self.driver).submitlist()
    #
    #     # backlist 返回列表
    #     StatsPage(self.driver).backlist()
    #     # 点击导出按钮
    #     StatsPage(self.driver).listexport()
    #     time.sleep(1)
    #     # 检查url
    #     url3 = str(self.driver.current_url)
    #     self.assertEqual(url3.find('error'), -1, "统计管理单击导出页面报错")
    #     # # 点击运行按钮
    #     # StatsPage(self.driver).listrun()
    #     # # 检查url 4
    #     # url4 = str(self.driver.current_url)
    #     # self.assertEqual(url4.find('error'), -1, "统计管理单击列表运行页面报错")
    #     #
    #     # # 检查运行页面元素
    #     # notexcitlist04,notexcitnum04 = OperationExcel(self.driver).check_element_whether_exists (slalist1, '运行')
    #     # self.assertEqual(notexcitnum04, 0, notexcitlist04)
    #     # 没有设置x轴数据，立即运行页面loading报错
    #     # # 点击立即运行
    #     # StatsPage(self.driver).run_immediately()
    #     # # 检查url 5
    #     # url5 = str(self.driver.current_url)
    #     # self.assertEqual(url5.find('error'), -1, "统计管理点击立即运行页面报错")
    #     # time.sleep(10)
    #     #
    #     # # 检查立即运行页面元素 5
    #     # notexcitlist05,notexcitnum05= OperationExcel(self.driver).check_element_whether_exists (slalist1, '立即运行')
    #     # self.assertEqual(notexcitnum05, 0, notexcitlist05)
    #     # # 关闭立即运行页面
    #     # StatsPage(self.driver).closerun()
    #     #
    #     # # 返回列表
    #     # StatsPage(self.driver).run_backlist()
    #     # time.sleep(2)
    #     # 搜索删除统计管理
    #     StatsPage(self.driver).search(Statsinfo.get('name'))
    #     # StatsPage(self.driver).search('name202012022117')
    #     # 点击删除
    #     StatsPage(self.driver).delete()
    #     time.sleep(1)
    #     # 检查url 6
    #     url6 = str(self.driver.current_url)
    #     self.assertEqual(url6.find('error'), -1, "统计管理点击删除页面报错")
    #     StatsPage(self.driver).detele_comfirm()
    #     time.sleep(1)
    #     StatsPage(self.driver).search(Statsinfo.get('name'))
    #     # StatsPage(self.driver).search('name202012022117')
    #     time.sleep(3)
    #     # 检查搜索后的结果
    #     tabtext = StatsPage(self.driver).get_total()
    #     self.assertEqual(tabtext, '有效 ( 0 )', msg='删除统计管理失败')



    def test_028(self):
        '''28统计组合管理'''
        statscombinelist = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '28统计组合管理')
        EntranceAgentPage(self.driver).enter_statscombine()
        time.sleep(3)
        # 检查url1
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "进入统计组合页面报错")
        # 检查默认页面元素
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (statscombinelist,'默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加
        StatscombinePage(self.driver).addstatscombine()
        # 检查url2
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "统计组合点击添加按钮页面报错")
        # 检查添加页面元素
        notexcitlist02,notexcitnum02 = OperationExcel(self.driver).check_element_whether_exists (statscombinelist, '添加页面')
        self.assertEqual(notexcitnum02, 0, notexcitlist02)

        # 填写必填，提交
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        StatscombinePage(self.driver).inputname(name)
        StatscombinePage(self.driver).submit()
        # 搜索进入编辑页面
        StatscombinePage(self.driver).search(name)
        StatscombinePage(self.driver).search_result()
        # 检查url3
        url3 = str(self.driver.current_url)
        self.assertEqual(url3.find('error'), -1, "统计组合点击进入编辑页面报错")

    def test_029(self):
        '''29内容模板'''
        EntranceAgentPage(self.driver).enter_contenttemplate()
        time.sleep(3)
        faqoverviewlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '29内容模板')

        # 检查url
        url1 = str(self.driver.current_url)
        self.assertEqual(url1.find('error'), -1, "进入内容模板页面报错")

        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (faqoverviewlist1, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加按钮
        self.driver.find_element_by_css_selector('.btn-cont button:nth-child(1)').click()
        # 检查ur2
        url2 = str(self.driver.current_url)
        self.assertEqual(url2.find('error'), -1, "内容模板点击添加按钮页面报错")

        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (faqoverviewlist1, '添加页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

    # def test_030(self):
    #     '''30管理员通知'''
    #     EntranceAgentPage(self.driver).enter_messagecool()
    #     time.sleep(3)
    #     messagelist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '30管理员通知')
    #     notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (messagelist1,'默认页面')
    #     self.assertEqual(notexcitnum01, 0, notexcitlist01)



    def test_031(self):
        '''工作台'''
        EntranceAgentPage(self.driver).enter_workbench()
        time.sleep(3)
        messagelist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '34工作台')
        notexcitlist01,notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists (messagelist1,'默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加
        self.driver.find_element(By.CSS_SELECTOR, '.tab-setting-btn.cursor').click()
        self.driver.find_element(By.CSS_SELECTOR, '.tab-setting-menu button.sp-btn-md').click()
        notexcitlist02, notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(messagelist1, '添加页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist02)
        # 关闭弹窗
        elem = self.driver.find_elements(By.CSS_SELECTOR, 'button.ant-drawer-close')
        elem[1].click()
        self.driver.find_element(By.CSS_SELECTOR, 'button.ant-drawer-close').click()

    def test_032(self):
        '''工作台管理'''
        EntranceAgentPage(self.driver).enter_workbenchmanage()
        time.sleep(3)
        messagelist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '33作台管理')
        notexcitlist01, notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(messagelist1, '默认页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist01)

        # 点击添加
        self.driver.find_element(By.CSS_SELECTOR, '[class="btns-div btn-md ant-btn ant-btn-primary"]').click()
        notexcitlist02, notexcitnum01 = OperationExcel(self.driver).check_element_whether_exists(messagelist1, '添加页面')
        self.assertEqual(notexcitnum01, 0, notexcitlist02)
        # 关闭弹窗
        self.driver.find_element(By.CSS_SELECTOR, 'button.ant-drawer-close').click()

    def test_33(self):
        """
            标签管理
        """
        EntranceAgentPage(self.driver).entre_tagmanagement()
        taglist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '35标签管理')
        non_existent_list_tag01, non_existent_num_tag = OperationExcel(self.driver).check_element_whether_exists(taglist1,
                                                                                                               '默认页面')
        try:
            self.assertEqual(non_existent_num_tag, 0, non_existent_list_tag01)
        except AssertionError as msg:
            print('标签管理默认页面打开元素出错！' + str(msg))

        # 点击添加按钮
        self.driver.find_element(By.ID, 'NewlyAdded').click()

        non_existent_list_tag, non_existent_num_tag = OperationExcel(self.driver).check_element_whether_exists(taglist1,
                                                                                                               '添加页面')
        try:
            self.assertEqual(non_existent_num_tag, 0, non_existent_list_tag)
        except AssertionError as msg:
            print('标签管理添加页面打开错误！' + str(msg))

    def test_34(self):
        """
            标签规则管理
        """
        # ---------------35标签规则管理-------------------------
        EntranceAgentPage(self.driver).enter_tagmanagement_rule()
        taglist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '36标签规则管理')
        non_existent_list_tag01, non_existent_num_tag = OperationExcel(self.driver).check_element_whether_exists(
            taglist1,
            '默认页面')
        self.assertEqual(non_existent_num_tag, 0, non_existent_list_tag01)


        # 点击添加按钮
        self.driver.find_element(By.ID, 'NewlyAdded').click()
        non_existent_list_tagrule, non_existent_num_tagrule = OperationExcel(self.driver).check_element_whether_exists(
            taglist1,
            '添加页面')
        try:
            self.assertEqual(non_existent_num_tagrule, 0, non_existent_list_tagrule)
        except AssertionError as msg:
            print('标签规则管理添加页面打开错误！' + str(msg))

    def test_035_other(self):
        """
            屏蔽入口校验，其他入口统一这里写，取文件数据check_elements
        """
        res = None
        model_num = 0
        # -------------test01 偏好设置---------------------------------------------------------
        EntranceAgentPage(self.driver).enter_preferences()
        userlist = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '33偏好设置')
        # 检查列表页面是否正常进入
        non_existent_list, non_existent_num = OperationExcel(self.driver).check_element_whether_exists(userlist, '修改密码')
        try:
            self.assertEqual(non_existent_num, 0, non_existent_list)
        except AssertionError as msg:
            print('偏好设置打开错误！' + str(msg))
            res = True
            model_num = model_num + 1

        # ---------------36到期提醒管理-------------------------
        EntranceAgentPage(self.driver).entre_serviceremind()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入到期提醒管理页面报错")
        except AssertionError as msg:
            print('进入到期提醒管理不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        self.driver.find_element(By.CSS_SELECTOR, '.btns-div.btn-md').click()

        serviceremind = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '36到期提醒管理')
        non_existent_list_tagrule, non_existent_num_tagrule = OperationExcel(
            self.driver).check_element_whether_exists(
            serviceremind, '批量操作页面')
        try:
            self.assertEqual(non_existent_num_tagrule, 0, non_existent_list_tagrule)
        except AssertionError as msg:
            print('标签规则管理添加页面打开错误！' + str(msg))
            res = True
            model_num = model_num + 1

        # 小程序配置管理
        EntranceAgentPage(self.driver).entre_wechat_config()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入小程序配置管理页面报错")
        except AssertionError as msg:
            print('进入小程序配置管理不正确！' + str(msg))
            res = True

        # ----------------------------sql屏幕查询--------------
        EntranceAgentPage(self.driver).enter_selectbox()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入sql屏幕查询页面报错")
        except AssertionError as msg:
            print('进入sql屏幕查询不正确！' + str(msg))
            res = True

        # ----------------------------kpi---------------------
        # 获取当前窗口句柄

        current_window = self.driver.current_window_handle
        EntranceAgentPage(self.driver).enter_kpi()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入kpi页面报错")
        except AssertionError as msg:
            print('进入kpi页面报错！' + str(msg))
            res = True

        # 切换窗口
        self.driver.switch_to.window(current_window)
        time.sleep(3)

        # ---------------------------通信日志-----------------------
        EntranceAgentPage(self.driver).enter_communicationlog()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入通信日志页面报错")
        except AssertionError as msg:
            print('进入通信日志不正确！' + str(msg))
            res = True

        # -----------------------------系统日志-------------------------
        EntranceAgentPage(self.driver).enter_systemlog()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入系统日志页面报错")
        except AssertionError as msg:
            print('进入系统日志不正确！' + str(msg))
            res = True

        # --------------------------------公共参数设置--------------------
        EntranceAgentPage(self.driver).enter_workbenchmanage()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入公共参数设置页面报错")
        except AssertionError as msg:
            print('进入公共参数设置页面不正确！' + str(msg))
            res = True

        # -------------------------'''16主页'''------------------
        EntranceAgentPage(self.driver).enter_home()
        time.sleep(3)
        homelist = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '16主页')
        non_existent_list01, non_existent_num01 = OperationExcel(self.driver).check_element_whether_exists(homelist,
                                                                                                           '默认页面')
        try:
            self.assertEqual(non_existent_num01, 0, non_existent_list01)
        except AssertionError as msg:
            print('主页打开错误！' + str(msg))
            res = True
            model_num = model_num + 1

        # ------------------------'''17会话'''（默认）-------------------
        EntranceAgentPage(self.driver).enter_session()
        time.sleep(3)
        sessionlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '17会话')
        non_existent_list0117, non_existent_num0117 = OperationExcel(self.driver).check_element_whether_exists(
            sessionlist1, '默认页面')
        try:
            self.assertEqual(non_existent_num0117, 0, non_existent_list0117)
        except AssertionError as msg:
            print('17会话页面打开报错！' + str(msg))
            res = True
            model_num = model_num + 1

        # --------------'''30管理员通知'''（测试系统无此模块）--------------
        EntranceAgentPage(self.driver).enter_messagecool()
        time.sleep(3)
        messagelist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '30管理员通知')
        non_existent_list0130, messagenumber = OperationExcel(self.driver).check_element_whether_exists(messagelist1,
                                                                                                        '默认页面')

        try:
            self.assertEqual(messagenumber, 0, non_existent_list0130)
        except AssertionError as msg:
            print('30管理员通知默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # --------------'''32软件包管理'''-------------------
        EntranceAgentPage(self.driver).enter_packagemanager()
        time.sleep(3)
        packagelist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '32软件包管理')
        non_existent_list032, non_existent_num032 = OperationExcel(self.driver).check_element_whether_exists(
            packagelist1, '默认页面')

        try:
            self.assertEqual(non_existent_num032, 0, non_existent_list032)
        except AssertionError as msg:
            print('32软件包管理默认页面不正确！' + str(msg))
            res = True

        # -----------------'''20工单搜索'''-------------------
        EntranceAgentPage(self.driver).enter_search()
        time.sleep(3)
        searchlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '20工单搜索')
        non_existent_list0120, non_existent_num0120= OperationExcel(self.driver).check_element_whether_exists(searchlist1,'默认页面')

        try:
            self.assertEqual(non_existent_num0120, 0, non_existent_list0120)
        except AssertionError as msg:
            print('20工单搜索默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1


        assert res is None, "报错位置有" + str(model_num) + "处"

    def test_036(self):
        """
            值班概览
        """
        EntranceAgentPage(self.driver).enter_duty()
        taglist1 = OperationExcel(self.driver).read_excel_value('./././data/check_element.xls', '37值班概览')
        non_existent_list01, non_existent_num01 = OperationExcel(self.driver).check_element_whether_exists(
            taglist1, '默认页面')
        self.assertEqual(non_existent_num01, 0, non_existent_list01)

        # 点击添加按钮
        self.driver.find_element(By.XPATH, "//span[text()='添加']").click()
        non_existent_list02, non_existent_num02 = OperationExcel(self.driver).check_element_whether_exists(
            taglist1, '添加页面')
        self.assertEqual(non_existent_num02, 0, non_existent_list02)

        self.driver.find_element(By.XPATH, "//div[text()='选择工单过滤条件']").click()
        non_existent_list03, non_existent_num03 = OperationExcel(self.driver).check_element_whether_exists(
            taglist1, '工单过滤条件')
        self.assertEqual(non_existent_num03, 0, non_existent_list03)

        # 点击取消按钮
        self.driver.find_element(By.XPATH, "//span[text()='取消']").click()



















