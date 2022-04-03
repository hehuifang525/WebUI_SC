"""
@author: DT_testing
@file:   cmdb_configure_case.py
@desc:  【cmdb配置】
@step： 001.检查区域列表默认表头，浏览器title tabtitle  SC_CMDB_1  SC_CMDB_2
        002. 添加-返回列表   C_CMDB_8
        003. 必填增加一个类 搜索存在数据 SC_CMDB_7  SC_CMDB_3
        004. 搜索：模糊搜索、搜索不存在数据、特殊字符搜索  SC_CMDB_4  SC_CMDB_5 SC_CMDB_6
        005. （1）检查添加页面的返回列表（2）添加-下一步，在填写表单字段信息页面  上一步-下一步-返回列表    C_CMDB_8 SC_CMDB_9 SC_CMDB_10
        006. 检查 添加-下一步-提交 检查定制模板页面的 上一步按钮，继续新建资产按钮，返回列表按钮
             SC_CMDB_11  SC_CMDB_12  SC_CMDB_13
        007. 复制类别  SC_CMDB_14
        008. 类别名称必填校验  SC_CMDB_15
        009. 类别名称唯一性检验 SC_CMDB_16
        010. 检查添加系统字段
        00. 添加自定义字段
        00. 修改必填修 非必填项等   模板内字段必填检验   定制模板的删除复制



"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.cmdb_configure_page import CmdbConfigurePage
from src.page.pagecommon.get_time_common import GetTimeCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.pagecommon.cmdb_configure_commom import CmdbConfigureCommon
import unittest
import random


class CmdbConfigure(BaseCaseUser, Base):

    def test_001(self):
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        time.sleep(5)
        # 检查页面路径
        roadText = CmdbConfigurePage(self.driver).getroadText()
        roadText = str.replace(roadText, ' ', '')
        # 检查浏览器title
        brosertitle = CmdbConfigurePage(self.driver).get_title()
        # 获取页面内tabtitle
        tabTitle = CmdbConfigurePage(self.driver).gettabTitle()
        self.assertEqual(roadText, '/CMDB/CMDB配置', 'cmdb配置导航路径显示不正确')
        self.assertEqual(brosertitle, 'CMDB 配置', 'cmdb配置浏览器窗口 title 显示不正确')
        self.assertEqual(tabTitle, 'CMDB 配置', 'cmdb配置 tab窗口 title 显示不正确')
        Districtindfo = ['', '类名称', '编号规则', '备注', '有效性', '创建时间', '创建人', '修改时间', '修改人', '操作']
        Districtindfo01 = CmdbConfigurePage(self.driver).gettable_head()
        for i in range(0, len(Districtindfo)):
            info = Districtindfo01[i].text
            self.assertEqual(info, Districtindfo[i], msg='错误：区域列表默认表头显示错误')

    # # 重复用例，整合到用例005，屏蔽该压用例
    # def test_002(self):
    #     '''添加返回列表'''
    #     EntranceAgentPage(self.driver).enter_cmdb_configure()
    #     time.sleep(5)
    #     CmdbConfigurePage(self.driver).click_add()
    #     time.sleep(2)
    #     CmdbConfigurePage(self.driver).click_backlist()
    #
    #     # 取添加按钮点击状态
    #     check1 = CmdbConfigurePage(self.driver).checkadd()
    #     self.assertEqual(check1, True, '填写类的基本信息返回列表错误')

    # # 填写必填，增加一个项
    # @unittest.skip("1201 2020120110000124  搜索页面loading,跳过") # 2022-01-06恢复
    def test_003(self):
        '''必填增加'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "cmdb配置必填" + strnumber
        name1 = "创建模板" + strnumber
        name2 = "编辑模板" + strnumber
        name3 = "详情模板" + strnumber
        name4 = "导入导出模板" + strnumber
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        time.sleep(5)
        CmdbConfigurePage(self.driver).click_add()
        time.sleep(2)
        CmdbConfigurePage(self.driver).inputname(name)
        CmdbConfigurePage(self.driver).choose_valid()
        time.sleep(2)
        CmdbConfigurePage(self.driver).click_next()
        CmdbConfigurePage(self.driver).click_submit2()

        CmdbConfigureCommon(self.driver).templaterequcommon(name1, 1)
        CmdbConfigureCommon(self.driver).templaterequcommon(name2, 2)
        CmdbConfigureCommon(self.driver).templaterequcommon(name3, 3)
        CmdbConfigureCommon(self.driver).templaterequcommon(name4, 4)

        # 点击完成
        CmdbConfigurePage(self.driver).clickcomplete()
        CmdbConfigurePage(self.driver).backlist4()
        time.sleep(3)
        # 搜索
        CmdbConfigurePage(self.driver).search_input(name)
        time.sleep(1)
        getname = CmdbConfigurePage(self.driver).getleftslaname()[0].text
        self.assertEqual(getname,name, msg='必填添加资产类出错')

    # @unittest.skip("1201 2020120110000124  搜索页面loading,跳过") # 2022-01-06恢复
    def test_004(self):
        '''搜索'''
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "TicketFree" + strnumber
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        time.sleep(5)
        CmdbConfigurePage(self.driver).click_add()
        time.sleep(2)
        CmdbConfigurePage(self.driver).inputname(name)
        CmdbConfigurePage(self.driver).choose_valid()
        time.sleep(2)
        CmdbConfigurePage(self.driver).click_next()
        CmdbConfigurePage(self.driver).click_submit2()
        CmdbConfigurePage(self.driver).backlist3()
        time.sleep(3)

        # 搜索不存在类型
        CmdbConfigurePage(self.driver).search_input('萨摩耶二哈资产祥龙十八航')
        getname = CmdbConfigurePage(self.driver).get_empty_tip()
        self.assertEqual(getname, '这里空空如也, 跟我的钱包一样', msg='搜索不存在类失败')
        time.sleep(3)

        # 模糊搜索
        num1, num2, num3 = 0,0,0
        CmdbConfigurePage(self.driver).search_input('Ticket')
        leftslaname = CmdbConfigurePage(self.driver).getleftslaname()
        for i in range(0, len(leftslaname)):
            listinfo = leftslaname[i].text
            if listinfo == name:
                num1 = num1+1

        CmdbConfigurePage(self.driver).search_input('Free')
        leftslaname = CmdbConfigurePage(self.driver).getleftslaname()
        for i in range(0, len(leftslaname)):
            listinfo = leftslaname[i].text
            if listinfo == name:
                num2 = num2+1

        CmdbConfigurePage(self.driver).search_input(strnumber)
        leftslaname = CmdbConfigurePage(self.driver).getleftslaname()
        for i in range(0, len(leftslaname)):
            listinfo = leftslaname[i].text
            if listinfo == name:
                num3 = num3+1

        self.assertEqual(num1, 1, msg='错误：模糊搜索前段数据未查到匹配数据')
        self.assertEqual(num2, 1, msg='错误：模糊搜索中段数据未查到匹配数据')
        self.assertEqual(num3, 1, msg='错误：模糊搜索后段数据未查到匹配数据')

    # 检查 （1）检查添加页面的返回列表（2）添加-下一步，在填写表单字段信息页面  上一步-下一步-返回列表
    # 1201 2020120110000124  搜索页面loading
    # @unittest.skip("20201012 同test007，添加后数据在第六页，第六页记录搜索不到,跳过")   # 2022-01-06恢复
    def test_005(self):
        name = CmdbConfigureCommon(self.driver).CmdbConfigure_requestCommon()
        CmdbConfigurePage(self.driver).click_next()

        # 上一步
        CmdbConfigurePage(self.driver).click_backbtn2()
        # 断言
        next1 = CmdbConfigurePage(self.driver).checknext()
        self.assertEqual(next1, True, msg='填写表单字段信息点击上一步失败')

        # 下一步
        CmdbConfigurePage(self.driver).click_next()
        # 返回列表
        CmdbConfigurePage(self.driver).click_backlist2()
        time.sleep(3)
        # 断言
        CmdbConfigurePage(self.driver).search_input(name)
        time.sleep(3)
        getname = CmdbConfigurePage(self.driver).get_empty_tip()
        self.assertEqual(getname, '这里空空如也, 跟我的钱包一样', msg='填写表单字段信息返回列表失败')

        # （1）检查添加页面的返回列表
        CmdbConfigurePage(self.driver).click_add()
        time.sleep(2)
        CmdbConfigurePage(self.driver).click_backlist()

        # 取添加按钮点击状态
        check1 = CmdbConfigurePage(self.driver).checkadd()
        self.assertEqual(check1, True, '填写类的基本信息返回列表错误')

    # # 检查 添加-下一步-提交 检查定制模板页面的 上一步按钮，继续新建资产按钮，返回列表按钮
    # @unittest.skip("20201012 同test007，添加后数据在第六页，第六页记录搜索不到,跳过")   # 2022-01-06恢复
    def test_006(self):
        name = CmdbConfigureCommon(self.driver).CmdbConfigure_requestCommon()
        CmdbConfigurePage(self.driver).click_next()
        CmdbConfigurePage(self.driver).click_submit2()

        # 上一步
        # Base(self.driver).move_to_pagebottom()
        CmdbConfigurePage(self.driver).Backbtn3()
        CmdbConfigurePage(self.driver).click_submit2()
        # 填写表单字段信息 ，返回列表
        CmdbConfigurePage(self.driver).backlist3()

        CmdbConfigurePage(self.driver).search_input(name)
        CmdbConfigurePage(self.driver).click_search_relust()

        # 继续添加
        CmdbConfigurePage(self.driver).click_next()
        CmdbConfigurePage(self.driver).click_submit2()
        # Base(self.driver).move_to_pagebottom()
        CmdbConfigurePage(self.driver).createagain()
        getnext = CmdbConfigurePage(self.driver).getnext()
        self.assertEqual(getnext, '下一步', msg='错误')

    # (1)检查类别复制  (2)类别名称唯一性检验
    # @unittest.skip("20201012，添加后数据在第六页，第六页记录搜索不到,跳过")  # 2022-01-06恢复
    def test_007(self):
        '''复制'''
        name = CmdbConfigureCommon(self.driver).CmdbConfigure_requestCommon()
        CmdbConfigurePage(self.driver).click_next()
        CmdbConfigurePage(self.driver).click_submit2()
        # Base(self.driver).move_to_pagebottom()
        CmdbConfigurePage(self.driver).backlist3()

        # 搜索 点击复制
        CmdbConfigurePage(self.driver).search_input(name)
        CmdbConfigurePage(self.driver).click_copy()

        CmdbConfigurePage(self.driver).click_next()
        CmdbConfigurePage(self.driver).click_submit2()
        # Base(self.driver).move_to_pagebottom()
        CmdbConfigurePage(self.driver).backlist3()

        # 搜索 断言
        CmdbConfigurePage(self.driver).search_input(name)

        temnumber = CmdbConfigurePage(self.driver).gettemnuber()  # 调整断言2022-01-06
        self.assertEqual(temnumber, 2, msg='复制工单模板失败')  # 调整断言2022-01-06

        # totaltab = CmdbConfigurePage(self.driver).get_total()
        # self.assertEqual(totaltab, '全部 ( 2 )', msg='错误，复制cmdb类别失败')

        # 类名唯一性校验
        CmdbConfigurePage(self.driver).click_add()
        time.sleep(2)
        CmdbConfigurePage(self.driver).inputname(name)
        name_tip = CmdbConfigurePage(self.driver).get_name_tip()
        submitinfo = CmdbConfigurePage(self.driver).checknext()
        self.assertEqual(name_tip, '类型名字已存在!', msg='名称重复未提示')
        self.assertEqual(submitinfo, False, msg='错误：cmdb配置名称重复，下一步按钮可触发')

    # @unittest.skip("20201012 同test007，添加后数据在第六页，第六页记录搜索不到,跳过")  # 2022-01-06恢复
    def test_008(self):
        '''类别名称必填校验'''
        # 进入页面首选判断必填
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "cmdb必填" + strnumber
        EntranceAgentPage(self.driver).enter_cmdb_configure()
        time.sleep(5)
        CmdbConfigurePage(self.driver).click_add()
        submitinfo = CmdbConfigurePage(self.driver).checknext()
        self.assertEqual(submitinfo, False, msg='错误：名称未输入，下一步按钮可触发')

        CmdbConfigurePage(self.driver).inputname('    ')
        time.sleep(2)
        submitinfo = CmdbConfigurePage(self.driver).checknext()
        self.assertEqual(submitinfo, False, msg='错误：必填项输入空格，提交按钮可触发')

        CmdbConfigurePage(self.driver).inputname(name)
        time.sleep(2)
        submitinfo = CmdbConfigurePage(self.driver).checknext()
        self.assertEqual(submitinfo, True, msg='错误：必填项已填写，提交按钮不可触发')

        CmdbConfigurePage(self.driver).delete_valid()
        time.sleep(2)
        submitinfo = CmdbConfigurePage(self.driver).checknext()
        self.assertEqual(submitinfo, False, msg='错误：有效性为空，提交按钮可触发')

    # @unittest.skip("20201012 同test007，添加后数据在第六页，第六页记录搜索不到,跳过")  # 2022-01-06恢复
    # 2022-01-06 整合用例到007，屏蔽该用例
    # def test_009(self):
    #     '''类别名称唯一性检验'''
    #     name = CmdbConfigureCommon(self.driver).CmdbConfigure_requestCommon()
    #     CmdbConfigurePage(self.driver).click_next()
    #     CmdbConfigurePage(self.driver).click_submit2()
    #     # Base(self.driver).move_to_pagebottom()
    #     CmdbConfigurePage(self.driver).backlist3()
    #     CmdbConfigurePage(self.driver).click_add()
    #     time.sleep(2)
    #     CmdbConfigurePage(self.driver).inputname(name)
    #     name_tip = CmdbConfigurePage(self.driver).get_name_tip()
    #     submitinfo = CmdbConfigurePage(self.driver).checknext()
    #     self.assertEqual(name_tip, '类型名字已存在!', msg='名称重复未提示')
    #     self.assertEqual(submitinfo, False, msg='错误：cmdb配置名称重复，下一步按钮可触发')

    # # 检查添加系统字段
    # @unittest.skip("20201012 同test007，添加后数据在第六页，第六页记录搜索不到,跳过")  # 2022-01-06恢复
    def test_010(self):
        '''检查添加系统字段'''
        name = CmdbConfigureCommon(self.driver).CmdbConfigure_requestCommon("添加系统字段")
        CmdbConfigurePage(self.driver).click_next()
        time.sleep(5)
        CmdbConfigurePage(self.driver).select_field('出库日期')
        CmdbConfigurePage(self.driver).click_submit2()

        # Base(self.driver).move_to_pagebottom()
        CmdbConfigurePage(self.driver).backlist3()

        CmdbConfigurePage(self.driver).search_input(name)
        CmdbConfigurePage(self.driver).click_search_relust()
        CmdbConfigurePage(self.driver).click_next()

        forminfo = ['名称','资产生命周期','资产状态','资产使用人','资产维护人','使用科室','资产数量','资产开始日期','资产截止日期',
                    '位置','出库日期','选择要显示的字段']
        getforminfo = CmdbConfigurePage(self.driver).getshow_field()
        # print(len(getforminfo))

        for i in range(0, len(getforminfo)-1):
            forminfo01 = getforminfo[i].text
            with self.subTest(i=i):
                # print(forminfo01)
                self.assertEqual(forminfo01, forminfo[i], msg='表单字段中添加系统字段失败')

        # EntranceAgentPage(self.driver).enter_cmdb_configure()
        # time.sleep(5)
        # CmdbConfigurePage(self.driver).search_input('电脑')
        # CmdbConfigurePage(self.driver).click_search_relust()
        # CmdbConfigurePage(self.driver).click_next()
        # time.sleep(5)
        # CmdbConfigurePage(self.driver).select_field('出库日期')
        # time.sleep(3)
