"""
@author: DT_testing
@file:   process_case.py
@desc:  【流程管理】
@step：001. 添加流程业务类型、 创建必填流程  SC_Process_7 、 SC_Process_9、SC_Process_21
      002. 添加流程业务类型、创建流程必填校验  SC_Process_20、SC_Process_8
      003. 业务类型名称校验、流程名称校验（同名、空格）SC_Process_10、SC_Process_11、SC_Process_23、SC_Process_24
      004. 查询业务类型、编辑业务类型，编辑流程 SC_Process_14、SC_Process_15、SC_Process_17、SC_Process_18 1



"""
import time

from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.service_commom import ServiceCommon
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.agent.generic_page import GenericPage
from src.page.pagecommon.process_common import ProcessCommon
from src.page.agent.process_page import ProcessPage

import random
from common.base import Base


class ProcessCase(BaseCaseUser, Base):
    def test_001(self):
        EntranceAgentPage(self.driver).enter_processmanagement()
        time.sleep(10)
        process_type_info = ProcessCommon(self.driver).process_type_common()
        process_type_name = process_type_info.get('name')
        ProcessPage(self.driver).type_submit()
        ProcessPage(self.driver).type_search(process_type_name)
        ProcessPage(self.driver).type_search_click(process_type_name)

        # 取无流程断言
        get_process_empty = ProcessPage(self.driver).get_process_empty()
        self.assertEqual(get_process_empty, '这里空空如也, 跟我的钱包一样', msg='创建流程业务类型失败')

        # 必填创建一个流程
        time.sleep(3)
        process_info = ProcessCommon(self.driver).process_request_common()
        process_name = process_info.get('name')
        process_describe = process_info.get('describe')
        ProcessPage(self.driver).savereturn()
        time.sleep(10)
        print('创建的流程名称为：' + process_name)

        # 搜索
        ProcessPage(self.driver).search(process_name)

        # 列表页面取名称和有效性断言
        gettable_list01 = ['', process_name, process_describe, process_type_name, '激活']
        gettable_list = ProcessPage(self.driver).gettabblelist()
        for i in range(1, len(gettable_list) - 5):
            gettable_head_one = gettable_list[i].text
            # print(gettable_head_one)
            self.assertEqual(gettable_head_one, gettable_list01[i], msg='错误：创建必填流程失败')

    def test_002(self):
        EntranceAgentPage(self.driver).enter_processmanagement()
        time.sleep(3)

        ProcessPage(self.driver).add_type()
        is_disabled_type_sumbit = ProcessPage(self.driver).is_disabled_type_sumbit()
        ProcessPage(self.driver).close_type()
        self.assertEqual(is_disabled_type_sumbit, 'true', msg='错误：添加流程业务类型必填未填写，提交按钮可触发')

        time.sleep(3)
        ProcessPage(self.driver).add()
        is_disabled_sava = ProcessPage(self.driver).is_disabled_sava()
        is_disabled_save_return = ProcessPage(self.driver).is_disabled_save_return()
        self.assertEqual(is_disabled_sava, 'true', msg='错误：添加流程必填未填写，保存按钮可触发')
        self.assertEqual(is_disabled_save_return, 'true', msg='错误：添加流程必填未填写，提交并返回按钮可触发')

    def test_003(self):

        EntranceAgentPage(self.driver).enter_processmanagement()
        time.sleep(3)
        process_type_info = ProcessCommon(self.driver).process_type_common()
        process_type_name = process_type_info.get('name')
        ProcessPage(self.driver).type_submit()

        ProcessPage(self.driver).add_type()
        # 输入重名
        ProcessPage(self.driver).send_type_name(process_type_name)
        type_name_error1 = ProcessPage(self.driver).get_type_name_error()
        self.assertEqual(type_name_error1,'该名称已存在，请更换其他名称！',msg='错误：流程业务类型重名未提示')
        # 输入空格
        ProcessPage(self.driver).send_type_name('  ')
        type_name_error2 = ProcessPage(self.driver).get_type_name_error()
        self.assertEqual(type_name_error2, '数据格式错误,请重新输入!', msg='错误：流程业务类型输入为空未提示')
        ProcessPage(self.driver).close_type()

        ProcessPage(self.driver).type_search(process_type_name)
        ProcessPage(self.driver).type_search_click(process_type_name)

        # 必填创建一个流程
        time.sleep(3)
        process_info = ProcessCommon(self.driver).process_request_common()
        process_name = process_info.get('name')
        ProcessPage(self.driver).savereturn()
        time.sleep(3)

        ProcessPage(self.driver).add()
        # 输入重名
        ProcessPage(self.driver).send_name(process_name)
        name_error1 = ProcessPage(self.driver).get_name_error()
        self.assertEqual(name_error1, '该名称已存在，请更换其他名称！', msg='错误：流程重名未提示')
        # 输入空格
        ProcessPage(self.driver).send_name('  ')
        name_error2 = ProcessPage(self.driver).get_name_error()
        self.assertEqual(name_error2, '数据格式错误,请重新输入!', msg='错误：流程名称输入为空未提示')

    def test_004(self):

        EntranceAgentPage(self.driver).enter_processmanagement()
        time.sleep(3)
        process_type_info = ProcessCommon(self.driver).process_type_common()
        process_type_name = process_type_info.get('name')
        ProcessPage(self.driver).type_submit()

        ProcessPage(self.driver).type_search(process_type_name)
        # 编辑
        ProcessPage(self.driver).edit_type(process_type_name)
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name2 = str('@#￥%*' + strnumber)
        ProcessPage(self.driver).send_type_name(name2)
        ProcessPage(self.driver).type_invalid()
        ProcessPage(self.driver).type_submit()

        # 搜索特殊字符数据
        ProcessPage(self.driver).type_search(name2)
        ProcessPage(self.driver).type_search_click(name2)
        # 取无流程断言
        get_process_empty = ProcessPage(self.driver).get_process_empty()
        self.assertEqual(get_process_empty, '这里空空如也, 跟我的钱包一样', msg='创建流程业务类型失败')

        # 搜索不存在数据
        ProcessPage(self.driver).type_search('不存在数据，祥龙')










