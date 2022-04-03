"""
@author: DT_testing
@file:   user_search_case.py
@desc:  【工单搜索】
@step： 001. 全文搜索一条无返回结果的内容 、不输入任何内容点击搜索 SC_Search_010、SC_Search_005  ok
        002. 全文-工单编号  SC_Search_011  ok
        003. 增加/移除搜索搜索条件 SC_Search_034、SC_Search_035 ok
        004. 搜索模板展开/收起、添加第一个模板  SC_Search_038、SC_Search_039  ok
        005. 添加第一个模板、第二模板、删除模板  SC_Search_040、SC_Search_041、SC_Search_042  ok
        006. 导出文件（确保导出不loading）SC_Search_045  未完成
"""
import time

from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.user_search_common import UserSearchCommon
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
import unittest2
from src.page.agent.user_search_page import UserSearchPage


class UserSearch(BaseCaseUser, Base):

    def test_001(self):
        EntranceAgentPage(self.driver).enter_search()
        UserSearchPage(self.driver).search_click()

        # 断言
        empty_text = UserSearchPage(self.driver).get_tip()
        self.assertEqual(empty_text, "搜索条件不能为空", msg="错误：搜索条件为空未正常提示")
        # 全文搜索
        UserSearchPage(self.driver).full_text_in("无内容搜索testtest")
        UserSearchPage(self.driver).search_click()

        # 断言
        empty_text = UserSearchPage(self.driver).get_empty_text()
        self.assertEqual(empty_text, "暂无数据", msg="搜索空数据失败")

    def test_002(self):
        """
            全文-工单编号搜索
        """
        EntranceAgentPage(self.driver).enter_search()
        # 搜索全部数据，取第一条记录，使用优先级，全部搜索
        UserSearchPage(self.driver).add_condition("优先级")

        # 以优先级为例，点击优先级输入框这里是第二个人
        UserSearchPage(self.driver).search_condition_input_click(1)
        UserSearchPage(self.driver).chose_all()
        UserSearchPage(self.driver).search_click()

        # 取搜索结果的列表标题，确定当前工单编号所在位置
        table_th = UserSearchPage(self.driver).get_table_th()
        ticket_number = ""
        ticket_title = ""
        ticket_number_flag = 0
        for each_table_th in table_th:
            if each_table_th.text == "工单编号":
                ticket_number = UserSearchPage(self.driver).get_table_td_first()[ticket_number_flag].text
            elif each_table_th.text == "标题":
                ticket_title = UserSearchPage(self.driver).get_table_td_first()[ticket_number_flag].text
            elif ticket_number and ticket_title:
                break
            ticket_number_flag = ticket_number_flag+1

        # print(ticket_number_flag,ticket_number,ticket_title,"输出")
        # ticket_title = UserSearchPage(self.driver).get_ticket_title()
        # print(ticket_number, ticket_title)

        # 按编号搜索
        # Base(self.driver).move_to_pagetop()
        UserSearchPage(self.driver).full_text_in(ticket_number)
        UserSearchPage(self.driver).search_click()

        # 跳转，断言应该跳转搜索的工单tab
        time.sleep(5)
        get_details_num = UserSearchPage(self.driver).get_details_num()
        get_details_title = UserSearchPage(self.driver).get_details_title()
        self.assertEqual(get_details_num, ticket_number, msg="错误：按工单号搜索工-工单编号显示错误，工单未正常跳转到详情页面")
        self.assertEqual(get_details_title, ticket_title, msg="错误：按工单号搜索工单-工单标题，工单未正常跳转到详情页面")


    def test_003(self):
        EntranceAgentPage(self.driver).enter_search()
        # 优先级-正常
        # 搜索条件-优先级选择-正常
        UserSearchPage(self.driver).add_condition("优先级")

        # 以优先级为例，查询系统内所有工单
        UserSearchPage(self.driver).search_condition_input_click(1)
        UserSearchPage(self.driver).select_by_title("正常")
        UserSearchPage(self.driver).close_optionall()

        # 删除优先级字段
        UserSearchPage(self.driver).delete_search_condition(1)
        # 再次选择优先级字段
        UserSearchPage(self.driver).add_condition("优先级")

        # 以优先级为例，查询系统内所有工单
        UserSearchPage(self.driver).search_condition_input_click(1)
        UserSearchPage(self.driver).select_by_title("非常高")
        UserSearchPage(self.driver).close_optionall()

        # 选择类型-问题
        UserSearchPage(self.driver).add_condition("指定处理人")
        # 取当前页面中的字段进行断言  get_dynamic_fields
        dynamic_fields = UserSearchPage(self.driver).get_dynamic_fields()
        dynamic_fields_list = ["全文", "指定处理人" ,"优先级"]
        for i in range(len(dynamic_fields)-1):
              self.assertIn(dynamic_fields[i].text.replace(" ", ""),dynamic_fields_list,
                             msg="错误：增加的搜索字段没有在页面中显示,正确应为:"+ dynamic_fields_list[i] +"实际为："+dynamic_fields[i].text)

    def test_004(self):
        EntranceAgentPage(self.driver).enter_search()
        UserSearchPage(self.driver).add_model()
        UserSearchPage(self.driver).cancel_model()
        UserSearchPage(self.driver).add_model()

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

        # 取搜索后的数据量  get_total_tab
        get_total_tab01 = UserSearchPage(self.driver).get_total_tab()
        # 关闭工单搜索
        UserSearchPage(self.driver).close_tab()
        # 右上角继续使用当前模板搜索
        # model_name = "ceshi202109230740"
        UserSearchPage(self.driver).upper_right_corner_temp_search(model_name)
        # 点击搜素框
        UserSearchPage(self.driver).search_click()

        # 取搜索后数据量
        Base(self.driver).move_to_pagetop()
        get_total_tab02 = UserSearchPage(self.driver).get_total_tab()

        # 断言
        self.assertEqual(get_total_tab01, get_total_tab02, msg="错误：模板搜索数据错误")

    def test_005(self):
        """
            添加第一个模板、第二模板、删除模板
        """
        EntranceAgentPage(self.driver).enter_search()

        # 下拉取当前系统搜索模板的数量
        UserSearchPage(self.driver).search_model()
        total_temp = UserSearchPage(self.driver).get_total_temp_loc()
        # total_temp_num = len(total_temp)
        # print("长度", total_temp_num)
        # 添加第一个模板
        # 输入模板名称
        UserSearchPage(self.driver).add_model()

        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        model_name01 = str('ceshi01' + strnumber)

        UserSearchPage(self.driver).input_model_name(model_name01)
        UserSearchPage(self.driver).save_model()

        # 搜索条件-优先级选择-正常
        UserSearchPage(self.driver).add_condition("优先级")

        # 以优先级为例，查询系统内所有工单
        UserSearchPage(self.driver).search_condition_input_click(1)
        UserSearchPage(self.driver).select_by_title("正常")
        UserSearchPage(self.driver).close_optionall()
        UserSearchPage(self.driver).search_click()

        # 等等待搜索结束
        UserSearchPage(self.driver).get_total_tab()

        # 添加第二个模板
        # Base(self.driver).move_to_pagetop()
        UserSearchPage(self.driver).add_model()
        model_name02 = str('ceshi02' + strnumber)
        UserSearchPage(self.driver).input_model_name(model_name02)
        UserSearchPage(self.driver).save_model()
        UserSearchPage(self.driver).search_click()


        # 等等待搜索结束
        UserSearchPage(self.driver).get_total_tab()
        Base(self.driver).move_to_pagetop()

        # 删除第一个模板
        # UserSearchPage(self.driver).search_model()
        UserSearchPage(self.driver).delete_model(model_name01)
        # UserSearchPage(self.driver).delete_model(6)
        # model_name01 = "ceshi02202109243858"
        UserSearchPage(self.driver).confirm_del_model()
        UserSearchPage(self.driver).get_total_tab()
        time.sleep(5)
        # Base(self.driver).move_to_pagetop()

        # 删除第二个模板
        # UserSearchPage(self.driver).search_model()
        # UserSearchPage(self.driver).delete_model(total_temp_num)  delete_model
        UserSearchPage(self.driver).delete_model(model_name02)
        # UserSearchPage(self.driver).delete_model(6)
        # model_name02 = "ceshi02202109244347"
        UserSearchPage(self.driver).confirm_del_model()

        # 刷新当前工单搜索tab
        UserSearchPage(self.driver).refresh_current_tab()

        # 取当前页面模板数据断言
        UserSearchPage(self.driver).search_model()
        total_temp = UserSearchPage(self.driver).get_total_temp_loc()

        list01 = []
        for i in range(len(total_temp)):
            list01.append(total_temp[i].text)

        self.assertNotIn(model_name01, list01, msg="错误01：被删除的模板仍然显示")
        self.assertNotIn(model_name02, list01, msg="错误02：被删除的模板仍然显示")

        # 取右上角模板数据断言
        time.sleep(5)  # 等待必须加，否则代码执行太快，页面数据没刷新，容易报错
        UserSearchPage(self.driver).move_upper_right()
        total_temp = UserSearchPage(self.driver).get_right_total_temp_loc()
        list02 = []
        for i in range(len(total_temp)):
            list02.append(total_temp[i].text)

        self.assertNotIn(model_name01, list02, msg="错误03：被删除的模板右上角仍然显示")
        self.assertNotIn(model_name02, list02, msg="错误04：被删除的模板右上角仍然显示")

    @unittest2.skip("编写中")
    def test_006(self):
        EntranceAgentPage(self.driver).enter_search()
        # 搜索条件-优先级选择-正常
        UserSearchPage(self.driver).add_condition("优先级")

        # 以优先级为例，查询系统内所有工单
        UserSearchPage(self.driver).search_condition_input_click(1)
        UserSearchPage(self.driver).select_by_title("非常高")
        UserSearchPage(self.driver).close_optionall()
        # 选择exccel
        time.sleep(2)
        UserSearchPage(self.driver).show_search_results_click("Excel")
        UserSearchPage(self.driver).search_click()

        # 取空判断下载文件后搜索结果是否还一直loading
        empty_text = UserSearchPage(self.driver).get_empty_text()
        self.assertEqual(empty_text, "暂无数据", msg="搜索结果为excel，搜索页面loading")






