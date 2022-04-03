"""
@author: DT_testing
@file:   check_elements_case.py
@desc:  【】
@step：对系统所以入口进行检查：1、进入模块入口  2、新增入口
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
from src.page.agent.generic_page import GenericPage
from src.page.agent.fieldimpacts_page import FieldimpactsPage
from src.page.agent.servicesla_page import ServiceSlaPage
from selenium.webdriver.common.by import By
from src.page.agent.process_page import ProcessPage
import time
import unittest
class check_elements(BaseCaseUser, Base):

    @unittest.skip("已在test6_element中检查，常规发布不重复运行，如需单独运行，请删除跳过后重新运行")
    def test_elements(self):
        """
            基本入口检查，1、各个模块入口进入页面不loading   2、不报请求出错（error）
        """
        res = None
        model_num = 0
        # -------------test01 偏好设置---------------------------------------------------------
        EntranceAgentPage(self.driver).enter_preferences()
        userlist = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '33偏好设置')
        # 检查列表页面是否正常进入
        non_existent_list, non_existent_num =OperationExcel(self.driver).check_element_whether_exists(userlist, '修改密码')
        try:
            self.assertEqual(non_existent_num, 0, non_existent_list)
        except AssertionError as msg:
            print('偏好设置打开错误！' + str(msg))
            res = True
            model_num = model_num + 1

        # 1.--------------服务人员（默认与添加）------------------------
        # 进入服务人员
        EntranceAgentPage(self.driver).enter_agent()
        time.sleep(3)
        userlist = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '服务人员')
        # 检查列表页面是否正常进入
        non_existent_list, non_existent_num =OperationExcel(self.driver).check_element_whether_exists(userlist, '默认页面')
        try:
            self.assertEqual(non_existent_num, 0, non_existent_list)
        except AssertionError as msg:
            print('服务人员默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1
        # 进入添加页面
        AgentPage(self.driver).addagent()
        time.sleep(3)
        non_existent_list2,non_existent_num2 = OperationExcel(self.driver).check_element_whether_exists(userlist, '添加页面')
        try:
            self.assertEqual(non_existent_num2, 0, non_existent_list2)

        except AssertionError as msg:
            print('服务人员添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 2.-------------------'''客户用户管理'''（默认）； 新增客户页面----------------------
        EntranceAgentPage(self.driver).enter_customer_user()
        time.sleep(3)
        customeruserlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '客户用户管理')
        non_existent_list, non_existent_num =OperationExcel(self.driver).check_element_whether_exists(customeruserlist1,'列表页面')

        try:
            self.assertEqual(non_existent_num , 0, non_existent_list)
        except AssertionError as msg:
            print('客户用户管理列表页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加客户，检查添加客户页面打开
        CustomerUserPage(self.driver).AddCompany()
        non_existent_list2, non_existent_num2 = OperationExcel(self.driver).check_element_whether_exists(customeruserlist1, '添加页面')
        try:
            self.assertEqual(non_existent_num2, 0, non_existent_list2)
        except AssertionError as msg:
            print('客户用户管理新增客户页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 3.-----------------'''工作时间管理'''（默认和添加）----------------------
        EntranceAgentPage(self.driver).enter_slacalendar()
        time.sleep(3)
        slacalendarlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '工作时间管理')
        non_existent_list, non_existent_num =OperationExcel(self.driver).check_element_whether_exists(slacalendarlist1, '默认页面')

        try:
            self.assertEqual(non_existent_num , 0, non_existent_list)
        except AssertionError as msg:
            print('工作时间管理默认页面不正确！',str(msg))
            res = True
        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()
        non_existent_list2, non_existent_num2 = OperationExcel(self.driver).check_element_whether_exists(slacalendarlist1,'添加页面')

        try:
            self.assertEqual(non_existent_num2, 0, non_existent_list2)
        except AssertionError as msg:
            print('工作时间管理添加页面不正确！' + str(msg))
            res = True

        # 4.----------------'''邮件过滤器'''（默认和添加）-----------------------
        EntranceAgentPage(self.driver).enter_postmasterfilter()
        time.sleep(3)
        userlist4 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '邮件过滤器')
        non_existent_list04, non_existent_num04= OperationExcel(self.driver).check_element_whether_exists(userlist4, '默认页面')

        try:
            self.assertEqual( non_existent_num04, 0, non_existent_list04)
        except AssertionError as msg:
            print('邮件过滤器默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加按钮
        PostmasterFilter_Page(self.driver).clickadd()
        # error_element = None
        # try:
        #     error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
        # except:
        #     pass
        #     # print('未出现请求出错报错')
        # self.assertIsNone(error_element, '邮件过滤器点击后页面请求出错')

        non_existent_list05, non_existent_num05 = OperationExcel(self.driver).check_element_whether_exists(userlist4,'添加页面')

        try:
            self.assertEqual(non_existent_num05, 0, non_existent_list05)
        except AssertionError as msg:
            print('邮件过滤器添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 5.-------------------'''工单模板'''（默认和添加）------------------------
        EntranceAgentPage(self.driver).enter_tickettemplate()
        time.sleep(3)
        templatelist5 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '工单模板')
        non_existent_list06, non_existent_num06 = OperationExcel(self.driver).check_element_whether_exists(templatelist5,'默认页面')

        try:
            self.assertEqual(non_existent_num06, 0, non_existent_list06)
        except AssertionError as msg:
            print('工单模板默认页面不正确！' + str(msg))
            model_num = model_num + 1
            res = True
        # 点击添加按钮
        TemplatePage(self.driver).addtemplate()
        non_existent_list08, non_existent_num08 = OperationExcel(self.driver).check_element_whether_exists(templatelist5,'添加页面')

        try:
            self.assertEqual(non_existent_num08, 0, non_existent_list08)
        except AssertionError as msg:
            print('工单模板添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1


        # 6.--------------------------'''工单通知'''（默认和添加）-----------------------
        # 调用的page为邮件过滤器的的page（暂时先放在一个page中）
        EntranceAgentPage(self.driver).enter_notificationevent()
        time.sleep(5)
        notificationlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '工单通知')
        non_existent_list09, non_existent_num09 = OperationExcel(self.driver).check_element_whether_exists(notificationlist1,'默认页面')
        try:
            self.assertEqual(non_existent_num09, 0, non_existent_list09)
        except AssertionError as msg:
            print('工单通知默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1
        # 点击添加通知
        PostmasterFilter_Page(self.driver).clickadd()
        time.sleep(5)
        non_existent_list10, non_existent_num10 = OperationExcel(self.driver).check_element_whether_exists(notificationlist1,'添加页面')

        try:
            self.assertEqual(non_existent_num10, 0, non_existent_list10)
        except AssertionError as msg:
            print('工单通知添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1


        # 7.---------------------------'''字段库'''（默认和添加）--------------------
        EntranceAgentPage(self.driver).enter_filed()
        time.sleep(3)
        filedlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '字段库')
        non_existent_list07, non_existent_num07 = OperationExcel(self.driver).check_element_whether_exists(filedlist1,
                                                                                                           '默认页面')
        try:
            self.assertEqual(non_existent_num07, 0, non_existent_list07)
        except AssertionError as msg:
            print('字段库默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加按钮
        self.driver.find_element(By.ID, 'CreateButton').click()
        time.sleep(3)
        non_existent_list077, non_existent_num077 = OperationExcel(self.driver).check_element_whether_exists(filedlist1,
                                                                                                             '添加页面')

        try:
            self.assertEqual(non_existent_num077, 0, non_existent_list077)
        except AssertionError as msg:
            print('字段库添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # ---------------------'''8.流程管理'''（默认）------------------------
        EntranceAgentPage(self.driver).enter_processmanagement()
        time.sleep(3)
        filedlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '流程管理')

        non_existent_list08, non_existent_num08 = OperationExcel(self.driver).check_element_whether_exists(filedlist1,
                                                                                                           '默认页面')
        try:
            self.assertEqual(non_existent_num08, 0, non_existent_list08)
        except AssertionError as msg:
            print('流程管理默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加
        ProcessPage(self.driver).add()
        non_existent_list_process, non_existent_num_process = OperationExcel(self.driver).check_element_whether_exists(filedlist1,
                                                                                                           '添加页面')
        try:
            self.assertEqual(non_existent_num_process, 0, non_existent_list_process)
        except AssertionError as msg:
            print('流程管理添加页面打开出错！' + str(msg))
            res = True
            model_num = model_num + 1

        # ----------------------'''9菜单权限管理'''（默认和添加）--------------------
        EntranceAgentPage(self.driver).enter_menuset()
        time.sleep(3)
        rolemenulist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '9菜单权限管理')
        non_existent_list09, non_existent_num09 = OperationExcel(self.driver).check_element_whether_exists(
            rolemenulist1, '默认页面')

        try:
            self.assertEqual(non_existent_num09, 0, non_existent_list09)
        except AssertionError as msg:
            print('菜单权限管理默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1
        # 点击添加按钮
        MenusetPage(self.driver).addmenu()
        # error_element = None
        # try:
        #     error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
        #
        # except:
        #     pass
        #     # print('未出现请求出错报错')
        # self.assertIsNone(error_element, '菜单权限管理点击新增按钮后页面请求出错')
        # 元素检查
        non_existent_list099, non_existent_num099 = OperationExcel(self.driver).check_element_whether_exists(
            rolemenulist1, '添加页面')
        try:
            self.assertEqual(non_existent_num099, 0, non_existent_list099)
        except AssertionError as msg:
            print('菜单权限管理默认添加不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # ------------------------'''10角色'''（默认和添加）-------------------

        EntranceAgentPage(self.driver).enter_role()
        time.sleep(3)
        rolelist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '10角色')
        non_existent_list0100, non_existent_num0100= OperationExcel(self.driver).check_element_whether_exists(rolelist1,'默认页面')
        try:
            self.assertEqual(non_existent_num0100, 0, non_existent_list0100)
        except AssertionError as msg:
            print('角色默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加按钮
        RolePage(self.driver).addrole()
        non_existent_list0100, non_existent_num0100 = OperationExcel(self.driver).check_element_whether_exists(
            rolelist1, '添加页面')
        try:
            self.assertEqual(non_existent_num0100, 0, non_existent_list0100)
        except AssertionError as msg:
            print('角色添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1


        # -------------------'''11区域'''（默认和添加）-----------------------
        EntranceAgentPage(self.driver).enter_district()
        time.sleep(3)
        districtlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '11区域')
        non_existent_list111, non_existent_num111 = OperationExcel(self.driver).check_element_whether_exists(
            districtlist1, '默认页面')

        try:
            self.assertEqual(non_existent_num111, 0, non_existent_list111)
        except AssertionError as msg:
            print('区域默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1
        # 点击添加按钮
        DistrictPage(self.driver).click_add()
        non_existent_list0211, non_existent_num0211 = OperationExcel(self.driver).check_element_whether_exists(
            districtlist1, '添加页面')
        try:
            self.assertEqual(non_existent_num0211, 0, non_existent_list0211)
        except AssertionError as msg:
            print('区域添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # -------------'''12cmdb概览'''（默认）-----------------------
        EntranceAgentPage(self.driver).enter_cmdb_overview()
        time.sleep(3)
        cmdb1list1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '12cmdb概览')
        non_existent_list12, non_existent_num12 = OperationExcel(self.driver).check_element_whether_exists(cmdb1list1,
                                                                                                           '默认页面')

        try:
            self.assertEqual(non_existent_num12, 0, non_existent_list12)
        except AssertionError as msg:
            print('12cmdb概览默认列表打开不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # -----------------'''13cmdb配置'''（默认和添加）----------------
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        time.sleep(3)
        cmdb2list1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '13cmdb配置')
        non_existent_list0113, non_existent_num0113 = OperationExcel(self.driver).check_element_whether_exists(
            cmdb2list1, '默认页面')
        try:
            self.assertEqual(non_existent_num0113, 0, non_existent_list0113)
        except AssertionError as msg:
            print('13cmdb配置默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加按钮
        self.driver.find_element(By.ID, 'fieldCreateButton').click()
        time.sleep(3)
        non_existent_list0213, non_existent_num0213 = OperationExcel(self.driver).check_element_whether_exists(
            cmdb2list1, '添加页面')
        try:
            self.assertEqual(non_existent_num0213, 0, non_existent_list0213)
        except AssertionError as msg:
            print('13cmdb配置添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # --------------'''14工单分组'''------------------
        EntranceAgentPage(self.driver).enter_ticketgroup()
        time.sleep(3)
        ticketgrouplist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '14工单分组')
        non_existent_list014, non_existent_num014 = OperationExcel(self.driver).check_element_whether_exists(
            ticketgrouplist1, '默认页面')

        try:
            self.assertEqual(non_existent_num014, 0, non_existent_list014)
        except AssertionError as msg:
            print('14工单分组默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加按钮
        # DistrictPage(self.driver).click_add()
        self.driver.find_element(By.ID, 'AddTicket').click()
        time.sleep(3)
        non_existent_list0214, non_existent_num0214 = OperationExcel(self.driver).check_element_whether_exists(
            ticketgrouplist1, '添加页面')
        try:
            self.assertEqual(non_existent_num0214, 0, non_existent_list0214)
        except AssertionError as msg:
            print('工单分组加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1


        # -----------------------'''15自动任务列表'''（默认）--------------------
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '15自动任务列表')
        non_existent_list0115, non_existent_num0115= OperationExcel(self.driver).check_element_whether_exists(genericlist1,'默认页面')

        try:
            self.assertEqual(non_existent_num0115, 0, non_existent_list0115)
        except AssertionError as msg:
            print('15自动任务列表默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1
        # 点击添加按钮
        GenericPage(self.driver).add()
        time.sleep(3)
        non_existent_list0215, non_existent_num0215= OperationExcel(self.driver).check_element_whether_exists(genericlist1,'添加页面')

        try:
            self.assertEqual(non_existent_num0215, 0, non_existent_list0215)
        except AssertionError as msg:
            print('15自动任务添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # -------------------------'''16主页'''------------------
        EntranceAgentPage(self.driver).enter_home()
        time.sleep(3)
        homelist = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '16主页')
        non_existent_list01, non_existent_num01= OperationExcel(self.driver).check_element_whether_exists(homelist,'默认页面')
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
        non_existent_list0117, non_existent_num0117= OperationExcel(self.driver).check_element_whether_exists(sessionlist1,'默认页面')
        try:
            self.assertEqual(non_existent_num0117, 0, non_existent_list0117)
        except AssertionError as msg:
            print('17会话页面打开报错！' + str(msg))
            res = True
            model_num = model_num + 1


        # -----------------------'''18知识库类别管理'''----------------------
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)
        faqlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '18知识库类别管理')
        non_existent_list0118, non_existent_num0118= OperationExcel(self.driver).check_element_whether_exists(faqlist1, '默认页面')

        try:
            self.assertEqual(non_existent_num0118, 0, non_existent_list0118)
        except AssertionError as msg:
            print('18知识库类别管理默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        self.driver.find_element(By.ID, 'addCatalog').click()
        time.sleep(3)
        # error_element = None
        # try:
        #     error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
        # except:
        #     pass
        #     # print('未出现请求出错报错')
        # self.assertIsNone(error_element, '知识库类别管理页面点击新增按钮后页面请求出错')

        non_existent_list0218, non_existent_num0218= OperationExcel(self.driver).check_element_whether_exists(faqlist1,'添加页面')
        try:
            self.assertEqual(non_existent_num0218, 0, non_existent_list0218)
        except AssertionError as msg:
            print('18知识库类别管理添加页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1


        # ------------------'''19邮箱'''--------------------
        EntranceAgentPage(self.driver).enter_mailmanagement()

        faqlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '19邮箱')
        # 进入
        # non_existent_list0119, non_existent_num0119= OperationExcel(self.driver).check_element_whether_exists(faqlist1, '默认页面')
        #
        # try:
        #     self.assertEqual(non_existent_num0119, 0, non_existent_list0119)
        # except AssertionError as msg:
        #     print('19邮箱默认页面不正确！' + str(msg))
        #     res = True

        # 新增
        try:
            self.driver.find_elements_by_css_selector('[class="admin-ticket-template-btn ant-btn"]')[0].click()
            time.sleep(3)
        except AssertionError as msg:
            print('点击邮箱新增按钮出现异常！' + str(msg))
            res = True
            model_num = model_num + 1

        # error_element = None
        # try:
        #     error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
        # except:
        #     pass
        #     # print('未出现请求出错报错')
        # self.assertIsNone(error_element, '邮箱页面点击新增按钮后页面请求出错')

        non_existent_list0219, non_existent_num0219= OperationExcel(self.driver).check_element_whether_exists(faqlist1,'添加页面')
        try:
            self.assertEqual(non_existent_num0219, 0, non_existent_list0219)
        except AssertionError as msg:
            print('19邮箱新增页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1


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


#         #-----------------'''21工单详情'''-----------------
#         # URL = sys.argv[1] + "/user/ticket/detail/1"
#         # # URL ='https://re1.otrs365.cn/user/ticket/detail/1'
#         # self.driver.get(URL)
#         # time.sleep(3)
#         # zoomlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '21工单详情',
#         #                                                      '默认页面')
#         # non_existent_list0121 = OperationExcel(self.driver).check_element_whether_exists(zoomlist1)
#         #
#         # try:
#         #     self.assertEqual(len(non_existent_list0121), 0, non_existent_list0121)
#         # except AssertionError as msg:
#         #     print('21工单详情默认页面不正确！' + str(msg))
#         #     res = True
#
#
#         # ----------------'''22字段影响关系'''-----------------
#         # EntranceAgentPage(self.driver).enter_relust('自定义字段影响关系')
#         EntranceAgentPage(self.driver).enter_fieldimpact()
#         time.sleep(3)
#         fieldimpactlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '22字段影响关系')
#         non_existent_list0122, non_existent_num0122= OperationExcel(self.driver).check_element_whether_exists(fieldimpactlist1,'默认页面')
#
#         try:
#             self.assertEqual(non_existent_num0122, 0, non_existent_list0122)
#         except AssertionError as msg:
#             print('22字段影响关系默认页面不正确！' + str(msg))
#             res = True
#
#         error_element = None
#         try:
#             error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
#         except:
#             pass
#             # print('未出现请求出错报错')
#         self.assertIsNone(error_element, '邮箱页面点击新增按钮后页面请求出错')
#         # 点击添加按钮
#         FieldimpactsPage(self.driver).add()
#         non_existent_list0222, non_existent_num0222 = OperationExcel(self.driver).check_element_whether_exists(fieldimpactlist1,'添加页面')
#         try:
#             self.assertEqual(non_existent_num0222, 0, non_existent_list0222)
#         except AssertionError as msg:
#             print('22字段影响关系新增页面不正确！' + str(msg))
#             res = True
#
#
#         # ----------------'''23知识库概览'''-----------------
#         EntranceAgentPage(self.driver).enter_faq_overview()
#         time.sleep(3)
#         faqoverviewlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '23知识库概览')
#
#         non_existent_list0123, non_existent_num0123 = OperationExcel(self.driver).check_element_whether_exists(faqoverviewlist1,'默认页面')
#
#         try:
#             self.assertEqual(non_existent_num0123, 0, non_existent_list0123)
#         except AssertionError as msg:
#             print('23知识库概览页面不正确！' + str(msg))
#             res = True
#
#         error_element = None
#         try:
#             error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
#         except:
#             pass
#             # print('未出现请求出错报错')
#         self.assertIsNone(error_element, '23知识库概览点击新增按钮后页面请求出错')
#
#         non_existent_list0223, non_existent_num0223 = OperationExcel(self.driver).check_element_whether_exists(faqoverviewlist1,'添加页面')
#         try:
#             self.assertEqual(non_existent_num0223, 0, non_existent_list0223)
#         except AssertionError as msg:
#             print('23知识库概览新增页面不正确！' + str(msg))
#             res = True
#
#
        # ------------ '''24服务'''-----------------
        EntranceAgentPage(self.driver).enter_service()
        time.sleep(3)
        faqoverviewlist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '24服务')
        non_existent_list0124, non_existent_num0124= OperationExcel(self.driver).check_element_whether_exists(faqoverviewlist1,'默认页面')
        try:
            self.assertEqual(non_existent_num0124, 0, non_existent_list0124)
        except AssertionError as msg:
            print('24服务页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        non_existent_list0224, non_existent_num0224= OperationExcel(self.driver).check_element_whether_exists(faqoverviewlist1,'添加页面')

        try:
            self.assertEqual(non_existent_num0224, 0, non_existent_list0224)
        except AssertionError as msg:
            print('24服务页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # -------------'''26服务水平协议'''--------------
        EntranceAgentPage(self.driver).enter_sla()
        time.sleep(3)
        slalist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '26服务水平协议')
        non_existent_list01, non_existent_num01= OperationExcel(self.driver).check_element_whether_exists(slalist1,'默认页面')

        try:
            self.assertEqual(non_existent_num01, 0, non_existent_list01)
        except AssertionError as msg:
            print('26服务水平协议默认页面不正确！' + str(msg))
            res = True

        # error_element = None
        # try:
        #     error_element = self.driver.find_element_by_css_selector('[class="ant-result ant-result-warning"]')
        # except:
        #     pass
        #     # print('未出现请求出错报错')
        # self.assertIsNone(error_element, 'sla页面点击新增按钮后页面请求出错')
        # 点击添加按钮
        ServiceSlaPage(self.driver).clickaddsla()

        non_existent_list0126, non_existent_num0126= OperationExcel(self.driver).check_element_whether_exists(slalist1,'添加页面')

        try:
            self.assertEqual(non_existent_num0126, 0, non_existent_list0126)
        except AssertionError as msg:
            print('26服务水平协议添加页面不正确！' + str(msg))
            res = True

        # --------------------'''27统计管理'''-----------------
        EntranceAgentPage(self.driver).enter_stats()
        time.sleep(3)
        slalist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '27统计管理')
        non_existent_list0127, non_existent_num0127= OperationExcel(self.driver).check_element_whether_exists(slalist1,'默认页面')

        try:
            self.assertEqual(non_existent_num0127, 0, non_existent_list0127)
        except AssertionError as msg:
            print('27统计管理页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # 点击添加，对点击页面进行校验

        # -----------------'''28统计组合管理'''-----------------
        EntranceAgentPage(self.driver).enter_statscombine()
        time.sleep(3)
        statscombine = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '28统计组合管理')
        non_existent_list0128, non_existent_num0128= OperationExcel(self.driver).check_element_whether_exists(statscombine,'默认页面')

        try:
            self.assertEqual(non_existent_num0128, 0, non_existent_list0128)
        except AssertionError as msg:
            print('28统计组合管理默认页面不正确！' + str(msg))
            res = True
            model_num = model_num + 1

        # ------------'''29内容模板'''----------------
        EntranceAgentPage(self.driver).enter_contenttemplate()
        time.sleep(3)
        contenttemplate = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '29内容模板')
        non_existent_list0129, non_existent_num0129= OperationExcel(self.driver).check_element_whether_exists(contenttemplate,'默认页面')

        try:
            self.assertEqual(non_existent_num0129, 0, non_existent_list0129)
        except AssertionError as msg:
            print('29内容模板默认页面不正确！' + str(msg))
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
        non_existent_list032, non_existent_num032= OperationExcel(self.driver).check_element_whether_exists(packagelist1,'默认页面')

        try:
            self.assertEqual(non_existent_num032, 0, non_existent_list032)
        except AssertionError as msg:
            print('32软件包管理默认页面不正确！' + str(msg))
            res = True

        # -----------------37工作台--------------------------
        EntranceAgentPage(self.driver).enter_workbench()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入工作台页面报错")
        except AssertionError as msg:
            print('进入工作台页面不正确！' + str(msg))
            res = True

        workbench = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '37工作台')
        non_existent_list0127, non_existent_num0127 = OperationExcel(self.driver).check_element_whether_exists(
            workbench,
            '默认页面')
        try:
            self.assertEqual(non_existent_num0127, 0, non_existent_list0127)
        except AssertionError as msg:
            print('工作台页面打开错误！' + str(msg))
            res = True
            model_num = model_num + 1

        # -----------------38工作台管理-------------------------
        EntranceAgentPage(self.driver).enter_workbenchmanage()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入工作台管理页面报错")
        except AssertionError as msg:
            print('进入工作台管理不正确！' + str(msg))
            res = True

        workbenchmanage = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '38工作台管理')
        non_existent_list0127, non_existent_num0127 = OperationExcel(self.driver).check_element_whether_exists(
            workbenchmanage,
            '默认页面')
        try:
            self.assertEqual(non_existent_num0127, 0, non_existent_list0127)
        except AssertionError as msg:
            print('工作台管理页面打开错误！' + str(msg))
            res = True
            model_num = model_num + 1

        # ---kpi---
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

        # 通信日志
        EntranceAgentPage(self.driver).enter_communicationlog()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入通信日志页面报错")
        except AssertionError as msg:
            print('进入通信日志不正确！' + str(msg))
            res = True

        # 系统日志
        EntranceAgentPage(self.driver).enter_systemlog()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入系统日志页面报错")
        except AssertionError as msg:
            print('进入系统日志不正确！' + str(msg))
            res = True

        # 公共参数设置
        EntranceAgentPage(self.driver).enter_workbenchmanage()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入公共参数设置页面报错")
        except AssertionError as msg:
            print('进入公共参数设置页面不正确！' + str(msg))
            res = True

        # sql屏幕查询
        EntranceAgentPage(self.driver).enter_selectbox()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入sql屏幕查询页面报错")
        except AssertionError as msg:
            print('进入sql屏幕查询不正确！' + str(msg))
            res = True

        # 服务台
        EntranceAgentPage(self.driver).enter_cti()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入CTI页面报错")
        except AssertionError as msg:
            print('进入CTI不正确！' + str(msg))
            res = True

        # 我的工单
        EntranceAgentPage(self.driver).enter_mytickets()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入我的工单页面报错")
        except AssertionError as msg:
            print('进入我的工单不正确！' + str(msg))
            res = True

        # ---------------34标签管理-------------------------
        EntranceAgentPage(self.driver).entre_tagmanagement()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入标签管理页面报错")
        except AssertionError as msg:
            print('进入标签管理不正确！' + str(msg))
            res = True
            model_num = model_num + 1
        # 点击添加按钮
        self.driver.find_element(By.ID, 'NewlyAdded').click()
        slalist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '34标签管理')
        non_existent_list_tag, non_existent_num_tag = OperationExcel(self.driver).check_element_whether_exists(slalist1,
                                                                                                               '添加页面')
        try:
            self.assertEqual(non_existent_num_tag, 0, non_existent_list_tag)
        except AssertionError as msg:
            print('标签管理添加页面打开错误！' + str(msg))
            res = True
            model_num = model_num + 1

        # ---------------35标签规则管理-------------------------
        EntranceAgentPage(self.driver).enter_tagmanagement_rule()
        # 检查url
        url1 = str(self.driver.current_url)
        try:
            self.assertEqual(url1.find('error'), -1, "进入标签规则管理页面报错")
        except AssertionError as msg:
            print('进入标签规则管理不正确！' + str(msg))
            res = True
            model_num = model_num + 1
        # 点击添加按钮
        self.driver.find_element(By.ID, 'NewlyAdded').click()
        slalist1 = OperationExcel(self.driver).read_excel_value('./././data/check_elements.xls', '35标签规则管理')
        non_existent_list_tagrule, non_existent_num_tagrule = OperationExcel(self.driver).check_element_whether_exists(
            slalist1,
            '添加页面')
        try:
            self.assertEqual(non_existent_num_tagrule, 0, non_existent_list_tagrule)
        except AssertionError as msg:
            print('标签规则管理添加页面打开错误！' + str(msg))
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
        non_existent_list_tagrule, non_existent_num_tagrule = OperationExcel(self.driver).check_element_whether_exists(
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

        assert res is None, "报错位置有" + str(model_num) + "处"