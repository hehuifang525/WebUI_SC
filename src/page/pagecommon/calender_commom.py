# calender_commom
"""
@author: DT_testing
@file:   calender_commom.py
@desc:  【日历-工作时间管理】
@step：
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.slacalender_page import SlacalenderPage
import time
from common.base import Base


class CalenderCommom(SlacalenderPage):

    def requestcommon(self):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "工作时间必填" + strnumber
        EntranceAgentPage(self.driver).enter_slacalendar()
        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()
        SlacalenderPage(self.driver).inputname(name)
        calenderinfo = {'name': name}
        return calenderinfo

    def fullcommon(self):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "工作时间全填" + strnumber
        EntranceAgentPage(self.driver).enter_slacalendar()
        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()
        SlacalenderPage(self.driver).inputname(name)
        # 输入指定的日期
        SlacalenderPage(self.driver).chose_date2(0,"2022-01-29 01:01:01")
        # SlacalenderPage(self.driver).chose_date(0)
        SlacalenderPage(self.driver).input_name2(0, '休假日名称')

        SlacalenderPage(self.driver).chose_date2(1,"2022-01-26 01:01:01")
        # SlacalenderPage(self.driver).chose_date(1)
        SlacalenderPage(self.driver).input_name2(1, '指定工作日名称')
        Base(self.driver).move_to_pagebottom()
        SlacalenderPage(self.driver).comment('这是备注')
        calenderinfo = {'name': name}
        return calenderinfo

    def is_exist_name(self, name, list_nam):
        """
         :param name: 名称
         :param  list_nam: 传入的是搜索后的名称列表对象
            判断搜索后，当前列表中是否存在与对应名称的数据
            存在则返回1，不存在则返回0
        """
        for i in list_nam:
            listinfo = i.text
            if listinfo == name:
                yield 1
            else:
                yield 0

