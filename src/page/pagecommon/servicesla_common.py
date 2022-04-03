"""
@author: DT_testing
@file:   servicesla_common.py
@desc:  【创建必填值填写的客户、用户 及 全部填写字段的组】
@step：  都是客户用户页面内部的值填写
"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.servicesla_page import ServiceSlaPage
from src.page.pagecommon.get_time_common import GetTimeCommon
import random


class ServiceSlaCommon(ServiceSlaPage):
    def Serviceslarequiredcommon(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_sla()
        ServiceSlaPage(self.driver).clickaddsla()
        ServiceSlaPage(self.driver).inputslaname(name)
        ServiceSlaPage(self.driver).clickslavalid()
        ServiceSlaPage(self.driver).clickslasubmit()
        slainfo = {'slaname': name}
        return slainfo

    def Serviceslarequiredcommon2(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_sla()
        time.sleep(3)
        ServiceSlaPage(self.driver).clickaddsla()
        ServiceSlaPage(self.driver).inputslaname(name)
        ServiceSlaPage(self.driver).clickslavalid()
        slainfo = {'slaname': name}
        return slainfo

    # 为检查页面元素添加，值输入值
    def Serviceslarequiredcommon3(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        ServiceSlaPage(self.driver).inputslaname(name)
        ServiceSlaPage(self.driver).clickslavalid()
        slainfo = {'slaname': name}
        return slainfo

    # 填写必填添加指标
    def targetrequiredcommon(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('tarname' + strnumber)
        field = str('field' + strnumber)
        time.sleep(5)
        ServiceSlaPage(self.driver).inputtargetfield(field)
        ServiceSlaPage(self.driver).inputtargetname(name)
        ServiceSlaPage(self.driver).clickaddup()
        ServiceSlaPage(self.driver).targetvalid()
        targetinfo = {'field': field, 'name': name}
        return targetinfo

    # 填写全填添加指标  未完成
    def targetfullcommon(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('tarname' + strnumber)
        field = str('field' + strnumber)
        ServiceSlaPage(self.driver).inputtargetfield(field)
        ServiceSlaPage(self.driver).inputtargetname(name)
        ServiceSlaPage(self.driver).clickaddup()
        # TicketCreate  startcondition
        ServiceSlaPage(self.driver).startcondition('TicketCreate')
        time.sleep(1)
        # TicketStateUpdate
        ServiceSlaPage(self.driver).endcondition('TicketDelete')
        ServiceSlaPage(self.driver).targetvalid()
        targetinfo = {'field': field, 'name': name}
        return targetinfo


