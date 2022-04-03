"""
@author: DT_testing
@file:   tickettemplate_case.py
@desc:  【工单模板】
@step：001. 检查工单模板浏览器title,tabtitle,表格路径，表格默认字段(SC_Template_1、SC_Template_5，SC_Template_8)
       002. 点击添加模板，检查添加页面默认值，点击返回列表  （SC_Template_14、SC_Template_16）
       003. 填写必填，添加一个模板,二次进入信息显示正确，编辑必填项 （SC_Template_30 （SC_Template_15、SC_Template_17、SC_Template_29、SC_Template_109）
       004. 列表中操作-删除工单模板 ,过滤不存在的模板  （SC_Template_111,SC_Template_122）
       005. 名称重名校验，名称回删,包含的名称校验     （SC_Template_23  SC_Template_25 、SC_Template_26）
       006.  全填创建服务人员模板，同时将模板置为无效  （SC_Template_33、 SC_Template_34）
       007.  全填创建处理模板，同时将模板无效   （SC_Template_35  SC_Template_36）
       008.  模板内部检查，分别选择服务人员、用户检查字段   （SC_Template_27）
       009. 编辑必填项 （SC_Template_30）
       010. 创建工单-删除可删除的字段，二次进入查看  SC_Template_69
       011. 复制模板  SC_Template_120
       012. 必填值隐藏再显示检查，检查提示  SC_Template_72
       013. 增加创建模板，检查挂起时间隐藏   SC_Template_73-1
       014. 增加处理模板，检查挂起时间隐藏   SC_Template_73-2
       015. 固定字段默认值检查   SC_Template_73-0   ok
       016. 检查工单模板默认的模板图片以及模板颜色  SC_Template_10  SC_Template_12  ok
       017. 检查工单模板修改后的模板图片和模板颜色   SC_Template_11  SC_Template_13   ok
       018. 固定字段的可选检查   SC_Template_78  SC_Template_79   ok
       019. 添加自定义字段    ok
       020. （在工单模板中直接添加字段）自定义字段默认值检查（添加自定义字段、选择默认值后隐藏）  SC_Template_73  ok
       021. （在工单模板中直接添加字段）自定义字段的可选检查    SC_Template_80   SC_Template_81   ok
       022. 二次编辑自定义的日期/日期时间字段  SC_Template_146  ok
       023. 二次编辑自定义的复选字段    SC_Template_147        ok
       024. 检查工单模板中是否显示字段“工单转派规则”    SC_Template_148
       025. 主题说明提示在目标栏下方、目标栏中，右侧提示图标中；修改说明；删除说明
        SC_Template_149、SC_Template_150、SC_Template_151 、SC_Template_152、SC_Template_153
       026. 工单模板，指定处理人设置为必填，检查提交按钮
       027. 检查客户用户下拉是否显示客户 SC_Template_171
       028. 处理模板中删除不填写值的必填字段，检查提交按钮  SC_Template_172


"""
from common.base import Base
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.template_page import TemplatePage
from src.page.agent.table_page import TablePage
from src.page.pagecommon.tickettemplate_common import TicketTemplateCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from src.page.pagecommon.get_time_common import GetTimeCommon
import time
from src.page.pagecommon.field_common import FieldCommon
import unittest2

class TicketTemplate(BaseCaseUser, Base):

    # 检查路径  #0910 不稳定，屏蔽，已转移到用例003检修校验
    # @Base.screenshot_about_case
    # def test_001_templatelist(self):
    #     EntranceAgentPage(self.driver).enter_tickettemplate()
    #     # 必须加强制等待，否则会取主页的列表值
    #     time.sleep(12)
    #     # 检查页面路径
    #     roadText = TemplatePage(self.driver).getroadText()
    #     roadText = str.replace(roadText, ' ', '')
    #     # 检查浏览器title
    #     titleText = TemplatePage(self.driver).get_title()
    #     # 获取页面内tabtitle
    #     tabTitle = TemplatePage(self.driver).gettabTitle()
    #     assert roadText == '/系统管理/工单模板', '工单模板列表路径显示不正确'
    #     assert titleText == '工单模板', '工单模板浏览器窗口 title 显示不正确'
    #     assert tabTitle == '工单模板', '工单模板tab窗口 title 显示不正确'
    #     # 检查列表表头
    #     # print(titleText, tabTitle, roadText)
    #     template_listinfo = ['', '名称', '前端', '移动端', '网页、web 端', '类型', 'windows 桌面端', '描述', '有效', '修改人', '修改时间', '创建人',
    #                          '创建时间', '操作']
    #     tabtableth = TemplatePage(self.driver).gettableth()
    #     # print('表列长度为：', len(tabtableth))

        # # 到此加循环
        # for i in range(0, len(tabtableth)):
        #     textinfo = tabtableth[i].text
        #     self.assertEqual(textinfo, template_listinfo[i], msg='工单模板列表表头显示不正确')


    @Base.screenshot_about_case
    def test_002(self):
        """
        点击添加模板，检查添加页面默认值，点击返回列表,搜索不存在的值
        """
        # EntranceAgentPage(self.driver).enter_tickettemplate()
        EntranceAgentPage(self.driver).enter_relust("工单模板")
        TemplatePage(self.driver).addtemplate()
        template_listinfo = ['名称','备注', '在以下界面可用','角色', '显示位置', '类型', '显示类型', '描述' , '关联知识库类型', '关联知识库内容','模板颜色' ,'模板图片' ,'有效性']
        for listheader01 in ['.ant-form-item-label label']:
            for i in range(0, 13):
                text = str.replace(self.driver.find_elements_by_css_selector(listheader01)[i].text,' ','')
                # print(i,text )
                self.assertEqual(text , template_listinfo[i] , msg='工单模板基本信息1显示不正确')
        template_listinfo2 = ['类型', '客户用户', '客户名称', '客户用户资产', '角色',  '指定处理人', '负责人', '主题', '内容', '状态', '优先级']

        gettemfiled = TemplatePage(self.driver).gettemshowfidld()
        for i in range(0, 11):
            temfiled = gettemfiled[i].text
            # print(i, temfiled, listinfo[i])
            self.assertEqual(temfiled, template_listinfo2[i], msg='工单模板基本信息2显示不正确')

        commi_clickable = TemplatePage(self.driver).commi_clickable()
        TemplatePage(self.driver).backlist()
        time.sleep(5)
        # 返回后搜索不存在的值
        TemplatePage(self.driver).search('黑社会测试001')
        emptydescribe = TemplatePage(self.driver).getemptydescribe()
        # print(emptydescribe, commi_clickable)
        self.assertEqual(commi_clickable, False, msg='错误：点击添加按钮进去，提交按钮可触发')
        self.assertEqual(emptydescribe, '这里空空如也, 跟我的钱包一样', msg='错误：点击添加模板，再点击返回列表失败')

    # 填写必填项，
    # @Base.screenshot_about_case
    def test_003_templateRequired(self):
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon()
        name = templateInfo['name']
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name)
        # 搜索后开始检查；列表数据展示
        template_listinfo = [name, '服务人员', '1', '1', '创建工单', '1', '', '有效']
        FiledList01 = TemplatePage(self.driver).getearchresult()
        filed_list01_list = []
        for i in range(0, len(FiledList01)):
            filed_list01_list.append(FiledList01[i].text)
        # print("列表数据显示：", filed_list01_list)
        # 将预期的数据与搜索后数据对比，检查列表的数据展示
        for i in range(0, len(template_listinfo)):
            with self.subTest(i=i):
                self.assertIn(template_listinfo[i], filed_list01_list,
                              msg='错误：添加工单模板后列表数据显示错误,缺少：' + template_listinfo[i])

        TemplatePage(self.driver).clicksearchresult()
        # 编辑进入取值必须增加强制时间等待，否则取到的值不正确
        time.sleep(3)
        # 等待界面显示
        TemplatePage(self.driver).check_name_input()
        bar = TemplatePage(self.driver).gettitlebar()
        # 检查浏览器title
        dirvertitle = TemplatePage(self.driver).get_title()
        # 获取页面内tabtitle
        tabTitle = TemplatePage(self.driver).gettabTitle()
        self.assertEqual(bar, '/系统管理/工单模板/工单模板编辑/'+name, msg='错误：工单模板编辑页面的bar显示错误')
        self.assertEqual(tabTitle, '工单模板编辑 - ' + name, msg='错误：工单模板编辑页面的tab title显示错误')
        self.assertEqual(dirvertitle, '工单模板编辑', msg='错误：工单模板编辑浏览器标题title显示错误')

        # 编辑必填信息
        newname = '工单模板修改必填' + time.strftime('%Y%m%d%M%S', time.localtime())
        time.sleep(2)
        TemplatePage(self.driver).inputname(newname)
        time.sleep(2)
        TemplatePage(self.driver).clickcustomer()
        TemplatePage(self.driver).clickweb()
        TemplatePage(self.driver).choseprocessticket()
        TemplatePage(self.driver).choseinvaild()
        TemplatePage(self.driver).commit()
        time.sleep(3)
        TemplatePage(self.driver).search(newname)
        TemplatePage(self.driver).clicksearchresult()
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        # 编辑后信息校验
        TemplatePage(self.driver).search(newname)
        # # 对比值
        # template_listinfo = [None, newname, '用户', '0', '1', '处理工单', '0', '', '无效']
        # FiledList01 = TemplatePage(self.driver).getearchresult()
        # for i in range(1, 9):
        #     text_zoom_01 = FiledList01[i].text
        #     # print(i, text)
        #     self.assertEqual(text_zoom_01, template_listinfo[i], msg='错误：编辑工单模板必填后列表数据显示错误，正确应为：' + text_zoom_01)
        # 预期列表值
        expect_list02 = [ newname, '用户', '0', '1', '处理工单', '0', '', '无效']
        # 取实际列表值
        template_listinfo02 = TemplatePage(self.driver).getearchresult()
        actual_list02 = []
        for i in range(0, len(template_listinfo02)):
            actual_list02.append(template_listinfo02[i].text)
        # 将预期的数据与搜索后数据对比，检查列表的数据展示
        for i in range(0, len(expect_list02)):
            with self.subTest(i=i):
                self.assertIn(expect_list02[i], actual_list02,
                              msg='错误：编辑工单模板必填后列表数据显示错误,缺少：' + expect_list02[i])

        # 搜索后点击
        TemplatePage(self.driver).clicksearchresult()
        # 点击编辑进入界面，取各个字段值与预期的进行校验（后续补充）
        # 返回列表
        TemplatePage(self.driver).backlist()
        time.sleep(1)
        bar2 = TemplatePage(self.driver).gettitlebar()
        self.assertEqual(bar2, '/系统管理/工单模板/', msg='错误：编辑模板返回列表失败')

    # 0728模板删除存在bug   2020072828000159 0814修复
    @Base.screenshot_about_case
    def test_004_deletemplate(self):
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon()
        time.sleep(5)
        name = templateInfo['name']
        # print(name)
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clickdete()
        # 取删除弹框的值
        deletitle = TemplatePage(self.driver).getdetetitle()
        self.assertEqual(deletitle, '你确定删除这条记录?', msg='错误：删除信息显示错误')
        TemplatePage(self.driver).clickcancledete()
        TemplatePage(self.driver).clickdete()
        TemplatePage(self.driver).clickconfirmdete()
        # 删除之后必须加时间等待
        time.sleep(1)
        TemplatePage(self.driver).search(name)
        # 取搜索为空的描述
        empty = TemplatePage(self.driver).getemptydescribe()
        self.assertEqual(empty, '这里空空如也, 跟我的钱包一样', msg='错误：模板删除失败')

    # 重名提示获取id丢失，暂时屏蔽 0902 恢复放出
    # @Base.screenshot_about_case
    @unittest2.skip("0924工单模板已支持重名,跳过")
    def test_005_checkTemplatename(self):
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon()
        name = templateInfo['name']
        # 再次点击添加
        TemplatePage(self.driver).addtemplate()
        TemplatePage(self.driver).inputname(name)
        TemplatePage(self.driver).clickagent()
        TemplatePage(self.driver).clickshowLocation()
        TemplatePage(self.driver).clickselectall()
        TemplatePage(self.driver).clickcloseOption()
        TemplatePage(self.driver).chosecreateticket()
        TemplatePage(self.driver).chosevaild()
        # 判断提交按钮
        commistatus = TemplatePage(self.driver).commi_clickable()
        # 取重名提示
        self.assertEqual(commistatus, False, msg='错误：模板名称重名后提交按钮可点击')
        rename = TemplatePage(self.driver).getrename()
        self.assertEqual(rename, '当前字段已存在', msg='错误：模板名称重名未提示')
        time.sleep(3)
        # 回删，重名提示消失
        # 创建包含的模板名称提交
        TemplatePage(self.driver).inputname(name+'123')
        TemplatePage(self.driver).commit()
        # 搜索到用户，返回名称相等
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name+'123')
        time.sleep(2)
        TemplatePage(self.driver).clicksearchresult()

    # 0924,显示类型字段出现问题，选择普通表单，提交按钮不亮
    @Base.screenshot_about_case
    # @unittest2.skip("显示类型字段bug2021092410000051,跳过")  # 20211231已恢复
    def test_006_fullcreatetemp(self):
        templateInfo = TicketTemplateCommon(self.driver).templatefullCommon('create')
        name = templateInfo['name']
        # 表头字段显示则开始搜索
        # TemplatePage(self.driver).gettableth()
        TablePage(self.driver).gettableth()
        # TemplatePage(self.driver).search(name)
        # EntranceAgentPage(self.driver).enter_tickettemplate()
        # time.sleep(3)
        # TemplatePage(self.driver).search("工单模板全填202112303709")

        TemplatePage(self.driver).clicksearchresult()
        TemplatePage(self.driver).commit()
        # 必须加强制等待，等待列表数据加载
        # time.sleep(3)
        # 表头字段显示则开始搜索
        TablePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name)

        expect_list = [name, '服务人员', '1', '1', '创建工单', '1', '全填创建模板', '有效']
        template_listinfo = TemplatePage(self.driver).getearchresult()
        actual_list = []
        for i in range(0, len(template_listinfo)):
            actual_list.append(template_listinfo[i].text)
        # 将预期的数据与搜索后数据对比，检查列表的数据展示
        for i in range(0, len(expect_list)):
            with self.subTest(i=i):
                self.assertIn(expect_list[i], actual_list,
                              msg='错误：添加工单模板后列表数据显示错误,缺少：' + expect_list[i])

        # 修改为无效
        TemplatePage(self.driver).clicksearchresult()
        TemplatePage(self.driver).choseinvaild()
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TablePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name)
        # 预期列表值
        expect_list02 = [name, '服务人员', '1', '1', '创建工单', '1', '全填创建模板', '无效']
        # 取实际列表值
        template_listinfo02 = TemplatePage(self.driver).getearchresult()
        actual_list02 = []
        for i in range(0, len(template_listinfo02)):
            actual_list02.append(template_listinfo02[i].text)
        # 将预期的数据与搜索后数据对比，检查列表的数据展示
        for i in range(0, len(expect_list02)):
            with self.subTest(i=i):
                self.assertIn(expect_list02[i], actual_list02,
                              msg='错误：添加工单模板后列表数据显示错误,缺少：' + expect_list02[i])

    @Base.screenshot_about_case
    # @unittest2.skip("显示类型字段bug2021092410000051,跳过")
    def test_007_fullprocesstemp(self):
        """
            全填创建处理模板，同时将模板无效   （SC_Template_35  SC_Template_36）
        """
        templateInfo = TicketTemplateCommon(self.driver).templatefullCommon('process')
        name = templateInfo['name']
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name)
        # tablelist = ['', name, '服务人员', '1', '1', '处理工单', '1', '全填创建模板', '有效']
        # FiledList01 = TemplatePage(self.driver).getearchresult()
        # for i in range(0, 8):
        #     text_zoom_01 = FiledList01[i].text
        #     # print(text_zoom_01, tablelist[i], i)
        #     self.assertEqual(text_zoom_01, tablelist[i], msg='错误：添加模板后数据列表显示错误' + text_zoom_01)
        expect_list = [name, '服务人员', '1', '1', '处理工单', '1', '全填创建模板', '有效']
        # 取实际列表值
        template_listinfo = TemplatePage(self.driver).getearchresult()
        actual_list = []
        for i in range(0, len(template_listinfo)):
            actual_list.append(template_listinfo[i].text)
        # 将预期的数据与搜索后数据对比，检查列表的数据展示
        for i in range(0, len(expect_list)):
            with self.subTest(i=i):
                self.assertIn(expect_list[i], actual_list,
                              msg='错误：添加工单模板后列表数据显示错误,缺少：' + expect_list[i])

        # 修改为无效
        # tablelist02 = ['', name, '服务人员', '1', '1', '处理工单', '1', '全填创建模板', '无效']
        TemplatePage(self.driver).clicksearchresult()
        TemplatePage(self.driver).choseinvaild()
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name)
        time.sleep(3)
        # FiledList01 = TemplatePage(self.driver).getearchresult()
        # for i in range(0, 8):
        #     text_zoom_01 = FiledList01[i].text
        #     # print(text_zoom_01, tablelist[i], i)
        #     self.assertEqual(text_zoom_01, tablelist02[i], msg='错误：添加模板后数据列表显示错误' + text_zoom_01)
        # 预期列表值
        expect_list02 = [ name, '服务人员', '1', '1', '处理工单', '1', '全填创建模板', '无效']
        # 取实际列表值
        template_listinfo02 = TemplatePage(self.driver).getearchresult()
        actual_list02 = []
        for i in range(0, len(template_listinfo02)):
            actual_list02.append(template_listinfo02[i].text)
        # 将预期的数据与搜索后数据对比，检查列表的数据展示
        for i in range(0, len(expect_list02)):
            with self.subTest(i=i):
                self.assertIn(expect_list02[i], actual_list02,
                              msg='错误：添加工单模板后列表数据显示错误,缺少：' + expect_list02[i])

    @Base.screenshot_about_case
    def test_008(self):
        """
         008.  模板内部检查，分别选择服务人员、用户检查字段
        """
        EntranceAgentPage(self.driver).enter_tickettemplate()
        TemplatePage(self.driver).addtemplate()
        TemplatePage(self.driver).clickcustomer()
        # time.sleep(5)
        text01 = TemplatePage(self.driver).getrolecompany()
        rolemessge = TemplatePage(self.driver).getmessage()
        self.assertEqual(text01, '客户', msg='错误：点击到用户，字段显示错误')
        self.assertEqual(rolemessge, '选择哪些客户可以使用该模板，如果不选, 所有客户可以使用该模板', msg='切换到用户提示信息错误' )
        TemplatePage(self.driver).clickagent()
        rolemessge = TemplatePage(self.driver).getmessage()
        self.assertEqual(rolemessge, '选择哪些角色可以使用该模板，如果不选, 所有服务人员都可以使用该模板', msg='切换到服务人员提示信息错误')

    # 合并到用例003，屏蔽该用例2021-12-31
    # @Base.screenshot_about_case
    # def test_009_editrequired(self):
    #     """
    #         编辑必填项 （SC_Template_30）
    #     """
    #     templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon()
    #     name = templateInfo['name']
    #     # print(name)
    #     TemplatePage(self.driver).search(name)
    #     TemplatePage(self.driver).clicksearchresult()
    #     # 编辑进入取值必须增加强制时间等待，否则取到的值不正确
    #     time.sleep(5)
    #     # 编辑必填信息
    #     newname = '工单模板修改必填' + time.strftime('%Y%m%d%M%S', time.localtime())
    #     time.sleep(2)
    #     TemplatePage(self.driver).inputname(newname)
    #     time.sleep(2)
    #     TemplatePage(self.driver).clickcustomer()
    #     TemplatePage(self.driver).clickweb()
    #     TemplatePage(self.driver).choseprocessticket()
    #     TemplatePage(self.driver).choseinvaild()
    #     TemplatePage(self.driver).commit()
    #     time.sleep(3)
    #     TemplatePage(self.driver).search(newname)
    #     TemplatePage(self.driver).clicksearchresult()
    #     TemplatePage(self.driver).commit()
    #     time.sleep(3)
    #     TemplatePage(self.driver).search(newname)
    #     # 对比值
    #     template_listinfo = [None, newname, '用户', '0', '1', '处理工单', '0', '', '无效']
    #     FiledList01 = TemplatePage(self.driver).getearchresult()
    #     for i in range(1, 9):
    #         text_zoom_01 = FiledList01[i].text
    #         # print(i, text)
    #         self.assertEqual(text_zoom_01, template_listinfo[i], msg='错误：编辑工单模板必填后列表数据显示错误，正确应为：' + text_zoom_01)

    @Base.screenshot_about_case
    def test_010_deletefield(self):
        """
        创建工单-删除可删除的字段，二次进入查看  SC_Template_69
        """
        EntranceAgentPage(self.driver).enter_tickettemplate()
        time.sleep(2)
        TemplatePage(self.driver).addtemplate()
        templatename = '工单模板必填' + time.strftime('%Y%m%d%M%S', time.localtime())
        TemplatePage(self.driver).inputname(templatename)
        TemplatePage(self.driver).clickweb()
        TemplatePage(self.driver).chosecreateticket()
        # 滑动到页面底部
        # Base(self.driver).move_to_pagebottom()
        TemplatePage(self.driver).clickdelresponsible()
        time.sleep(1)
        TemplatePage(self.driver).clickdelOwner()
        time.sleep(1)
        TemplatePage(self.driver).clickdelConfigItems()
        time.sleep(1)
        TemplatePage(self.driver).clickdelCustomerUser()
        # TemplatePage(self.driver).clickdelCustomerID()
        time.sleep(2)
        TemplatePage(self.driver).commit()
        time.sleep(10)
        TemplatePage(self.driver).search(templatename)
        time.sleep(2)
        TemplatePage(self.driver).clicksearchresult()
        time.sleep(1)
        # Base(self.driver).move_to_pagebottom()
        template_listinfo2 = ['类型', '角色',  '主题',  '内容', '状态', '优先级']
        for listheader02 in ['.ant-form-item.ant-row.ng-star-inserted>.ant-form-item-label>label']:
            for i in range(0, 6):
                text = str.replace(self.driver.find_elements_by_css_selector(listheader02)[i].text, ' ', '')
                # print(i, text, template_listinfo2[i])
                with self.subTest(i=i):
                    self.assertEqual(text, template_listinfo2[i], msg='删除字段失败')

    @Base.screenshot_about_case
    def test_011_coyptem(self):
        """
        复制模板  SC_Template_120
        """
        # 必填增加一个模板，点击复制
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon()
        time.sleep(5)
        name = templateInfo['name']
        # time.sleep(3)
        TemplatePage(self.driver).search(name)
        time.sleep(1)
        TemplatePage(self.driver).clickcopy()
        # TemplatePage(self.driver).clickdete()
        TemplatePage(self.driver).commit()
        # 提交后页面loading时间过长，一定添加
        time.sleep(5)
        TemplatePage(self.driver).search(name)
        time.sleep(1)
        # 工单模板模块取消了tab数量显示，调整断言2021-12-31
        # temnumber = TemplatePage(self.driver).gettemnuber()   #  调整断言2021-12-31
        # self.assertEqual(temnumber, '全部 ( 2 )', msg='复制工单模板失败')   # 调整断言2021-12-31
        # tbody tr.cursor
        temnumber = TemplatePage(self.driver).gettemnuber()   # 调整断言2021-12-31
        self.assertEqual(temnumber, 2 , msg='复制工单模板失败')  # 调整断言2021-12-31

    # 0805 bug 2020040128000124
    @Base.screenshot_about_case
    def test_012_requredhidden(self):
        """
          012. 必填值隐藏再显示检查，检查提示  SC_Template_72
        """
        EntranceAgentPage(self.driver).enter_tickettemplate()
        time.sleep(6)
        TemplatePage(self.driver).addtemplate()
        templatename = '隐藏字段' + time.strftime('%Y%m%d%M%S', time.localtime())
        TemplatePage(self.driver).inputname(templatename)
        TemplatePage(self.driver).clickweb()
        TemplatePage(self.driver).chosecreateticket()
        # # 滑动到页面底部
        # Base(self.driver).move_to_pagebottom()
        time.sleep(3)
        TemplatePage(self.driver).clickdelresponsible()
        time.sleep(2)
        TemplatePage(self.driver).clickdelOwner()
        TemplatePage(self.driver).clickdelConfigItems()
        TemplatePage(self.driver).clickdelCustomerUser()
        time.sleep(2)
        # TemplatePage(self.driver).clickdelCustomerID()
        TemplatePage(self.driver).clicktypehidden()
        TemplatePage(self.driver).clickqueuehidden()
        TemplatePage(self.driver).clicksubjecthidden()
        TemplatePage(self.driver).clickbodyhidden()
        TemplatePage(self.driver).clickstatehidden()
        TemplatePage(self.driver).clickpriorityhidden()
        # 取几个必填项的隐藏、同时做断言
        typecolor1 = TemplatePage(self.driver).gettypehiddencolor()
        queuecolor1 = TemplatePage(self.driver).gettypehiddencolor()
        subjecolor1 = TemplatePage(self.driver).gettypehiddencolor()
        bodycolor1 = TemplatePage(self.driver).gettypehiddencolor()
        statecolor1 = TemplatePage(self.driver).gettypehiddencolor()
        prioritycolor1 = TemplatePage(self.driver).getpriorityhiddencolor()
        self.assertEqual(typecolor1,'background: rgb(92, 92, 92);',msg='隐藏类型字段失败')
        self.assertEqual(queuecolor1, 'background: rgb(92, 92, 92);', msg='隐藏角色字段失败')
        self.assertEqual(subjecolor1, 'background: rgb(92, 92, 92);', msg='隐藏主题字段失败')
        self.assertEqual(bodycolor1, 'background: rgb(92, 92, 92);', msg='隐藏内容字段失败')
        self.assertEqual(statecolor1, 'background: rgb(92, 92, 92);', msg='隐藏状态字段失败')
        self.assertEqual(prioritycolor1, 'background: rgb(92, 92, 92);', msg='隐藏优先级字段失败')
        time.sleep(2)
        TemplatePage(self.driver).clicktypeshown()
        TemplatePage(self.driver).clickqueueshown()
        TemplatePage(self.driver).clicksubjectshown()
        TemplatePage(self.driver).clickbodyshown()
        TemplatePage(self.driver).clickstateshown()
        TemplatePage(self.driver).clickpriorityshown()
        # 缺文字信息的判断
        time.sleep(2)
        submit12 = TemplatePage(self.driver).commi_clickable()
        self.assertEqual(submit12, True, msg='必填项点击隐藏再点击显示，提交按钮不可触发')


    # bug 挂起时间隐藏失败  2020070928000122
    # def test_013(self):
    #     try:
    #         templateInfo = TicketTemplateCommon(self.driver).templatefullCommon('create')
    #         name = templateInfo['name']
    #         # print(name)
    #         time.sleep(3)
    #         TemplatePage(self.driver).search(name)
    #         time.sleep(2)
    #         TemplatePage(self.driver).clicksearchresult()
    #         # 编辑进入取值必须增加强制时间等待，否则取到的值不正确
    #         time.sleep(5)
    #         # 滑动到页面底部
    #         js = "window.scrollTo(0,10000);"
    #         self.driver.execute_script(js)
    #         TemplatePage(self.driver).chosepeding()
    #         TemplatePage(self.driver).clickpendinghidden()
    #         TemplatePage(self.driver).chosependingmonth()
    #         TemplatePage(self.driver).chosependingdate()
    #         TemplatePage(self.driver).commit()
    #         time.sleep(3)
    #         TemplatePage(self.driver).search(name)
    #         time.sleep(2)
    #         TemplatePage(self.driver).clicksearchresult()
    #         # 滑动到页面底部
    #         time.sleep(5)
    #         js = "window.scrollTo(0,10000);"
    #         self.driver.execute_script(js)
    #         pendcolor = TemplatePage(self.driver).getpendinghiddencolor()
    #         print(pendcolor)
    #         self.assertEqual(pendcolor, 'background: rgb(92, 92, 92);', msg='创建工单隐藏挂起时间失败')
    #     except Exception as msg:
    #         Base.get_windows_img(self)
    #         self.logger.error('创建工单隐藏挂起时间失败' + str(msg))

    # bug 挂起时间隐藏失败  2020070928000122
    # def test_014(self):
    #     try:
    #         templateInfo = TicketTemplateCommon(self.driver).templatefullCommon('process')
    #         name = templateInfo['name']
    #         # print(name)
    #         time.sleep(3)
    #         TemplatePage(self.driver).search(name)
    #         time.sleep(2)
    #         TemplatePage(self.driver).clicksearchresult()
    #         # 编辑进入取值必须增加强制时间等待，否则取到的值不正确
    #         time.sleep(5)
    #         # 滑动到页面底部
    #         js = "window.scrollTo(0,10000);"
    #         self.driver.execute_script(js)
    #         TemplatePage(self.driver).chosepeding()
    #         TemplatePage(self.driver).clickpendinghidden()
    #         TemplatePage(self.driver).chosependingmonth()
    #         TemplatePage(self.driver).chosependingdate()
    #         TemplatePage(self.driver).commit()
    #         time.sleep(3)
    #         TemplatePage(self.driver).search(name)
    #         time.sleep(2)
    #         TemplatePage(self.driver).clicksearchresult()
    #         # 滑动到页面底部
    #         time.sleep(5)
    #         js = "window.scrollTo(0,10000);"
    #         self.driver.execute_script(js)
    #         pendcolor = TemplatePage(self.driver).getpendinghiddencolor()
    #         # print(pendcolor)
    #         self.assertEqual(pendcolor, 'background: rgb(92, 92, 92);', msg='处理模板隐藏挂起时间失败')
    #     except Exception as msg:
    #         Base.get_windows_img(self)
    #         self.logger.error('处理模板隐藏挂起时间失败' + str(msg))

    @Base.screenshot_about_case
    def test_015_defaultvalue(self):
        """
        固定字段默认值检查   SC_Template_73-0
        """
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        templatename = templateInfo.get('name')
        # print(templatename)
        # # 滑动到页面底部
        # Base(self.driver).move_to_pagebottom()
        # Base(self.driver).move_to_pagebottom()
        time.sleep(3)
        # 此处删除一些项保证屏幕不需要滚动
        TemplatePage(self.driver).clickdelresponsible()
        time.sleep(2)
        TemplatePage(self.driver).clickdelOwner()
        time.sleep(2)
        TemplatePage(self.driver).clickdelCustomerUser()
        time.sleep(2)
        # 选择类型为问题
        TemplatePage(self.driver).chosetype2("问题")
        TemplatePage(self.driver).inputsubject('测试输入主题')
        # 进入内容ifrem
        # TemplatePage(self.driver).enteriframe()
        # TemplatePage(self.driver).inputcontent('这是测试的内容输入')
        # self.driver.switch_to.default_content()
        TemplatePage(self.driver).inputcontent2('这这是测试的内容输入')

        TemplatePage(self.driver).chosepeding("挂起提醒")
        TemplatePage(self.driver).chosepriority("非常高")
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).searchclick(templatename)
        # Base(self.driver).move_to_pagebottom()
        getsubject = TemplatePage(self.driver).getsubject()
        gettypetext = TemplatePage(self.driver).gettypetext()
        # getroletext = TemplatePage(self.driver).getroletext()
        getstatetext = TemplatePage(self.driver).getstatetext()
        # 进入内容ifrem
        # TemplatePage(self.driver).enteriframe()
        # getiframe = TemplatePage(self.driver).getiframe()
        # self.driver.switch_to.default_content()
        getcontent = TemplatePage(self.driver).getcontent()
        # 状态、优先级
        getPrioritytext = TemplatePage(self.driver).getPrioritytext()
        # print(getsubject, gettypetext, getstatetext, getPrioritytext, getiframe)
        self.assertEqual(getsubject, '测试输入主题', msg='主题默认显示失败')
        self.assertEqual(gettypetext, '问题', msg='问题默认显示失败')
        self.assertEqual(getstatetext, '挂起提醒', msg='状态默认显示失败')
        self.assertEqual(getPrioritytext, '非常高', msg='优先级默认显示失败')
        self.assertEqual(getcontent, '这是测试的内容输入', msg='内容默认显示失败')

    # 屏蔽，与017用例合并检查
    # @Base.screenshot_about_case
    # def test_016_colorimg(self):
    #     """
    #      检查工单模板默认的模板图片以及模板颜色 SC_Template_10  SC_Template_12
    #     """
    #     EntranceAgentPage(self.driver).enter_tickettemplate()
    #     TemplatePage(self.driver).addtemplate()
    #     defaultcolor = TemplatePage(self.driver).getticketcolor()
    #     defaultimg = TemplatePage(self.driver).getimgstyle()
    #     self.assertEqual(defaultcolor, 'background: rgb(153, 171, 180);', msg='进入工单模板，默认颜色显示错误')
    #     self.assertEqual(defaultimg, 'template-icon template-icon-click ng-star-inserted', msg='进入工单模板，默认图片显示错误')

    @Base.screenshot_about_case
    # @unittest2.skip("显示类型字段bug2021092410000051,跳过")  # 2021-12-31 恢复
    def test_017_changecolorimg(self):
        """
            016. 检查工单模板默认的模板图片以及模板颜色  SC_Template_10  SC_Template_12  ok
            017. 检查工单模板修改后的模板图片和模板颜色   SC_Template_11  SC_Template_13   ok
        """
        templateInfo = TicketTemplateCommon(self.driver).templatefullCommon('create')
        templatename = templateInfo.get('name')
        time.sleep(3)
        TemplatePage(self.driver).searchclick(templatename)
        color = TemplatePage(self.driver).getticketcolor()
        defaultimg = TemplatePage(self.driver).getimgstyle()
        img = TemplatePage(self.driver).getchoseimgstyle()
        self.assertEqual(color, 'background: rgb(102, 102, 102);', msg='进入工单模板，修改颜色显示错误')
        self.assertEqual(defaultimg, 'template-icon ng-star-inserted', msg='进入工单模板，修改图片后默认图片显示错误')
        self.assertIn('template-icon-click', img, msg='进入工单模板，选择的图片显示错误')
        # 返回列表
        TemplatePage(self.driver).backlist()
        time.sleep(5)
        TemplatePage(self.driver).addtemplate()
        defaultcolor = TemplatePage(self.driver).getticketcolor()
        defaultimg = TemplatePage(self.driver).getimgstyle()
        self.assertEqual(defaultcolor, 'background: rgb(153, 171, 180);', msg='进入工单模板，默认颜色显示错误')
        self.assertEqual(defaultimg, 'template-icon template-icon-click ng-star-inserted', msg='进入工单模板，默认图片显示错误')

    # 20210302 运行自动化的环境，字段最后的黑色按钮点击没有反应，暂时屏蔽用例
    @Base.screenshot_about_case
    def test_018(self):
        """
        固定字段-状态的可选检查   SC_Template_78  SC_Template_79
        """
        # fieldInfo = FieldCommon(self.driver).fieldRequiredCommon('Ticket')
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        templatename = templateInfo.get('name')
        # Base(self.driver).move_to_pagebottom()
        # 点击状态后的黑色小三角
        time.sleep(3)
        TemplatePage(self.driver).clickdownState()
        time.sleep(2)
        TemplatePage(self.driver).clickStateoptions()
        time.sleep(2)
        TemplatePage(self.driver).chosestatenew()
        # TemplatePage(self.driver).sendesc()
        # 删除遮罩层继续操作
        # TemplatePage(self.driver).delete_backdrop_showing()
        time.sleep(2)
        TemplatePage(self.driver).commit()
        # 必须加强制等待
        time.sleep(2)
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).searchclick(templatename)
        # Base(self.driver).move_to_pagebottom()
        TemplatePage(self.driver).clickdownState()
        # 取状态的选项值
        Stateoptionstext = TemplatePage(self.driver).getStateoptionstext()
        self.assertEqual(Stateoptionstext, '新建', msg='状态可选值为新建设置出错')

    @Base.screenshot_about_case
    def test_019(self):
        """添加自定义字段 """
        fieldInfo = FieldCommon(self.driver).fieldRequiredCommon('Ticket')
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")

        name = ''.join(fieldInfo.get('name').split())
        sys = ''.join(fieldInfo.get('sysField').split())
        # fieldname = str(name + ' ( DynamicField_' + sys + ' )')
        # Base(self.driver).move_to_pagebottom()
        TemplatePage(self.driver).choseField(name, sys)
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).searchclick(templateInfo.get('name'))
        # 点击展开编辑页面必须强制等待
        # time.sleep(3)
        # Base(self.driver).move_to_pagebottom()
        listinfo = ['类型', '客户用户', '客户名称', '客户用户资产', '角色',  '指定处理人', '负责人',
                    '主题', '内容', '状态', '优先级', name]
        gettemfiled = TemplatePage(self.driver).gettemshowfidld()
        for i in range(0, len(gettemfiled)):
            temfiled = gettemfiled[i].text
            # print(i, temfiled, listinfo[i])
            with self.subTest(i=i):
                self.assertEqual(temfiled, listinfo[i], msg='自定义字段添加失败')

    # 1130 bug 通过工单模板没的添加按钮添加的字段提交后，二次进入在工单模板中不显示 --已修复
    @Base.screenshot_about_case
    def test_020(self):
        """
        （在工单模板中直接添加字段）自定义字段默认值检查（添加自定义字段、选择默认值后隐藏）
        """
        # 填写工单必填值
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        # Base(self.driver).move_to_pagebottom()
        time.sleep(3)
        fieldinfo = TicketTemplateCommon(self.driver).fullSelectFieldCommon()
        time.sleep(3)
        fieldsys = fieldinfo.get('sysField')
        fieldname = fieldinfo.get('name')
        # print(fieldsys, fieldname)
        TemplatePage(self.driver).hiddenfield(fieldsys)
        TemplatePage(self.driver).chosefielddefault(fieldsys)
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).searchclick(templateInfo.get('name'))
        time.sleep(3)
        getfieldlcolor = TemplatePage(self.driver).gethiddenfieldcolor(fieldsys)
        getfieldltext = TemplatePage(self.driver).getfieldtext(fieldsys)
        self.assertEqual(getfieldlcolor, 'background: rgb(92, 92, 92);', msg='下拉框自定义字段隐藏失败')
        self.assertEqual(getfieldltext, 'value0', msg='下拉框自定义字段设置默认值失败')

    # 1130 bug 通过工单模板没的添加按钮添加的字段提交后，二次进入在工单模板中不显示  --修复
    # 20210302 自动化环境bug，模板中字段后面的黑色下拉按钮点击没反应，暂时屏蔽用例  --修复
    def test_021(self):
        """
        添加下拉类型自定义字段，设置可选项后二次检查
        """
        # 填写工单必填值
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        # Base(self.driver).move_to_pagebottom()
        time.sleep(1)
        fieldinfo = TicketTemplateCommon(self.driver).fullSelectFieldCommon()
        # 点击
        fieldsys = fieldinfo.get('sysField')
        fieldname = fieldinfo.get('name')
        # print(fieldsys, fieldname)
        TemplatePage(self.driver).clickfielddown(fieldsys)
        TemplatePage(self.driver).clickfieldoptions(fieldsys)

        # delete_backdrop_showing
        TemplatePage(self.driver).delete_backdrop_showing()
        TemplatePage(self.driver).commit()
        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        # time.sleep(1)

        TemplatePage(self.driver).searchclick(templateInfo.get('name'))
        # 等待提交按钮出现后继续操作
        TemplatePage(self.driver).check_sumbit()
        # time.sleep(5)
        # Base(self.driver).move_to_pagebottom()
        TemplatePage(self.driver).clickfielddown(fieldsys)
        time.sleep(2)
        getfieldoptions = TemplatePage(self.driver).getfieldoptions(fieldsys)
        self.assertEqual(getfieldoptions, 'value0', msg='下拉框自定义字段设置可选选项失败')

    # 2021-06-01增加用例待，因有bug，暂时屏蔽用例  bug 2021053110000026 ---20210616放出
    def test_022(self):
        """
        二次编辑自定义日期时间字段
        """
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        # Base(self.driver).move_to_pagebottom()
        time.sleep(1)
        # 添加自定义的日期/日期时间字段
        TicketTemplateCommon(self.driver).fullSelectFieldCommon02('date')
        time.sleep(5)
        TicketTemplateCommon(self.driver).fullSelectFieldCommon02('datetime')

        # date选择今日日期
        time.sleep(3)
        TemplatePage(self.driver).chose_data(0)
        # datetime选择日期时间
        TemplatePage(self.driver).chose_datetime(1, '2020-02-01 00:00:00')

        TemplatePage(self.driver).commit()
        time.sleep(5)

        name = templateInfo['name']
        TemplatePage(self.driver).search(name)
        time.sleep(5)
        # print("当前模板:"+name)
        TemplatePage(self.driver).clicksearchresult()
        # Base(self.driver).move_to_pagebottom()

        # 编辑
        # date选择日期-点开了日期控件，日期还是选择今天a
        TemplatePage(self.driver).chose_data(0)
        # datetime选择日期时间
        TemplatePage(self.driver).chose_datetime(1, '2021-02-01 00:00:00')
        # 提交
        TemplatePage(self.driver).commit()
        # 搜索搜索进去页面
        time.sleep(5)
        name = templateInfo['name']
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        # Base(self.driver).move_to_pagebottom()

        # 断言默认值是否正确
        data1 = TemplatePage(self.driver).get_data(0)
        datatime = TemplatePage(self.driver).get_data(1)
        today = time.strftime('%Y-%m-%d', time.localtime())
        # print(today, '今天')
        self.assertEqual(data1, today , msg='编辑日期字段，显示错误')
        self.assertEqual(datatime, '2021-02-01 00:00:00', msg='编辑日期字段，显示错误')

    #  2021-06-01增加用例待，因有bug，暂时屏蔽用例  bug 2021053110000035  ---20210616放出
    def test_023(self):
        """
        二次编辑自定义的复选字段
        """
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        # Base(self.driver).move_to_pagebottom()
        time.sleep(1)
        # 添加自定义的复选字段

        checkboxinfo = TicketTemplateCommon(self.driver).fullSelectFieldCommon02('checkbox')

        # 复选选择2个项
        TicketTemplateCommon(self.driver).chose_checkbox(0)
        TicketTemplateCommon(self.driver).chose_checkbox(1)
        TemplatePage(self.driver).commit()

        time.sleep(7)
        name = templateInfo['name']
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        # Base(self.driver).move_to_pagebottom()
        time.sleep(2)
        # 编辑复选字段,取消一个项
        # 定位到添加字段的位置
        TicketTemplateCommon(self.driver).move_to_addfield()
        TicketTemplateCommon(self.driver).chose_checkbox(1)

        # 提交
        TemplatePage(self.driver).commit()
        # 搜索搜索进去页面
        time.sleep(7)
        name = templateInfo['name']
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        # Base(self.driver).move_to_pagebottom()
        TicketTemplateCommon(self.driver).move_to_addfield()
        time.sleep(2)

        # 取数据断言
        checkboxnum = TemplatePage(self.driver).checkboxnum()
        self.assertEqual(checkboxnum, 1, msg='自定义复选框字段，修复默认值失败')

    def test_024(self):
        """
            检查工单模板中是否显示字段“工单转派规则
        """
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        # Base(self.driver).move_to_pagebottom()
        TemplatePage(self.driver).choseField("工单转派规则", "TransferRuleID")

        TemplatePage(self.driver).commit()
        # 搜索搜索进去页面
        time.sleep(5)
        name = templateInfo['name']
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        # Base(self.driver).move_to_pagebottom()
        time.sleep(2)
        TransferRule = TemplatePage(self.driver).check_TransferRule()
        self.assertEqual(TransferRule, 1, msg='错误：工单转派规则字段未在工单模板中显示')

    @unittest2.expectedFailure
    def test_025(self):
        """
            模板主题提示校验
        """
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        time.sleep(3)
        # Base(self.driver).move_to_pagebottom()
        # 点击主题黑色小三角

        TemplatePage(self.driver).down_fieldssubject()
        # 选择主题说明提示在目标栏下
        TemplatePage(self.driver).subject_explain_type(0)
        TemplatePage(self.driver).subject_explain_content("这是显示在目标栏下方的说明")
        TemplatePage(self.driver).commit()
        # 搜索搜索进去页面
        time.sleep(5)
        name = templateInfo['name']
        print(name)
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        time.sleep(5)
        # Base(self.driver).move_to_pagebottom()
        time.sleep(2)
        # 点击展开
        TemplatePage(self.driver).down_fieldssubject()
        time.sleep(5)
        # 取值断言
        subject_explain_type = TemplatePage(self.driver).get_subject_explain_type()
        subject_explain_content = TemplatePage(self.driver).get_subject_explain_content()
        self.assertEqual(subject_explain_type, '提示在目标栏下方',msg='主题说明提示类型显示错误')
        self.assertEqual(subject_explain_content, '这是显示在目标栏下方的说明', msg='主题说明提示内容显示错误')

        # 变更一次类型，同时修改说明内容
        TemplatePage(self.driver).subject_explain_type(2)
        TemplatePage(self.driver).subject_explain_content("这是显示在目标栏中的提示")
        TemplatePage(self.driver).commit()
        # 搜索搜索进去页面
        time.sleep(5)
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        time.sleep(5)
        # Base(self.driver).move_to_pagebottom()
        time.sleep(2)
        TemplatePage(self.driver).down_fieldssubject()
        time.sleep(5)
        # 取值断言
        subject_explain_type = TemplatePage(self.driver).get_subject_explain_type()
        subject_explain_content = TemplatePage(self.driver).get_subject_explain_content()
        self.assertEqual(subject_explain_type, '提示在目标栏中', msg='主题说明提示类型显示错误')
        self.assertEqual(subject_explain_content, '这是显示在目标栏中的提示', msg='主题说明提示内容显示错误')

        # 再次变更类型，同时删除说明内容
        TemplatePage(self.driver).subject_explain_type(1)
        TemplatePage(self.driver).subject_explain_content_clear()
        TemplatePage(self.driver).commit()
        # 搜索搜索进去页面
        time.sleep(10)
        TemplatePage(self.driver).search(name)
        TemplatePage(self.driver).clicksearchresult()
        time.sleep(5)
        # Base(self.driver).move_to_pagebottom()
        time.sleep(2)
        TemplatePage(self.driver).down_fieldssubject()
        # 取值断言
        subject_explain_type = TemplatePage(self.driver).get_subject_explain_type()
        subject_explain_content = TemplatePage(self.driver).get_subject_explain_content()
        self.assertEqual(subject_explain_type, '提示在目标栏中', msg='主题说明提示类型显示错误')
        self.assertEqual(subject_explain_content, '', msg='主题说明提示内容 删除错误')

    def test_026(self):
        """
        固有字段设置为必填-指定处理人，检查提交按钮
        """
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        name = templateInfo.get("name")
        # Base(self.driver).move_to_pagebottom()
        # 点击指定处理人的必填
        TemplatePage(self.driver).required_fields_Owner()

        TemplatePage(self.driver).commit()

        # 表头字段显示则开始搜索
        TemplatePage(self.driver).gettableth()
        TemplatePage(self.driver).search(name)
        template_listinfo = [None, name, '服务人员', '0', '1', '创建工单', '0', '', '有效']
        FiledList01 = TemplatePage(self.driver).getearchresult()
        for i in range(1, 9):
            text_zoom_01 = FiledList01[i].text
            with self.subTest(i=i):
            # print(i, text)
                self.assertEqual(text_zoom_01, template_listinfo[i], msg='错误:指定处理人设置为必填，提交失败')

    # 检查客户用户下拉显示
    def test_027(self):
        """
        检查客户用户下拉是否可以正常搜索用户，并设置用户默认值
        """
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("create")
        # Base(self.driver).slide_bar("DynamicFieldSelect_Search1")
        TemplatePage(self.driver).chose_customer_user("小酷Cool")
        # TemplatePage(self.driver).chose_customer_user("默认客户用户")
        TemplatePage(self.driver).commit()
        # 等待表头元素显示
        TemplatePage(self.driver).wait_tableth()
        # time.sleep(15)
        # 提交

        # 搜索二次进入
        TemplatePage(self.driver).search(templateInfo.get("name"))
        TemplatePage(self.driver).clicksearchresult()
        #
        # Base(self.driver).slide_bar("DynamicFieldSelect_Search1")

        # 取当前客户的值
        get_customer_user = TemplatePage(self.driver).get_customer_user()
        self.assertEqual(get_customer_user, "小酷Cool", msg="错误：客户用户设置默认值失败")
        # self.assertEqual(get_customer_user, "默认客户用户", msg="错误：客户用户设置默认值失败")

    def test_028(self):
        """
            处理模板删除必填字段检查
        """
        # 创建必填的处理模板不提交
        templateInfo = TicketTemplateCommon(self.driver).templateRequiredCommon2("process")
        # 删除必填字段-类型、角色、主题、内容、状态、优先级
        # print(templateInfo)
        TemplatePage(self.driver).delete_type()
        TemplatePage(self.driver).delete_queue()
        TemplatePage(self.driver).delete_subject()
        TemplatePage(self.driver).delete_body()
        TemplatePage(self.driver).delete_state()
        TemplatePage(self.driver).delete_priority()
        # 提交
        time.sleep(3)
        TemplatePage(self.driver).commit()

        # 等待表头元素显示
        TemplatePage(self.driver).wait_tableth()
        # 搜索二次进入
        TemplatePage(self.driver).search(templateInfo.get("name"))
        TemplatePage(self.driver).clicksearchresult()
        template_listinfo2 = ['客户用户', '客户名称', '客户用户资产', '指定处理人', '负责人', '用户是否可见']
        for listheader02 in ['.ant-form-item.ant-row.ng-star-inserted>.ant-form-item-label>label']:
            for i in range(0, 6):
                text = str.replace(self.driver.find_elements_by_css_selector(listheader02)[i].text, ' ', '')
                # print(i, text, template_listinfo2[i])
                with self.subTest(i=i):
                    self.assertEqual(text, template_listinfo2[i], msg='删除字段失败')



















