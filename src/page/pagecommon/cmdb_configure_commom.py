"""
@author: DT_testing
@file:   cmdb_configure_common_common.py
@desc:  【cmdb配置】
@step：
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.cmdb_configure_page import CmdbConfigurePage
import time
from common.base import Base


class CmdbConfigureCommon(CmdbConfigurePage):

    def CmdbConfigure_requestCommon(self, name="cmdb配置必填"):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = name + strnumber
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        time.sleep(5)
        CmdbConfigurePage(self.driver).click_add()
        time.sleep(2)
        CmdbConfigurePage(self.driver).inputname(name)
        CmdbConfigurePage(self.driver).choose_valid()
        time.sleep(2)
        # CmdbConfigurePage(self.driver).click_next()
        # CmdbConfigurePage(self.driver).click_submit2()
        return name

    def templaterequcommon(self, templaterename, type=1):
        '''
        cmdb 各个模板中输入名称
        :param type: 1 创建 、2 编辑 、3 详情 、4 导入导出
        :return:
        '''

        if type == 1:
            Base(self.driver).move_to_pagetop()
            CmdbConfigurePage(self.driver).create_tempalte()
        elif type == 2:
            CmdbConfigurePage(self.driver).edit_tempalte()
        elif type == 3:
            CmdbConfigurePage(self.driver).details_tempalte()
        else:
            CmdbConfigurePage(self.driver).import_tempalte()

        Base(self.driver).move_to_pagetop()
        CmdbConfigurePage(self.driver).input_tempalte_name(templaterename)
        Base(self.driver).move_to_pagebottom()
        CmdbConfigurePage(self.driver).clicksubmit3()

    def add_temp_default_value_commom(self):
        """
            实现：新增/编辑资产-资产名称，资产生命周期，资产状态，使用科室，资产开始日期设置默认值基础模板设置
            该用例非常规检查用例，用于初始化检查，搜索无对应的资产类“UI自动化默认值校验”，则运行该用例，
            辅助src/testcase/test2_admin/cmdb_overview_case.py中用例
            创建模板默认值：资产名称（HD惠普LP001）资产生命周期（已计划）,资产状态（正常）,使用科室（默认客户）
            编辑模板默认值：资产名称（HD联想LP001）资产生命周期（出库）,资产状态（事件）,使用科室（默认客户）
        """
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        tep_create_name = "UI创建" + strnumber
        tep_edit_name = "UI编辑" + strnumber
        tep_details_name = "UI详情" + strnumber
        name = CmdbConfigureCommon(self.driver).CmdbConfigure_requestCommon("UI自动化默认值校验")
        CmdbConfigurePage(self.driver).click_next()
        time.sleep(5)
        # 新增创建-编辑-详情模板
        CmdbConfigurePage(self.driver).click_submit2()
        CmdbConfigureCommon(self.driver).templaterequcommon(tep_create_name, 1)
        CmdbConfigureCommon(self.driver).templaterequcommon(tep_edit_name, 2)
        CmdbConfigureCommon(self.driver).templaterequcommon(tep_details_name, 3)

        # # -----搜索点击 UI自动化默认值校验2201055350 ---
        # tep_create_name = "UI创建2201055350"
        # tep_edit_name = "UI编辑2201055350"
        # EntranceAgentPage(self.driver).enter_cmdb_configure()
        # CmdbConfigurePage(self.driver).search_input("UI自动化默认值校验2201055350")
        # CmdbConfigurePage(self.driver).click_search_relust()
        # submitinfo = CmdbConfigurePage(self.driver).click_next()
        # CmdbConfigurePage(self.driver).click_submit2()
        #
        # # ----结束搜索点击------

        # 编辑-新增模板--名称，资产生命周期，资产状态，资产使用科室，资产开始日期设置默认值
        CmdbConfigurePage(self.driver).temp_click(tep_create_name)
        # 2022-01-05 创建资产界面资产名称设置默认值，创建资产页面loading，屏蔽该书写
        # CmdbConfigurePage(self.driver).field_name("HD惠普LP001")
        CmdbConfigurePage(self.driver).depl_state("已计划")
        CmdbConfigurePage(self.driver).incistate("正常")
        CmdbConfigurePage(self.driver).customer_company("默认客户")
        CmdbConfigurePage(self.driver).start_date()
        CmdbConfigurePage(self.driver).clicksubmit3()

        # 编辑-编辑模板--名称，资产生命周期，资产状态，资产使用科室，资产开始日期设置默认值
        CmdbConfigurePage(self.driver).temp_click(tep_edit_name)
        CmdbConfigurePage(self.driver).field_name("HD联想LP001")
        CmdbConfigurePage(self.driver).depl_state("出库")
        CmdbConfigurePage(self.driver).incistate("事件")
        CmdbConfigurePage(self.driver).customer_company("默认客户")
        CmdbConfigurePage(self.driver).start_date()
        CmdbConfigurePage(self.driver).clicksubmit3()

        # 点击完成
        CmdbConfigurePage(self.driver).clickcomplete()

        # 写入当前创建的数据 url 类名称

