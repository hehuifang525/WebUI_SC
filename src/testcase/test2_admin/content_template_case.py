"""
@author: testing
@file:   content_template_case.py
@desc:  【】
@step： 001.必填增加 SC_Conenttemplate_003
        002.全填增加（不含附件）
        003.编辑（不编辑附件） SC_Conenttemplate_015
        004.删除  SC_Conenttemplate_019
        005.设置为无效，无效-有效，添加-返回   SC_Conenttemplate_006 、SC_Conenttemplate_017、SC_Conenttemplate_018


"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.table_page import TablePage
from src.page.agent.content_template_page import ContentTemplatePage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from src.page.pagecommon.content_template_commom import ContentTemplateCommon
from src.page.pagecommon.get_time_common import GetTimeCommon


class ContentTemplateCase(BaseCaseUser, Base):
    def test_001(self):
        EntranceAgentPage(self.driver).enter_contenttemplate()
        ContentTemplatePage(self.driver).add()
        temp_info = ContentTemplateCommon(self.driver).content_template_required_common("valid")
        temp_name = temp_info.get("name")
        ContentTemplatePage(self.driver).submit()

        # 搜索
        ContentTemplatePage(self.driver).search(temp_name)
        TablePage(self.driver).search_result()

        # 取编辑页面的值校验
        get_value = ContentTemplateCommon(self.driver).get_value_commom()
        self.assertEqual(get_value.get("name"), temp_name, msg="错误：创建必填，二次编辑名称显示错误")
        self.assertEqual(get_value.get("role"), temp_info.get("role"), msg="错误：创建必填，二次编辑角色显示错误")
        self.assertEqual(get_value.get("valid"), temp_info.get("valid"), msg="错误：创建必填，二次编辑有效性显示错误")

        #   全填

    def test_002(self):
        EntranceAgentPage(self.driver).enter_contenttemplate()
        ContentTemplatePage(self.driver).add()
        temp_info = ContentTemplateCommon(self.driver).content_template_full_common("valid")
        temp_name = temp_info.get("name")
        ContentTemplatePage(self.driver).submit()

        # 搜索
        ContentTemplatePage(self.driver).search(temp_name)
        TablePage(self.driver).search_result()

        # 取编辑页面的值校验
        get_value = ContentTemplateCommon(self.driver).get_value_commom()
        # print(get_value.get("subject"), get_value.get("content"), get_value.get("comment"))
        self.assertEqual(get_value.get("name"), temp_name, msg="错误：创建必填，二次编辑名称显示错误")
        self.assertEqual(get_value.get("role"), temp_info.get("role"), msg="错误：创建必填，二次编辑角色显示错误")
        self.assertEqual(get_value.get("valid"), temp_info.get("valid"), msg="错误：创建必填，二次编辑有效性显示错误")

        self.assertEqual(get_value.get("subject"), temp_info.get("subject"), msg="错误：创建必填，二次编辑主题显示错误")
        self.assertEqual("设" + get_value.get("content"), temp_info.get("content"), msg="错误：创建必填，二次编辑内容显示错误")
        self.assertEqual(get_value.get("comment"), temp_info.get("comment"), msg="错误：创建必填，二次编辑备注显示错误")

    # 全填-编辑
    def test_003(self):
        EntranceAgentPage(self.driver).enter_contenttemplate()
        ContentTemplatePage(self.driver).add()
        temp_info = ContentTemplateCommon(self.driver).content_template_full_common("valid")
        temp_name = temp_info.get("name")
        ContentTemplatePage(self.driver).submit()

        # 搜索
        ContentTemplatePage(self.driver).search(temp_name)
        time.sleep(2)
        TablePage(self.driver).search_result()

        # 编辑值，提交
        ContentTemplatePage(self.driver).name_in(temp_name+"edit")
        ContentTemplatePage(self.driver).role("Postmaster")
        ContentTemplatePage(self.driver).subject_in("这是编辑内容模板的主题")

        ContentTemplatePage(self.driver).content_in("设置编辑内容模板的正文")
        ContentTemplatePage(self.driver).comment("这是编辑的备注")
        ContentTemplatePage(self.driver).invalid()
        ContentTemplatePage(self.driver).submit()

        # 搜索
        # 切换到无效
        ContentTemplatePage(self.driver).invalid_tab_click()
        ContentTemplatePage(self.driver).search(temp_name)
        time.sleep(2)
        TablePage(self.driver).search_result()

        # 取编辑页面的值校验
        get_value = ContentTemplateCommon(self.driver).get_value_commom()
        # print(get_value.get("subject"), get_value.get("content"), get_value.get("comment"))
        self.assertEqual(get_value.get("name"), temp_name+"edit", msg="错误：创建必填，二次编辑名称显示错误")
        self.assertEqual(get_value.get("role"), "Misc\nPostmaster", msg="错误：创建必填，二次编辑角色显示错误")
        self.assertEqual(get_value.get("valid"),"无效", msg="错误：创建必填，二次编辑有效性显示错误")

        self.assertEqual(get_value.get("subject"), "这是编辑内容模板的主题", msg="错误：创建必填，二次编辑主题显示错误")
        self.assertEqual("设"+get_value.get("content"), "设置编辑内容模板的正文置内容模板的正文", msg="错误：创建必填，二次编辑内容显示错误")
        self.assertEqual(get_value.get("comment"), "这是编辑的备注", msg="错误：创建必填，二次编辑备注显示错误")

    def test_004(self):
        EntranceAgentPage(self.driver).enter_contenttemplate()
        ContentTemplatePage(self.driver).add()
        temp_info = ContentTemplateCommon(self.driver).content_template_required_common("valid")
        temp_name = temp_info.get("name")
        ContentTemplatePage(self.driver).submit()
        # 添加等待，提交后让列表加载再继续
        time.sleep(3)

        # 搜索
        ContentTemplatePage(self.driver).search(temp_name)
        ContentTemplatePage(self.driver).delete()
        ContentTemplatePage(self.driver).confirm_del_model()

        ContentTemplatePage(self.driver).search(temp_name)
        get_empty = ContentTemplatePage(self.driver).get_empty()
        self.assertEqual(get_empty,"暂无数据",msg="错误:删除内容模板失败")

    def test_005(self):
        EntranceAgentPage(self.driver).enter_contenttemplate()
        ContentTemplatePage(self.driver).add()
        temp_info = ContentTemplateCommon(self.driver).content_template_required_common("valid")
        temp_name = temp_info.get("name")
        ContentTemplatePage(self.driver).submit()

        # 搜索
        ContentTemplatePage(self.driver).search(temp_name)
        TablePage(self.driver).search_result()

        # 进入列表，点击返回列表
        ContentTemplatePage(self.driver).return_list()

        # 修改为无效
        ContentTemplatePage(self.driver).search(temp_name)
        TablePage(self.driver).search_result()

        # 再修改为有效
        ContentTemplatePage(self.driver).valid()
        ContentTemplatePage(self.driver).submit()

        ContentTemplatePage(self.driver).search(temp_name)
        TablePage(self.driver).search_result()

        # 取编辑页面的值校验
        get_value = ContentTemplateCommon(self.driver).get_value_commom()
        self.assertEqual(get_value.get("name"), temp_name, msg="错误：创建必填，二次编辑名称显示错误")
        self.assertEqual(get_value.get("role"), temp_info.get("role"), msg="错误：创建必填，二次编辑角色显示错误")
        self.assertEqual(get_value.get("valid"), temp_info.get("valid"), msg="错误：创建必填，二次编辑有效性显示错误")







