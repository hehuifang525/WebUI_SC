
"""
@author: testing
@file:   content_template_common.py
@desc:  【内容模板】
@step：
"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.content_template_page import ContentTemplatePage
from src.page.pagecommon.get_time_common import GetTimeCommon
from common.base import Base


class ContentTemplateCommon(ContentTemplatePage):

    # 创建必填
    def content_template_required_common(self, valid):
        now_time = GetTimeCommon(self.driver).get_time()
        tempname = "temp必填_" + now_time

        ContentTemplatePage(self.driver).name_in(tempname)
        ContentTemplatePage(self.driver).role("Misc")
        # ContentTemplatePage(self.driver).subject_in("这是内容模板的主题")
        # ContentTemplatePage(self.driver).content_in("设置内容模板的正文")

        if valid == "invalid":
            ContentTemplatePage(self.driver).invalid()
            valid_content = "无效"
        else:
            ContentTemplatePage(self.driver).valid()
            valid_content = "有效"

        # ContentTemplatePage(self.driver).comment("这是设置的备注")
        temp_info = {"name": tempname, "role":"Misc", "valid": valid_content}
        return temp_info

    def content_template_full_common(self, valid):
        now_time = GetTimeCommon(self.driver).get_time()
        tempname = "temp全填_" + now_time

        ContentTemplatePage(self.driver).name_in(tempname)
        ContentTemplatePage(self.driver).role("Misc")
        ContentTemplatePage(self.driver).subject_in("这是内容模板的主题")

        ContentTemplatePage(self.driver).content_in("设置内容模板的正文")
        Base(self.driver).move_to_pagebottom()
        if valid == "invalid":
            ContentTemplatePage(self.driver).invalid()
            valid_content = "无效"
        else:
            ContentTemplatePage(self.driver).valid()
            valid_content = "有效"

        ContentTemplatePage(self.driver).comment("这是设置的备注")
        temp_info = {"name": tempname, "role": "Misc", "subject": "这是内容模板的主题", "content": "设置内容模板的正文",
                     "valid": valid_content, "comment": "这是设置的备注"}
        return temp_info

    def get_value_commom(self):
        # 取编辑页面的值校验
        name = ContentTemplatePage(self.driver).get_name()
        role = ContentTemplatePage(self.driver).get_role()
        subject = ContentTemplatePage(self.driver).get_subject()
        content = ContentTemplatePage(self.driver).get_content()
        valid = ContentTemplatePage(self.driver).get_valid()
        comment = ContentTemplatePage(self.driver).get_comment()
        value_info = {"name":name,"role":role,"subject":subject,"content":content,"valid":valid,"comment":comment}
        return value_info


