"""
@author: DT_testing
@file:   process_common.py
@desc:  【流程管理】
@step：
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.process_page import ProcessPage
import time


class ProcessCommon(ProcessPage):

    # 添加业务流程类型
    def process_type_common(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('type' + strnumber)
        ProcessPage(self.driver).add_type()
        ProcessPage(self.driver).send_type_name(name)
        process_type_info = {"name": name}
        return process_type_info

    # 添加新流程-必填
    def process_request_common(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('process' + strnumber)
        ProcessPage(self.driver).add()
        ProcessPage(self.driver).send_name(name)
        ProcessPage(self.driver).send_describe('这是描述信息')
        process_info = {"name": name, 'describe':'这是描述信息' }
        return process_info

