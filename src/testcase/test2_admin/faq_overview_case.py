"""
@author: DT_testing
@file:   faq_overview_case.py
@desc:  【知识库概览】
@step： 001.填写必填，点击提交按钮，
        002. 检查自定义类别的下知识打开详情页 SC_Faq_39




"""
import time

from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.service_commom import ServiceCommon
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.agent.faq_overview_page import FaqOverviewPage
from src.page.pagecommon.faq_overview_commom import FaqOverviewCommon
from src.page.agent.faq_page import FaqPage
from src.page.pagecommon.faq_commom import FaqCommon
import random


class FaqOverview(BaseCaseUser, Base):
    def test_001(self):
        '''填写必填，点击提交'''
        EntranceAgentPage(self.driver).enter_faq_overview()
        time.sleep(3)

        FaqOverviewPage(self.driver).add()
        FaqOverviewCommon(self.driver).FaqOverviewrequiredcommon('事故报告')

        FaqOverviewPage(self.driver).submit()

    def test_002(self):
        '''自定义类别添加文章'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        # 添加一个自定义的
        FaqPage(self.driver).add()
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        faq_sort_name = faqsortinfo.get("name")
        FaqPage(self.driver).submitreturn()

        EntranceAgentPage(self.driver).enter_faq_overview()
        time.sleep(2)
        FaqOverviewPage(self.driver).add()
        Overviewre_name = FaqOverviewCommon(self.driver).FaqOverviewrequiredcommon(faq_sort_name)
        FaqOverviewPage(self.driver).submit()

        # 点击编辑按钮
        FaqOverviewPage(self.driver).edit()
        time.sleep(5)
        # 取名称进行断言  gettitle
        gettitle = FaqOverviewPage(self.driver).gettitle()
        self.assertEqual(Overviewre_name.get('name'),gettitle,msg='创建自定义类别的知识，打开详情失败')





