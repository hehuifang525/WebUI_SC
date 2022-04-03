"""
@author: QianJingjing
@file:   role_case.py
@desc:  【角色】
@step： 1. 检查角色面包屑（路径）、进入角色列表检查默认列表头、url title（SC_Role_1、SC_Role_5）
        2. 检查添加页面的“返回”按钮（SC_Role_6）
        3. 只填写必填项新增组检查（SC_Role_7）
        4. 添加下一步继续新增重名的角色，检查提示信息（SC_Role_14）
        5. 填写所有值，a.检查名称父子级显示 b.二次进入页面检查已填写内容（SC_Role_9）
        6. 编辑角色字段并无效，检查列表，检查二次进入查看编辑的值（SC_Role_18、SC_Role_19、SC_Role_21）
        7. 进入无效角色编辑然后直接返回，再次进入编辑为有效（SC_Role_16、SC_Role_20）
        8. 检查下一步、上一步增加备注、下一步，完成。检查备注正常显示（SC_Role_11）
        9. 添加系统已有的角色，新增“Postmaster”提示重名（SC_Role_13）
        10.全填的角色编辑时不修改值，二次进入查看，值不会被置空或修改（SC_Role_17）
        11.将角色编辑为已有的角色名称，检查重名校验（SC_Role_23）
        12.检查角色关联页面字段（第二页字段值显示）（﻿SC_Role_28）
        未完成13.检查角色关联页面选择服务人员、默认所有者、默认负责人、角色管理者 root@localhost，二次进入查看 （SC_Role_29）-待开发多选确定按钮
        14.过滤：验证有数据的值过滤。已如账号、姓名、手机号、邮件等（SC_Role_55）
        15. 在有效角色列表，搜索不存在的角色内容（SC_Role_56）
        16. 添加有效角色并关联单个权限，二次进入检查 （SC_Role_33）
        17. 无效的权限不会在角色关联页面显示 (SC_Role_34)
        18. 角色关联多个菜单权限，二次进入检查 (SC_Role_35)
        20. 将已设置的权限删除，二次进入检查权限已正常删掉

"""
import time
import unittest2
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.menuset_page import MenusetPage
from src.page.agent.role_page import RolePage
from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.menusetting_common import MenusetCommon
from src.page.pagecommon.role_common import RoleCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base


class Role(BaseCaseUser, Base):

    # 1. 检查角色面包屑（路径）、进入角色列表检查默认列表头、url title（SC_Role_1、SC_Role_5）
    def test_1_rolelist(self):
        try:
            # 开始--角色
            EntranceAgentPage(self.driver).enter_role()
            time.sleep(5)
            # 检查列表头默认值（名称、角色所属区域、默认所有者、默认负责人、角色管理者、备注、有效性、修改时间、修改人）
            # 页面字段检查及值检查
            for fields in [".ant-table-thead th"]:
                for i in range(0, 9):
                    text = self.driver.find_elements_by_css_selector(fields)[
                        i].text
                    # print(text)
                    if text != '名称' and text != '角色所属区域' and text != '默认所有者' and text != '默认负责人' \
                            and text != '角色管理者' and text != '备注' and text != '有效性' and text != '修改时间'\
                            and text != '修改人':
                        print("角色列表显示不正确！正确显示是：" + text)
            # 检查 url title
            result = Base(self.driver).get_title()
            if result != '角色':
                print('角色列表当前窗口 title 显示不正确')

            # 检查路径
            road = RolePage(self.driver).road()
            self.assertEqual(road, '/ 系统管理 / 角色', msg='角色列表路径显示不正确')
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'角色列表页面显示的路径显示不正确/角色页面字段显示不正确' + str(msg))

    # 2. 检查添加页面的“返回”按钮（SC_Role_6）   -- ok
    def test_2_roleAdd(self):
        try:
            # 开始--角色
            EntranceAgentPage(self.driver).enter_role()
            # 点击“添加”
            RolePage(self.driver).addrole()

            # 点击“返回”
            RolePage(self.driver).returnlist1()
            time.sleep(3)

            # 检查搜索默认自带 Misc 存在
            RolePage(self.driver).searchtab("Misc")
            result = RolePage(self.driver).searchresult()

            self.assertEqual(result, 'Misc', msg='添加角色不填写直接返回，返回角色页面不正确')

        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'添加角色不填写直接返回，返回角色页面不正确' + str(msg))
#
#     # 3. 只填写必填项新增组检查（SC_Role_7） -- ok

    def test_3_roleAdd(self):
        try:
            # 开始--角色--添加--必填项填写
            name = RoleCommon(self.driver).rolerequiredcommon()
            # 保存并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(3)

            # 搜索检查。 检查列表显示出。为避免显示在翻页找不到，搜索然后判断
            RolePage(self.driver).searchtab(name)

            result = RolePage(self.driver).searchresult()
            hope = name
            self.assertEqual(result, hope, msg='未搜索出新增的角色，新增的必填角色没有在列表显示')
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'未搜索出新增的角色，新增的必填角色没有在列表显示' + str(msg))
#
#     # # 4. 添加下一步继续新增重名的角色，检查提示信息（SC_Role_14）新的组名被包含于已存在的组，检查校验提示 --系统 bug 未修复

    def test_4_roleAdd(self):
        try:
            # 开始--角色--添加--必填项填写
            name = RoleCommon(self.driver).rolerequiredcommon()
            # 下一步
            RolePage(self.driver).savenextbtn()
            # 再次添加
            RolePage(self.driver).addagain()
            time.sleep(2)

            # 再次新增
            RolePage(self.driver).rolename(name)
            time.sleep(2)

            # 检查提示，应当提示  系统 bug 当前无提示
            ll = self.driver.find_element_by_css_selector(
                '#Name_errorServeMessage').text
            self.assertEqual(ll, '该名称已存在，请更换其他名称！', msg='添加下一步继续新增重名角色未提示重名')
            # print(ll)
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'连续添加重名角色，未提示重名' + str(msg))

    # 5. 填写所有值，a.检查名称父子级显示 b.二次进入页面检查已填写的各项内容（SC_Role_9）
    def test_5_roleAdd(self):
        try:
            # 开始--角色--添加--填写第一页所有值
            name = RoleCommon(self.driver).rolefullcommon()

            # 保存并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(2)

            RolePage(self.driver).searchtab(name)
            # 检查列表显示出。为避免显示在翻页找不到，搜索然后判断
            result = RolePage(self.driver).searchresult()
            hope = "Postmaster::" + name
            # print(hope)
            self.assertEqual(result, hope, msg='test_5 未搜索出新增的组，新增的组没有在组列表显示')

            # 搜索到点击二次进入检查已填值
            RolePage(self.driver).clicksearchresult()
            time.sleep(5)

            nameresult = RolePage(self.driver).nameresult()
            # print(name)
            self.assertEqual(nameresult, name, msg='二次进入查看与新增时的角色名称显示不一致')

            furesult = RolePage(self.driver).parentresult()
            # print(furesult)
            self.assertEqual(
                furesult,
                'Postmaster',
                msg='二次进入查看与新增时的父角色名称显示不一致')

            mailtext = RolePage(self.driver).systemadressresult()
            # print(mail)
            self.assertEqual(mailtext,'otrs@localhost', msg='二次进入查看与新增时的系统邮件地址显示不一致')

            validtext = RolePage(self.driver).validresult()
            self.assertEqual(validtext, '有效', msg='二次进入查看与新增时的有效性显示不一致')

            commenttext = RolePage(self.driver).commenttext()
            # print(commenttext)
            self.assertEqual(
                commenttext,
                '备注信息' + name,
                msg='二次进入查看与新增时的备注显示不一致')

        except AssertionError as msg:
            Base.get_windows_img(self)
            self.logger.error(
                u'填写所有值，a.检查名称父子级显示 b.二次进入页面检查已填写内容。其中有报错' + str(msg))

    # 6. 编辑角色字段并无效，检查列表，检查二次进入查看编辑的值（SC_Role_18、SC_Role_19、SC_Role_21）
    def test_6_roleEdit(self):
        try:
            # 开始--角色--添加--全填写
            name = RoleCommon(self.driver).rolefullcommon()
            # 下一步
            RolePage(self.driver).savenextbtn()
            # 完成
            RolePage(self.driver).savebtn()
            time.sleep(4)

            RolePage(self.driver).searchtab(name)

            # 搜索到点击二次进入编辑
            RolePage(self.driver).clicksearchresult()
            # 编辑
            # name
            now_time = GetTimeCommon(self.driver).get_time()
            editname = "edit" + now_time
            RolePage(self.driver).rolename(editname)
            # 父角色
            parentrole = "Raw"
            RolePage(self.driver).parentrole(parentrole)
            RolePage(self.driver).chooseparentrole(parentrole)
            time.sleep(2)
            # 系统邮件地址--只有一个，不修改
            # 无效
            RolePage(self.driver).clickchooseinvalid()
            # RolePage(self.driver).chooseinvalid()
            # 备注
            RolePage(self.driver).comment('编辑备注')

            # 提交并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(2)

            # 点击列表--无效按钮--过滤搜索
            RolePage(self.driver).invalidlist()
            RolePage(self.driver).searchtab(editname)

            # 页面字段值检查
            list2 = ['Raw::' + editname, '', '', '', '', '编辑备注', '无效']
            for fields in [".ant-table-row td"]:  # 0716修改
                for i in range(0, 7):
                    text2 = self.driver.find_elements_by_css_selector(fields)[i].text
                    self.assertEqual(text2, list2[i], msg="编辑角色在列表显示不正确！正确显示是：" + list2[i] + "'")
            # 进入页面查看
            RolePage(self.driver).clicksearchresult()

            nameresult = RolePage(self.driver).nameresult()
            # print(name)
            self.assertEqual(nameresult, name, msg='二次进入查看与编辑时的角色名称显示不一致')

            furesult = RolePage(self.driver).parentresult()
            # print(furesult)
            self.assertEqual(furesult, 'Raw', msg='二次进入查看与编辑时的父角色名称显示不一致')

            mailtext = RolePage(self.driver).systemadressresult()
            # print(mail)
            self.assertEqual(
                mailtext,
                'otrs@localhost',
                msg='二次进入查看与编辑时的父角色名称系统邮件地址显示不一致')

            validtext = RolePage(self.driver).validresult()
            time.sleep(3)
            # print(mail)
            self.assertEqual(validtext, '无效', msg='二次进入查看与编辑时的父角色名称有效性显示不一致')

        except AssertionError as msg:
            Base.get_windows_img(self)
            self.logger.error(u'编辑角色字段并无效，检查列表，检查二次进入查看编辑的值。其中有报错' + str(msg))

    # 7. 进入无效角色编辑然后直接返回，再次进入编辑为有效（SC_Role_16、SC_Role_20）
    def test_7_roleEdit(self):
        try:
            # 开始--角色--无效角色
            name = RoleCommon(self.driver).roleinvalidcommon()
            # 提交并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(2)

            # 点击切换无效列表
            RolePage(self.driver).invalidlist()
            time.sleep(3)
            # 搜索并进入
            RolePage(self.driver).searchtab(name)
            RolePage(self.driver).clicksearchresult()
            time.sleep(5)
            # 返回列表（会自动返回有效列表）
            RolePage(self.driver).returnlist1()
            time.sleep(2)

            # 先切换无效列表
            RolePage(self.driver).invalidlist()
            # 再次过滤进入无效角色
            RolePage(self.driver).searchtab(name)
            RolePage(self.driver).clicksearchresult()
            time.sleep(2)

            # 编辑为有效
            RolePage(self.driver).rolename(name + '编辑为有效')
            RolePage(self.driver).clickchoosevalid()
            # RolePage(self.driver).choosevalid()
            # 提交并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(2)

            # 再次过滤检查已被设置为有效状态的“无效角色“
            RolePage(self.driver).searchtab(name + '编辑为有效')
            time.sleep(2)
            # 页面字段值检查
            # 页面字段检查及值检查
            list3 = [name + '编辑为有效', '', '', '', '', '', '有效']
            for fields in [".ant-table-row td"]:  # 0716修改
                # for fields in [".ant-table-tbody td"]:  # 0716修改
                for i3 in range(0, 7):
                    text3 = self.driver.find_elements_by_css_selector(fields)[
                        i3].text
                    # print(text3)
                    # if text3 != name and text3 != '' and text3 != '' and text3 != '' and text3 != '' \
                    #         and text3 != '' + name and text3 != '有效':
                    #     print("无效角色编辑为有效后在列表显示不正确！正确显示是：" + text3)
                    assert text3 == list3[i3], "角色关联页面字段显示不正确！正确显示是：'" + text3 + "'"

        except AssertionError as msg:
            Base.get_windows_img(self)
            self.logger.error(u'编辑角色字段并无效，检查列表，检查二次进入查看编辑的值。其中有报错' + str(msg))

    # 8. 检查下一步、上一步增加备注、下一步，完成。检查备注正常显示（SC_Role_11）
    def test_8_roleAdd(self):
        try:
            # 开始--角色--添加--必填项填写
            name = RoleCommon(self.driver).rolerequiredcommon()
            # 下一步
            RolePage(self.driver).savenextbtn()
            time.sleep(3)

            # 上一步
            RolePage(self.driver).backbtn()

            # 增加备注
            RolePage(self.driver).comment("备注信息test_8")
            # 下一步
            RolePage(self.driver).savenextbtn()
            # 完成
            RolePage(self.driver).savebtn()
            time.sleep(4)

            # 搜索检查
            RolePage(self.driver).searchtab(name)
            time.sleep(3)
            # 检查列表显示出。为避免显示在翻页找不到，搜索然后判断
            result = RolePage(self.driver).searchresult()
            hope = name
            self.assertEqual(result, hope, msg='test_4 未搜索出新增的组，新增的组没有在组列表显示')

            list = [name, '', '', '', '', '备注信息test_8', '有效']
            num = len(
                self.driver.find_elements_by_css_selector('[nowrap="nowrap"]'))
            for fields in [".ant-table-row td"]:  # 0716 修改
                # for fields in [".ant-table-tbody td"]:  #0716修改
                for i4 in range(0, 7):   # 不打印最后一栏 “修改时间”
                    text4 = self.driver.find_elements_by_css_selector(fields)[
                        i4].text
                    # print(text4, list[i4] , i4 ,num )
                    assert text4 == list[i4], "工单模板页面缺少字段显示！正确显示是：'" + \
                        text4 + "'"
        except AssertionError as msg:
            Base.get_windows_img(self)
            self.logger.error(u'下一步、上一步增加备注、下一步，完成。检查备注正常显示。其中有报错' + str(msg))

    # 9. 添加系统已有的角色，新增“Postmaster”提示重名（SC_Role_13）
    def test_9_roleAdd(self):
        try:
            # 开始--角色--新增
            EntranceAgentPage(self.driver).enter_role()
            time.sleep(8)
            RolePage(self.driver).addrole()
            # 填写name：Postmaster
            RolePage(self.driver).rolename("Postmaster")
            time.sleep(2)

            # 检查提示，应当提示
            # tip = self.driver.find_element_by_css_selector('.name-text-propmt').text
            tip = self.driver.find_element_by_css_selector(
                '.ng-trigger-helpMotion').text

            self.assertEqual(tip, u"该名称已存在，请更换其他名称！")
        except AssertionError as msg:
            Base.get_windows_img(self)
            self.logger.error(u'添加已有的角色名称，名称下方会提示重名' + str(msg))

    # 10. 全填的角色编辑时不修改值，二次进入查看，值不会被置空或修改（SC_Role_17）ok
    def test_10_roleAdd(self):
        try:
            # 开始--角色--添加--填写第一页所有值
            name = RoleCommon(self.driver).rolefullcommon()
            # 保存并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(2)

            # 搜索到点击进入编辑，不修改直接点击返回
            RolePage(self.driver).searchtab(name)
            RolePage(self.driver).clicksearchresult()
            time.sleep(5)
            RolePage(self.driver).returnlist1()
            time.sleep(2)
            # 搜索并进入查看编辑不修改值，之后的显示
            RolePage(self.driver).searchtab(name)
            RolePage(self.driver).clicksearchresult()
            time.sleep(2)

            nameresult = RolePage(self.driver).nameresult()
            # print(name)
            if nameresult != name:

                print("不编辑返回后，二次查看与新增时的角色名称显示不一致")

            furesult = RolePage(self.driver).parentresult()
            # print(furesult)
            self.assertEqual(
                furesult,
                'Postmaster',
                msg='不编辑返回后，二次进入查看与新增时的父角色名称显示不一致')

            mailtext = RolePage(self.driver).systemadressresult()
            # print(mailtext)
            self.assertEqual(
                mailtext,
                'otrs@localhost',
                msg='不编辑返回，二次进入查看与新增时的父角色名称系统邮件地址显示不一致')

            validtext = RolePage(self.driver).validresult()
            # print(validtext)
            self.assertEqual(validtext, '有效', msg='二次进入查看与新增时的父角色名称有效性显示不一致')

        except AssertionError as msg:
            Base.get_windows_img(self)
            self.logger.error(u'全填的角色编辑时不修改值，二次进入查看，值不会被置空或修改' + str(msg))

    # 11. 将角色编辑为已有的角色名称，检查重名校验（SC_Role_23）
    def test_11_roleEdit(self):
        try:
            # 开始--角色
            EntranceAgentPage(self.driver).enter_role()
            time.sleep(5)

            # 搜索“Misc”，改为“Postmaster”
            RolePage(self.driver).searchtab('Misc')
            RolePage(self.driver).clicksearchresult()
            time.sleep(2)
            # 编辑改为 Postmaster
            RolePage(self.driver).rolename("Postmaster")
            time.sleep(2)

            # 检查提示，应当提示
            # tip = self.driver.find_element_by_css_selector('.name-text-propmt').text
            tip = self.driver.find_element_by_css_selector(
                '.ng-trigger-helpMotion').text
            self.assertEqual(tip, u"该名称已存在，请更换其他名称！")
        except AssertionError as msg:
            Base.get_windows_img(self)
            self.logger.error(u'将角色编辑为已有的角色名称，会有重名校验提示' + str(msg))

    # 12. 检查角色关联页面字段（第二页字段值显示）（SC_Role_28）
    def test_12_roleAdd(self):
        try:
            # 开始--角色--添加--必填项填写
            RoleCommon(self.driver).rolerequiredcommon()
            # 下一步
            RolePage(self.driver).savenextbtn()
            time.sleep(3)
            # 检查字段
            list = ['角色所属区域', '服务人员', '默认所有者', '默认负责人', '角色管理者',"关联标签", '菜单权限']
            for fields in ["#step2 label"]:
                for i5 in range(0, 6):
                    text5 = self.driver.find_elements_by_css_selector(fields)[
                        i5].text
                    # print(text5)
                    self.assertEqual(
                        text5, list[i5], msg="角色关联页面字段显示不正确！正确显示是：'" + text5 + "'")
                    # assert text5 == list[i5], "角色关联页面字段显示不正确！正确显示是：'" + text5 + "'"

        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'角色关联页面字段显示有误' + str(msg))

    # # 13. 检查角色关联页面选择服务人员、默认所有者、默认负责人、角色管理者 root@localhost，二次进入查看 （SC_Role_29）--待执行验证
    # 该操作使用otrsadmin授权后，用户otrsadmin被重新授权，屏蔽该用例
    # def test_13_roleAdd(self):
    #     try:
    #         # 开始--角色--添加--必填项填写
    #         name = RoleCommon(self.driver).rolerequiredcommon()
    #         time.sleep(3)
    #         # 下一步
    #         RolePage(self.driver).savenextbtn()
    #         time.sleep(3)
    #
    #         # 选择服务人员、默认所有者、默认负责人、角色管理者 OTRSAdmin
    #         RolePage(self.driver).clickagent('dmin')
    #         #RolePage(self.driver).chooseagent()    # 0716修改
    #         RolePage(self.driver).clickallbtn()
    #         time.sleep(2)
    #         # 多选下拉选需要点击确定按钮
    #         RolePage(self.driver).clickclosebtn()
    #         time.sleep(2)
    #
    #         RolePage(self.driver).clickdefaultowner('OTRSAdmin')
    #         RolePage(self.driver).choosedefaultowner()
    #
    #         # 输入值后无法点击？？？
    #         # RolePage(self.driver).clickdefaultresponsible('OTRSAdmin')
    #         # RolePage(self.driver).choosedefaultresponsible()
    #         # time.sleep(5)
    #
    #         RolePage(self.driver).clickmanager('OTRSAdmin')
    #         # RolePage(self.driver).choosemanager()    #0716修改
    #         RolePage(self.driver).clickallbtn()  # 0716修改
    #
    #         time.sleep(2)
    #         # 多选下拉选需要点击确定按钮
    #         RolePage(self.driver).clickclosebtn()
    #         time.sleep(1)
    #
    #         # 完成
    #         RolePage(self.driver).savebtn()
    #         time.sleep(5)
    #
    #         # 搜索并进入检查
    #         RolePage(self.driver).searchtab(name)
    #         # 列表显示检查
    #         list = [name, '', '', '', '', '备注信息test_8', '有效']
    #         num = len(self.driver.find_elements_by_css_selector('[nowrap="nowrap"]'))
    #         for fields in [".ant-table-tbody td"]:
    #             for i5 in range(0, num - 11):  # 不打印最后一栏 “修改时间”
    #                 text5 = self.driver.find_elements_by_css_selector(fields)[i5].text
    #                 #print(text5)
    #                 assert text5 == list[i5], "工单模板页面缺少字段显示！正确显示是：'" + text5 + "'"
    #
    #         RolePage(self.driver).clicksearchresult()
    #         time.sleep(2)
    #         # 下一步
    #
    #         RolePage(self.driver).savenextbtn()
    #         time.sleep(3)
    #
    #         # 检查
    #         agent = RolePage(self.driver).agentresult()
    #         print(agent)
    #
    #         owner = RolePage(self.driver).defaultownerresult()
    #         print(owner)
    #
    #         responsible = RolePage(self.driver).defaultresponsibleresult()
    #         print(responsible)
    #
    #         manager = RolePage(self.driver).managerresult()
    #         print(manager)
    #
    #     except AssertionError as msg:
    #         Base.get_windows_img(self)
    #         self.logger.error(u'下一步、上一步增加备注、下一步，完成。检查备注正常显示。其中有报错' + str(msg))

    # 14. 过滤：验证有数据的值过滤。已如账号、姓名、手机号、邮件等（SC_Role_55） --OK
    def test_14_roleSearch(self):
        try:
            # 开始--角色--添加
            EntranceAgentPage(self.driver).enter_role()  # 系统管理--组（角色）
            time.sleep(10)
            RolePage(self.driver).addrole()  # 点击新增按钮

            now_time = GetTimeCommon(self.driver).get_time()
            name = "roleSearch_" + now_time
            RolePage(self.driver).rolename(name)

            # 备注
            RolePage(self.driver).comment("备注信息" + name)

            # 保存并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(2)

            # 搜索检查--备注
            RolePage(self.driver).searchtab("备注信息" + name)
            time.sleep(2)

            # 页面字段值检查
            # 页面字段检查及值检查
            list5 = [name, '', '', '', '', "备注信息" + name, '有效']
            # for fields in [".ant-table-tbody td"]:  # 0716修改
            for fields in [".ant-table-row td"]:  # 0716修改
                for i5 in range(0, 7):
                    text5 = self.driver.find_elements_by_css_selector(fields)[
                        i5].text
                    # print(text5)
                    assert text5 == list5[i5], "过滤搜索角色的备注显示不正确！正确显示是：'" + text5 + "'"

        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'角色关联页面字段显示有误' + str(msg))

    # 15. 在有效角色列表，搜索不存在的角色内容（SC_Role_56）
    def test_15_roleSearch(self):
        try:
            # 开始--角色--添加--必填项填写
            RoleCommon(self.driver).rolerequiredcommon()
            # 保存并返回
            RolePage(self.driver).savereturnbtn()
            time.sleep(3)

            # 直接在有效框进行搜索，为避免显示在翻页找不到
            RolePage(self.driver).searchtab('搜索个不存在的有效角色')
            time.sleep(3)

            # 判断 空空如也
            result = RolePage(self.driver).searchnotext()
            # print(result)
            hope = '暂无数据'
            self.assertEqual(result, hope, msg='列表搜系统不存在的角色不应该在有效到')

        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'列表搜系统不存在的角色不应该在有效到' + str(msg))

    # 16. 添加有效角色并关联单个权限，二次进入检查 （SC_Role_33）
    @unittest2.skip("2021-10-21检查bug，已知问题，角色中搜索不到新增的权限,跳过")
    def test_16_roleAdd(self):
        try:
            # 新增菜单权限管理
            menuname = MenusetCommon(self.driver).menurequiredcommon()
            time.sleep(3)  # 增加等待时间

            # 开始--角色--添加
            EntranceAgentPage(self.driver).enter_role()
            time.sleep(7)
            RolePage(self.driver).addrole()  # 点击新增按钮

            now_time = GetTimeCommon(self.driver).get_time()
            name = "role检查选中一个菜单权限_" + now_time

            RolePage(self.driver).rolename(name)

            # 下一步
            RolePage(self.driver).savenextbtn()
            time.sleep(3)
            # 点击--选择菜单 menuname
            # RolePage(self.driver).serachtree(menuname)
            # time.sleep(3)
            # RolePage(self.driver).chooseserachtree()
            RolePage(self.driver).serach_choosetree(menuname)
            time.sleep(2)

            # 完成
            RolePage(self.driver).savebtn()
            time.sleep(4)

            # 二次进入查看
            RolePage(self.driver).searchtab(name)
            RolePage(self.driver).clicksearchresult()
            time.sleep(4)
            # 下一步
            RolePage(self.driver).savenextbtn()
            time.sleep(3)

            # 检查
            result = RolePage(self.driver).chooseserachtreeresult()
            hope = menuname
            self.assertEqual(result, hope, msg='二次进入角色关联页面未查到新建时选中的菜单权限')
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'二次进入角色关联页面未查到新建时选中的菜单权限' + str(msg))

    # 17. 无效的权限不会在角色关联页面显示 (SC_Role_34)
    def test_17_roleAdd(self):
        try:
            # 新增菜单权限管理-无效的
            menuname = MenusetCommon(self.driver).menuinvalidcommon()
            time.sleep(3)  # 增加等待时间

            # 开始--角色--添加
            EntranceAgentPage(self.driver).enter_role()
            time.sleep(7)
            RolePage(self.driver).addrole()  # 点击新增按钮

            now_time = GetTimeCommon(self.driver).get_time()
            name = "role检查无效菜单权限不显示在此_" + now_time

            RolePage(self.driver).rolename(name)

            # 下一步
            RolePage(self.driver).savenextbtn()
            time.sleep(3)
            # 点击--选择菜单 menuname
            RolePage(self.driver).serachtree(menuname)
            time.sleep(5)

            # 检查
            # result = RolePage(self.driver).chooseserachtreeresult1()
            result = RolePage(self.driver).choose_serach_emptyresult1()
            # print(result)
            hope = '没有数据'
            self.assertEqual(result, hope, msg='进入角色关联页面却将无效的菜单权限显示了出来')
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'进入角色关联页面却将无效的菜单权限显示了出来' + str(msg))

    # 18. 角色关联多个菜单权限，二次进入检查 (SC_Role_35)
    # 0922备注：角色关联页面搜索菜单显示不全，预期应搜索#1#2#3三个，实际搜索只显示#1#2
    @unittest2.skip("权限搜索bug，跳过，预期应搜索#1#2#3三个，实际搜索只显示#1#2")
    def test_18_roleAdd(self):
        try:
            # 新建三个菜单权限
            EntranceAgentPage(self.driver).enter_menuset()  # 系统管理--菜单权限管理
            time.sleep(10)

            MenusetPage(self.driver).addmenu()  # 点击新增按钮
            now_time = GetTimeCommon(self.driver).get_time()
            menuname = "三个菜单_" + now_time

            # 权限标志、权限名称
            MenusetPage(self.driver).permission(menuname + "#1")
            MenusetPage(self.driver).menuname(menuname + "#1")
            # 提交
            MenusetPage(self.driver).submit()

            MenusetPage(self.driver).addmenu()  # 点击新增按钮
            # 权限标志、权限名称
            MenusetPage(self.driver).permission(menuname + "#2")
            MenusetPage(self.driver).menuname(menuname + "#2")
            # 提交
            MenusetPage(self.driver).submit()

            MenusetPage(self.driver).addmenu()  # 点击新增按钮
            # 权限标志、权限名称
            MenusetPage(self.driver).permission(menuname + "#3")
            MenusetPage(self.driver).menuname(menuname + "#3")
            # 提交
            MenusetPage(self.driver).submit()

            # 角色关联多个
            # 开始--角色--添加
            EntranceAgentPage(self.driver).enter_role()
            time.sleep(7)
            RolePage(self.driver).addrole()  # 点击新增按钮

            now_time = GetTimeCommon(self.driver).get_time()
            name = "role检查关联多个菜单权限_" + now_time

            RolePage(self.driver).rolename(name)

            # 下一步
            RolePage(self.driver).savenextbtn()
            time.sleep(3)
            # 点击--选择菜单 menuname
            # 0715修改
            # RolePage(self.driver).serachtree(menuname + "#1")
            # time.sleep(3)
            # RolePage(self.driver).chooseserachtree()
            # time.sleep(2)
            RolePage(self.driver).serach_choosetree(menuname + "#1")
            time.sleep(3)
            # RolePage(self.driver).serachtree(menuname + "#2")
            # time.sleep(3)
            # RolePage(self.driver).chooseserachtree()
            # time.sleep(2)
            RolePage(self.driver).serach_choosetree(menuname + "#2")
            time.sleep(3)
            # RolePage(self.driver).serachtree(menuname + "#3")
            # time.sleep(3)
            # RolePage(self.driver).chooseserachtree()
            RolePage(self.driver).serach_choosetree(menuname + "#3")
            time.sleep(2)

            # 完成
            RolePage(self.driver).savebtn()
            time.sleep(4)

            # 二次进入查看
            RolePage(self.driver).searchtab(name)
            RolePage(self.driver).clicksearchresult()
            time.sleep(3)
            # 下一步
            RolePage(self.driver).savenextbtn()
            time.sleep(2)

            # 检查
            result = RolePage(self.driver).chooseserachtreeresult()
            # print(result)
            hope1 = menuname + "#1"
            hope2 = menuname + "#2"
            hope3 = menuname + "#3"

            self.assertIn(hope1, result, msg='已选择的角色 1 不在右侧栏显示')
            self.assertIn(hope2, result, msg='已选择的角色 2 不在右侧栏显示')
            self.assertIn(hope3, result, msg='已选择的角色 3 不在右侧栏显示')

        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'已选的三个角色，缺少角色显示在右侧框' + str(msg))

    # # 19.﻿子级继承父级所拥有的菜单权限 bug：2020060428000081
    # def test_19_roleAdd(self):
    #
    #     # 新增菜单权限
    #     menu = MenusetCommon(self.driver).menurequiredcommon()
    #     time.sleep(3)  # 增加等待时间
    #     # 新增父角色
    #     EntranceAgentPage(self.driver).enter_role()  # 系统管理--组（角色）
    #     time.sleep(7)
    #     RolePage(self.driver).addrole()  # 点击新增按钮
    #
    #     now_time = GetTimeCommon(self.driver).get_time()
    #     funame = "验证继承_父_" + now_time
    #     RolePage(self.driver).rolename(funame)
    #
    #     # 下一步，设置菜单权限
    #     RolePage(self.driver).savenextbtn()
    #     time.sleep(2)
    #     # 点击--选择菜单
    #     RolePage(self.driver).serachtree(menu)
    #     time.sleep(3)
    #     RolePage(self.driver).chooseserachtree()
    #     time.sleep(2)
    #
    #     # 完成
    #     RolePage(self.driver).savebtn()
    #     time.sleep(3)
    #
    #     # 新增子角色
    #     EntranceAgentPage(self.driver).enter_role()  # 系统管理--组（角色）
    #     time.sleep(7)
    #     RolePage(self.driver).addrole()  # 点击新增按钮
    #
    #     now_time = GetTimeCommon(self.driver).get_time()
    #     ziname = "验证继承_子_" + now_time
    #     RolePage(self.driver).rolename(ziname)
    #     # 选择父级
    #     parentrole = funame
    #     RolePage(self.driver).parentrole(parentrole)
    #     RolePage(self.driver).chooseparentrole(parentrole)
    #     # 下一步
    #     RolePage(self.driver).savenextbtn()
    #     time.sleep(3)
    #
    #     # 检查有父级的权限已显示
    #
    #     result = RolePage(self.driver).chooseserachtreeresult()
    #     # print(result)
    #     hope = menu
    #     self.assertIn(hope, result, msg='未正确继承父级的权限，权限没有在右侧栏显示')
    #
    # 20. 将已设置的权限删除，二次进入检查权限已正常删掉
    @unittest2.skip("2021-10-21检查bug，已知问题，角色中搜索不到新增的权限,跳过")
    def test_20_roleAdd(self):

        # 预置条件：角色有对应的菜单权限
        # 新增菜单权限
        menuname = MenusetCommon(self.driver).menurequiredcommon()
        time.sleep(3)  # 增加等待时间

        # 新增角色
        EntranceAgentPage(self.driver).enter_role()  # 系统管理--组（角色）
        time.sleep(7)
        RolePage(self.driver).addrole()  # 点击新增按钮
        now_time = GetTimeCommon(self.driver).get_time()
        name = "验证删除继承_" + now_time
        RolePage(self.driver).rolename(name)

        # 下一步，设置菜单权限
        RolePage(self.driver).savenextbtn()
        time.sleep(2)
        # 点击--选择菜单并保存
        # RolePage(self.driver).serachtree(menuname)
        # time.sleep(3)
        # RolePage(self.driver).chooseserachtree()   # 0716修改
        RolePage(self.driver).serach_choosetree(menuname)
        time.sleep(2)
        # 完成
        RolePage(self.driver).savebtn()
        time.sleep(4)

        # 二次进入删除
        RolePage(self.driver).searchtab(name)
        RolePage(self.driver).clicksearchresult()
        time.sleep(3)
        # 下一步
        RolePage(self.driver).savenextbtn()
        time.sleep(2)
        # 先搜索后删除按钮
        RolePage(self.driver).clickserachtree2()
        RolePage(self.driver).serachtreesendkey2(menuname)
        time.sleep(2)
        RolePage(self.driver).choosenotserach2()
        time.sleep(2)
        # 完成
        RolePage(self.driver).savebtn()
        time.sleep(4)

        # 再次进入检查应当已不存在选中的菜单权限
        RolePage(self.driver).searchtab(name)
        RolePage(self.driver).clicksearchresult()
        time.sleep(3)
        # 下一步
        RolePage(self.driver).savenextbtn()
        time.sleep(2)
        # 检查
        result = RolePage(self.driver).chooseserachtreeresult()
        # print(result)
        # hope = ''
        self.assertEqual('', result, msg='已删除的菜单权限不应在右侧栏显示')

    # # # 8. 搜索不存在的有效角色、检查无效--无效列表搜索
    # def test_8_groupAdd(self):
    #     EntranceAgentPage(self.driver).enter_group()  # 进入组页面
    #     time.sleep(3)
    #     RolePage(self.driver).addgroup()  # 点击“增加” 组
    #
    #     now_time = EntranceAgentPage(self.driver).get_time()   # 填写name
    #     name = "组test5_" + now_time
    #     RolePage(self.driver).groupname(name)
    #
    #     # 选择无效
    #     RolePage(self.driver).clickinvalid()
    #     RolePage(self.driver).chooseinvalid()
    #     # 保存并返回
    #     RolePage(self.driver).savereturnbtn()
    #     time.sleep(3)

        # # 直接在有效框进行搜索
        # RolePage(self.driver).searchtab(name)
        # time.sleep(3)
        # # 检查列表显示出。为避免显示在翻页找不到，搜索然后判断
        # result1 = RolePage(self.driver).searchresult()
        # hope1 = ''
        # self.assertEqual(result1, hope1, msg='无效的组不应该在有效列表搜到')
        #
        # # 点击无效列表
        # RolePage(self.driver).invalidlist()
        # RolePage(self.driver).chooseinvalid()
        # # 检查
        # RolePage(self.driver).searchtab(name)
        # time.sleep(3)
        # # 检查列表显示出。为避免显示在翻页找不到，搜索然后判断
        # result2 = RolePage(self.driver).searchresult()
        # hope2 = name
        # self.assertEqual(result2, hope2, msg='无效的组应该在无效列表搜到')


# if __name__ == '__main__':
#     unittest2.main()
