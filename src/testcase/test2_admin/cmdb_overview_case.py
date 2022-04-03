"""
@author: DT_testing
@file:   cmdb_overview_case.py
@desc:  【cmdb概览】
@step： 001.检查路径  tab titel，浏览器title   SC_CMDB_19
        002.增加一个资产、搜索存在资产、搜索不存在资产   SC_CMDB_20
        003.删除一个资产   SC_CMDB_21
        004. 批量删除资产   SC_CMDB_22
        005. 高级搜索：按资产编号搜索，按资产名称搜索  SC_CMDB_28 SC_CMDB_29
        006. 编辑资产必填项   SC_CMDB_25
        007. cmdb新建，新建一个资产（从菜单权限中新建）  SC_CMDB_30
        008. 创建一个资产，链接到另外一个资产 删除资产链接  SC_CMDB_26  SC_CMDB_27



"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.cmdb_overview_page import CmdbOverviewPage
from src.page.pagecommon.get_time_common import GetTimeCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.pagecommon.cmdb_overview_common import CmdbOverviewCommon
import unittest2
from src.page.agent.cmdb_configure_page import CmdbConfigurePage
from src.page.pagecommon.cmdb_configure_commom import CmdbConfigureCommon

import random


class CmdbOverview(BaseCaseUser, Base):
    @Base.screenshot_about_case
    def test_001(self):
        EntranceAgentPage(self.driver).enter_cmdb_overview()
        time.sleep(5)
        # 检查页面路径
        roadText = CmdbOverviewPage(self.driver).getroadText()
        roadText = str.replace(roadText, ' ', '')
        # 检查浏览器title
        brosertitle = CmdbOverviewPage(self.driver).get_title()
        # 获取页面内tabtitle
        tabTitle = CmdbOverviewPage(self.driver).gettabTitle()
        self.assertEqual(roadText, '/CMDB/CMDB概览', 'cmdb概览导航路径显示不正确')
        self.assertEqual(brosertitle, 'CMDB 概览', 'cmdb概览浏览器窗口 title 显示不正确')
        self.assertEqual(tabTitle, 'CMDB 概览', 'cmdb概览 tab窗口 title 显示不正确')

    # 增加一个资产、搜索存在资产、搜索不存在资产
    @Base.screenshot_about_case
    def test_002(self):
        '''新增资产，搜索存在/不存在资产'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "cmdb必填" + strnumber

        # EntranceAgentPage(self.driver).enter_cmdb_overview()
        time.sleep(5)
        EntranceAgentPage(self.driver).enter_relust('电脑')
        # CmdbOverviewPage(self.driver).click_add()
        # CmdbOverviewPage(self.driver).choose_class('电脑')
        CmdbOverviewPage(self.driver).click_create_template()
        CmdbOverviewPage(self.driver).input_name(name)
        CmdbOverviewPage(self.driver).choose_DeplState('已计划')
        CmdbOverviewPage(self.driver).choose_InciState('正常')
        CmdbOverviewPage(self.driver).click_commit()
        time.sleep(2)
        roadText = CmdbOverviewPage(self.driver).getroadText()
        roadText = str.replace(roadText, ' ', '')
        self.assertEqual(roadText,'/CMDB/CMDB概览/CMDB详情\n' +name, '添加一个资产失败')

        CmdbOverviewPage(self.driver).back_overview()

        # 搜索存在数据
        Base(self.driver).check_loading()
        time.sleep(3)
        CmdbOverviewPage(self.driver).search_input(name)
        time.sleep(1)
        # getname01 = CmdbOverviewPage(self.driver).get_total()  # 32版本元素删除
        table_tr = CmdbOverviewPage(self.driver).table_tr()
        # print(table_tr)
        self.assertEqual(len(table_tr), 1, '必填添加一个资产失败')

        # table_head = CmdbOverviewPage(self.driver).gettable_head()
        # table_body = CmdbOverviewPage(self.driver).gettable_body()
        # tablelist = {'name': name, 'cmdbtype': '电脑', 'DeplState': '已计划', 'InciState': '正常'}
        #
        # tablelist01 = CmdbOverviewCommon(self.driver).tablelistCommon(table_head,table_body)
        #
        # self.assertEqual(tablelist, tablelist01, msg='错误：必填添加一个资产失败')
        # 搜索不存在数据
        CmdbOverviewPage(self.driver).search_input('祥龙十八掌')
        # 必须等待
        time.sleep(5)
        getname = CmdbOverviewPage(self.driver).empty_text()   # 32调整
        self.assertEqual(getname, '这里空空如也, 跟我的钱包一样', '搜索不存在的资产失败')

        # 删除一个资产

    @Base.screenshot_about_case
    def test_003(self):
        '''删除一个资产'''
        name = CmdbOverviewCommon(self.driver).CmdbOverview_requestCommon()
        CmdbOverviewPage(self.driver).search_input(name)

        # 取消删除
        CmdbOverviewPage(self.driver).delete_cmdb()
        time.sleep(2)
        CmdbOverviewPage(self.driver).delete_cancel()

        # 确认删除
        CmdbOverviewPage(self.driver).delete_cmdb()
        CmdbOverviewPage(self.driver).delete_comfire()
        time.sleep(6)
        # 搜索
        CmdbOverviewPage(self.driver).search_input(name)
        # 必须的强制等待
        time.sleep(3)
        getname = CmdbOverviewPage(self.driver).get_total()
        self.assertEqual(getname, '这里空空如也, 跟我的钱包一样', '搜索一个存在的资产失败')


    # 批量删除
    @Base.screenshot_about_case
    def test_004(self):
        '''批量删除'''
        name = CmdbOverviewCommon(self.driver).CmdbOverview_requestCommon()

        # 增加第二个资产
        # 必须的等待
        time.sleep(5)
        # CmdbOverviewPage(self.driver).click_add()
        # CmdbOverviewPage(self.driver).choose_class('电脑')
        EntranceAgentPage(self.driver).enter_relust('电脑')
        CmdbOverviewPage(self.driver).click_create_template()
        CmdbOverviewPage(self.driver).input_name(name + '1')
        CmdbOverviewPage(self.driver).choose_DeplState('已计划')
        CmdbOverviewPage(self.driver).choose_InciState('正常')
        CmdbOverviewPage(self.driver).click_commit()
        CmdbOverviewPage(self.driver).back_overview()

        # 搜索资产
        CmdbOverviewPage(self.driver).search_input(name)
        # 全选资产
        CmdbOverviewPage(self.driver).click_all_select()
        # 删除资产
        time.sleep(2)
        CmdbOverviewPage(self.driver).detele_all()
        time.sleep(5)
        CmdbOverviewPage(self.driver).delete_comfire()
        # print('检查是否删除成功：' + name)
        time.sleep(1)

        # 删除后必须等待几秒后再进行搜索
        # time.sleep(15)
        Base(self.driver).check_loading()
        time.sleep(3)
        # 断言判断
        CmdbOverviewPage(self.driver).search_input(name)
        time.sleep(8)
        getname = CmdbOverviewPage(self.driver).get_total()
        self.assertEqual(getname, '这里空空如也, 跟我的钱包一样', '批量删除的资产失败')

    # 高级搜索：按资产编号搜索，按资产名称搜索
    # 12-01bug 高级搜索无效、数据不匹配  2020120110000099
    @unittest2.skip("bug2020120110000099,跳过")
    def test_005(self):
        '''高级搜索-按资产编号'''
        name = CmdbOverviewCommon(self.driver).CmdbOverview_requestCommon()
        # 取字段编号
        CmdbOverviewPage(self.driver).search_input(name)
        cmdbid = CmdbOverviewPage(self.driver).getleftslaname()
        cmdbid = cmdbid[0].text
        # print(cmdbid)

        CmdbOverviewPage(self.driver).click_height_search()
        CmdbOverviewPage(self.driver).input_cmdb_id2(cmdbid)
        CmdbOverviewPage(self.driver).click_height_search2()
        time.sleep(3)
        search_result = CmdbOverviewPage(self.driver).get_height_search_result()
        # print(search_result)
        self.assertEqual(search_result, '全部 ( 1 )', msg='高级搜索中按资产编号搜索失败')

        Base(self.driver).move_to_pagetop()
        CmdbOverviewPage(self.driver).input_cmdb_name2('北京天安门')

        Base(self.driver).move_to_pagetop()
        CmdbOverviewPage(self.driver).input_cmdb_name2(name)
        CmdbOverviewPage(self.driver).click_height_search2()
        time.sleep(3)
        search_result = CmdbOverviewPage(self.driver).get_height_search_result()
        self.assertEqual(search_result, '全部 ( 1 )', msg='高级搜索中按资产名称搜索失败')

    # 编辑必填项
    @Base.screenshot_about_case
    def test_006(self):
        '''编辑必填'''
        name = CmdbOverviewCommon(self.driver).CmdbOverview_requestCommon()
        # EntranceAgentPage(self.driver).enter_cmdb_overview()
        # time.sleep(6)
        # name = "cmdb必填2109245143"
        newname= 'new' + name
        time.sleep(3)
        CmdbOverviewPage(self.driver).search_input(name)
        CmdbOverviewPage(self.driver).click_search_relust()
        CmdbOverviewPage(self.driver).click_cmdb_edit()

        CmdbOverviewPage(self.driver).input_name(newname)
        CmdbOverviewPage(self.driver).choose_DeplState('已过期')
        CmdbOverviewPage(self.driver).choose_InciState('事件')
        CmdbOverviewPage(self.driver).click_commit()
        time.sleep(5)
        # CmdbOverviewPage(self.driver).back_overview()

        CmdbOverviewPage(self.driver).close_active_tab()
        # EntranceAgentPage(self.driver).enter_cmdb_overview()
        EntranceAgentPage(self.driver).enter_relust("CMDB 概览")
        # # CmdbOverviewPage(self.driver).back_overview()
        # Base(self.driver).check_loading()
        # time.sleep(3)
        CmdbOverviewPage(self.driver).search_input(name)
        time.sleep(3)
        # table_head = CmdbOverviewPage(self.driver).gettable_head()
        # table_body = CmdbOverviewPage(self.driver).gettable_body()
        CmdbOverviewPage(self.driver).click_search_relust()
        time.sleep(3)

        tablelist = {'name': newname, 'DeplState': '已过期', 'InciState': '事件'}
        tablelist01 = CmdbOverviewCommon(self.driver).tablelistCommon002()
        # tablelist01 = CmdbOverviewCommon(self.driver).tablelistCommon(table_head, table_body)
        self.assertEqual(tablelist, tablelist01, msg='错误：编辑必填项失败')

    # cmdb新建
    @Base.screenshot_about_case
    def test_007(self):
        '''cmdb新建'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "新建cmdb" + strnumber
        # EntranceAgentPage(self.driver).enter_newcodb_network()
        # enter_relust
        time.sleep(5)
        EntranceAgentPage(self.driver).enter_relust('电脑')
        time.sleep(5)
        CmdbOverviewPage(self.driver).click_create_template()
        CmdbOverviewPage(self.driver).input_name(name)
        CmdbOverviewPage(self.driver).choose_DeplState('已计划')
        CmdbOverviewPage(self.driver).choose_InciState('正常')
        CmdbOverviewPage(self.driver).click_commit()
        time.sleep(2)
        CmdbOverviewPage(self.driver).back_overview()

        CmdbOverviewPage(self.driver).search_input(name)
        # time.sleep(2)
        # getname = CmdbOverviewPage(self.driver).get_total()
        # self.assertEqual(getname, '全部 ( 1 )', '左侧菜单栏新建一个网络类的资产失败')

    # 创建一个资产，链接到另外一个资产 删除资产链接  SC_CMDB_26  SC_CMDB_27
    # 20210616运行不通过bug记录  2021061610000081
    @unittest2.skip("bug2021061610000081,跳过")
    @Base.screenshot_about_case
    def test_008(self):
        '''链接资产，删除链接资产'''
        # # 创建一个资产
        name = CmdbOverviewCommon(self.driver).CmdbOverview_requestCommon()
        # # 创建第二个资产
        name2 = CmdbOverviewCommon(self.driver).CmdbOverview_requestCommon2()
        # 取资产编号
        CmdbOverviewPage(self.driver).search_input(name2)
        cmdbidinfo02 = CmdbOverviewPage(self.driver).getleftslaname()
        cmdbid02 = cmdbidinfo02[0].text
        time.sleep(5)
        # 搜索第一个资产
        CmdbOverviewPage(self.driver).search_input(name)
        time.sleep(5)
        CmdbOverviewPage(self.driver).click_search_relust()
        CmdbOverviewPage(self.driver).click_link()
        CmdbOverviewPage(self.driver).linktocmdb()

        CmdbOverviewPage(self.driver).addsearchcondition('资产编号')
        # 输入第二个资产的资产编号
        CmdbOverviewPage(self.driver).input_cmdb_number(cmdbid02)
        CmdbOverviewPage(self.driver).link_search()
        time.sleep(2)
        # 选中搜索出来的资产
        CmdbOverviewPage(self.driver).chose_cmdb_option()

        # 0513 系统存在bug，需要点2次才可以显示链接按钮
        CmdbOverviewPage(self.driver).chose_cmdb_option()
        CmdbOverviewPage(self.driver).chose_cmdb_option()

        # 选择链接关系
        CmdbOverviewPage(self.driver).choose_link_relationship()
        # 点击添加链接
        time.sleep(2)
        CmdbOverviewPage(self.driver).addlink()
        time.sleep(2)

        CmdbOverviewPage(self.driver).closelink()

        time.sleep(5)
        # 滑到页面底部
        Base(self.driver).move_to_pagebottom()
        time.sleep(5)
        linknumberinfo = CmdbOverviewPage(self.driver).getlink_cmdbnumber()
        linknumber = linknumberinfo[0].text
        self.assertEqual(linknumber, cmdbid02, msg='一个资产链接到另一个资产失败')
        time.sleep(3)

        # 滑到页面顶部
        Base(self.driver).move_to_pagetop()
        # 点击链接资产
        CmdbOverviewPage(self.driver).click_link()
        # 点击管理现有资产
        CmdbOverviewPage(self.driver).managelink()
        CmdbOverviewPage(self.driver).chose_cmdb_option()

        # 点击删除按钮
        CmdbOverviewPage(self.driver).deletelink()
        time.sleep(2)
        CmdbOverviewPage(self.driver).delete_comfire()
        Base(self.driver).check_loading()
        # time.sleep(5)

        # 取页面无链接的提示语
        link_empty_description = CmdbOverviewPage(self.driver).link_empty_description()
        self.assertEqual(link_empty_description, '这里空空如也, 跟我的钱包一样', msg='')
        time.sleep(1)
        CmdbOverviewPage(self.driver).closelink()
        time.sleep(1)

    def test_009(self):
        """
         实现：新增/编辑资产-资产名称，资产生命周期，资产状态，使用科室，资产开始日期设置默认值
        """
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        CmdbConfigurePage(self.driver).search_input("UI自动化默认值校验")
        # 检查运行系统中是否有已经预置的“UI自动化默认值校验”相关模板，没有则创新创建
        try:
            CmdbConfigurePage(self.driver).check_td()
        except:
            CmdbConfigureCommon(self.driver).add_temp_default_value_commom()

        # 进入cmdb配置，检查是否存在预置的分类，不存在则创建，存在则直接创建
        # CmdbConfigureCommon(self.driver).add_temp_default_value_commom()
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "默认值校验" + strnumber
        EntranceAgentPage(self.driver).enter_cmdb_overview()
        CmdbOverviewPage(self.driver).click_add()

        # UI自动化默认值校验，搜索模板并点击
        CmdbOverviewPage(self.driver).chose_cmdb_class("UI自动化默认值校验")
        CmdbOverviewPage(self.driver).click_create_template()
        # 创建模板的默认值校验,取名称、生命周期等
        get_name = CmdbOverviewPage(self.driver).get_name()
        get_depl_state = CmdbOverviewPage(self.driver).get_depl_state()
        get_incitate = CmdbOverviewPage(self.driver).get_incitate()
        get_customer_company = CmdbOverviewPage(self.driver).get_customer_company()
        get_stsrt_data = CmdbOverviewPage(self.driver).get_stsrt_data()
        # 2022-01-05 创建资产界面资产名称设置默认值，创建资产页面loading，屏蔽该校验
        # self.assertEqual(get_name,"HD惠普LP001",msg="web创建资产，资产名称默认值显示错误")
        self.assertEqual(get_depl_state,"已计划",msg="web创建资产，资产生命周期默认值显示错误")
        self.assertEqual(get_incitate,"正常",msg="web创建资产，资产状态默认值显示错误")
        # 32版本默认值无法设置
        # self.assertEqual(get_customer_company,"DefaultCustomer 默认客户",msg="web创建资产，使用科室默认值显示错误")
        self.assertIsNotNone(get_stsrt_data, msg="web创建资产，资产开始日期默认值显示错误")

        # 输入新增的名称值，提交
        CmdbOverviewPage(self.driver).input_name(name)
        CmdbOverviewPage(self.driver).click_commit()
        time.sleep(2)
        # 进入编辑页面，对编辑页面的默认值进行校验
        CmdbOverviewPage(self.driver).click_cmdb_edit()
        time.sleep(2)
        get_name = CmdbOverviewPage(self.driver).get_name()
        get_depl_state = CmdbOverviewPage(self.driver).get_depl_state()
        get_incitate = CmdbOverviewPage(self.driver).get_incitate()
        get_customer_company = CmdbOverviewPage(self.driver).get_customer_company()
        get_stsrt_data = CmdbOverviewPage(self.driver).get_stsrt_data()

        self.assertEqual(get_name, "HD联想LP001", msg="web编辑资产，资产名称默认值显示错误")
        self.assertEqual(get_depl_state, "出库", msg="web编辑资产，资产生命周期默认值显示错误")
        self.assertEqual(get_incitate, "事件", msg="web编辑资产，资产状态默认值显示错误")
        # 32版本默认值无法设置
        # self.assertEqual(get_customer_company, "DefaultCustomer 默认客户", msg="web创建资产，使用科室默认值显示错误")
        self.assertIsNotNone(get_stsrt_data, msg="web创建资产，资产开始日期默认值显示错误")

















