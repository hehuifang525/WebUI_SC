"""
@author: DT_testing
@file:   cmdb_overview_common.py
@desc:  【cmdb概览】
@step： 001.必填创建一个资产
        002. 取资产表格中的指定列值



"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.cmdb_overview_page import CmdbOverviewPage
import time
from common.base import Base


class CmdbOverviewCommon(CmdbOverviewPage):

    def CmdbOverview_requestCommon(self):
        '''
            创建一个电脑分类的资产，计划中
        :return: 资产名称
        '''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "cmdb必填" + strnumber
        EntranceAgentPage(self.driver).enter_relust('电脑')
        # EntranceAgentPage(self.driver).enter_cmdb_overview()
        time.sleep(5)
        # CmdbOverviewPage(self.driver).click_add()
        # CmdbOverviewPage(self.driver).choose_class('电脑')
        CmdbOverviewPage(self.driver).click_create_template()
        CmdbOverviewPage(self.driver).input_name(name)
        CmdbOverviewPage(self.driver).choose_DeplState('已计划')
        CmdbOverviewPage(self.driver).choose_InciState('正常')
        CmdbOverviewPage(self.driver).click_commit()
        time.sleep(2)
        CmdbOverviewPage(self.driver).back_overview()
        return name

    def CmdbOverview_requestCommon2(self):
        '''
            已经进入了cmdb概览页面，创建一个电脑分类的资产，计划中
        :return: 资产名称
        '''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "cmdb必填" + strnumber
        EntranceAgentPage(self.driver).enter_relust('电脑')
        # CmdbOverviewPage(self.driver).click_add()
        # CmdbOverviewPage(self.driver).choose_class('电脑')
        CmdbOverviewPage(self.driver).click_create_template()
        CmdbOverviewPage(self.driver).input_name(name)
        CmdbOverviewPage(self.driver).choose_DeplState('已计划')
        CmdbOverviewPage(self.driver).choose_InciState('正常')
        CmdbOverviewPage(self.driver).click_commit()
        time.sleep(3)
        CmdbOverviewPage(self.driver).back_overview()
        return name


    def tablelistCommon(self,table_head,table_body):
        '''
        :param table_head: 传入表头元素
        :param table_body: 传入表格元素
        :return: 以字典形式返回列表值：类，资产生命周期，资产状态，资产名称，为了方便列表顺序被调整后，代码仍然可以
        执行
        '''
        tablelist01 = {}
        for i in range(0, len(table_head)):
            if table_head[i].text == '类':
                tablelist01['cmdbtype'] = table_body[i].text
                # tablelist01.append({'cmdbtype': table_body[i].text})
            elif table_head[i].text == '资产生命周期':
                tablelist01['DeplState'] = table_body[i].text
                # tablelist01.append({'DeplState': table_body[i].text})
            elif table_head[i].text == '资产状态':
                tablelist01['InciState'] = table_body[i].text
                # tablelist01.append({'InciState': table_body[i].text})
            elif table_head[i].text == '资产名称':
                tablelist01['name'] = table_body[i].text
                # tablelist01.append({'name': table_body[i].text})

        return tablelist01

    def tablelistCommon002(self):
        '''
        :return: 以字典形式返回列表值：资产名称,资产生命周期，资产状态，为了方便列表顺序被调整后，代码仍然可以
        执行  DeplState
        '''
        tablelist01 = {}
        tablelist01['name'] = CmdbOverviewPage(self.driver).detail_name()
        tablelist01['DeplState'] = CmdbOverviewPage(self.driver).detail_cycle()
        tablelist01['InciState'] = CmdbOverviewPage(self.driver).detail_status()
        return tablelist01