"""
@author: DT_testing
@file:   stats_common.py
@desc:  【统计管理】
@step：
"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.stats_page import StatsPage
from src.page.pagecommon.get_time_common import GetTimeCommon
import random


class StatsCommon(StatsPage):
    # 必填创建一个统计,不包含配置xy轴
    def statsrequiredcommon(self, type1='动态矩阵', role='', format='Excel'):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        # EntranceAgentPage(self.driver).enter_stats()
        # StatsPage(self.driver).addstats()
        StatsPage(self.driver).title(name)
        StatsPage(self.driver).chosetype(type1)
        if type1 == '动态列表':
            StatsPage(self.driver).choseobject('工单清单')
        else:
            StatsPage(self.driver).choseobject('工单累计')

        # 选择权限
        StatsPage(self.driver).chosePermission(role)
        # 选择结果格式
        StatsPage(self.driver).choseFormat(format)
        StatsPage(self.driver).clickallbtn()
        StatsPage(self.driver).clickclosebtn()

        statsinfo = {'name': name}
        return statsinfo