"""
@author: DT_testing
@file:   menuset_case.py
@desc:  【】
@step：  1. 检查角色面包屑（路径）、进入角色列表检查默认列表头、url title (SC_Menu_1、SC_Menu_12)
         2. 检查添加页面的“返回”按钮（SC_Menu_13）
         3. 只填写必填项新增服务人员菜单菜单检查  SC_Menu_14
         4. 检查必填项  SC_Menu_32  SC_Menu_33
         5. 名称唯一性检验，权限标记唯一性检验    SC_Menu_17 SC_Menu_20 SC_Menu_21
         6. 填写必填添加客户用户菜单（不选单位、不选权限）   SC_Menu_15
         7. 过滤不存在的菜单、切换tab、过滤存在的菜单，有效性修改
            SC_Menu_40  SC_Menu_41 SC_Menu_55 SC_Menu_56 SC_Menu_57 SC_Menu_58 SC_Menu_59 SC_Menu_60

         名称输入类型检验，权限标记 输入类型校验  未开始 SC_Menu_18  SC_Menu_22 未开始
         4编辑服务人员必填项  SC_Menu_28  未开始

"""
import time

from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.menuset_page import MenusetPage
from src.page.pagecommon.menusetting_common import MenusetCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base

class Menu(BaseCaseUser, Base):

    # 1. 检查角色面包屑（路径）、进入角色列表检查默认列表头、url title（SC_Menu_1、SC_Menu_12）
    def test_001_menulist(self):
        try:
            # 开始--菜单权限管理
            EntranceAgentPage(self.driver).enter_menuset()
            time.sleep(5)

            # 检查列表头默认值
            list = ['名称', '类型', '父权限', '备注', '有效', '修改时间', '修改人']
            for fields in [".ant-table-thead th"]:
                for i in range(0, 7):
                    text = self.driver.find_elements_by_css_selector(fields)[i].text
                    # print(text ,i )
                    assert text == list[i], "菜单权限列表头默认显示不正确！正确显示是：" + text + "'"

            # 检查 url title
            result = Base(self.driver).get_title()
            if result != '菜单权限管理':
                print('菜单权限管理列表当前窗口 title 显示不正确')

            # 检查路径
            road = MenusetPage(self.driver).road()
            self.assertEqual(road, '/ 系统管理 / 菜单权限管理', msg='菜单权限管理列表路径显示不正确')
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'菜单权限管理列表页面显示的路径显示不正确/菜单权限管理页面字段显示不正确' + str(msg))

    # 2. 检查添加页面的“返回”按钮（SC_Menu_13）
    def test_002_menuAdd(self):
        try:
            # 开始--菜单权限管理
            EntranceAgentPage(self.driver).enter_menuset()
            # 点击“添加”
            MenusetPage(self.driver).addmenu()

            # 点击“返回”
            MenusetPage(self.driver).returnlist()
            time.sleep(3)

            # # 检查搜索默认自带 “一线权限” 存在，保证正确返回列表
            # MenusetPage(self.driver).searchtab("一线权限")
            # result = MenusetPage(self.driver).searchresult()
            # time.sleep(1)
            # self.assertEqual(result, '一线权限', msg='添加菜单权限不填写直接返回，返回页面不正确')
            # 0810 修改返回列表成功判断 ,判断页面中存在“添加”按钮
            result = MenusetPage(self.driver).getaddmenu()
            self.assertEqual(result, '添加', msg='添加菜单权限不填写直接返回，返回页面不正确')


        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'添加菜单权限不填写直接返回，返回页面不正确' + str(msg))

    # 3. 只填写必填项新增菜单检查
    def test_003_menuAdd(self):
        try:
            # 开始--菜单权限--添加--必填项填写
            name = MenusetCommon(self.driver).menurequiredcommon()
            # 保存并返回提交
            # MenusetPage(self.driver).submit()
            time.sleep(3)

            # 搜索检查。 检查列表显示出。为避免显示在翻页找不到，搜索然后判断
            MenusetPage(self.driver).searchtab(name)
            time.sleep(3)

            result = MenusetPage(self.driver).searchresult()
            hope = name
            self.assertEqual(result, hope, msg='未搜索出新增的角色，新增的必填角色没有在列表显示')
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error(u'未搜索出新增的角色，新增的必填角色没有在列表显示' + str(msg))
     # SC_Menu_14

    # 4.必填项为空 必填项输入空检查
    @Base.screenshot_about_case
    def test_004(self):
        EntranceAgentPage(self.driver).enter_menuset()  # 系统管理--菜单权限管理
        time.sleep(8)
        MenusetPage(self.driver).addmenu()  # 点击新增按钮

        submitcolor = MenusetPage(self.driver).getsubmitcolor()
        self.assertEqual(submitcolor,'true',
                         msg='错误：权限标记和名称不填写提交按钮可触发')

        MenusetPage(self.driver).permission('    ')
        MenusetPage(self.driver).menuname('    ')
        time.sleep(2)
        permissiontip = MenusetPage(self.driver).getpermissiontip()
        menunametip = MenusetPage(self.driver).getmenunametip()
        self.assertEqual(permissiontip, '数据格式错误,请重新输入!', msg='错误：权限标记空格输入检验通过')
        self.assertEqual(menunametip, '数据格式错误,请重新输入!', msg='错误：名称空格输入检验通过')
        time.sleep(3)

        # 输入权限标记,名称 删除有效无效
        MenusetPage(self.driver).permission('0918789')
        MenusetPage(self.driver).menuname('陌上花开一世芳华')
        MenusetPage(self.driver).dele_type()
        MenusetPage(self.driver).dele_valid()
        submitcolor2 = MenusetPage(self.driver).getsubmitcolor()
        self.assertEqual(submitcolor2, 'true',
                         msg='错误：类型和有效性不填写提交按钮可触发')
        time.sleep(2)

        # 选择类型，有效无效，检查提交
        MenusetPage(self.driver).chosetypeagent()
        MenusetPage(self.driver).clickchoosevalid()
        submitcolor3 = MenusetPage(self.driver).getsubmitcolor()
        self.assertEqual(submitcolor3, None,
                         msg='错误：必填项都填写了提交按钮不可触发')

    # 5.权限标记，名称唯一性检验
    @Base.screenshot_about_case
    def test_005(self):
        name = MenusetCommon(self.driver).menurequiredcommon()
        # 保存并返回提交
        time.sleep(3)
        MenusetPage(self.driver).addmenu()
        MenusetPage(self.driver).permission(name)
        MenusetPage(self.driver).menuname(name)
        permissiontip = MenusetPage(self.driver).getpermissiontip()
        menunametip = MenusetPage(self.driver).getmenunametip()
        self.assertEqual(permissiontip, '当前权限标记已经存在！', msg='错误：添加菜单权限标记唯一性校验失败')
        self.assertEqual(menunametip, '当前名称已经存在!', msg='错误：添加菜单名称唯一性校验失败')

        time.sleep(2)
        menuname = name + 'new'
        MenusetPage(self.driver).permission(menuname)
        MenusetPage(self.driver).menuname(menuname)
        MenusetPage(self.driver).submit()
        time.sleep(2)

        # 搜索菜单，二次进入编辑
        MenusetPage(self.driver).searchtab(menuname)
        time.sleep(1)
        MenusetPage(self.driver).clicksearchresult()
        MenusetPage(self.driver).menuname(name)
        menunametip = MenusetPage(self.driver).getmenunametip()
        self.assertEqual(menunametip, '当前名称已经存在!', msg='错误：编辑菜单名称唯一性校验失败')

    # 6.填写必填添加客户用户菜单（不选单位、不选权限）
    @Base.screenshot_about_case
    def test_006(self):
        name = MenusetCommon(self.driver).menurequiredcommon(False)
        time.sleep(3)
        # 搜索后点击，不修改任何值提交，
        MenusetPage(self.driver).clickcustomertab()
        MenusetPage(self.driver).searchtab(name)
        time.sleep(1)
        MenusetPage(self.driver).clicksearchresult()
        MenusetPage(self.driver).submit()
        time.sleep(3)
        # 打开页面再检查 取编辑页面的各个值检查
        MenusetPage(self.driver).clickcustomertab()
        MenusetPage(self.driver).searchtab(name)
        time.sleep(1)
        MenusetPage(self.driver).clicksearchresult()
        time.sleep(2)
        menuvalue = MenusetCommon(self.driver).getmenuvalue(False)
        menuvalueinfo01 = {'name': name, 'parentper': None, 'type1': '用户', 'common': None,
         'valid': '有效', 'menupermission': '选择属于此权限的菜单', 'Permission': '选择属于此客户的权限'}
        self.assertEqual(menuvalue, menuvalueinfo01, msg='错误：填写必填项创建客户菜单编辑信息显示错误')

    @Base.screenshot_about_case
    def test_007(self):
        name = MenusetCommon(self.driver).menurequiredcommon()
        time.sleep(3)
        # 搜索不存在的服务人员菜单
        MenusetPage(self.driver).searchtab('祥龙十八掌倚天屠龙记')
        time.sleep(1)
        emptylist = MenusetPage(self.driver).getemptylist()
        self.assertEqual(emptylist, '暂无数据', msg='错误：搜索不存在的服务人员菜单组失败')

        # 搜索有效服务人员菜单--打开编辑页面修改有效为无效
        MenusetPage(self.driver).searchtab(name)
        searchresult = MenusetPage(self.driver).searchresult()
        self.assertEqual(searchresult, name, msg='错误：搜索有效服务人员菜单组失败')
        time.sleep(2)
        MenusetPage(self.driver).clicksearchresult()
        MenusetPage(self.driver).clickchooseinvalid()
        MenusetPage(self.driver).submit()
        # 增加时长 0427
        # time.sleep(5)
        # --------------------修改

        # 搜索无效服务人员菜单--打开编辑页面修改类型为客户
        MenusetPage(self.driver).searchtab(name)
        searchresult = MenusetPage(self.driver).searchresult()
        self.assertEqual(searchresult, name, msg='错误：搜索无效服务人员菜单组失败')
        # 取数数据
        searchresult02 = [name, '服务人员', '', '', '无效']
        searchresultrow = MenusetPage(self.driver).getsearchresultrow()
        for i in range(0, 5):
            searchresultrowtext = searchresultrow[i].text
            self.assertEqual(searchresultrowtext, searchresult02[i], msg='错误：菜单有效修改为无效失败')

        time.sleep(2)
        MenusetPage(self.driver).clicksearchresult()
        MenusetPage(self.driver).chosetypeustomer()
        MenusetPage(self.driver).submit()

        # 切换tab，搜索不存在的客户用户
        MenusetPage(self.driver).clickcustomertab()
        MenusetPage(self.driver).searchtab('祥龙十八掌倚天屠龙记')
        time.sleep(1)
        emptylist = MenusetPage(self.driver).getemptylist()
        self.assertEqual(emptylist, '暂无数据', msg='错误：搜索不存在的客户用户菜单组失败')

        # 搜索无效的客户用户菜单---并修改无效为有效
        MenusetPage(self.driver).clickcustomertab()
        MenusetPage(self.driver).searchtab(name)
        searchresult = MenusetPage(self.driver).searchresult()
        self.assertEqual(searchresult, name, msg='错误：搜索无效的客户用户菜单组失败')
        MenusetPage(self.driver).clicksearchresult()
        MenusetPage(self.driver).clickchoosevalid()
        MenusetPage(self.driver).submit()

        # 搜索有效的客户用户
        MenusetPage(self.driver).clickcustomertab()
        MenusetPage(self.driver).searchtab(name)
        searchresult = MenusetPage(self.driver).searchresult()
        self.assertEqual(searchresult, name, msg='错误：搜索有效的客户用户菜单组失败')
        searchresult02 = [name, '用户', '', '', '有效']
        searchresultrow = MenusetPage(self.driver).getsearchresultrow()
        for i in range(0, 5):
            searchresultrowtext = searchresultrow[i].text
            self.assertEqual(searchresultrowtext, searchresult02[i], msg='错误：菜单无效修改为有效失败')

    # 全填添加一个服务人员菜单，不修改任何值直接提交
    @Base.screenshot_about_case
    def test_008(self):
        menuinfo = MenusetCommon(self.driver).menufullcommon()
        time.sleep(3)
        MenusetPage(self.driver).searchtab(menuinfo.get('menuname'))
        MenusetPage(self.driver).clicksearchresult()
        # 增加强制等待
        time.sleep(3)
        MenusetPage(self.driver).submit()
        time.sleep(3)
        MenusetPage(self.driver).searchtab(menuinfo.get('menuname'))
        MenusetPage(self.driver).clicksearchresult()
        menuinfo = {'name': menuinfo.get('menuname'), 'parentper': menuinfo.get('MenuParent'), 'type1': '服务人员',
                    'common': '这是备注',
                    'valid': '有效', 'menupermission': 'CMDB', 'Permission': menuinfo.get('rolecompay')}
        # 增加强制等待
        time.sleep(5)
        menuvalue = MenusetCommon(self.driver).getmenuvalue()
        self.assertEqual(menuvalue, menuinfo, msg='错误：填写全填项创建服务人员菜单信息显示错误')

    # 全填增加客户用户菜单，不修改任何值直接提交
    # 2021-01-05 屏蔽该用例，客户添加提交页面非常慢，应该该用例
    # @Base.screenshot_about_case
    # def test_009(self):
    #     menuinfo = MenusetCommon(self.driver).menufullcommon(False)
    #     time.sleep(3)
    #     # 切换到客户用户tab
    #     MenusetPage(self.driver).clickcustomertab()
    #     MenusetPage(self.driver).searchtab(menuinfo.get('menuname'))
    #     MenusetPage(self.driver).clicksearchresult()
    #     # 增加强制等待
    #     time.sleep(3)
    #     MenusetPage(self.driver).submit()
    #     time.sleep(3)
    #     MenusetPage(self.driver).clickcustomertab()
    #     MenusetPage(self.driver).searchtab(menuinfo.get('menuname'))
    #     MenusetPage(self.driver).clicksearchresult()
    #
    #     # 增加强制等待
    #     time.sleep(3)
    #     menuinfo = {'name': menuinfo.get('menuname'), 'parentper': menuinfo.get('MenuParent'), 'type1': '用户',
    #                 'common': '这是备注客户',
    #                 'valid': '有效', 'menupermission': '工单', 'Permission': menuinfo.get('rolecompay')}
    #     menuvalue = MenusetCommon(self.driver).getmenuvalue(False)
    #     self.assertEqual(menuvalue, menuinfo, msg='错误：填写全填项创建客户用户菜单信息显示错误')















