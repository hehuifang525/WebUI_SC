"""
@author: DT_testing
@file:   generic_case.py
@desc:  【自动任务1】
@step： 001.填写必填，点击提交按钮 SC_generic_017
        002.删除单条自动任务、删除确认、删除取消  SC_generic_045 SC_generic_044 SC_generic_046
        003.名称同名校验、名称空格校验、返回列表按钮校验 、查询不存在数据、精确查询存在数据
         SC_generic_015 SC_generic_019 SC_generic_020 SC_generic_005 、SC_generic_003
        004. 不填写必填时提交不可触发、再添加一条  SC_generic_016 SC_generic_024
        005. 有效无效tab切换 SC_generic_002
        006. 工单搜索添加添加多个，删除搜索条件；  SC_generic_060  SC_generic_061
        007. 更新字段添加多个，删除搜索条件  SC_generic_063  SC_generic_064
        008. 复制自动任务（不修改值提交、修改值提交） SC_generic_039  SC_generic_040 SC_generic_041
        009. 表头字段检查，复制按钮、删除按钮、导出、允许按钮显示检查；添加页面显示检查
            SC_generic_007 SC_generic_009  SC_generic_014
        010. 全填创建一条记录；编辑所有字段；删除必填字段 SC_generic_018 SC_generic_022  SC_generic_023 SC_generic_065
        011. 填写全部/必填字段点击再添加一条；编辑记录点击再添加一条；删除非必填点击再添加一条
           SC_generic_024 SC_generic_025  SC_generic_026 SC_generic_027  wait
        012. 基于时间执行，添加单个/多个/删除计划的天/小时/分钟  SC_generic_054、SC_generic_055 SC_generic_056
        013. 基于事件执行，选择单个触发事件，多个触发时间，删除触发时间SC_generic_057
        014. 执行定制模块：模块名称填写，参数添加/删除
             SC_generic_069 SC_generic_070  SC_generic_071 SC_generic_072



"""
import time

from src.page.pagecommon.get_time_common import GetTimeCommon
from src.page.pagecommon.service_commom import ServiceCommon
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.agent.generic_page import GenericPage
from src.page.pagecommon.generic_common import GenericCommon

import random


class Generic(BaseCaseUser, Base):

    def test_001(self):
        '''填写必填，点击提交'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")
        GenericPage(self.driver).sumbit()
        # 搜索
        GenericPage(self.driver).search(name)
        # 点击结果
        GenericPage(self.driver).search_result()
        # 取名称值对比，断言
        get_name = GenericPage(self.driver).get_name()
        self.assertEqual(get_name, name, msg='填写必填提交自动任务失败')

    def test_002(self):
        '''删除单条自动任务'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")
        GenericPage(self.driver).sumbit()
        time.sleep(3)
        # 搜索
        GenericPage(self.driver).search(name)
        # 点击删除
        GenericPage(self.driver).delete()
        # 必须的强制等待
        time.sleep(2)
        GenericPage(self.driver).delete_cancel()

        GenericPage(self.driver).delete()
        # 必须的强制等待
        time.sleep(2)
        GenericPage(self.driver).delete_confirm()
        time.sleep(2)
        GenericPage(self.driver).search(name)
        get_empty = GenericPage(self.driver).get_empty()
        self.assertEqual(get_empty, "暂无数据", msg='删除单个自动任务失败')

    def test_003(self):
        '''名称校验'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")
        GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 添加第二个
        GenericPage(self.driver).add()
        GenericPage(self.driver).inputname('   ')
        name_error_message = GenericPage(self.driver).name_error_message()
        self.assertEqual(name_error_message, '数据格式错误,请重新输入!', msg='名称空格校验失败')

        GenericPage(self.driver).inputname(name)
        name_error_message = GenericPage(self.driver).name_error_message()
        self.assertEqual(name_error_message, '该名称已存在，请更换其他名称！', msg='名称重名校验失败')

        # 点击返回按钮
        GenericPage(self.driver).backlist()
        GenericPage(self.driver).search(name)
        # 点击结果
        GenericPage(self.driver).search_result()
        # 取名称值对比，断言
        get_name = GenericPage(self.driver).get_name()
        self.assertEqual(get_name, name, msg='返回列表失败')

    def test_004(self):
        '''再来一条'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")
        # GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 添加第二个
        GenericPage(self.driver).addmore()
        time.sleep(3)
        sumbit_disabled = GenericPage(self.driver).sumbit_disabled()
        addmore_disabled = GenericPage(self.driver).addmore_disabled()

        self.assertEqual(sumbit_disabled, "true", msg='必填未填写，提交按钮可点击')
        self.assertEqual(addmore_disabled, "true", msg='必填未填写，再添加一条按钮可点击')

    def test_005(self):
        '''添加无效数据'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('generic' + strnumber)
        GenericPage(self.driver).add()
        GenericPage(self.driver).inputname(name)
        GenericPage(self.driver).invalid()
        GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 切换无效tab
        GenericPage(self.driver).invalid_tab()
        GenericPage(self.driver).search(name)
        # 点击结果
        GenericPage(self.driver).search_result()
        # 取名称值对比，断言
        get_name = GenericPage(self.driver).get_name()
        self.assertEqual(get_name, name, msg='添加无效数据，切换无效tab失败')
        GenericPage(self.driver).backlist()

        # 切换回有效tab
        GenericPage(self.driver).valid_tab()
        GenericPage(self.driver).search(name)
        get_empty = GenericPage(self.driver).get_empty()
        self.assertEqual(get_empty, "暂无数据", msg='切换有效tab失败')

    def test_006(self):
        '''添加删除搜索条件'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")

        # 选择搜索条件主题、角色、优先级  chose_tickect_fidld
        GenericPage(self.driver).chose_tickect_fidld("主题")
        GenericPage(self.driver).chose_tickect_priority("优先级")
        GenericPage(self.driver).chose_tickect_fidld("角色")

        # 分别往选择的条件中输入值
        GenericPage(self.driver).input_condition_subject("这是搜索条件的主题")
        GenericPage(self.driver).chose_queue("系统默认角色")
        GenericPage(self.driver).chose_priority("高")

        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(8)

        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()
        time.sleep(3)

        # 对显示的字段进行断言检查
        condition_subject = GenericPage(self.driver).get_condition_subject()
        condition_priority = GenericPage(self.driver).get_condition_priority()
        condition_queue = GenericPage(self.driver).get_condition_queue()
        self.assertEqual(condition_subject, '这是搜索条件的主题',msg='二次进入，添加的主题条件值显示错误')
        self.assertEqual(condition_priority, '高\n非常高', msg='二次进入，添加的优先级条件值显示错误')
        self.assertEqual(condition_queue, '系统默认角色', msg='二次进入，添加的角色条件值显示错误')

        # 删除角色、优先级  delete_condition_queue
        GenericPage(self.driver).delete_condition_queue()
        GenericPage(self.driver).delete_condition_priority()
        # 提交
        GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        # 对显示的字段进行断言检查  如何判断已经删除成功了搜索条件？
        # 搜索一次角色，取一次控制判断即可
        GenericPage(self.driver).chose_tickect_priority("优先级")
        GenericPage(self.driver).chose_priority("非常高")

        condition_subject = GenericPage(self.driver).get_condition_subject()
        condition_priority = GenericPage(self.driver).get_condition_priority()

        self.assertEqual(condition_subject, '这是搜索条件的主题', msg='二次进入，添加的主题条件值显示错误')
        self.assertEqual(condition_priority, '非常高', msg='二次进入，添加的优先级条件值显示错误')

    def test_007(self):
        '''添加删除更新字段'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")

        # 选择搜索条件主题、角色、优先级  chose_tickect_fidld
        GenericPage(self.driver).chose_update_fidld("指定标题")
        GenericPage(self.driver).chose_update_fidld("设置新的角色")
        GenericPage(self.driver).chose_update_fidld("设置新的优先级")

        # 分别往选择的条件中输入值
        GenericPage(self.driver).update_title("这是更新的标题")
        GenericPage(self.driver).update_queue("系统默认角色")
        GenericPage(self.driver).update_priority("非常高")

        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()
        # 必须等待，否则取不到值
        time.sleep(10)

        # 对显示的字段进行断言检查
        new_subject = GenericPage(self.driver).get_new_subject()
        new_priority = GenericPage(self.driver).get_new_priority()
        new_queue = GenericPage(self.driver).get_new_queue()
        self.assertEqual(new_subject, '这是更新的标题', msg='二次进入，更新标题值显示错误')
        self.assertEqual(new_priority, '非常高', msg='二次进入，添设置新优先级值显示错误')
        self.assertEqual(new_queue, '系统默认角色', msg='二次进入，设置新角色值显示错误')

        # 删除角色、优先级
        GenericPage(self.driver).delete_new_priority()
        GenericPage(self.driver).delete_new_queue()
        # 提交
        GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        # 对显示的字段进行断言检查  如何判断已经删除成功了搜索条件？
        # 搜索一次角色，取一次控制判断即可
        GenericPage(self.driver).chose_update_fidld("设置新的优先级")
        GenericPage(self.driver).update_priority("高")

        condition_subject = GenericPage(self.driver).get_new_subject()
        condition_priority = GenericPage(self.driver).get_new_priority()

        self.assertEqual(condition_subject, '这是更新的标题', msg='二次进入，主题条件值显示错误')
        self.assertEqual(condition_priority, '高', msg='二次进入，删除后再次添加更细字段值显示错误')

    def test_008(self):
        '''复制'''

        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")

        # 选择搜索条件主题、角色、优先级
        GenericPage(self.driver).chose_tickect_fidld("主题")
        GenericPage(self.driver).chose_tickect_priority("优先级")

        # 分别往选择的条件中输入值
        GenericPage(self.driver).input_condition_subject("这是搜索条件的主题")
        GenericPage(self.driver).chose_priority("高")

        # 选择搜索条件主题、角色、优先级
        GenericPage(self.driver).chose_update_fidld("指定标题")
        GenericPage(self.driver).chose_update_fidld("设置新的优先级")

        # 分别往选择的条件中输入值
        GenericPage(self.driver).update_title("这是更新的标题")
        GenericPage(self.driver).update_priority("非常高")
        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 搜索复制
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).copy()
        time.sleep(3)
        copy_name = GenericPage(self.driver).get_name()
        new_name = name + " - 复制"
        self.assertEqual(copy_name, new_name, msg='复制后名称显示错误')
        GenericPage(self.driver).sumbit()
        time.sleep(5)

        # 不修改值提交，二次进入，断言
        GenericPage(self.driver).search(new_name)
        GenericPage(self.driver).search_result()
        # 必须等待，否则取不到值
        time.sleep(5)
        condition_subject = GenericPage(self.driver).get_condition_subject()
        condition_priority = GenericPage(self.driver).get_condition_priority()
        new_subject = GenericPage(self.driver).get_new_subject()
        new_priority = GenericPage(self.driver).get_new_priority()

        self.assertEqual(condition_subject, '这是搜索条件的主题', msg='复制不修改值，添加的主题条件值显示错误')
        self.assertEqual(condition_priority, '高\n非常高', msg='复制不修改值，添加的优先级条件值显示错误')
        self.assertEqual(new_subject, '这是更新的标题', msg='复制不修改值，更新标题值显示错误')
        self.assertEqual(new_priority, '非常高', msg='复制不修改值，添设置新优先级值显示错误')

        # 返回列表
        GenericPage(self.driver).backlist()
        GenericPage(self.driver).search(new_name)
        GenericPage(self.driver).copy()

        # 复制修改对应字段值 此处需要修改
        name002 = name+'二次复制'
        GenericPage(self.driver).inputname(name002)
        GenericPage(self.driver).input_condition_subject("这是搜索条件的主题修改")
        GenericPage(self.driver).chose_priority("低")

        GenericPage(self.driver).update_title("这是复制修改的标题")
        GenericPage(self.driver).update_priority("非常低")
        GenericPage(self.driver).sumbit()
        time.sleep(8)

        GenericPage(self.driver).search(name002)
        GenericPage(self.driver).search_result()
        time.sleep(2)
        condition_subject = GenericPage(self.driver).get_condition_subject()
        condition_priority = GenericPage(self.driver).get_condition_priority()
        new_subject = GenericPage(self.driver).get_new_subject()
        new_priority = GenericPage(self.driver).get_new_priority()

        self.assertEqual(condition_subject, '这是搜索条件的主题修改', msg='复制修改值，添加的主题条件值显示错误')
        self.assertEqual(condition_priority, '非常低\n低\n高\n+ 1 ...', msg='复制修改值，添加的优先级条件值显示错误')
        self.assertEqual(new_subject, '这是复制修改的标题', msg='复制修改值，更新标题值显示错误')
        self.assertEqual(new_priority, '非常低', msg='复制修改值，添设置新优先级值显示错误')

    def test_009(self):
        '''表头字段，操作按钮检查'''
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")

        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(3)

        # 搜索复制
        GenericPage(self.driver).search(name)

        # 断言1：检查表头字段
        table_head = GenericPage(self.driver).get_table_head()
        table_head01 = ['','名称', '最后运行', '上次执行人', '备注', '有效性', '创建时间', '修改人','修改时间','操作']
        for i in range(1, len(table_head)):
            self.assertEqual(table_head[i].text,table_head01[i] ,msg='错误：表头字段显示错误')

        # 断言2: 检查操作按钮

        GenericPage(self.driver).checkcopy()
        GenericPage(self.driver).checkdelete()
        GenericPage(self.driver).checkexport()
        GenericPage(self.driver).checkrun()
        # 断言3：检查添加页面的显示
        GenericPage(self.driver).add()
        time.sleep(4)
        tab = GenericPage(self.driver).get_add_tab()
        tab01 = ['任务设置', '选择工单', '更新/添加工单属性', '添加备注', '执行工单指令', '执行定制模块']

        for i in range(0, len(tab)):
            self.assertEqual(tab[i].text,tab01[i] ,msg='错误：添加页面的tab模块错误')

    # 全填创建一条记录；编辑所有字段；删除必填字段 SC_generic_018 SC_generic_022  SC_generic_023
    def test_010(self):
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        # 全填添加一个任务
        genericinfo = GenericCommon(self.driver).generic_full_common()
        name = genericinfo.get("name")
        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(5)

        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        # 编辑修改任务，二次进入断言
        GenericPage(self.driver).inputname(name + "edit")
        GenericPage(self.driver).chose_priority("正常")

        GenericPage(self.driver).update_priority("非常低")
        time.sleep(3)
        Base(self.driver).move_to_pagebottom()
        GenericPage(self.driver).new_note_from('发件人testedit')
        GenericPage(self.driver).new_note_subject('主题testedit')
        GenericPage(self.driver).send_content('内容testedit')
        GenericPage(self.driver).new_cmd('命令testedit')
        GenericPage(self.driver).new_module('模块testedit')
        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(name + "edit")
        GenericPage(self.driver).search_result()

        # 取值断言  get_name
        newname = GenericPage(self.driver).get_name()
        condition_priority = GenericPage(self.driver).get_condition_priority()
        new_priority = GenericPage(self.driver).get_new_priority()
        Base(self.driver).move_to_pagebottom()
        get_new_note_from = GenericPage(self.driver).get_new_note_from()
        get_new_subject = GenericPage(self.driver).get_new_note_subject()
        get_content = GenericPage(self.driver).get_content()
        get_new_cmd = GenericPage(self.driver).get_new_cmd()
        get_new_module = GenericPage(self.driver).get_new_module()

        self.assertEqual(newname, name + "edit", msg="错误：编辑名称二次打开名称显示错误")
        self.assertEqual(condition_priority, "正常\n高\n非常高", msg="错误：编辑选择工单条件")
        self.assertEqual(new_priority, '非常低', msg="错误：更新工单属性编辑二次进入显示错误")
        list01 = [get_new_note_from,get_new_subject, get_content, get_new_cmd,  get_new_module]
        list02 = ['发件人testedit', '主题testedit', '内容testedit', '命令testedit', '模块testedit']
        self.assertEqual(list01, list02, msg="错误：编辑非必填字段二次打开显示错误")

        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(5)

        # 搜索进入
        GenericPage(self.driver).search(name + "edit")
        GenericPage(self.driver).search_result()

        # 删除选择工单的条件和搜索工单的条件
        GenericPage(self.driver).delete_condition_priority()
        GenericPage(self.driver).delete_new_priority()

        # 清除其他非必填
        Base(self.driver).move_to_pagebottom()
        time.sleep(1)
        GenericPage(self.driver).clear_new_note_from()
        GenericPage(self.driver).clear_new_note_subject()
        GenericPage(self.driver).clear_content()
        GenericPage(self.driver).clear_new_cmd()
        GenericPage(self.driver).clear_new_module()
        # 提交，二次进入断言
        # 点击提交
        GenericPage(self.driver).sumbit()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(name + "edit")
        GenericPage(self.driver).search_result()

        GenericPage(self.driver).chose_tickect_priority("优先级")
        GenericPage(self.driver).chose_priority("高")

        GenericPage(self.driver).chose_update_fidld("设置新的优先级")
        GenericPage(self.driver).update_priority("非常高")
        Base(self.driver).move_to_pagebottom()

        get_new_note_from = GenericPage(self.driver).get_new_note_from()
        get_new_subject = GenericPage(self.driver).get_new_note_subject()
        get_content = GenericPage(self.driver).get_content()
        get_new_cmd = GenericPage(self.driver).get_new_cmd()
        get_new_module = GenericPage(self.driver).get_new_module()

        list03 = [get_new_note_from, get_new_subject, get_content, get_new_cmd, get_new_module]
        list04 = ['', '', '', '', '']
        self.assertEqual(list03, list04, msg="错误：删除非必填字段二次打开显示错误")

    # 011. 填写必填/全部字段点击再添加一条；编辑记录点击再添加一条；删除非必填点击再添加一条
    def test_011(self):
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        # 全填添加一条
        genericinfo = GenericCommon(self.driver).generic_full_common()
        fullname = genericinfo.get("name")
        # 点击继续添加一条
        GenericPage(self.driver).addmore()
        time.sleep(5)
        GenericPage(self.driver).backlist()
        time.sleep(5)

        # 必填增加一条
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        required_name = str('generic' + strnumber)
        GenericPage(self.driver).add()
        GenericPage(self.driver).inputname(required_name)
        # 点击继续添加一条
        GenericPage(self.driver).addmore()
        time.sleep(5)
        GenericPage(self.driver).backlist()
        time.sleep(5)

        # 搜索进入一个全部任务，编辑所有字段
        GenericPage(self.driver).search(fullname)
        GenericPage(self.driver).search_result()
        GenericPage(self.driver).inputname(fullname + "edit")
        GenericPage(self.driver).chose_priority("正常")

        GenericPage(self.driver).update_priority("非常低")
        Base(self.driver).move_to_pagebottom()
        GenericPage(self.driver).new_note_from('发件人testedit')
        GenericPage(self.driver).new_note_subject('主题testedit')
        GenericPage(self.driver).send_content('内容testedit')
        GenericPage(self.driver).new_cmd('命令testedit')
        GenericPage(self.driver).new_module('模块testedit')
        # 点击继续添加一条
        GenericPage(self.driver).addmore()
        time.sleep(5)
        GenericPage(self.driver).backlist()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(fullname + "edit")
        GenericPage(self.driver).search_result()

        # 取值断言  get_name
        newname = GenericPage(self.driver).get_name()
        condition_priority = GenericPage(self.driver).get_condition_priority()
        new_priority = GenericPage(self.driver).get_new_priority()
        Base(self.driver).move_to_pagebottom()
        get_new_note_from = GenericPage(self.driver).get_new_note_from()
        get_new_subject = GenericPage(self.driver).get_new_note_subject()
        get_content = GenericPage(self.driver).get_content()
        get_new_cmd = GenericPage(self.driver).get_new_cmd()
        get_new_module = GenericPage(self.driver).get_new_module()

        self.assertEqual(newname, fullname + "edit", msg="错误：编辑名称二次打开名称显示错误")
        self.assertEqual(condition_priority, "正常\n高\n非常高", msg="错误：编辑选择工单条件")
        self.assertEqual(new_priority, '非常低', msg="错误：更新工单属性编辑二次进入显示错误")
        list01 = [get_new_note_from, get_new_subject, get_content, get_new_cmd, get_new_module]
        list02 = ['发件人testedit', '主题testedit', '内容testedit', '命令testedit', '模块testedit']
        self.assertEqual(list01, list02, msg="错误：编辑非必填字段二次打开显示错误")

        # 进入全填任务，删除非必填
        Base(self.driver).move_to_pagetop()
        GenericPage(self.driver).delete_condition_priority()
        GenericPage(self.driver).delete_new_priority()

        # 清除其他非必填
        Base(self.driver).move_to_pagebottom()
        time.sleep(1)
        GenericPage(self.driver).clear_new_note_from()
        GenericPage(self.driver).clear_new_note_subject()
        GenericPage(self.driver).clear_content()
        GenericPage(self.driver).clear_new_cmd()
        GenericPage(self.driver).clear_new_module()
        # 提交，二次进入断言
        # 点击提交
        GenericPage(self.driver).addmore()
        time.sleep(5)
        GenericPage(self.driver).backlist()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(fullname + "edit")
        GenericPage(self.driver).search_result()

        GenericPage(self.driver).chose_tickect_priority("优先级")
        GenericPage(self.driver).chose_priority("高")

        GenericPage(self.driver).chose_update_fidld("设置新的优先级")
        GenericPage(self.driver).update_priority("非常高")
        Base(self.driver).move_to_pagebottom()

        get_new_note_from = GenericPage(self.driver).get_new_note_from()
        get_new_subject = GenericPage(self.driver).get_new_note_subject()
        get_content = GenericPage(self.driver).get_content()
        get_new_cmd = GenericPage(self.driver).get_new_cmd()
        get_new_module = GenericPage(self.driver).get_new_module()

        list03 = [get_new_note_from, get_new_subject, get_content, get_new_cmd, get_new_module]
        list04 = ['', '', '', '', '']
        self.assertEqual(list03, list04, msg="错误：删除非必填字段二次打开显示错误")

    def test_012(self):
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        # 全填添加一条
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")
        GenericPage(self.driver).generic_schedule(0)
        GenericPage(self.driver).generic_schedule_option(0)

        GenericPage(self.driver).generic_schedule(1)
        GenericPage(self.driver).generic_schedule_option(0)

        GenericPage(self.driver).generic_schedule(2)
        GenericPage(self.driver).generic_schedule_option(0)
        GenericPage(self.driver).sumbit()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        plan_day = GenericPage(self.driver).get_generic_schedule(0)
        plan_h = GenericPage(self.driver).get_generic_schedule(1)
        plan_min = GenericPage(self.driver).get_generic_schedule(2)

        self.assertEqual(plan_day, '周五', msg='设置单个计划的天失败')
        self.assertEqual(plan_h, '00', msg='设置单个计划的小时失败')
        self.assertEqual(plan_min, '00', msg='设置单个计划的分钟失败')

        # 编辑计划的天小时分钟
        GenericPage(self.driver).generic_schedule(0)
        GenericPage(self.driver).generic_schedule_option(1)

        GenericPage(self.driver).generic_schedule(1)
        GenericPage(self.driver).generic_schedule_option(1)

        GenericPage(self.driver).generic_schedule(2)
        GenericPage(self.driver).generic_schedule_option(1)
        GenericPage(self.driver).sumbit()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        plan_day = GenericPage(self.driver).get_generic_schedule(0)
        plan_h = GenericPage(self.driver).get_generic_schedule(1)
        plan_min = GenericPage(self.driver).get_generic_schedule(2)

        self.assertEqual(plan_day, '周五\n+ 1 ...', msg='设置多个计划的天失败')
        self.assertEqual(plan_h, '00\n+ 1 ...', msg='设置单多计划的小时失败')
        self.assertEqual(plan_min, '00\n+ 1 ...', msg='设置多个计划的分钟失败')

        # 删除选择的计划的天小时分钟
        GenericPage(self.driver).delete_generic_schedule(0,0)
        GenericPage(self.driver).delete_generic_schedule(1,0)
        GenericPage(self.driver).delete_generic_schedule(2,0)
        GenericPage(self.driver).sumbit()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        plan_day = GenericPage(self.driver).get_generic_schedule(0)
        plan_h = GenericPage(self.driver).get_generic_schedule(1)
        plan_min = GenericPage(self.driver).get_generic_schedule(2)

        self.assertEqual(plan_day, '', msg='删除设置计划的天失败')
        self.assertEqual(plan_h, '', msg='删除设置计划的小时失败')
        self.assertEqual(plan_min, '', msg='删除设置计划的分钟失败')

    def test_013(self):
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        # 全填添加一条
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")
        # 选择触发事件
        GenericPage(self.driver).event_execution()
        GenericPage(self.driver).event_values("stateupdate")
        GenericPage(self.driver).sumbit()
        time.sleep(15)
        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        # 取事件断言  get_event_values
        event_values = GenericPage(self.driver).get_event_values()
        self.assertEqual(event_values, 'TicketStateUpdate', msg='单个事件设置错误')

        # 选择多个事件
        GenericPage(self.driver).event_execution()
        GenericPage(self.driver).event_values("PriorityUpdateup")

        # 提交
        GenericPage(self.driver).sumbit()
        time.sleep(10)
        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()

        # 二次进入断言
        event_values02 = GenericPage(self.driver).get_event_values()
        self.assertEqual(event_values02, 'TicketPriorityUpdateUp\nTicketStateUpdate', msg='多个事件设置错误')

        # 删除事件，提交  delete_event_values
        GenericPage(self.driver).delete_event_values()
        # 提交
        GenericPage(self.driver).sumbit()
        time.sleep(10)
        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()
        # 三次断言
        event_values02 = GenericPage(self.driver).get_event_values()
        self.assertEqual(event_values02, '', msg='删除事件失败')

    def test_014(self):
        EntranceAgentPage(self.driver).enter_generic()
        time.sleep(3)

        # 全填添加一条
        genericinfo = GenericCommon(self.driver).generic_required_common()
        name = genericinfo.get("name")
        Base(self.driver).move_to_pagebottom()
        GenericPage(self.driver).new_module('模块test')
        # 指定定制模板点击添加值
        GenericPage(self.driver).add_value()
        GenericPage(self.driver).add_value()
        Base(self.driver).move_to_pagebottom()
        GenericPage(self.driver).add_value()

        GenericPage(self.driver).send_parameter_key(0, 'key01')
        GenericPage(self.driver).send_parameter_key(1, 'key02')
        GenericPage(self.driver).send_parameter_key(2, 'key03')

        GenericPage(self.driver).send_parameter_value(0, 'value01')
        GenericPage(self.driver).send_parameter_value(1, 'value02')
        GenericPage(self.driver).send_parameter_value(2, 'value03')

        # 提交
        GenericPage(self.driver).sumbit()
        time.sleep(5)
        # 搜索进入
        GenericPage(self.driver).search(name)
        GenericPage(self.driver).search_result()
        Base(self.driver).move_to_pagebottom()

        # 取参数的键值断言
        count_parameter = GenericPage(self.driver).count_parameter()
        self.assertEqual(count_parameter, '选项数 : 3', msg='执行定制模块添加参数失败')
        get_parameter_key01 = GenericPage(self.driver).get_parameter_key(0)
        get_parameter_key02 = GenericPage(self.driver).get_parameter_key(1)
        get_parameter_key03 = GenericPage(self.driver).get_parameter_key(2)
        parameter_key_list = ['key01', 'key02', 'key03']
        parameter_key_list02 = [get_parameter_key01, get_parameter_key02, get_parameter_key03]
        self.assertEqual(parameter_key_list,parameter_key_list02, msg='参数键名显示错误')

        get_parameter_value01 = GenericPage(self.driver).get_parameter_value(0)
        get_parameter_value02 = GenericPage(self.driver).get_parameter_value(1)
        get_parameter_value03 = GenericPage(self.driver).get_parameter_value(2)
        parameter_key_list = ['value01', 'value02', 'value03']
        parameter_value_list01 = [get_parameter_value01, get_parameter_value02, get_parameter_value03]
        self.assertEqual(parameter_key_list, parameter_value_list01, msg='参数值名显示错误')

        # bug 删除参数失败 2021052710000089
        # # 删除参数
        # GenericPage(self.driver).delete_parameter(0)
        # GenericPage(self.driver).delete_parameter(0)
        #
        # # 提交
        # GenericPage(self.driver).sumbit()
        # time.sleep(5)
        # # 搜索进入
        # GenericPage(self.driver).search(name)
        # GenericPage(self.driver).search_result()
        # Base(self.driver).move_to_pagebottom()
        # # 取参数的键值断言
        # count_parameter = GenericPage(self.driver).count_parameter()
        # self.assertEqual(count_parameter, '选项数 : 1', msg='执行定制模块删除参数失败')
























