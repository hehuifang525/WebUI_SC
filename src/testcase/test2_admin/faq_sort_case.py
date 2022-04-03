"""
@author: DT_testing
@file:   faq_sort_case.py
@desc:  【知识库类别管理】
@step： 001.填写必填，点击提交按钮，删除
        002.检查返回列表按钮，检查路径显示  SC_Faq_5  SC_Faq_6  SC_Faq_7 SC_Faq_1
        003.新增必填知识库类别（检查上一步修改值、下一步、完成）  SC_Faq_8
        004.全填添加类型、使用完成再添加一条 SC_Faq_9  SC_Faq_10
        005 增加无效     SC_Faq_12
        006 删除单条知识库类别  SC_Faq_23
        007 关联角色 关联客户 SC_Faq_8_1
        008 删除已经有文章的知识库类别，删除父类别  SC_Faq_24  SC_Faq_25





"""
import time

from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.service_commom import ServiceCommon
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.agent.faq_page import FaqPage
from src.page.pagecommon.faq_commom import FaqCommon
from src.page.agent.faq_overview_page import FaqOverviewPage
from src.page.pagecommon.faq_overview_commom import FaqOverviewCommon

import random


class FaqSort(BaseCaseUser, Base):

    def test_001(self):
        '''填写必填，点击提交'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        FaqPage(self.driver).add()
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        name = faqsortinfo.get("name")
        FaqPage(self.driver).submitreturn()
        # 搜索
        FaqPage(self.driver).right_search(name)
        # 点击结果
        FaqPage(self.driver).search_result()
        # 取名称值对比，断言
        get_name = FaqPage(self.driver).get_name()
        self.assertEqual(get_name, name, msg='填写必填提交知识库类型失败')




    def test_002(self):
        '''返回列表'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        FaqPage(self.driver).add()
        FaqPage(self.driver).goback1()
        time.sleep(3)

        FaqPage(self.driver).add()
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        name = faqsortinfo.get("name")

        FaqPage(self.driver).goback1()

        # 取左上角路径显示
        get_bar = FaqPage(self.driver).get_bar()
        tab_title = FaqPage(self.driver).tab_title()
        url_title = self.driver.title

        self.assertEqual(get_bar, '/ 知识库 / 知识库类别管理', msg='路径显示错误')
        self.assertEqual(tab_title, '知识库类别管理', msg='tabtitle错误')
        self.assertEqual(url_title, '知识库类别管理', msg='urltitle显示错误')


        # 搜索
        FaqPage(self.driver).right_search(name)
        getempty = FaqPage(self.driver).getempty()
        self.assertEqual(getempty, '这里空空如也, 跟我的钱包一样', msg='输入值后点击返回列表失败')

        FaqPage(self.driver).add()
        FaqPage(self.driver).inputname(name)
        FaqPage(self.driver).inputcommen('备注123')
        FaqPage(self.driver).next()
        FaqPage(self.driver).goback2()
        FaqPage(self.driver).right_search(name)
        # 对列表值进行断言
        tableinfo = FaqPage(self.driver).table_list_td()
        tablelist = [name, '备注123', '有效']
        for i in range(0, 3):
            textinfo = tableinfo[i].text
            self.assertEqual(textinfo, tablelist[i], msg='创建知识库类别列表值显示错误')

    def test_003(self):
        '''上一步、下一步、完成'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        FaqPage(self.driver).add()
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        name = faqsortinfo.get("name")
        FaqPage(self.driver).inputcommen('备注2')
        FaqPage(self.driver).next()
        time.sleep(3)
        FaqPage(self.driver).previous()
        time.sleep(3)

        FaqPage(self.driver).inputname(name+'edit')
        FaqPage(self.driver).inputcommen('备注edit')
        FaqPage(self.driver).next()
        time.sleep(3)
        FaqPage(self.driver).finished()

        time.sleep(2)
        FaqPage(self.driver).right_search(name)
        # 对列表值进行断言
        tableinfo = FaqPage(self.driver).table_list_td()
        tablelist = [name+'edit', '备注edit', '有效']
        for i in range(0, 3):
            textinfo = tableinfo[i].text
            self.assertEqual(textinfo, tablelist[i], msg='上一步下一步完成操作后列表值显示错误')

    # 待验证--添加子级类别提交后，页面loading bug
    # def test_004(self):
    #     '''完成再添加'''
    #     EntranceAgentPage(self.driver).enter_faq()
    #     time.sleep(3)
    #
    #     FaqPage(self.driver).add()
    #     faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
    #     name = faqsortinfo.get("name")
    #     FaqPage(self.driver).inputcommen('备注1')
    #     FaqPage(self.driver).next()
    #     time.sleep(2)
    #     FaqPage(self.driver).finish_another()
    #
    #     time.sleep(2)
    #     FaqPage(self.driver).inputname(name + 'tow')
    #     FaqPage(self.driver).parent(name)
    #     FaqPage(self.driver).inputcommen('备注tow')
    #     FaqPage(self.driver).submitreturn()
    #
    #     time.sleep(5)
    #     FaqPage(self.driver).right_search(name)
    #
    #     FaqPage(self.driver).right_search(name+ 'tow')
    #     # 对列表值进行断言
    #     tableinfo = FaqPage(self.driver).table_list_td()
    #     tablelist = [name+ 'tow', '备注tow', '有效']
    #     for i in range(0, 3):
    #         textinfo = tableinfo[i].text
    #         self.assertEqual(textinfo, tablelist[i], msg='提交并再添加一条失败02')
    #
    #     # 左侧搜索子级，检查父级的显示
    #     FaqPage(self.driver).left_search(name + 'tow')
    #     get_parent_tree = FaqPage(self.driver).get_parent_tree()
    #     self.assertEqual(get_parent_tree,name,msg='添加子级类别失败')

    def test_005(self):
        '''添加无效数据'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        FaqPage(self.driver).add()
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('name' + strnumber)
        FaqPage(self.driver).inputname(name)
        FaqPage(self.driver).invalid()
        FaqPage(self.driver).submitreturn()
        time.sleep(3)

        # 对列表值进行断言
        FaqPage(self.driver).right_search(name)
        tableinfo = FaqPage(self.driver).table_list_td()
        tablelist = [name, '', '无效']
        for i in range(0, 3):
            textinfo = tableinfo[i].text
            self.assertEqual(textinfo, tablelist[i], msg='添加无效数据失败')


    def test_006(self):
        '''删除独立类别'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        FaqPage(self.driver).add()
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        name = faqsortinfo.get("name")
        FaqPage(self.driver).submitreturn()
        time.sleep(10)
        FaqPage(self.driver).right_search(name)

        # 点击删除
        FaqPage(self.driver).detele()
        FaqPage(self.driver).comfire_delete()
        time.sleep(10)
        print("删除的项为：" + name)

        # 搜索
        FaqPage(self.driver).right_search(name)
        getempty = FaqPage(self.driver).getempty()
        self.assertEqual(getempty, '这里空空如也, 跟我的钱包一样', msg='删除独立实知识库类别失败')

    def test_007(self):
        '''关联角色、关联客户'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        FaqPage(self.driver).add()
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        name = faqsortinfo.get("name")
        FaqPage(self.driver).next()
        time.sleep(5)
        FaqPage(self.driver).rolero('系统默认角色')
        time.sleep(2)
        FaqPage(self.driver).rolerw('系统默认角色')
        FaqPage(self.driver).LinkCompany('默认客户')
        FaqPage(self.driver).finished()
        time.sleep(3)

        # 搜索
        FaqPage(self.driver).right_search(name)

        FaqPage(self.driver).search_result()
        time.sleep(3)

        FaqPage(self.driver).next()
        get_rolero = FaqPage(self.driver).get_rolero()
        get_rolerw = FaqPage(self.driver).get_rolerw()
        get_Company = FaqPage(self.driver).get_Company()

        self.assertEqual(get_rolero,'系统默认角色',msg='新增知识库类别关联只读角色二次进入查看显示错误')
        self.assertEqual(get_rolerw, '系统默认角色', msg='新增知识库类别关联读取角色二次进入查看显示错误')
        self.assertEqual(get_Company, '默认客户', msg='新增知识库类别关联客户二次进入查看显示错误')

    def test_008(self):
        '''删除已创建知识的类别'''
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(3)

        FaqPage(self.driver).add()
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        faq_sort_parent_name = faqsortinfo.get("name")
        FaqPage(self.driver).submitreturn()
        time.sleep(10)

        # 创建一个子类
        FaqPage(self.driver).add()
        time.sleep(5)
        faqsortinfo = FaqCommon(self.driver).Faqrequiredcommon()
        faq_sort_child_name = faqsortinfo.get("name")
        FaqPage(self.driver).parent(faq_sort_parent_name)
        FaqPage(self.driver).submitreturn()

        EntranceAgentPage(self.driver).enter_faq_overview()
        time.sleep(2)
        FaqOverviewPage(self.driver).add()
        FaqOverviewCommon(self.driver).FaqOverviewrequiredcommon(faq_sort_child_name)
        FaqOverviewPage(self.driver).submit()

        time.sleep(2)
        EntranceAgentPage(self.driver).enter_faq()
        time.sleep(2)
        FaqPage(self.driver).right_search(faq_sort_child_name)
        time.sleep(2)
        FaqPage(self.driver).detele()
        time.sleep(5)
        # 遇到多次该删除按钮触发不了
        FaqPage(self.driver).comfire_delete()
        # 弹框检查
        time.sleep(10)
        print("删除的项为子：" + faq_sort_child_name)
        get_detele_tip = FaqPage(self.driver).get_detele_tip()
        self.assertEqual(get_detele_tip, '你不能删除这个类别，该类别至少包含一篇FAQ文章，或者至少包含一个子类别。',
                         msg='删除已存在知识的类别提示错误')
        FaqPage(self.driver).clickok()

        # 删除父类
        FaqPage(self.driver).right_search(faq_sort_parent_name)
        time.sleep(2)
        FaqPage(self.driver).detele()
        FaqPage(self.driver).comfire_delete()
        time.sleep(5)
        print("删除的项为父：" + faq_sort_parent_name)
        get_detele_tip = FaqPage(self.driver).get_detele_tip()
        self.assertEqual(get_detele_tip, '你不能删除这个类别，该类别至少包含一篇FAQ文章，或者至少包含一个子类别。',
                         msg='删除父类别提示错误')
        FaqPage(self.driver).clickok()


























