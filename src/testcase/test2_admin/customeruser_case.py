"""
@author: DT_testing
@file:   customer_user_case.py
@desc:  【客户用户管理】
@step： 001. 检查角色面包屑（路径）,客户用户管理的tab title、浏览器title (SC_CustomerUser_1)
        002. 检查添加页面的“返回”按钮    (SC_CustomerUser_13)
        003. 只填写必填项新增客户，且增加后可查询到，查询到后点击客户编辑页面，页面中显示的信息与新增时填写的内容一致 (SC_CustomerUser_14)
        004. 验证添加客户页面的必填项   (SC_CustomerUser_16)
        005. 客户页面验证客户编号、客户名称重复  (SC_CustomerUser_18 SC_CustomerUser_27)
        006. 客户用户页面修改必填项,切换有效性(SC_CustomerUser_42、SC_CustomerUser_46、)
        007. 客户将无效修改为有效  SC_CustomerUser_47
        008. 客户新增/编辑页面 提交后 上一步  (SC_CustomerUser_48)
        009. 添加一个客户后，进入关联服务页面，不关联任何服务直接提交 ，检查“继续设置关联信息”，
          设置部门关联服务页-返回关联项，设置部门关联服务页-返回列表
         (SC_CustomerUser_61、SC_CustomerUser_66 、SC_CustomerUser_68、SC_CustomerUser_69)
        010. 填写必填项添加一个用户  （SC_CustomerUser_81）
        011. 填写全填项添加一个用户 （SC_CustomerUser_82）
        012. 添加用户-返回按钮验证（SC_CustomerUser_83）
        013. 验证添加用户页面的必填项 (SC_CustomerUser_89)
        014. 验证添加重复用户账号 （SC_CustomerUser_93）
        015. 编辑用户，不修改任何内容直接提交（SC_CustomerUser_85）
        016. 编辑用户，修改必填项   （SC_CustomerUser_86）
        017. 编辑用户，修改非必填项  （SC_CustomerUser_87）
        018. 编辑用户，填写非必填项    （SC_CustomerUser_88）
        019. 客户设置一个负责人 ，删除一个负责人  （SC_CustomerUser_23，SC_CustomerUser_25）  --页面变更，该用例被取消
        021. 客户设置多个负责人    （SC_CustomerUser_24）
        021. 设置子级为父部门  ，删除父部门    （SC_CustomerUser_33、SC_CustomerUser_34）
        022. 设置父级为父部门(变更父部门)  （SC_CustomerUser_32）
        023. 添加客户必填项输入空格验证  SC_CustomerUser_17
        024. 客户编号、名称、邮编、街道、网址、备注输入类型验证 SC_CustomerUser_19、SC_CustomerUser_36，SC_CustomerUser_37、SC_CustomerUser_38
        025. 客户编号、名称、邮编、街道、网址、备注输入字符长度验证 （SC_CustomerUser_20、SC_CustomerUser_36，SC_CustomerUser_37、SC_CustomerUser_38）
        026. 添加用户，必填项输入为空格   SC_CustomerUser_90
        027. 添加用户，必填项输入类型验证 （SC_CustomerUser_91、SC_CustomerUser_94）
        028. 添加用户，必填项输入字符长度验证 （SC_CustomerUser_92、SC_CustomerUser_95）
        029. 添加用户，邮件地址唯一性验证  SC_CustomerUser_96
        030. 添加用户，密码的可见与隐藏，修改用户密码 （SC_CustomerUser_99、SC_CustomerUser_100）未完成，缺少客户登录验证部分
"""
import time
from selenium.webdriver.support.ui import WebDriverWait

import unittest2
from common.base import Base
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.customer_user_page import CustomerUserPage
from src.page.pagecommon.customer_user_commom import CustomerUserCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from src.page.pagecommon.get_time_common import GetTimeCommon
import random


class CustomerUser(BaseCaseUser, Base):

    # 检查客户用户页面的导航栏  SC_CustomerUser_1 OK
    def test_001_title(self):
        try:
            # 进入页面
            EntranceAgentPage(self.driver).enter_customer_user()
            # 检查浏览器title
            result = Base(self.driver).get_title()
            self.assertEqual(result, '客户用户管理', '客户用户管理页面浏览器窗口 title 显示不正确')
            tabtitle = CustomerUserPage(self.driver).tabtitle()
            self.assertEqual(tabtitle, '客户用户管理', '客户用户管理页面tab窗口 title 显示不正确')
            road = CustomerUserPage(self.driver).road()
            self.assertEqual(road, '/ 系统管理 / 客户用户管理', msg='客户用户管理列表路径显示不正确')

        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('客户用户管理列表路径显示不正确:'+str(msg))

    # 添加客户页面的返回按钮检查,编辑页面的返回按钮    SC_CustomerUser_13  ok
    def test_002_cusback(self):
        try:
            # 进入页面
            EntranceAgentPage(self.driver).enter_customer_user()
            # 进入客户用户页面，必须增加强制等待
            time.sleep(15)
            CustomerUserPage(self.driver).AddCompany()
            CustomerUserPage(self.driver).Companyback()
            # 在列表搜索一个不存在的用户
            # newtime = GetTimeCommon(self.driver).get_time()
            # CustomerUserPage(self.driver).Searchuser(newtime)
            addtext = self.driver.find_element_by_id('AddSubCompany').get_attribute('title')
            # userempty = CustomerUserPage(self.driver).userempty()
            self.assertEqual(addtext,'添加客户',msg='错误：添加客户点击返回失败！')
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('添加客户点击返回失败:'+str(msg))

#     # 填写必填项添加客户,二次进入打开页面信息显示正确    SC_CustomerUser_14  ok
#     def test_003_AddCompany(self):
#         try:
#             # 填写必填值
#             # self.driver.implicitly_wait(10)
#             str_name = CustomerUserCommon(self.driver).Companyrequiredcommon()
#             name = str_name[0]
#             company_id = str_name[1]
#             Company_text_valid = [company_id,  name, None, None, None, None, None, None, None, None, '有效']
#             # 点击提交
#             CustomerUserPage(self.driver).Companysub()
#             time.sleep(5)
#             # 查询左侧客户列表树，看是否有数据
#             CustomerUserPage(self.driver).SearchCompany(name)
#             time.sleep(1)
#             # 点击搜索的结果
#             CustomerUserPage(self.driver).Searchresultcom_click()
#             time.sleep(1)
#             # 进入客户编辑页面
#             CustomerUserPage(self.driver).EditCompany()
#             time.sleep(1)
#             # 提取编辑页面内的所有元素
#             Company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#
#             # if 判断二次进入页面信息是否显示正确
#             for i in range(len(Company_text_valid)):
#                 if Company_all_text[i] == '':
#                     Company_all_text[i] = None
#                 self.assertEqual(Company_all_text[i], Company_text_valid[i] , msg = '创建用户填写必填项二次编辑信息显示错误')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('填写必填添加客户失败:'+str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 检查添加客户页面必填项  SC_CustomerUser_16
#     def test_004_check_required(self):
#         try:
#             # 进入客户用户页面，点击新增客户
#             EntranceAgentPage(self.driver).enter_customer_user()
#             time.sleep(10)
#             CustomerUserPage(self.driver).AddCompany()
#             time.sleep(2)
#             # 初始化变量，提交按钮3次不可操作
#             enabled_num = 3
#
#             # 进入页面后第一次检查提交按钮是否可以触发   不可触发1
#             enabled_a= CustomerUserPage(self.driver).submit_enabled()
#             time.sleep(2)
#
#             # 输入客户编号后第二次检查提交按钮是否可以触发   不可触发2
#             CustomerUserPage(self.driver).CustomerID('1234567890')
#             enabled_b = CustomerUserPage(self.driver).submit_enabled()
#             time.sleep(2)
#             # 输入客户名称后
#             CustomerUserPage(self.driver).CompanyName('1234567890')
#
#             # 将鼠标移动到有效性，删除有效性，第三次提交按钮是否可以触发  不可触发3
#             CustomerUserPage(self.driver).move_valid()
#             CustomerUserPage(self.driver).vaild_dete()
#             time.sleep(2)
#             enabled_c = CustomerUserPage(self.driver).submit_enabled()
#             str1= enabled_a+enabled_b+enabled_c
#
#             lista = [enabled_a, enabled_b, enabled_c]
#             for i in lista:
#                 if i == True:
#                     enabled_num -= 1
#             self.assertEqual(enabled_num, 3, msg='添加客户必填项验证失败:' + str(str1))
#
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('添加客户页面必填项验证失败'+str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 验证客户编号、客户名称重复    ok
#     # 0814 重复信息的id值被丢弃   0828修复恢复
#     def test_005_check_repeat(self):
#         try:
#             # 填写必填值添加一个客户
#             str_name = CustomerUserCommon(self.driver).Companyrequiredcommon()
#             name = str_name[0]
#             company_id = str_name[1]
#             # 点击提交
#             CustomerUserPage(self.driver).Companysub()
#             # 点击返回列表、点击添加按钮
#             CustomerUserPage(self.driver).associate_GoBack()
#             time.sleep(5)
#             CustomerUserPage(self.driver).AddCompany()
#             time.sleep(5)
#             # 往编号、名称中传入值。然后判断重复信息是否存在，同时提交按钮不可触发
#             CustomerUserPage(self.driver).CustomerID(company_id)
#             CustomerUserPage(self.driver).CompanyName(name)
#             time.sleep(2)
#             # # 点击有效性，选择有效
#             # CustomerUserPage(self.driver).valid()
#             # time.sleep(5)
#             # 取重复的提示信息
#             repeat_CustomerID = CustomerUserPage(self.driver).repeat_CustomerID()
#             repeat_CompanyName = CustomerUserPage(self.driver).repeat_CompanyName()
#             sumit1 = CustomerUserPage(self.driver).submit_enabled()
#             self.assertEqual(repeat_CustomerID,'数据校验不通过，该值已存在，请重新输入！' ,msg='客户编号重复未提示' )
#             self.assertEqual(repeat_CompanyName, '数据校验不通过，该值已存在，请重新输入！', msg='客户名称重复未提示')
#             self.assertEqual(sumit1, False, msg='客户编号、名称重复提交按钮可触发')
#
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('重复客户编号，重复客户名称验证失败'+str(msg))
#
#     # 修改必填项(修改编号、用户名称、有效性)
#     # 0814客户名称校验时间过长   0828检查检验仍然过长
#     # def test_006_modify_required(self):
#     #     try:
#     #         # 创建一个必填项
#     #         # 进入修改内容（修改编号、用户名称、有效性），提交，
#     #         # 二次点击后进入，信息显示正确
#     #         str_name = CustomerUserCommon(self.driver).Companyrequiredcommon()
#     #         CustomerUserPage(self.driver).Companysub()
#     #         old_CompanyName = str_name[0]
#     #         company_id = str_name[1]
#     #         new_CompanyName = old_CompanyName + 'new'
#     #         new_CustomerID = company_id + 'new'
#     #         Company_text_invaild = [new_CustomerID, new_CompanyName, None,None,None,None,None,None, None,None,'无效']
#     #         # 点击提交
#     #         time.sleep(10)
#     #         CustomerUserPage(self.driver).SearchCompany(old_CompanyName)
#     #         time.sleep(3)
#     #         CustomerUserPage(self.driver).Searchresultcom_click()
#     #         # 进入编辑页面  第一次进入编辑页面
#     #         time.sleep(3)
#     #         CustomerUserPage(self.driver).EditCompany()
#     #         time.sleep(4)
#     #         CustomerUserPage(self.driver).invalid()
#     #         CustomerUserPage(self.driver).CompanyName(new_CompanyName)
#     #         CustomerUserPage(self.driver).CustomerID(new_CustomerID)
#     #         time.sleep(5)
#     #         CustomerUserPage(self.driver).associate_GoBack()
#     #         CustomerUserPage(self.driver).SearchCompany(new_CompanyName)
#     #         time.sleep(5)
#     #         CustomerUserPage(self.driver).Searchresultcom_click()
#     #         time.sleep(3)
#     #
#     #         # 进入编辑页面  第二次进入编辑页面
#     #         CustomerUserPage(self.driver).EditCompany()
#     #         time.sleep(3)
#     #         Company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#     #         for j in range(len(Company_all_text)):
#     #             if Company_all_text[j] == '':
#     #                 Company_all_text[j] = None
#     #             # 区域部分存在bug，此处跳过区域判断
#     #             if j == 4:
#     #                 pass
#     #             else:
#     #                 self.assertEqual(Company_all_text[j], Company_text_invaild[j], '客户修改必填项二次进入信息显示错误' )
#     #
#     #     except Exception as msg:
#     #         Base.get_windows_img(self)
#     #         self.logger.error('客户页面必填项修改失败'+str(msg))
#
#     # 将无效客户修改为有效
#     def test_007_modify_valid(self):
#         try:
#             # 创建一个无效客户
#             str = CustomerUserCommon(self.driver).Companyinvalidcommon()
#             name = str[0]
#             company_id = str[1]
#             Company_text_vaild = [company_id, name, None, None, None, None, None, None, None, None,'有效']
#             # 点击提交
#             CustomerUserPage(self.driver).Companysub()
#             time.sleep(2)
#             # 点击返回列表、点击添加按钮
#             CustomerUserPage(self.driver).associate_GoBack()
#             time.sleep(2)
#             CustomerUserPage(self.driver).SearchCompany(name)
#             time.sleep(3)
#             CustomerUserPage(self.driver).Searchresultcom_click()
#             time.sleep(3)
#             CustomerUserPage(self.driver).EditCompany()
#             # 修改有效性为有效
#             CustomerUserPage(self.driver).valid()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).SearchCompany(name)
#             time.sleep(2)
#             CustomerUserPage(self.driver).Searchresultcom_click()
#             time.sleep(3)
#             CustomerUserPage(self.driver).EditCompany()
#             time.sleep(2)
#             Company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#             for j in range(len(Company_text_vaild)):
#                 if Company_all_text[j] == '':
#                     Company_all_text[j] = None
#                 # #  区域部分存在bug，此处跳过区域判断
#                 # if j==4:
#                 #     pass
#                 # else:
#                 self.assertEqual(Company_all_text[j], Company_text_vaild[j], '无效客户修改为有效客户二次进入信息显示错误' )
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('无效客户修改为有效客户失败'+str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#
#     # 客户添加/编辑页面 提交后 上一步  SC_CustomerUser_48   ok
#     def test_008_Companysub_back(self):
#
#        try:
#            operation = ['添加', '编辑']
#            list1 = CustomerUserCommon(self.driver).Companyrequiredcommon()
#
#            Company_text_vaild = [list1[1],  list1[0], None, None, None, None, None, None, None, None, '有效']
#
#            for i in operation:
#                # 添加时跳过这个
#                if i == '编辑':
#                    # 搜索客户并进入编辑页面
#                    CustomerUserPage(self.driver).SearchCompany(list1[0])
#                    time.sleep(3)
#                    CustomerUserPage(self.driver).Searchresultcom_click()
#                    time.sleep(4)
#                    CustomerUserPage(self.driver).EditCompany()
#                # 提交
#                CustomerUserPage(self.driver).Companysub()
#                time.sleep(5)
#
#                # 添加提交后上一步
#                CustomerUserPage(self.driver).Previous()
#                time.sleep(2)
#
#                Company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#                Company_title = CustomerUserCommon(self.driver).Edit_title()
#                for j in range(len(Company_all_text)):
#                    if Company_all_text[j] == '':
#                        Company_all_text[j] = None
#                    # #  区域部分存在bug，此处跳过区域判断
#                    # if j == 4:
#                    #     pass
#                    # else:
#                    if i =='添加':
#                        self.assertEqual(Company_all_text[j],Company_text_vaild[j],'添加客户提交后点上一步，页面信息显示错误' )
#                        self.assertEqual(Company_title,'编辑客户' ,'添加客户页面左上角标题错误')
#                    else:
#                        self.assertEqual(Company_all_text[j], Company_text_vaild[j], '编辑客户提交后点上一步，页面信息显示错误')
#                        self.assertEqual(Company_title, '编辑客户', '编辑客户页面左上角标题错误')
#                # 返回列表，搜索客户，进入编辑客户页面
#                CustomerUserPage(self.driver).Companyback()
#                time.sleep(2)
#            addtext = self.driver.find_element_by_id('AddSubCompany').get_attribute('title')
#            # # 查询一个不存在的用户
#            # CustomerUserPage(self.driver).Searchuser('祥龙十八章')
#            # userempty = CustomerUserPage(self.driver).userempty()
#            self.assertEqual(addtext, '添加客户', msg='客户用户-添加客户页面-返回列表失败')
#
#        except Exception as msg:
#            Base.get_windows_img(self)
#            self.logger.error('客户新增/编辑页面提交后上一步,信息显示错误'+str(msg))
#            # self.assertEqual(msg, '', '用例执行失败')
#
#     # 添加一个客户后，进入关联服务页面，不关联任何服务直接提交
#     # 0731 bug阻碍2020042328000173  0828检查未修复
#     # def test_009_Company_noneservice(self):
#     #     try:
#     #         CustomerUserCommon(self.driver).Companyrequiredcommon()
#     #         # 提交-关联服务-提交-继续设置关联信息-关联服务-返回关联项-返回列表
#     #         CustomerUserPage(self.driver).Companysub()
#     #         time.sleep(2)
#     #         CustomerUserPage(self.driver).associate_service()
#     #         CustomerUserPage(self.driver).Submit_server()
#     #         time.sleep(4)
#     #         CustomerUserPage(self.driver).ContinueSetting()
#     #         CustomerUserPage(self.driver).associate_service()
#     #         # 0730 屏蔽该获取，服务数量不同，页面元素不同
#     #         # server_text = CustomerUserPage(self.driver).server_text()
#     #
#     #         time.sleep(2)
#     #         CustomerUserPage(self.driver).ReturnAssocia_server()
#     #         # 取返回关联项页面的标题
#     #         Associa_title = CustomerUserPage(self.driver).Edit_title()
#     #         CustomerUserPage(self.driver).associate_GoBack()
#     #         # CustomerUserPage(self.driver).Searchuser('祥龙十八章')
#     #         # userempty = CustomerUserPage(self.driver).userempty()
#     #         addtext = self.driver.find_element_by_id('AddSubCompany').get_attribute('title')
#     #         self.assertEqual(Associa_title, '设置关联项', msg='设置部门关联服务-返回关联项失败')
#     #         self.assertEqual(addtext, '添加客户', msg='编辑客户提交服务后点击返回列表失败')
#     #         # self.assertEqual(server_text, '', msg='添加客户进入关联服务页不选择任何服务直接提交后二次查看服务不为空')
#     #     except Exception as msg:
#     #         Base.get_windows_img(self)
#     #         self.logger.error('添加客户进入关联服务页不选择任何服务直接提交报错'+str(msg))
#
#     # 填写必填创建一个用户 ok
#     def test_010_adduser_required(self):
#         # 先创建一个必填客户
#         # 创建一个必填用户，客户选择第一步中创建的客户
#         # 在用户列表中搜索创建的用户，进入用户编辑页面，用户信息显示正确
#         try:
#             login_num = CustomerUserCommon(self.driver).userrequiredcommom()[0]
#             user_true_text = [None,'何必填','何', '必填', login_num,None, None, login_num, None,
#                               None, None, None, None, None, None, None, None, 'valid']
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             Validusesrnumbe = CustomerUserPage(self.driver).getValidusesrnumber()
#             time.sleep(5)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#             for i in range(len(usermsg)):
#                 if usermsg[i] == '':
#                     usermsg[i] = None
#                 self.assertEqual(usermsg[i], user_true_text[i], '虽然填写必填添加用户成功，但是二次进入信息显示错误')
#             self.assertEqual(Validusesrnumbe, '有效 ( 1 )', msg='填写必填项添加用户失败')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('填写必填项添加用户失败'+str(msg))
#
#
#     # 填写全填创建一个用户 ok
#     # 0814bug 2020081428000021  全填创建用户后二次打开邮件地址和手机号不显示  0828恢复
#     def test_011_userfull(self):
#         # 先创建一个必填客户
#         # 创建一个必填用户，客户选择第一步中创建的客户
#         # 在用户列表中搜索创建的用户，进入用户编辑页面，用户信息显示正确
#         try:
#             # 暂缺区域创建，后续补充
#             str1 = CustomerUserCommon(self.driver).userfullcommom()
#             login_num = str1[0]
#             Mobile = str1[2]
#             user_true_text = ['全填标题','何全填','何', '全填', login_num,None, login_num+'@qq.com', login_num, None,
#                               '全填电话', '全填传真', Mobile, '全填街道','全填邮编', '全填城市', '全填国家', '全填备注',  'valid']
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             # Validusesrnumbe = CustomerUserPage(self.driver).getValidusesrnumber()
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#             for i in range(len(usermsg)):
#                 # print(usermsg[i])
#                 if i == 11:
#                     usermsg[i] = str(usermsg[i]).replace(' ', '')
#                 if usermsg[i] == '':
#                     usermsg[i] = None
#                 # print(usermsg[i])
#                 self.assertEqual(usermsg[i], user_true_text[i], msg='虽然填写全填添加用户成功，但是二次进入信息显示错误')
#             # self.assertEqual(Validusesrnumbe,'有效 ( 1 )', msg='填写全填项添加用户失败')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('填写全填项添加用户失败'+str(msg))
#
#
#     # 添加用户-返回  ok
#     def test_012_adduser_back(self):
#         try:
#             CustomerUserCommon(self.driver).Companyrequiredcommon()
#             CustomerUserPage(self.driver).Companysub()
#             time.sleep(2)
#             CustomerUserPage(self.driver).associate_GoBack()
#             time.sleep(2)
#             CustomerUserPage(self.driver).adduser()
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_adduser_back()
#             # 搜索一个不存在的用户验证返回成功
#             addtext = self.driver.find_element_by_id('AddSubCompany').get_attribute('title')
#             # CustomerUserPage(self.driver).Searchuser('瞎弄弄堂十八湾')
#             # time.sleep(2)
#             # userempty = CustomerUserPage(self.driver).userempty()
#             self.assertEqual(addtext, '添加客户', msg='客户用户-添加用户页面-返回列表失败')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('客户用户-添加用户页面-返回列表失败'+str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # # 检查添加用户页面的必填项 ok
#     def test_013_user_required(self):
#         try:
#             # 进入页面先检查一次提交按钮是否可用
#
#             login = GetTimeCommon(self.driver).get_time()
#             CustomerUserCommon(self.driver).Companyrequiredcommon()
#             CustomerUserPage(self.driver).Companysub()
#             time.sleep(2)
#             CustomerUserPage(self.driver).associate_GoBack()
#             # 创建一个用户
#             time.sleep(8)
#
#             CustomerUserPage(self.driver).adduser()
#             time.sleep(3)
#             CustomerUserPage(self.driver).clear_userlogin()
#             CustomerUserPage(self.driver).user_vaild_dete()
#             time.sleep(3)
#             enabled_a = CustomerUserPage(self.driver).adduser_Submit_enabled()
#             self.assertEqual(enabled_a, False, msg='错误：不填写任何必填项，提交按钮可点击')
#             CustomerUserPage(self.driver).userfullname('何测试')
#             enabled_b = CustomerUserPage(self.driver).adduser_Submit_enabled()
#             self.assertEqual(enabled_b, False ,msg = '错误：只填写姓名，提交按钮可点击' )
#             CustomerUserPage(self.driver).userlogin(login)
#             enabled_c = CustomerUserPage(self.driver).adduser_Submit_enabled()
#             self.assertEqual(enabled_c, False, msg='错误：只填写姓名，账号，提交按钮可点击')
#
#             enabled_d = CustomerUserPage(self.driver).adduser_Submit_enabled()
#             self.assertEqual(enabled_d, False, msg='错误：只填写姓名，账号，有效性，提交按钮可点击')
#
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('客户用户-添加用户页面-必填项验证出错'+str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 重复用户账号  ok
#     # 0814 重复提示语的id被丢弃  0828恢复
#     def test_014_repeatuser(self):
#         try:
#             str1 = CustomerUserCommon(self.driver).userrequiredcommom()
#             login_num = str1[0]
#             name = str1[1]
#             time.sleep(3)
#             CustomerUserPage(self.driver).adduser()
#             time.sleep(3)
#             # CustomerUserPage(self.driver).click_usercustomerid()
#             # CustomerUserPage(self.driver).selectcustomer(name)
#             CustomerUserPage(self.driver).userlogin_enter(login_num)
#             time.sleep(3)
#             CustomerUserPage(self.driver).userfullname('何测试')
#             # time.sleep(2)
#             # CustomerUserPage(self.driver).uservaild()
#             time.sleep(10)
#             repeat_userlogin = CustomerUserPage(self.driver).repeat_userlogin()
#             self.assertEqual(repeat_userlogin,'数据校验不通过，该值已存在，请重新输入！',msg='添加用户页面-账户重复未提示')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('客户用户-添加用户页面-账户重复未提示'+str(msg))
#
#     # 编辑用户不修改任何信息直接提交
#     # 0814 bug  2020081228000196  0828恢复
#     def test_015_usernoeditcommit(self):
#         try:
#             str1 = CustomerUserCommon(self.driver).userfullcommom()
#             login_num = str1[0]
#             Mobile = str1[2]
#             user_true_text = ['全填标题','何全填','何', '全填', login_num,None, login_num+'@qq.com', login_num, None,
#                               '全填电话', '全填传真', Mobile, '全填街道','全填邮编', '全填城市', '全填国家', '全填备注',  'valid']
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(3)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_adduser_Submit()
#             time.sleep(2)
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#             for i in range(len(usermsg)):
#                 if i == 11:
#                     usermsg[i] = str(usermsg[i]).replace(' ','')
#                 if usermsg[i] == '':
#                     usermsg[i] = None
#                 self.assertEqual(usermsg[i],user_true_text[i] ,msg='编辑用户不修改内容直接提交，二次进入信息显示错误' )
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('编辑用户不修改任何信息直接提交出错'+str(msg))
#
#     # 编辑修改用户必填项    # 0723修改ok
#     # 0814 有效无效tab的id 被丢弃
#     def test_016_useredit_requeired(self):
#         try:
#             str1 = CustomerUserCommon(self.driver).userfullcommom()
#             login_num = str1[0]
#             Mobile = str1[2]
#             login_num_new = login_num + 'new'
#             user_true_text = ['全填标题','宋修改','宋', '修改', login_num_new, None, login_num+'@qq.com', login_num, None,
#                               '全填电话', '全填传真', Mobile, '全填街道','全填邮编', '全填城市', '全填国家', '全填备注',  'invalid']
#             time.sleep(8)
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             # 修改用户必填 ,姓名、姓、名、有效性
#             CustomerUserPage(self.driver).userinvaild()
#             CustomerUserPage(self.driver).userlogin(login_num_new)
#             CustomerUserPage(self.driver).userfullname('宋修改')
#             CustomerUserPage(self.driver).userlastname('宋')
#             CustomerUserPage(self.driver).userfirstname('修改')
#             time.sleep(5)
#             CustomerUserPage(self.driver).click_adduser_Submit()
#             # 必须的强制等待
#             time.sleep(8)
#             # 切换到无效按钮
#             CustomerUserPage(self.driver).click_invaliduser()
#             time.sleep(1)
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#             for i in range(len(usermsg)):
#                 if i == 11:
#                     usermsg[i] = str(usermsg[i]).replace(' ', '')
#                 if usermsg[i] == '':
#                     usermsg[i] = None
#                 self.assertEqual(usermsg[i], user_true_text[i], msg='修改用户必填项，二次进入信息显示错误' )
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('编辑用户修改必填项出错'+str(msg))
#
#
#     # 编辑修改用户非必填项   ok
#     # 0810 数据校验耗时过长影响操作，暂时屏蔽改用例 0828恢复
#     # @Base.screenshot_about_case
#     def test_017_useredit_notrequeired(self):
#         # try:
#         str1 = CustomerUserCommon(self.driver).userfullcommom()
#         login_num = str1[0]
#         Mobile0 = random.randint(1000, 9999)
#         newMobile = '138' + str(Mobile0) + str(Mobile0)
#         email = login_num + '@163.com'
#         (city, phone, street, zip, Comment, Country, Fax ,pwd, title) = \
#             ['newcity','4587987' ,'new街道' ,'mewzip' ,'newComment','newCountry','newFax', '123456','new标题']
#         user_true_text = [title,'何全填','何', '全填', login_num,None, email, login_num, None,
#                           phone, Fax, newMobile, street,zip, city, Country, Comment,  'valid']
#         CustomerUserPage(self.driver).Searchuser(login_num)
#         time.sleep(3)
#         CustomerUserPage(self.driver).click_Searchfirstuser()
#         time.sleep(2)
#         # 修改值
#         CustomerUserPage(self.driver).usertitle(title)
#         CustomerUserPage(self.driver).userpwd(pwd)
#         CustomerUserPage(self.driver).useremail(email)
#         CustomerUserPage(self.driver).userphone(phone)
#         CustomerUserPage(self.driver).userfax(Fax)
#         CustomerUserPage(self.driver).usermobile(newMobile)
#         CustomerUserPage(self.driver).userstreet(street)
#         CustomerUserPage(self.driver).userzip(zip)
#         CustomerUserPage(self.driver).usercity(city)
#         CustomerUserPage(self.driver).usercountry(Country)
#         CustomerUserPage(self.driver).usercommom(Comment)
#         CustomerUserPage(self.driver).click_adduser_Submit()
#         time.sleep(2)
#         CustomerUserPage(self.driver).Searchuser(login_num)
#         time.sleep(2)
#         CustomerUserPage(self.driver).click_Searchfirstuser()
#         time.sleep(2)
#         usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#         for i  in range(len(usermsg)):
#             if i == 11:
#                 usermsg[i] = str(usermsg[i]).replace(' ', '')
#             if usermsg[i] == '':
#                 usermsg[i] = None
#             self.assertEqual(usermsg[i], user_true_text[i], msg='修改用户非必填项，二次进入信息显示错误' )
#
#
#     # 填写用户非必填项
#     # 0814 二次打开页面时，邮箱、手机号不显示
#     def test_018_filluser_notrequeired(self):
#         try:
#             str1 = CustomerUserCommon(self.driver).userrequiredcommom()
#             login_num = str1[0]
#             Mobile0 = random.randint(1000, 9999)
#             newMobile = '138' + str(Mobile0) + str(Mobile0)
#             email = login_num + '@163.com'
#             (city, phone, street, zip, Comment, Country, Fax, pwd, title) = \
#                 ['fillusercity', '4587987', 'filluser街道', 'filluserzip', 'filluserComment', 'filluserCountry', 'filluserFax', '123456', 'filluser标题']
#             user_true_text = [title, '何必填', '何', '必填', login_num, None, email, login_num, None,
#                               phone, Fax, newMobile, street, zip, city, Country, Comment, 'valid']
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(3)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             # 填写值
#             CustomerUserPage(self.driver).usertitle(title)
#             CustomerUserPage(self.driver).userpwd(pwd)
#             CustomerUserPage(self.driver).useremail(email)
#             CustomerUserPage(self.driver).userphone(phone)
#             CustomerUserPage(self.driver).userfax(Fax)
#             CustomerUserPage(self.driver).usermobile(newMobile)
#             CustomerUserPage(self.driver).userstreet(street)
#             CustomerUserPage(self.driver).userzip(zip)
#             CustomerUserPage(self.driver).usercity(city)
#             CustomerUserPage(self.driver).usercountry(Country)
#             CustomerUserPage(self.driver).usercommom(Comment)
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_adduser_Submit()
#             time.sleep(2)
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#             for i in range(len(usermsg)):
#                 if i == 11:
#                     usermsg[i] = str(usermsg[i]).replace(' ', '')
#                 if usermsg[i] == '':
#                     usermsg[i] = None
#                 self.assertEqual(usermsg[i], user_true_text[i] ,msg='填写用户非必填项，二次进入信息显示错误')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('填写用户非必填项二次编辑进入显示错误' + str(msg))
#
#     # 0714添加编辑客户页面已经取消负责人的显示，该测试例子取消
#     # 设置一个负责人后，再删除一个负责人
#     # def test_019_setone_Responsible(self):
#     #     # 必填项创建客户，再创建一个
#     #     try:
#     #         str1 = CustomerUserCommon(self.driver).userrequiredcommom()
#     #         # 编辑客户
#     #         time.sleep(2)
#     #         CustomerUserPage(self.driver).EditCompany()
#     #         time.sleep(5)
#     #         CustomerUserPage(self.driver).click_Responsible()
#     #         CustomerUserPage(self.driver).click_Responsible_Select()
#     #         CustomerUserPage(self.driver).click_Responsible_closeOption()
#     #         CustomerUserPage(self.driver).Companysub()
#     #         CustomerUserPage(self.driver).associate_GoBack()
#     #         time.sleep(3)
#     #         CustomerUserPage(self.driver).EditCompany()
#     #         time.sleep(5)
#     #         # 取值
#     #         company_true_text = [str1[0] ,'何 必填',str1[1],None,None,None,None,None,None,None,None,'有效']
#     #         company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#     #         for i in range(len(company_all_text)):
#     #             if company_all_text[i] == '':
#     #                 company_all_text[i] = None
#     #             self.assertEqual(company_all_text[i],company_true_text[i], msg = '添加一个负责人错误')
#     #
#     #         CustomerUserPage(self.driver).click_Responsible_dele()
#     #         CustomerUserPage(self.driver).Companysub()
#     #         CustomerUserPage(self.driver).associate_GoBack()
#     #         time.sleep(3)
#     #         CustomerUserPage(self.driver).EditCompany()
#     #         time.sleep(5)
#     #         company_true_dele_text = [str1[0], None, str1[1], None, None, None, None, None, None, None, None, '有效']
#     #         company_alldele_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#     #
#     #         for i in range(len(company_alldele_text)):
#     #             if company_alldele_text[i] == '':
#     #                 company_alldele_text[i] = None
#     #             self.assertEqual(company_alldele_text[i], company_true_dele_text[i], msg='删除一个负责人错误')
#     #
#     #     except Exception as msg:
#     #         Base.get_windows_img(self)
#     #         self.logger.error('添加/删除一个负责人错误' + str(msg))
#
#     # 0714添加编辑客户页面已经取消负责人的显示，该测试例子取消
#     # 设置多个客户负责人(设置三个)，20200623设置多负责人存在bug
#     # def test_020_setthree_Responsible(self):
#     #     # 必填项创建客户，创建3个用户
#     #     try:
#     #         str1 = CustomerUserCommon(self.driver).userrequiredcommom()
#     #         # 编辑客户
#     #         time.sleep(2)
#     #         # 继续创建2个用
#     #         user1 = CustomerUserCommon(self.driver).userrequiredcommom2()[1]
#     #         user2 = CustomerUserCommon(self.driver).userrequiredcommom2()[1]
#     #         CustomerUserPage(self.driver).EditCompany()
#     #         time.sleep(5)
#     #         CustomerUserPage(self.driver).click_Responsible()
#     #         CustomerUserPage(self.driver).click_Responsible_Select()
#     #         CustomerUserPage(self.driver).click_Responsible_closeOption()
#     #         CustomerUserPage(self.driver).Companysub()
#     #         CustomerUserPage(self.driver).associate_GoBack()
#     #         time.sleep(3)
#     #         CustomerUserPage(self.driver).EditCompany()
#     #         time.sleep(3)
#     #         # 取值
#     #         company_true_text = [str1[0] ,'何 必填'+user1+user2,str1[1],None,None,None,None,None,None,None,None,'有效']
#     #         company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#     #         print(company_all_text)
#     #         print(user1,user2)
#     #         for i in range(len(company_all_text)):
#     #             if company_all_text[i] == '':
#     #                 company_all_text[i] = None
#     #             # 区域存在bug，跳过bug
#     #             if i == 4:
#     #                 pass
#     #             else:
#     #                 self.assertEqual(company_all_text[i],company_true_text[i], msg = '添加多个负责人失败')
#     #     except Exception as msg:
#     #         Base.get_windows_img(self)
#     #         self.logger.error('添加多个负责人失败' + str(msg))
#     # 设置子集为父部门
#     def test_021_setParentCustomer(self):
#         try:
#             CustomerUserCommon(self.driver).Companyrequiredcommon()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             str2 = CustomerUserCommon(self.driver).Companyrequiredcommon2()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             str3 = CustomerUserCommon(self.driver).Companyrequiredcommon2()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             company_true_text = [str3[1], str3[0], str2[0], None, None, None, None, None, None, None, '有效']
#             CustomerUserPage(self.driver).EditCompany()
#             time.sleep(5)
#             company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#
#             for i in range(len(company_all_text)):
#                 if company_all_text[i] == '':
#                     company_all_text[i] = None
#                 self.assertEqual(company_all_text[i], company_true_text[i], msg='设置子级为父部门失败')
#
#             # 删除部门-提交-编辑-取值-对比
#             CustomerUserPage(self.driver).ParentCustomer_dele()
#             time.sleep(2)
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             time.sleep(3)
#             CustomerUserPage(self.driver).EditCompany()
#             time.sleep(5)
#             company_true_dele_text = [str3[1],str3[0], None, None , None, None, None, None, None, None, '有效']
#             company_alldele_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#             for i in range(len(company_alldele_text)):
#                 if company_alldele_text[i] == '':
#                     company_alldele_text[i] = None
#                 self.assertEqual(company_alldele_text[i], company_true_dele_text[i], msg='删除父部门失败')
#
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('设置子级/删除部门负责人失败' + str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 选择父部门问题  #0723修改ok
#     def test_022_changeParentCustomer(self):
#         try:
#             CustomerID = str(random.randint(100000, 999999))
#             CompanyName = 'name' + CustomerID
#             str1 = CustomerUserCommon(self.driver).Companyrequiredcommon()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             str2 = CustomerUserCommon(self.driver).Companyrequiredcommon2()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             # 新增客户-选择父部门-提交-取值-对比
#             CustomerUserPage(self.driver).AddCompany()
#             time.sleep(3)
#             # 客户编号
#             CustomerUserPage(self.driver).CustomerID(CustomerID)
#             # 客户名称
#             CustomerUserPage(self.driver).CompanyName(CompanyName)
#             # 选择父部门
#             CustomerUserPage(self.driver).select_ParentCustomer(str1[0])
#             # 选择有效
#             CustomerUserPage(self.driver).valid()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#
#             company_true_text = [CustomerID, CompanyName, str1[0], None, None, None, None, None, None, None, '有效']
#             CustomerUserPage(self.driver).EditCompany()
#             time.sleep(5)
#             company_all_text = list(CustomerUserCommon(self.driver).get_company_alltext())
#
#             for i in range(len(company_all_text)):
#                 if company_all_text[i] == '':
#                     company_all_text[i] = None
#                 self.assertEqual(company_all_text[i], company_true_text[i], msg='修改父部门失败')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('修改父部门' + str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 添加客户，必填项空格输入   SC_CustomerUser_17  ok
#     # 0814 2020081328000023  系统必填项允许只输入空格  0828 恢复
#     def test_023_addcompany_Spaceinput(self):
#         try:
#             EntranceAgentPage(self.driver).enter_customer_user()
#             time.sleep(8)
#             CustomerUserPage(self.driver).AddCompany()
#             time.sleep(5)
#             # 客户编号
#             CustomerUserPage(self.driver).CustomerID('     ')
#             # 客户名称
#             CustomerUserPage(self.driver).CompanyName('     ')
#             CustomerUserPage(self.driver).valid()
#             # 判断提交按钮是否可以触发
#             enabled_a = CustomerUserPage(self.driver).submit_enabled()
#             self.assertFalse(enabled_a, msg= '添加客户时，必填项只输入空格，校验通过')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('添加客户时，必填项只输入空格，校验通过' + str(msg))
#
#     # 添加客户，编号、名称、邮编、城市、街道、网址、备注输入类型验证  ok
#     def test_024_addcompany_inputtype(self):
#         try:
#             EntranceAgentPage(self.driver).enter_customer_user()
#             time.sleep(8)
#             CustomerUserPage(self.driver).AddCompany()
#             time.sleep(5)
#             CustomerID = 'diantong' + str(random.randint(1, 100000))+'@#客户:id'
#             CompanyName = 'diantong' + str(random.randint(1, 100000))+'@#客户:name'
#             CompanyStreet = 'diantong12315@#街道:Street'
#             CompanyURL = 'http://diantong.com/cn/123/网址@#'
#             CompanyComment = 'diantong12315@#备注:Comment'
#             CompanyZIP = 'diantong12315@#邮编:ZIP'
#             CompanyCity = 'diantong12315@#城市:City'
#             CustomerUserPage(self.driver).CustomerID(CustomerID)
#             # 客户名称
#             CustomerUserPage(self.driver).CompanyName(CompanyName)
#             CustomerUserPage(self.driver).CompanyStreet(CompanyStreet)
#             CustomerUserPage(self.driver).CompanyZIP(CompanyZIP)
#             CustomerUserPage(self.driver).CompanyCity(CompanyCity)
#             CustomerUserPage(self.driver).CompanyURL(CompanyURL)
#             CustomerUserPage(self.driver).CompanyComment(CompanyComment)
#             CustomerUserPage(self.driver).valid()
#             time.sleep(3)
#             # 提交后进入编辑页面
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             time.sleep(2)
#             CustomerUserPage(self.driver).EditCompany()
#             time.sleep(2)
#             # 编辑页面取值
#             company_true_text = [CustomerID ,  CompanyName,None,None,CompanyStreet,CompanyZIP,CompanyCity,None,CompanyURL,CompanyComment,'有效']
#             company_alltext = list(CustomerUserCommon(self.driver).get_company_alltext())
#             for i in range(len(company_alltext)):
#                 if company_alltext[i] == '':
#                     company_alltext[i] = None
#                 self.assertEqual(company_alltext[i], company_true_text[i], msg='添加客户:编号名称、邮编、城市、街道、网址、备注输入类型存在问题')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('添加客户:编号名称、邮编、城市、街道、网址、备注输入类型存在问题' + str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 添加客户，编号、名称、邮编、城市、街道、网址、备注输入长度验证
#     def test_025_addcompany_Longcharacters(self):
#         try:
#             get_number = str(GetTimeCommon(self.driver).get_number())
#             CustomerID1 = str(GetTimeCommon(self.driver).get_number())
#             CustomerID2 = str(GetTimeCommon(self.driver).get_number())
#             for i in range(0, 3):
#                 get_number += get_number
#             for i in range(0, 2):
#                 CustomerID1 += CustomerID1
#             for i in range(0, 3):
#                 CustomerID2 += CustomerID2
#             CustomerID = 'ID'+CustomerID1+CustomerID2
#             CompanyName = 'Name' + get_number
#             CompanyURL = 'URL' + get_number
#             CompanyStreet = 'Street' + get_number
#             CompanyComment = 'Comment' + get_number
#             CompanyZIP = 'ZIP' + get_number
#             CompanyCity = 'City' + get_number
#             EntranceAgentPage(self.driver).enter_customer_user()
#             time.sleep(8)
#             CustomerUserPage(self.driver).AddCompany()
#             time.sleep(5)
#             CustomerUserPage(self.driver).CustomerID(CustomerID)
#             # 客户名称
#             CustomerUserPage(self.driver).CompanyName(CompanyName)
#             CustomerUserPage(self.driver).CompanyStreet(CompanyStreet)
#             CustomerUserPage(self.driver).CompanyZIP(CompanyZIP)
#             CustomerUserPage(self.driver).CompanyCity(CompanyCity)
#             CustomerUserPage(self.driver).CompanyURL(CompanyURL)
#             CustomerUserPage(self.driver).CompanyComment(CompanyComment)
#             CustomerUserPage(self.driver).valid()
#             time.sleep(3)
#             # 提交后进入编辑页面
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             time.sleep(2)
#             CustomerUserPage(self.driver).EditCompany()
#             time.sleep(2)
#             # 编辑页面取值
#             company_true_text = [CustomerID,  CompanyName, None, None, CompanyStreet, CompanyZIP, CompanyCity, None,
#                                  CompanyURL, CompanyComment, '有效']
#             company_alltext = list(CustomerUserCommon(self.driver).get_company_alltext())
#             for i in range(len(company_alltext)):
#                 if company_alltext[i] == '':
#                     company_alltext[i] = None
#                 self.assertEqual(company_alltext[i], company_true_text[i], msg='错误:编号名称、邮编、城市、街道、网址、备注输入最大字符200未通过验证')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('错误:编号名称、邮编、城市、街道、网址、备注输入最大字符200未通过验证' + str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 添加用户时，必填项只输入空格
#     # 0814 2020081328000023 bug必填项允许了空格输入并且提交成功   0828恢复
#     def test_026_adduser_Spaceinput(self):
#         try:
#             CustomerUserCommon(self.driver).Companyrequiredcommon()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             CustomerUserPage(self.driver).adduser()
#             time.sleep(5)
#             CustomerUserPage(self.driver).userfullname('     ')
#             CustomerUserPage(self.driver).userlastname('     ')
#             CustomerUserPage(self.driver).userfirstname('     ')
#             CustomerUserPage(self.driver).userlogin('        ')
#             CustomerUserPage(self.driver).uservaild()
#             time.sleep(2)
#             enabled_a = CustomerUserPage(self.driver).adduser_Submit_enabled()
#             self.assertFalse(enabled_a, msg='错误：添加用户必填项只输入空格，校验通过')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('错误：添加用户必填项只输入空格，校验通过' + str(msg))
#
#     # 验证用户姓名、账号输入类型
#     def test_027_adduser_inputtype(self):
#         try:
#             userreturn = CustomerUserCommon(self.driver).Companyrequiredcommon()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             CustomerUserPage(self.driver).adduser()
#             time.sleep(5)
#             fullname = 'fullname'+ str(GetTimeCommon(self.driver).get_number())+ '@ #全名:id'
#             lastname = 'lastname'+ str(GetTimeCommon(self.driver).get_number())+ '@ #姓:id'
#             firstname = 'firstname' + str(GetTimeCommon(self.driver).get_number()) + '@ #名:id'
#             login_num = 'login_num' + str(GetTimeCommon(self.driver).get_number()) + '@ #账号:id'
#             CustomerUserPage(self.driver).userfullname(fullname)
#             CustomerUserPage(self.driver).userlastname(lastname)
#             CustomerUserPage(self.driver).userfirstname(firstname)
#             CustomerUserPage(self.driver).userlogin(login_num)
#             CustomerUserPage(self.driver).uservaild()
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_adduser_Submit()
#             # 搜索用户
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             user_true_text = [None, fullname,lastname, firstname, login_num, None, None, userreturn[1], None,
#                               None, None, None, None, None, None, None, None, 'valid']
#             usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#             for i in range(len(usermsg)):
#                 if usermsg[i] == '':
#                     usermsg[i] = None
#                     self.assertEqual(usermsg[i], user_true_text[i], msg='错误：添加用户必填项输入类型校验出错')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('错误：添加用户必填项输入类型校验出错' + str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 验证用户姓名、账号输入长度
#     def test_028_adduser_Longcharacters(self):
#         # 账号200，全名250，姓、名100
#         try:
#             get_number = str(GetTimeCommon(self.driver).get_number())
#             get_number2 = str(GetTimeCommon(self.driver).get_number())
#             for i in range(0, 3):
#                 get_number += get_number
#             for i in range(0, 3):
#                 get_number2 += get_number2
#             fullname = 'fullname' + get_number
#             login_num = 'login' + get_number
#             lastname = 'la' + get_number2
#             firstname = 'fi' + get_number2
#             userreturn = CustomerUserCommon(self.driver).Companyrequiredcommon()
#             CustomerUserPage(self.driver).Companysub()
#             CustomerUserPage(self.driver).associate_GoBack()
#             CustomerUserPage(self.driver).adduser()
#             time.sleep(5)
#             CustomerUserPage(self.driver).userfullname(fullname)
#             CustomerUserPage(self.driver).userlastname(lastname)
#             CustomerUserPage(self.driver).userfirstname(firstname)
#             CustomerUserPage(self.driver).userlogin(login_num)
#             CustomerUserPage(self.driver).uservaild()
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_adduser_Submit()
#             # 搜索用户
#             CustomerUserPage(self.driver).Searchuser(login_num)
#             time.sleep(2)
#             CustomerUserPage(self.driver).click_Searchfirstuser()
#             time.sleep(2)
#             user_true_text = [None, fullname,lastname, firstname, login_num, None, None, userreturn[1], None,
#                               None, None, None, None, None, None, None, None, 'valid']
#             usermsg = list(CustomerUserCommon(self.driver).getuser_alltext())
#             for i in range(len(usermsg)):
#                 if usermsg[i] == '':
#                     usermsg[i] = None
#                     self.assertEqual(usermsg[i], user_true_text[i], msg='错误：添加用户必填项长度200检验出错')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('错误：添加用户必填项长度200检验出错' + str(msg))
#             # self.assertEqual(msg, '', '用例执行失败')
#
#     # 0810邮箱校验耗时太长，暂时屏蔽用例   0828恢复
#     # 添加用户，验证邮箱重复
#     def test_029_adduser_repeatemil(self):
#         try:
#             userreturn = CustomerUserCommon(self.driver).userfullcommom()
#             useremail = userreturn[3]
#             CustomerUserPage(self.driver).adduser()
#             time.sleep(5)
#             CustomerUserPage(self.driver).useremail_enter(useremail)
#             time.sleep(4)
#             # 向邮件地址输入框中输入回车键
#             CustomerUserPage(self.driver).uservaild()
#             repeat_UserEmail = CustomerUserPage(self.driver).repeat_UserEmail()
#             self.assertEqual(repeat_UserEmail,'数据校验不通过，该值已存在，请重新输入！', msg='错误：用户邮件地址重复未提示')
#         except Exception as msg:
#             Base.get_windows_img(self)
#             self.logger.error('错误：用户邮件地址重复未提示' + str(msg))
#
#     # # 用户密码可见与隐藏，修改用户密码，修改密码未完成（暂无客户页面）
#     # def test_030_user_modifypwd(self):
#     #     #全填创建一个用户
#     #     try:
#     #         newpwd = '13878190014'
#     #         userreturn = CustomerUserCommon(self.driver).userfullcommom()
#     #         login_num = userreturn[0]
#     #         time.sleep(2)
#     #         CustomerUserPage(self.driver).Searchuser(login_num)
#     #         time.sleep(2)
#     #         CustomerUserPage(self.driver).click_Searchfirstuser()
#     #         time.sleep(2)
#     #         # 输入密码
#     #         CustomerUserPage(self.driver).userpwd(newpwd)
#     #         hidepwdtype = CustomerUserPage(self.driver).userpwd_type()
#     #         CustomerUserPage(self.driver).click_userpwd_eyeicon()
#     #         displaypwdtype = CustomerUserPage(self.driver).userpwd_type()
#     #         CustomerUserPage(self.driver).click_adduser_Submit()
#     #         print(hidepwdtype, displaypwdtype)
#     #         self.assertEqual(displaypwdtype, 'text' , msg='错误：密码显示错误')
#     #         self.assertEqual(hidepwdtype, 'password', msg='错误：密码隐藏错误')
#     #         # 检查客户用户 登录页面 login_num  ，newpwd
#     #     except Exception as msg:
#     #         Base.get_windows_img(self)
#     #         self.logger.error('错误：用户密码显示与隐藏出错' + str(msg))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
