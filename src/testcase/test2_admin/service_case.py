"""
@author: DT_testing
@file:   service_case.py
@desc:  【服务】
@step： 001. （1）检查添加按钮，SC_service_4
            （2）填写必填增，点击提交并返回,验证返回列表按钮  SC_service_20
            （3）右侧查询存在的数据  SC_service_6
        002. 填写必填，点击下一步  SC_service_27  SC_service_22  OK
        003. 不填写必填项，检查下一步按钮，返回列表   SC_service_19  SC_service_10 SC_service_36  ok
        004. 检验服务名称(重名，空格输入) SC_service_24、SC_service_25
        005. 关联一个服务协议,删除协议，修改协议 ,完成按钮
          SC_service_32 、SC_service_39   SC_service_38  SC_service_34   ok（流程太长，出错几率大，考虑拆分该用例）
        006. 关联多个服务协议  SC_service_33 ok
        007. 服务关联页面，检查上一步按钮  SC_service_35  ok
        008. 检查列表过滤功能：过滤存在数据，不存在数据，模糊过滤，特殊字符过滤  ok


"""
import time

from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.service_commom import ServiceCommon
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.agent.service_page import ServicePage
from src.page.pagecommon.servicesla_common import ServiceSlaCommon

import random


class Service(BaseCaseUser, Base):

    def test_001(self):
        '''验证填写必填增,验证返回列表按钮'''

        # 填写必填添加服务

        Serviceinfo = ServiceCommon(self.driver).ServiceRequiredCommon()
        name = Serviceinfo.get('name')
        # 提交并返回按钮
        ServicePage(self.driver).submitreturn()
        time.sleep(3)

        # 搜索后进入服务
        ServicePage(self.driver).right_search(name)
        time.sleep(2)
        # 进入编辑页面
        ServicePage(self.driver).search_result()

        getname = ServicePage(self.driver).getname()
        self.assertEqual(getname, name, msg='填写必填新增服务，提交并返回按钮，服务添加失败')

    def test_002(self):
        '''填写必填，点击下一步,返回列表 '''

        # 填写必填添加服务
        Serviceinfo = ServiceCommon(self.driver).ServiceRequiredCommon()
        name = Serviceinfo.get('name')
        # 点击下一步
        ServicePage(self.driver).next()
        time.sleep(3)
        # 点击返回列表
        ServicePage(self.driver).goBack2()
        time.sleep(1)

        # 搜索后进入服务
        ServicePage(self.driver).right_search(name)
        time.sleep(2)
        # 进入编辑页面
        ServicePage(self.driver).search_result()
        time.sleep(2)

        # 取服务名称进行断言 getname
        getname = ServicePage(self.driver).getname()
        self.assertEqual(getname, name, msg='填写必填新增服务，直接点击下一步，服务添加失败')

    def test_003(self):
        '''不填写必填，检查下一步/提交返回,检查返回列表 '''

        EntranceAgentPage(self.driver).enter_service()
        time.sleep(2)
        ServicePage(self.driver).add()
        time.sleep(2)
        next_disabled = ServicePage(self.driver).is_disabled('下一步')
        submitreturn_disabled = ServicePage(self.driver).is_disabled('提交并返回列表')

        self.assertEqual(next_disabled, 'true', msg='错误：不填写必填项，下一步按钮可点击')
        self.assertEqual(
            submitreturn_disabled,
            'true',
            msg='错误：不填写必填项，提交并返回按钮可点击')

        time.sleep(2)
        # 检查返回列表按钮
        ServicePage(self.driver).goBack1()
        time.sleep(3)

        # 检查列表字段  gettable_head
        table_head = ['名称', '备注', '有效性', '创建时间', '修改时间']
        gettable_head = ServicePage(self.driver).gettable_head()
        for i in range(0, len(table_head)):
            gettable_head_one = gettable_head[i].text
            self.assertEqual(
                gettable_head_one,
                table_head[i],
                msg='错误：列表表头列显示错误')

    # 出现报错的情况有：校验时间过长
    def test_004(self):
        '''服务名称校验'''

        # 填写必填添加服务
        Serviceinfo = ServiceCommon(self.driver).ServiceRequiredCommon()
        name = Serviceinfo.get('name')
        # 点击下一步
        ServicePage(self.driver).next()
        time.sleep(3)
        # 点击返回列表
        ServicePage(self.driver).goBack2()

        # 进入新增页面，名称输入空格
        time.sleep(2)
        ServicePage(self.driver).add()
        ServicePage(self.driver).inputname('    ')
        nametip = ServicePage(self.driver).getnametip()
        next_disabled = ServicePage(self.driver).is_disabled('下一步')
        submitreturn_disabled = ServicePage(self.driver).is_disabled('提交并返回列表')

        self.assertEqual(next_disabled, 'true', msg='错误：服务名称为空格，下一步按钮可点击')
        self.assertEqual(
            submitreturn_disabled,
            'true',
            msg='错误：服务名称为空格，提交并返回按钮可点击')
        self.assertEqual(nametip, '数据格式错误,请重新输入!', msg='错误：服务名称为空格，提示错误')

        ServicePage(self.driver).inputname(name)
        # 重名校验时间过长，增加等待时间
        # time.sleep(5)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),'第一个时间')
        nametip2 = ServicePage(self.driver).getnametip()
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '第二个时间')
        next_disabled = ServicePage(self.driver).is_disabled('下一步')
        submitreturn_disabled = ServicePage(self.driver).is_disabled('提交并返回列表')

        self.assertEqual(next_disabled, 'true', msg='错误：服务名称重复，下一步按钮可点击')
        self.assertEqual(
            submitreturn_disabled,
            'true',
            msg='错误：服务名称重复，提交并返回按钮可点击')
        self.assertEqual(nametip2, '数据校验不通过，该值已存在，请重新输入！', msg='错误：服务名称重复，提示错误')
    # 20210220 创建协议需要工作时间必填，先屏蔽该用例，后续调整
    # def test_005(self):
    #     '''关联一个服务协议，删除协议, 切换协议'''
    #     slainfo01 = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
    #     slaname01 = slainfo01.get('slaname')
    #
    #     slainfo02 = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
    #     slaname02 = slainfo02.get('slaname')
    #
    #     Serviceinfo = ServiceCommon(self.driver).ServiceRequiredCommon()
    #     servicename = Serviceinfo.get('name')
    #
    #     ServicePage(self.driver).next()
    #     time.sleep(2)
    #     # 搜索服务水平协议，点击添加
    #     ServicePage(self.driver).choose_sla(slaname01)
    #     # 点击完成
    #     ServicePage(self.driver).complete()
    #     time.sleep(8)
    #
    #     # 搜索服务，点击  这里出错！！！
    #     ServicePage(self.driver).right_search(servicename)
    #     time.sleep(2)
    #     # 进入编辑页面
    #     ServicePage(self.driver).search_result()
    #     time.sleep(2)
    #     # 下一步，进入服务关联项页面
    #     ServicePage(self.driver).next()
    #
    #     # 取协议值，断言 Association_sla
    #     Association_sla = ServicePage(self.driver).Association_sla()
    #     self.assertEqual(Association_sla, slaname01, msg='服务关联一个服务协议失败')
    #
    #     # 删除一个服务协议，断言检查
    #     ServicePage(self.driver).delete_all_sla()
    #     ServicePage(self.driver).complete_add()
    #     time.sleep(4)
    #     ServicePage(self.driver).goBack1()
    #     time.sleep(2)
    #     # 此处出现问题
    #     ServicePage(self.driver).right_search(servicename)
    #     time.sleep(2)
    #     # 进入编辑页面
    #     ServicePage(self.driver).search_result()
    #     time.sleep(2)
    #     # 下一步，进入服务关联项页面
    #     ServicePage(self.driver).next()
    #
    #     # 取协议值，断言 Association_sla
    #     Association_sla = ServicePage(self.driver).Association_sla()
    #     self.assertEqual(Association_sla, '', msg='删除关联的服务失败')
    #
    #     # 编辑修改新的协议
    #     ServicePage(self.driver).choose_sla(slaname02)
    #     # 点击完成
    #     ServicePage(self.driver).complete()
    #     time.sleep(8)
    #     # 搜索服务，点击
    #     ServicePage(self.driver).right_search(servicename)
    #     time.sleep(2)
    #     # 进入编辑页面
    #     ServicePage(self.driver).search_result()
    #     time.sleep(2)
    #     ServicePage(self.driver).next()
    #     # 取协议值，断言 Association_sla
    #     Association_sla = ServicePage(self.driver).Association_sla()
    #     self.assertEqual(Association_sla, slaname02, msg='服务修改关联一个服务协议失败')

    # def test_006(self):   # ----需要验证
    #     '''关联多个服务协议'''
    #     slainfo01 = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
    #     slaname01 = slainfo01.get('slaname')
    #     slainfo02 = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
    #     slaname02 = slainfo02.get('slaname')
    #     Serviceinfo = ServiceCommon(self.driver).ServiceRequiredCommon()
    #     servicename = Serviceinfo.get('name')
    #
    #     ServicePage(self.driver).next()
    #     # 搜索服务水平协议，点击添加
    #     ServicePage(self.driver).choose_sla(slaname01)
    #     ServicePage(self.driver).choose_sla(slaname02)
    #     # 点击完成
    #     ServicePage(self.driver).complete()
    #     time.sleep(2)
    #
    #     # 搜索服务，点击
    #     ServicePage(self.driver).right_search(servicename)
    #     time.sleep(2)
    #     # 进入编辑页面
    #     ServicePage(self.driver).search_result()
    #     time.sleep(2)
    #     # 下一步，进入服务关联项页面
    #     ServicePage(self.driver).next()
    #
    #     # 取协议值，断言 Association_sla
    #     Association_sla = ServicePage(self.driver).Association_sla()
    #     # print(Association_sla)
    #     self.assertEqual(Association_sla, slaname, msg='服务关联一个服务协议失败')

    def test_007(self):
        '''服务关联页面，检查上一步按钮，返回列表 '''

        # 填写必填添加服务
        Serviceinfo = ServiceCommon(self.driver).ServiceRequiredCommon()
        name = Serviceinfo.get('name')
        # 点击下一步
        ServicePage(self.driver).next()
        time.sleep(3)

        # 上一步
        ServicePage(self.driver).previous()
        # 点击返回列表
        ServicePage(self.driver).goBack1()
        # 通过列表返回
        getbar = ServicePage(self.driver).getbar()
        # print(getbar)

        self.assertEqual(getbar, '/ 系统管理 / 服务', msg='服务关联页面-上一步-返回列表错误')

    def test_008(self):
        '''列表过滤'''

        # 填写必填添加服务
        EntranceAgentPage(self.driver).enter_service()
        time.sleep(2)
        ServicePage(self.driver).add()
        time.sleep(2)
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = strnumber + "TicketFreeText!@#$%^&" + strnumber
        ServicePage(self.driver).inputname(name)

        # 点击提交并返回列表
        ServicePage(self.driver).submitreturn()
        time.sleep(6)
        num1 = 0
        # num2 = 0
        num3 = 0

        ServicePage(self.driver).right_search(strnumber)
        leftslaname = ServicePage(self.driver).getleftslaname()
        #
        time.sleep(3)
        for i in range(0, len(leftslaname)):
            listinfo = leftslaname[i].text
            if listinfo == name:
                num1 = num1 + 1

        # ServicePage(self.driver).right_search('FreeText')
        # leftslaname = ServicePage(self.driver).getleftslaname()
        # for i in range(0, len(leftslaname)):
        #     listinfo = leftslaname[i].text
        #     if listinfo == name:
        #         num2 = num2+1

        ServicePage(self.driver).right_search('@#$%^&' + strnumber)
        leftslaname = ServicePage(self.driver).getleftslaname()
        for i in range(0, len(leftslaname)):
            listinfo = leftslaname[i].text
            if listinfo == name:
                num3 = num3 + 1
        self.assertEqual(num1, 1, msg='错误：模糊搜索前段数据未查到匹配数据')
        # self.assertEqual(num2, 1, msg='错误：模糊搜索中段数据未查到匹配数据')
        self.assertEqual(num3, 1, msg='错误：模糊搜索后段数据，特殊字符未查到匹配数据')

        # 搜索不存在的数据
        ServicePage(self.driver).right_search('想喇十八章')
        # 取表格的搜索  get_tab_text
        tab_text = ServicePage(self.driver).get_tab_text()
        # 断言
        self.assertEqual(tab_text, '有效 ( 0 )', msg='搜索不存在的数据失败')
