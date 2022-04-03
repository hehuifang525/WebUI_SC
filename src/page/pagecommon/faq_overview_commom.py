"""
@author: DT_testing
@file:   faq_overview_commom.py
@desc:  【知识库类别】
@step：
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.faq_overview_page import FaqOverviewPage
import time


class FaqOverviewCommon(FaqOverviewPage):
    # 输入必填信息
    def FaqOverviewrequiredcommon(self, category):
        '''

        :param category: 类别
        :return:
        '''
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('FaqOver' + strnumber)

        FaqOverviewPage(self.driver).send_context('这是知识库的正文内容')
        FaqOverviewPage(self.driver).inputtitle(name)
        FaqOverviewPage(self.driver).category(category)
        faqinfo = {'name': name}
        return faqinfo