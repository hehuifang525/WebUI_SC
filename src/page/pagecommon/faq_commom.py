"""
@author: DT_testing
@file:   faq_commom.py
@desc:  【知识库类别】
@step：
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.faq_page import FaqPage
import time


class FaqCommon(FaqPage):
    # 输入必填信息
    def Faqrequiredcommon(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        # EntranceAgentPage(self.driver).enter_faq()
        FaqPage(self.driver).inputname(name)
        FaqPage(self.driver).valid()
        faqinfo = {'name': name}
        return faqinfo