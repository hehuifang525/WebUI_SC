"""
@author: DT_testing
@file:   generic_common.py
@desc:  【】
@step：1、必填
       2、全填
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.generic_page import GenericPage
import time
from common.base import Base


class GenericCommon(GenericPage):

    def generic_required_common(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('generic' + strnumber)
        GenericPage(self.driver).add()
        GenericPage(self.driver).inputname(name)
        genericinfo = {"name": name}
        return genericinfo

    def generic_full_common(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('generic' + strnumber)
        GenericPage(self.driver).add()
        GenericPage(self.driver).inputname(name)
        GenericPage(self.driver).chose_tickect_fidld("优先级")
        GenericPage(self.driver).chose_priority("高")

        GenericPage(self.driver).chose_update_fidld("设置新的优先级")
        GenericPage(self.driver).update_priority("非常高")

        Base(self.driver).move_to_pagebottom()

        GenericPage(self.driver).new_note_from('发件人test')
        GenericPage(self.driver).new_note_subject('主题test')
        GenericPage(self.driver).send_content('内容test')
        GenericPage(self.driver).new_cmd('命令test')
        GenericPage(self.driver).new_module('模块test')

        genericinfo = {"name": name, 'from': '发件人test', 'subject': '主题test','content': '内容test',
                       'cmd': '命令test', 'module': '模块test'}
        return genericinfo

