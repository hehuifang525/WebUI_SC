"""
@author: DT_testing
@file:   service_common.py
@desc:  【服务】
@step：
"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.service_page import ServicePage
from src.page.pagecommon.get_time_common import GetTimeCommon


class ServiceCommon(ServicePage):

    # 填写必填
    def ServiceRequiredCommon(self):
        EntranceAgentPage(self.driver).enter_service()
        time.sleep(6)
        ServicePage(self.driver).add()
        time.sleep(2)
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "服务必填" + strnumber
        # 填写必填添加服务
        ServicePage(self.driver).inputname(name)
        serviceinfo = {'name': name}
        return serviceinfo

