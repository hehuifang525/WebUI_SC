"""
@author: DT_testing
@file:   user_search_common.py
@desc:  【工单搜索】
@step：
"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.user_search_page import UserSearchPage
from src.page.pagecommon.get_time_common import GetTimeCommon
import random


class UserSearchCommon(UserSearchPage):

    # 创建一个模板，选择优先级正常
    def add_temp_commom(self):
        # 输入模板名称
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        model_name = str('ceshi' + strnumber)

        UserSearchPage(self.driver).input_model_name(model_name)
        UserSearchPage(self.driver).save_model()

        # 搜索条件-优先级选择-正常
        UserSearchPage(self.driver).add_condition("优先级")

        # 以优先级为例，查询系统内所有工单
        UserSearchPage(self.driver).search_condition_input_click(1)
        UserSearchPage(self.driver).select_by_title("正常")
        UserSearchPage(self.driver).close_optionall()
        UserSearchPage(self.driver).search_click()

        return model_name