"""
@author: DT_testing
@file:   notification_commom.py
@desc:  【工单通知】
@step：
"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.notification_page import NotificationPage
from src.page.agent.notification_page import NotificationPage
from src.page.pagecommon.get_time_common import GetTimeCommon
from common.base import Base

class NotificationCommon(NotificationPage):
    # 添加页面输入必填值
    def rquiredcommon(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        NotificationPage(self.driver).inputname(name)
        NotificationPage(self.driver).chose_first_eveents('ArticleAutoResponse')
        NotificationPage(self.driver).closeOption()
        # 滚动到页面底部
        Base(self.driver).move_to_pagebottom()
        # 输入主题
        NotificationPage(self.driver).inputsubject('测试通知主题')
        # 输入内容
        NotificationPage(self.driver).inputbody('测试通知内容')

        NotificationPage(self.driver).submit()
        Notificationinfo ={'name': name}
        return Notificationinfo
