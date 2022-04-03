"""
@author: DT_testing
@file:   calender_case.py
@desc:  【日历-工作时间管理】
@step： 001. 填写必填点击提交，表头字段检查,搜索存在数据
              SC_calender_15,SC_calender_7,SC_calender_3 ，SC_calender_2
        002. 搜索模糊数据，不存在数据，特殊字符数据; 检查返回列表按钮跳转
              SC_calender_4 SC_calender_5 SC_calender_6 SC_calender_13
        003. 不填写必填项时，检查提交按钮; 名称校验：重名，空格 SC_calender_14 SC_calender_17 SC_calender_18
        004. 全填检查  SC_calender_16
        005. 增加多个休假日  SC_calender_24
        006. 增加多个指定工作日  SC_calender_25
        007. 检查休假日、指定工作后的按钮可正常删除  SC_calender_24、SC_calender_25
        008. 无效的工作时间创建，检查在服务水平协议中不能选择   SC_calender_22、SC_calender_26
        009. 编辑工作时间   SC_calender_20、SC_calender_21
        010. 选择工作时间  SC_calender_33、SC_calender_34 SC_calender_35


"""
import time
from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.agent.slacalender_page import SlacalenderPage
# CalenderCommom
from src.page.pagecommon.calender_commom import CalenderCommom
import random
from src.page.agent.servicesla_page import ServiceSlaPage


class Calende(BaseCaseUser, Base):

    def test_001(self):
        '''填写必填点击提交，表头字段检查'''
        calenderinfo = CalenderCommom(self.driver).requestcommon()

        name = calenderinfo.get('name')
        # 点击提交
        SlacalenderPage(self.driver).submit()
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()
        # 取编辑名称断言 getname
        getname = SlacalenderPage(self.driver).getname()
        # 返回列表，检查列表字段，断言
        self.assertEqual(getname, name, msg='错误：填写必填创建工作时间失败')

        # 返回列表
        SlacalenderPage(self.driver).goback()
        table_head = ['名称', '时区', '周起始日', '备注', '有效性', '修改时间', '创建时间']
        gettable_head = SlacalenderPage(self.driver).table_head()
        for i in range(0, len(table_head)):
            gettable_head_one = gettable_head[i].text
            self.assertEqual(gettable_head_one, table_head[i], msg='错误：列表表头列显示错误')

    def test_002(self):
        '''搜索数据1'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = strnumber + "calender!@#$%^&" + strnumber

        EntranceAgentPage(self.driver).enter_slacalendar()
        time.sleep(2)
        SlacalenderPage(self.driver).clickadd()
        time.sleep(2)
        SlacalenderPage(self.driver).inputname(name)
        # 点击提交并返回列表
        SlacalenderPage(self.driver).submit()
        # 等待列表出现后搜索  table_head
        SlacalenderPage(self.driver).table_head()

        SlacalenderPage(self.driver).search(strnumber)
        SlacalenderPage(self.driver).search_result()
        time.sleep(5)
        # 取编辑名称断言 getname
        getname = SlacalenderPage(self.driver).getname()
        # 返回列表，检查列表字段，断言
        self.assertEqual(getname, name, msg='错误：模糊搜索前段数据未查到匹配数据')
        SlacalenderPage(self.driver).goback()
        # 等待列表出现后搜索  table_head
        SlacalenderPage(self.driver).table_head()

        SlacalenderPage(self.driver).search(strnumber + 'calender')
        leftslaname = SlacalenderPage(self.driver).getleftslaname()
        num1 = CalenderCommom(self.driver).is_exist_name(name,leftslaname)
        self.assertIn(1, [i for i in num1], msg='错误：模糊搜索前端数据未查到匹配数据')

        time.sleep(2)
        SlacalenderPage(self.driver).search('!@#$%^&' + strnumber)

        leftslaname = SlacalenderPage(self.driver).getleftslaname()
        time.sleep(3)
        num2 = CalenderCommom(self.driver).is_exist_name(name, leftslaname)
        self.assertIn(1, [i for i in num2] ,msg='错误：模糊搜索前端数据未查到匹配数据')

        # 搜索不存在的数据
        SlacalenderPage(self.driver).search('想喇十八章')
        # 取表格的搜索  get_tab_text get_empty_text
        tab_text = SlacalenderPage(self.driver).get_empty_text()
        self.assertEqual(tab_text, '暂无数据', msg='搜索不存在的数据失败')

    def test_003(self):
        '''名称校验、不填写必填检查提交'''
        calenderinfo = CalenderCommom(self.driver).requestcommon()
        name01 = calenderinfo.get('name')
        # 点击提交
        SlacalenderPage(self.driver).submit()

        # 创建一个带空格的日历
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        spacename = strnumber + "  带空格"
        SlacalenderPage(self.driver).clickadd()
        time.sleep(2)
        SlacalenderPage(self.driver).inputname(spacename)
        SlacalenderPage(self.driver).submit()
        time.sleep(2)

        SlacalenderPage(self.driver).clickadd()
        time.sleep(2)

        # 不填写必填检查提交
        sumbit_disabled = SlacalenderPage(self.driver).is_disabled()
        self.assertEqual(sumbit_disabled, 'true', msg='错误：工作时间名称不填写，提交按钮可点击')
        time.sleep(1)

        # 名称空格校验
        SlacalenderPage(self.driver).inputname('    ')
        nametip = SlacalenderPage(self.driver).getnametip()
        sumbit_disabled = SlacalenderPage(self.driver).is_disabled()
        self.assertEqual(sumbit_disabled, 'true', msg='错误：工作时间名称为空，提交按钮可点击')
        self.assertEqual(nametip, '数据格式错误,请重新输入!', msg='错误：工作时间名称为空，提示错误')

        # 名称重名校验
        SlacalenderPage(self.driver).inputname(name01)
        nametip = SlacalenderPage(self.driver).getnametip()
        sumbit_disabled = SlacalenderPage(self.driver).is_disabled()
        self.assertEqual(sumbit_disabled, 'true', msg='错误：工作时间名称重复，提交按钮可点击')
        self.assertEqual(nametip, '该名称已存在，请更换其他名称！', msg='错误：工作时间名称重复，提示错误')

        # 带空格的名称重复
        SlacalenderPage(self.driver).inputname(spacename)
        nametip = SlacalenderPage(self.driver).getnametip()
        sumbit_disabled = SlacalenderPage(self.driver).is_disabled()
        self.assertEqual(sumbit_disabled, 'true', msg='错误：工作时间带空格的名称重复，提交按钮可点击')
        self.assertEqual(nametip, '该名称已存在，请更换其他名称！', msg='错误：工作时间带空格的名称重复，提示错误')

    def test_004(self):
        '''填写全填点击提交'''
        calenderinfo = CalenderCommom(self.driver).fullcommon()

        name = calenderinfo.get('name')
        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()

        # 取编辑名称断言 getname
        getname = SlacalenderPage(self.driver).getname()
        # 返回列表，检查列表字段，断言
        self.assertEqual(getname, name, msg='错误：填写必填创建工作时间失败')
        # 取各个值断言
        data_name1 = SlacalenderPage(self.driver).get_data_name(0)
        data_name2 = SlacalenderPage(self.driver).get_data_name(1)
        comment = SlacalenderPage(self.driver).get_comment()
        datanamelist = ['休假日名称', '指定工作日名称', '这是备注']
        datanamelist01 = [data_name1, data_name2, comment]
        self.assertEqual(datanamelist, datanamelist01, msg='错误，编辑休假日，指定工作日名称、备注名称失败')

    def test_005(self):
        '''添加多个休假日'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "添加多个休假日" + strnumber
        EntranceAgentPage(self.driver).enter_slacalendar()
        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()
        SlacalenderPage(self.driver).inputname(name)
        SlacalenderPage(self.driver).chose_date2(0, '2020-01-01')
        SlacalenderPage(self.driver).input_name2(0, '第一个休假日')

        SlacalenderPage(self.driver).add_data()
        SlacalenderPage(self.driver).chose_date2(1, '2020-05-01')
        SlacalenderPage(self.driver).input_name2(1, '第二个休假日')

        SlacalenderPage(self.driver).add_data()
        SlacalenderPage(self.driver).chose_date2(2, '2020-10-01')
        SlacalenderPage(self.driver).input_name2(2, '第三个休假日')

        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()

        data1= SlacalenderPage(self.driver).get_data(0)
        data2 = SlacalenderPage(self.driver).get_data(1)
        data3 = SlacalenderPage(self.driver).get_data(2)

        data_name1 = SlacalenderPage(self.driver).get_data_name(0)
        data_name2 = SlacalenderPage(self.driver).get_data_name(1)
        data_name3 = SlacalenderPage(self.driver).get_data_name(2)
        datalist = ['2020-01-01','2020-05-01', '2020-10-01']
        datalist01 = [data1, data2, data3]
        datanamelist = ['第一个休假日', '第二个休假日', '第三个休假日']
        datanamelist01 = [data_name1, data_name2, data_name3]

        self.assertEqual(datalist, datalist01, msg='休假日创建多个日期，日期显示错误')
        self.assertEqual(datanamelist, datanamelist01, msg='休假日创建多个日期，名称显示错误')

    def test_006(self):
        '''添加多个指定工作日'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "添加多个指定工作日" + strnumber
        EntranceAgentPage(self.driver).enter_slacalendar()
        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()
        SlacalenderPage(self.driver).inputname(name)
        SlacalenderPage(self.driver).chose_date2(1, '2020-01-01')
        SlacalenderPage(self.driver).input_name2(1, '第一个指定工作日')

        SlacalenderPage(self.driver).add_data(1)
        SlacalenderPage(self.driver).chose_date2(2, '2020-05-01')
        SlacalenderPage(self.driver).input_name2(2, '第二个指定工作日')

        SlacalenderPage(self.driver).add_data(1)
        SlacalenderPage(self.driver).chose_date2(3, '2020-10-01')
        SlacalenderPage(self.driver).input_name2(3, '第三个指定工作日')

        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()

        data1 = SlacalenderPage(self.driver).get_data(1)
        data2 = SlacalenderPage(self.driver).get_data(2)
        data3 = SlacalenderPage(self.driver).get_data(3)

        data_name1 = SlacalenderPage(self.driver).get_data_name(1)
        data_name2 = SlacalenderPage(self.driver).get_data_name(2)
        data_name3 = SlacalenderPage(self.driver).get_data_name(3)
        datalist = ['2020-01-01', '2020-05-01', '2020-10-01']
        datalist01 = [data1, data2, data3]
        datanamelist = ['第一个指定工作日', '第二个指定工作日', '第三个指定工作日']
        datanamelist01 = [data_name1, data_name2, data_name3]

        self.assertEqual(datalist, datalist01, msg='指定工作日创建多个日期，日期显示错误')
        self.assertEqual(datanamelist, datanamelist01, msg='指定工作日创建多个日期，名称显示错误')

    def test_007(self):
        '''添加多个指定工作日'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "删除" + strnumber
        EntranceAgentPage(self.driver).enter_slacalendar()
        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()
        SlacalenderPage(self.driver).inputname(name)
        SlacalenderPage(self.driver).chose_date2(0, '2020-01-01')
        SlacalenderPage(self.driver).input_name2(0, '第一个休假日')

        SlacalenderPage(self.driver).add_data()
        SlacalenderPage(self.driver).chose_date2(1, '2020-05-01')
        SlacalenderPage(self.driver).input_name2(1, '第二个休假日')

        SlacalenderPage(self.driver).chose_date2(2, '2020-10-01')
        SlacalenderPage(self.driver).input_name2(2, '第一个指定工作日')

        SlacalenderPage(self.driver).add_data(1)
        SlacalenderPage(self.driver).chose_date2(3, '2020-12-01')
        SlacalenderPage(self.driver).input_name2(3, '第二个指定工作日')

        SlacalenderPage(self.driver).del_date(3)
        SlacalenderPage(self.driver).del_date(1)

        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()

        data_num = SlacalenderPage(self.driver).get_data_num()
        self.assertEqual(data_num, 2, msg='删除失败')

    def test_008(self):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "无效工作时间" + strnumber
        EntranceAgentPage(self.driver).enter_slacalendar()
        # 点击添加按钮
        SlacalenderPage(self.driver).clickadd()
        SlacalenderPage(self.driver).inputname(name)
        SlacalenderPage(self.driver).invalid()
        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        SlacalenderPage(self.driver).search(name)
        # 列表页面取名称和有效性断言
        gettable_list01 = [name, 'Asia/Shanghai', '星期一', '', '无效']
        gettable_list = SlacalenderPage(self.driver).gettabblelist()
        for i in range(0, len(gettable_list)-2):
            gettable_head_one = gettable_list[i].text
            self.assertEqual(gettable_head_one, gettable_list01[i], msg='错误：无效记录列表显示错误')

        # 进入服务水平协议页面
        EntranceAgentPage(self.driver).enter_sla()
        ServiceSlaPage(self.driver).clickaddsla()
        # 搜索工作时间管理
        ServiceSlaPage(self.driver).chose_calendar(name)
        get_empty_calendar = ServiceSlaPage(self.driver).get_empty_calendar()
        self.assertEqual(get_empty_calendar, '暂无数据', msg='错误：无效的工作时间管理在服务水平协议中可以被搜索到')
        ServiceSlaPage(self.driver).esc_chose_calendar()

    def test_009(self):
        '''编辑工作时间'''
        calenderinfo = CalenderCommom(self.driver).fullcommon()

        name = calenderinfo.get('name')
        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()

        SlacalenderPage(self.driver).inputname(name+'edit')
        SlacalenderPage(self.driver).chose_date2(0, '2012-01-09')
        SlacalenderPage(self.driver).input_name2(0, '休假日名称edit')
        SlacalenderPage(self.driver).chose_date2(1, '2012-02-09')
        SlacalenderPage(self.driver).input_name2(1, '指定工作日名称edit')
        SlacalenderPage(self.driver).comment('这是备注edit')
        time.sleep(2)

        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()

        # 取编辑名称断言 getname
        getname = SlacalenderPage(self.driver).getname()
        # 返回列表，检查列表字段，断言
        self.assertEqual(getname, name+'edit', msg='错误：编辑工作时间管理名称失败')

        data1 = SlacalenderPage(self.driver).get_data(0)
        data2 = SlacalenderPage(self.driver).get_data(1)
        data_name1 = SlacalenderPage(self.driver).get_data_name(0)
        data_name2 = SlacalenderPage(self.driver).get_data_name(1)
        comment= SlacalenderPage(self.driver).get_comment()

        datalist = ['2012-01-09', '2012-02-09']
        datalist01 = [data1, data2]
        datanamelist = ['休假日名称edit', '指定工作日名称edit', '这是备注edit']
        datanamelist01 = [data_name1, data_name2, comment]
        self.assertEqual(datalist, datalist01, msg='错误，编辑休假日，指定工作日失败')
        self.assertEqual(datanamelist, datanamelist01, msg='错误，编辑休假日，指定工作日名称、备注名称失败')

        # 清空非比较项，再次提交
        SlacalenderPage(self.driver).del_date(0)
        SlacalenderPage(self.driver).del_date(0)
        # SlacalenderPage(self.driver).comment('这是备注edit')
        SlacalenderPage(self.driver).comment(' ')
        # 点击提交
        SlacalenderPage(self.driver).submit()
        time.sleep(5)
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()

        # 取非必填项检查
        data1 = SlacalenderPage(self.driver).get_data(0)
        data2 = SlacalenderPage(self.driver).get_data(1)
        data_name1 = SlacalenderPage(self.driver).get_data_name(0)
        data_name2 = SlacalenderPage(self.driver).get_data_name(1)
        comment = SlacalenderPage(self.driver).get_comment()

        datalist = ['', '', '', '', '']
        datalist01 = [data1, data2, data_name1, data_name2, comment]
        self.assertEqual(datalist, datalist01, msg='错误:删除非必填项失败')

    def test_010(self):
        '''选择工作时间'''
        calenderinfo = CalenderCommom(self.driver).requestcommon()

        name = calenderinfo.get('name')
        SlacalenderPage(self.driver).clear_time()
        SlacalenderPage(self.driver).chose_time(0)
        time.sleep(1)
        SlacalenderPage(self.driver).chose_time(1)
        time.sleep(1)
        SlacalenderPage(self.driver).chose_time(1)
        time.sleep(1)
        # 点击提交
        SlacalenderPage(self.driver).submit()
        # 搜索数据，点击进入编辑
        SlacalenderPage(self.driver).search(name)
        SlacalenderPage(self.driver).search_result()
        get_selected_time_num = SlacalenderPage(self.driver).get_selected_time_num()
        self.assertEqual(get_selected_time_num, 1, msg='清空工作时间失败，点击和取消工作时间失败')


























