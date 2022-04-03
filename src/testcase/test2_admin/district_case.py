"""
@author: DT_testing
@file:   district_case.py
@desc:  【区域】
@step： 001.检查区域列表默认表头，浏览器title tabtitle  SC_District_12
        002. 必填增加区域，搜索区域   SC_District_8  SC_District_27
        003. 检查必填项  空格校验 返回列表  SC_District_21  SC_District_22  SC_District_25  SC_District_15
        004. 名称重名校验   SC_District_23  SC_District_24
        005. 添加无效      SC_District_28  SC_District_16
        006. 过滤存在的数据，检查模糊搜索， 特殊字符搜索 SC_District_9 SC_District_10 SC_District_11
        008. 全填创建一个区域  SC_District_29
        009. 编辑区域所有字段、编辑非必填字段



"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.district_page import DistrictPage
from src.page.pagecommon.get_time_common import GetTimeCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.pagecommon.district_common import DistrictCommon

import random

class District(BaseCaseUser, Base):

    # title tab 列表的检查 SC_District_12
    def test_001(self):
        EntranceAgentPage(self.driver).enter_district()
        time.sleep(5)
        # 检查页面路径
        roadText = DistrictPage(self.driver).getroadText()
        roadText = str.replace(roadText, ' ', '')
        # 检查浏览器title
        brosertitle = DistrictPage(self.driver).get_title()
        # 获取页面内tabtitle
        tabTitle = DistrictPage(self.driver).gettabTitle()
        self.assertEqual(roadText, '/系统管理/区域', '区域列表路径显示不正确')
        self.assertEqual(brosertitle, '区域', '区域浏览器窗口 title 显示不正确')
        self.assertEqual(tabTitle, '区域', '区域tab窗口 title 显示不正确')
        Districtindfo = ['名称', '备注', '修改时间', '修改人', '创建时间', '创建人']
        Districtindfo01 = DistrictPage(self.driver).gettable_head()
        for i in range(0, len(Districtindfo)):
            info = Districtindfo01[i].text
            self.assertEqual(info, Districtindfo[i], msg='错误：区域列表默认表头显示错误')

    def test_002(self):
        name = DistrictCommon(self.driver).DistrictRequiredCommon()
        # print(name)
        DistrictPage(self.driver).search(name)
        DistrictPage(self.driver).click_search_result()
        DistrictPage(self.driver).addsubmit()
        DistrictPage(self.driver).search(name)
        Districname = DistrictPage(self.driver).gettable_body()[0].text
        Districcommon = DistrictPage(self.driver).gettable_body()[1].text
        self.assertEqual(Districname, name, msg='错误，必填添加区域列表中名称显示错误')
        self.assertEqual(Districcommon, '', msg='错误，必填添加区域列表中备注显示错误')

        DistrictPage(self.driver).click_search_result()
        Districtinfo= DistrictCommon(self.driver).GetDistrictInfo()
        districtlist = [name, None, '有效', None]
        Districtinfo2 = []
        for i in range(0, len(Districtinfo)):
            Districtinfo2.append(Districtinfo[i])
            if Districtinfo2[i] == '':
                Districtinfo2[i] = None

        self.assertEqual(Districtinfo2, districtlist, msg='必填添加区域二次编辑进入，数据显示错误')

    # 检查必填项，必填项空格输入
    def test_003(self):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "区域必填" + strnumber
        EntranceAgentPage(self.driver).enter_district()
        time.sleep(5)
        DistrictPage(self.driver).click_add()
        submitinfo = DistrictPage(self.driver).check_submit_clickable()
        self.assertEqual(submitinfo, False, msg='错误：名称未输入，提交按钮可触发')

        DistrictPage(self.driver).input_name('    ')
        time.sleep(2)
        submitinfo = DistrictPage(self.driver).check_submit_clickable()
        self.assertEqual(submitinfo, False, msg='错误：必填项输入空格，提交按钮可触发')

        DistrictPage(self.driver).input_name(name)
        time.sleep(2)
        submitinfo = DistrictPage(self.driver).check_submit_clickable()
        self.assertEqual(submitinfo, True, msg='错误：必填项已填写，提交按钮不可触发')

        DistrictPage(self.driver).delete_valid()
        time.sleep(2)
        submitinfo = DistrictPage(self.driver).check_submit_clickable()
        self.assertEqual(submitinfo, False, msg='错误：有效性为空，提交按钮可触发')

        # 检查返回列表按钮 返回页面添加按钮可点击
        DistrictPage(self.driver).backlist()
        submitinfo = DistrictPage(self.driver).check_add_clickable()
        self.assertEqual(submitinfo, True, msg='错误：点击返回列表按钮，返回列表失败')

    # 名称重名检验
    def test_004(self):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name2 = name = "区域  必填" + strnumber
        name1 = DistrictCommon(self.driver).DistrictRequiredCommon()

        DistrictPage(self.driver).click_add()
        time.sleep(3)
        DistrictPage(self.driver).input_name(name2)
        DistrictPage(self.driver).choose_valid()
        DistrictPage(self.driver).addsubmit()

        DistrictPage(self.driver).click_add()
        time.sleep(3)
        DistrictPage(self.driver).input_name(name1)
        name_tip = DistrictPage(self.driver).get_name_tip()
        submitinfo = DistrictPage(self.driver).check_submit_clickable()
        self.assertEqual(name_tip,'该名称已存在，请更换其他名称！', msg='名称重复未提示')
        self.assertEqual(submitinfo, False, msg='错误：名称重复，提交按钮可触发')

        # 检查带有空格的名称重名检验
        DistrictPage(self.driver).input_name(name2)
        name_tip = DistrictPage(self.driver).get_name_tip()
        submitinfo = DistrictPage(self.driver).check_submit_clickable()
        self.assertEqual(name_tip, '该名称已存在，请更换其他名称！', msg='检查带有空格的名称重复未提示')
        self.assertEqual(submitinfo, False, msg='错误：检查带有空格的名称重复，提交按钮可触发')

    # 添加一个无效区域
    @Base.screenshot_about_case
    def test_005(self):
        name = DistrictCommon(self.driver).DistrictinvalidCommon()
        # 切换到无效tab click_invalid_tab
        DistrictPage(self.driver).click_invalid_tab()
        DistrictPage(self.driver).search(name)
        DistrictPage(self.driver).click_search_result()
        DistrictPage(self.driver).addsubmit()

        DistrictPage(self.driver).click_invalid_tab()
        DistrictPage(self.driver).search(name)
        Districname = DistrictPage(self.driver).gettable_body()[0].text
        Districcommon = DistrictPage(self.driver).gettable_body()[1].text
        self.assertEqual(Districname, name, msg='错误，必填添加区域列表中名称显示错误')
        self.assertEqual(Districcommon, '', msg='错误，必填添加区域列表中备注显示错误')

        DistrictPage(self.driver).click_search_result()
        Districtinfo= DistrictCommon(self.driver).GetDistrictInfo()
        districtlist = [name, None, '无效', None]
        Districtinfo2 = []
        for i in range(0, len(Districtinfo)):
            Districtinfo2.append(Districtinfo[i])
            if Districtinfo2[i] == '':
                Districtinfo2[i] = None

        self.assertEqual(Districtinfo2, districtlist, msg='必填添加区域二次编辑进入，数据显示错误')

    # 检查搜索
    def test_006(self):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        # 加号,英文冒号 系统未处理
        name2 = "TicketFree!@#$%^&*()Text" + strnumber
        # .get_attribute('content')
        EntranceAgentPage(self.driver).enter_district()
        time.sleep(5)

        # DistrictPage(self.driver).click_add()
        # time.sleep(3)
        # DistrictPage(self.driver).input_name(name2)
        # DistrictPage(self.driver).choose_valid()
        # DistrictPage(self.driver).addsubmit()
        #
        # num1, num2, num3, num4 = 0, 0, 0, 0
        # DistrictPage(self.driver).search('Ticket')
        # leftslaname = DistrictPage(self.driver).getleftslaname()
        # for i in range(0, len(leftslaname)):
        #     print(len(leftslaname))
        #     listinfo = leftslaname[i].get_attribute('content')
        #     print(listinfo,1,name2)
        #     if listinfo == name2:
        #         num1 = num1 + 1
        #
        # DistrictPage(self.driver).search('Free')
        # leftslaname = DistrictPage(self.driver).getleftslaname()
        # for i in range(0, len(leftslaname)):
        #     listinfo = leftslaname[i].text
        #     if listinfo == name2:
        #         num2 = num2 + 1
        #
        # DistrictPage(self.driver).search('Text')
        # leftslaname = DistrictPage(self.driver).getleftslaname()
        # for i in range(0, len(leftslaname)):
        #     listinfo = leftslaname[i].text
        #     if listinfo == name2:
        #         num3 = num3 + 1
        #
        # DistrictPage(self.driver).search('!@#$%^&*()')
        # leftslaname = DistrictPage(self.driver).getleftslaname()
        # for i in range(0, len(leftslaname)):
        #     listinfo = leftslaname[i].text
        #     if listinfo == name2:
        #         num4 = num4 + 1

        DistrictPage(self.driver).search('祥龙十八掌倚天屠龙记')
        empty_tip = DistrictPage(self.driver).get_empty_tip()

        # self.assertEqual(num1, 1, msg='错误：模糊搜索前段数据未查到匹配数据')
        # self.assertEqual(num2, 1, msg='错误：模糊搜索中段数据未查到匹配数据')
        # self.assertEqual(num3, 1, msg='错误：模糊搜索后段数据未查到匹配数据')
        # self.assertEqual(num4, 1, msg='错误：模糊搜索特殊字符未查到匹配数据')
        self.assertEqual(empty_tip, '暂无数据', msg='错误：模糊搜索特殊字符未查到匹配数据')

    # 全填创建区域 bug 列表中不显示备注，暂不判断列表数据
    # @Base.screenshot_about_case
    # def test_007(self):
    #     # 未完成，区域值未取到
    #     name, coment, parentdistrict = DistrictCommon(self.driver).DistrictFullCommon()
    #     DistrictPage(self.driver).search(name)
    #     DistrictPage(self.driver).click_search_result()
    #     DistrictPage(self.driver).addsubmit()
    #     DistrictPage(self.driver).search(name)
    #     Districname = DistrictPage(self.driver).gettable_body()[0].text
    #     Districcommon = DistrictPage(self.driver).gettable_body()[1].text
    #     name2 = parentdistrict + "::" + name
    #     self.assertEqual(Districname, name2, msg='错误，全填添加区域列表中名称显示错误')
    #     # self.assertEqual(Districcommon, coment, msg='错误，全填添加区域列表中备注显示错误')
    #
    #     DistrictPage(self.driver).click_search_result()
    #     Districtinfo = DistrictCommon(self.driver).GetDistrictInfo()
    #     districtlist = (name, parentdistrict, '有效', coment)
    #     self.assertEqual(Districtinfo, districtlist, msg='必填添加区域二次编辑进入，数据显示错误')







