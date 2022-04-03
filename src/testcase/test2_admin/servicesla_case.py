"""
@author: DT_testing
@file:   servicesla_case.py
@desc:  【服务水平协议】
@step： 001. 路径检查，默认表头检查   SC_SLA_7
       002. 填写必填项增加服务水平协议  SC_SLA_2 、SC_SLA_3 、SC_SLA_15
       003. 返回按钮检查，搜索不存在的服务协议检查   SC_SLA_13 SC_SLA_14
       004. 不修改任何值直接提交，编辑必填项检查  SC_SLA_20
       005. 服务水平协议名称输入空格检验  SC_SLA_17
       006. 服务水平协议重名检验   SC_SLA_18
       007. 模糊查询 列表界面过滤功能检验--模糊查询  SC_SLA_4  SC_SLA_6
       008. 添加服务协议后下一步点击完成   SC_SLA_51
       009. 添加服务协议后下一步点击完成并再添加一条  SC_SLA_52
       010. 添加服务协议后下一步点击上一步，再点击返回列表   SC_SLA_53
       011. 指标质量管理点击取消按钮 指标质量管理点击×关闭弹窗  不填写必填项查看提交按钮显示 ，指标度量管理表头检查
        SC_SLA_37 SC_SLA_38 SC_SLA_39  SC_SLA_40
       012. 填写必填后查看添加指标数据  SC_SLA_41
       013. 修改必填项         SC_SLA_41-1
       014. 填写全填添加指标数据   SC_SLA_42
       015. 修改指标非必填项         SC_SLA_42-1
       016. 指标字段检验输入类型 重名检验 空格检验；指标名称重名校验 输入空格检验  SC_SLA_43 SC_SLA_44   SC_SLA_47  SC_SLA_46
       017. 检查指标度量名称必填、指标时长必填  SC_SLA_60  SC_SLA_61
       018. 必填创建指标  查看指标详情   SC_SLA_56
       019. 添加通知阈值 删除通知阈值 修改通知阈值   SC_SLA_62、SC_SLA_63、SC_SLA_64  SC_SLA_54
       020. 触发开始计时条件选择多个、触发停止计时条件选择多个  SC_SLA_49  SC_SLA_50



"""
import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest2
from common.base import Base
from src.page.agent.servicesla_page import ServiceSlaPage
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.pagecommon.servicesla_common import  ServiceSlaCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from src.page.pagecommon.get_time_common import GetTimeCommon
import random

class ServiceSla(BaseCaseUser, Base):


    @Base.screenshot_about_case
    def test_001_title(self):
        EntranceAgentPage(self.driver).enter_sla()
        # 从主页进入该模块费时较长，故加强制等待避免取到主页的值
        time.sleep(3)
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
        time.sleep(3)
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))

        brosertitle = Base(self.driver).get_title()
        tabtitle = ServiceSlaPage(self.driver).gettabtitle()
        bar = ServiceSlaPage(self.driver).getbar()
        # print(bar)
        tablelist = ['服务水平协议', '工作时间管理', '备注', '有效性', '修改时间', '创建时间']
        self.assertEqual(brosertitle, '服务水平协议', msg='错误：浏览器标题显示错误')
        self.assertEqual(tabtitle, '服务水平协议', msg='错误：页面内tab标题显示错误')
        self.assertEqual(bar, '/ 系统管理 / 服务水平协议', msg='错误：页面内tab标题显示错误')
        tablehead = ServiceSlaPage(self.driver).gettablehead()

        for i in range(0, 6):
            textinfo = tablehead[i].text
            # print(textinfo)
            self.assertEqual(textinfo, tablelist[i], msg='列表表头展示字段显示错误')

    @Base.screenshot_about_case
    def test_002_addrequired(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
        time.sleep(3)
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
        tableinfo = ServiceSlaPage(self.driver).getserchresult()
        tablelist = [slainfo.get('slaname'), '5*8', '', '有效']
        for i in range(0, 4):
            textinfo = tableinfo[i].text
            self.assertEqual(textinfo, tablelist[i], msg='填写必填添加SLA列表数据显示错误')

    @Base.screenshot_about_case
    # 0922备注，28版本遗留问题，协议搜索失效
    def test_003_backlist(self):
        EntranceAgentPage(self.driver).enter_sla()
        ServiceSlaPage(self.driver).clickaddsla()
        ServiceSlaPage(self.driver).clickslabacklist()
        ServiceSlaPage(self.driver).inputserch('祥龙十八章')
        # 取搜索结果
        emptytext = ServiceSlaPage(self.driver).getserchempty()
        self.assertEqual(emptytext, '暂无数据', msg='添加sla返回列表后搜索不存在的数据报错')
        #self.assertEqual(emptytext, '这里空空如也, 跟我的钱包一样', msg='添加sla返回列表后搜索不存在的数据报错')

    # 0818bug 进入编辑页面，提交按钮不可触发  0820修改恢复
    @Base.screenshot_about_case
    def test_004_editresla(self):
        """
            不修改任何值直接提交，编辑必填项检查  SC_SLA_20
        """
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
        newslaname = slainfo.get('slaname') + 'new'
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
        ServiceSlaPage(self.driver).clickserchresult()
        time.sleep(3)
        # 修改必填值提交
        ServiceSlaPage(self.driver).inputslaname(newslaname)
        ServiceSlaPage(self.driver).clickslainvalid()
        ServiceSlaPage(self.driver).clickslasubmit()
        time.sleep(3)
        # 二次搜索打开，啥也不写直接提交
        ServiceSlaPage(self.driver).inputserch(newslaname)
        ServiceSlaPage(self.driver).clickserchresult()
        ServiceSlaPage(self.driver).clickslasubmit()

        # 再搜索一次查表列数据
        time.sleep(5)
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
        rer = ServiceSlaPage(self.driver).getserchresult()
        tablelist = [newslaname, '5*8', '', '无效']
        for i in range(0, 4):
            textinfo = rer[i].text
            self.assertEqual(textinfo, tablelist[i], msg='编辑必填项后SLA列表数据显示错误')

    # 空格校验，重名校验  bug 0819  0820 修改恢复
    def test_005_checkname(self):
        EntranceAgentPage(self.driver).enter_sla()
        ServiceSlaPage(self.driver).clickaddsla()
        ServiceSlaPage(self.driver).inputslaname('  ')
        nextstyle = ServiceSlaPage(self.driver).getnextstyle()
        sunmitbackstyle = ServiceSlaPage(self.driver).getsunmitbackstyle()
        self.assertEqual(nextstyle, 'true', msg='错误：协议名为空格时下一步按钮可触发')
        self.assertEqual(sunmitbackstyle, 'true', msg='错误：协议名为空格时提交返回按钮可触发')

    # 重名校验
    def test_006_checkname2(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon()
        newslaname = slainfo.get('slaname')
        ServiceSlaPage(self.driver).clickaddsla()
        ServiceSlaPage(self.driver).inputslaname(newslaname)
        time.sleep(2)
        namemessage = ServiceSlaPage(self.driver).getnamemessage()
        self.assertEqual(namemessage,'该名称已存在，请更换其他名称！', msg='错误：服务协议重名验证通过')

    # 模糊查询服务协议, 特殊字符查询协议
    # +号存在bug，加号添加显示为空格
    def test_007(self):
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str(strnumber+'TicketFreeText@&%$' + strnumber)
        EntranceAgentPage(self.driver).enter_relust('服务水平协议')
        EntranceAgentPage(self.driver).enter_sla()
        ServiceSlaPage(self.driver).clickaddsla()
        ServiceSlaPage(self.driver).inputslaname(name)
        ServiceSlaPage(self.driver).clickslavalid()
        ServiceSlaPage(self.driver).clickslasubmit()
        num1 = 0
        num3 = 0

        ServiceSlaPage(self.driver).inputserch(strnumber+'Ticket')
        leftslaname = ServiceSlaPage(self.driver).getleftslaname()
        for i in range(0, len(leftslaname)):
            listinfo = leftslaname[i].text
            if listinfo == name:
                num1 = num1+1


        ServiceSlaPage(self.driver).inputserch('@&%$'+ strnumber)
        leftslaname = ServiceSlaPage(self.driver).getleftslaname()
        for i in range(0, len(leftslaname)):
            listinfo = leftslaname[i].text
            if listinfo == name:
                num3 = num3+1

        self.assertEqual(num1, 1, msg='错误：模糊搜索前段数据未查到匹配数据')
        self.assertEqual(num3, 1, msg='错误：模糊搜索后段数据，特殊字符未查到匹配数据')

    # 添加服务协议下一步-完成
    def test_008(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clickcomplite()
        time.sleep(5)
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
        tableinfo = ServiceSlaPage(self.driver).getserchresult()
        tablelist = [slainfo.get('slaname'), '5*8', '', '有效']
        for i in range(0, 4):
            textinfo = tableinfo[i].text
            self.assertEqual(textinfo, tablelist[i], msg='错误：添加服务协议下一步后点击完成列表数据错误')

    # 添加服务协议下一步-完成并再添加一条
    def test_009(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clickcompliteadd()
        time.sleep(3)
        # 再添加一条数据
        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name2 = str('name' + strnumber)
        ServiceSlaPage(self.driver).inputslaname(name2)
        ServiceSlaPage(self.driver).clickslavalid()
        ServiceSlaPage(self.driver).clickslasubmit()
        time.sleep(3)
        # 搜索两次检查数据
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
        tableinfo = ServiceSlaPage(self.driver).getserchresult()
        tablelist = [slainfo.get('slaname'), '5*8', '', '有效']
        for i in range(0, 4):
            textinfo = tableinfo[i].text
            self.assertEqual(textinfo, tablelist[i], msg='错误1：添加服务协议下一步后点击再添加一条返回列表数据显示错误')
        time.sleep(2)
        ServiceSlaPage(self.driver).inputserch(name2)
        rer2 = ServiceSlaPage(self.driver).getserchresult()
        tablelist = [name2, '5*8', '', '有效']
        for i in range(0, 4):
            textinfo2 = rer2[i].text
            self.assertEqual(textinfo2, tablelist[i], msg='错误1：添加服务协议下一步后点击再添加一条返回列表数据显示错误')

    # 添加服务协议下一步-上一步；下一步-返回列表
    def test_010(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clickBack2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clickbastlist2()
        time.sleep(3)
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
        tableinfo = ServiceSlaPage(self.driver).getserchresult()
        tablelist = [slainfo.get('slaname'), '5*8', '', '有效']
        for i in range(0, 4):
            textinfo = tableinfo[i].text
            self.assertEqual(textinfo, tablelist[i], msg='错误：添加服务协议下一步，上一步，再返回列表，列表数据显示错误')

    # 指标度量管理×关闭弹窗，取消关闭弹窗 ，指标度量管理页面列表表头展示检查
    def test_011(self):
        ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicktarget()
        # 必须添加强制等待
        time.sleep(2)

        # 取表头数据断言  空系统无表头判断
        # targettable = ServiceSlaPage(self.driver).gettargettablehead()
        # print(targettable)
        # targettableinfo = ['指标字段', '指标度量名称', '计时类型', '有效性', '操作']
        # for i in range(0, 5):
        #
        #     targettableth = targettable[i].text
        #     # print(i, targettableth, targettableinfo[i])
        #     self.assertEqual(targettableth, targettableinfo[i], msg='错误：指标度量管理列表表头显示错误')

        ServiceSlaPage(self.driver).closetar()
        time.sleep(2)
        enabled1 = ServiceSlaPage(self.driver).bastlist2enabled()
        self.assertEqual(enabled1, True, '错误：指标度量管理弹窗点击右上角×关闭失败')
        # 必须添加强制等待
        time.sleep(2)
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(2)
        submitstyle = ServiceSlaPage(self.driver).getsubmittar_style()
        self.assertEqual(submitstyle, 'true', '错误：指标度量管理不填写必填提交按钮可触发')

        ServiceSlaPage(self.driver).targetcancle()
        enabled2= ServiceSlaPage(self.driver).bastlist2enabled()
        self.assertEqual(enabled2, True, '错误：指标度量管理弹窗点击取消失败')


        time.sleep(2)
        # ServiceSlaPage(self.driver).closetar()

    # 填写必填增加指标
    def test_012(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(2)
        targetinfo = ServiceSlaCommon(self.driver).targetrequiredcommon()
        ServiceSlaPage(self.driver).clicksubmittar()
        # print(targetinfo.get('name'))
        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))
        # time.sleep(1)
        targettext = [targetinfo.get('field'), targetinfo.get('name'), '累计', '有效']
        # 取列表的值
        targetsearchresult = ServiceSlaPage(self.driver).getsearchtarget()
        for i in range(0, 4):
            resulit = targetsearchresult[i].text
            self.assertEqual(resulit, targettext[i], msg='错误：添加指标必填项失败，列表数据错误')

        time.sleep(2)
        ServiceSlaPage(self.driver).closetar()

    # 编辑指标必填
    def test_013(self):

        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        targetinfo = ServiceSlaCommon(self.driver).targetrequiredcommon()
        newname = 'new' + targetinfo.get('name')

        ServiceSlaPage(self.driver).clicksubmittar()
        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))

        # 点击编辑按钮，进入编辑页面
        ServiceSlaPage(self.driver).targetedit()

        time.sleep(1)
        # edittargetname
        ServiceSlaPage(self.driver).edittargetname(targetinfo.get('name'), newname)
        # ServiceSlaPage(self.driver).inputtargetname(newname)
        ServiceSlaPage(self.driver).clickreset()
        ServiceSlaPage(self.driver).targetinvalid()
        ServiceSlaPage(self.driver).clicksubmittar()

        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))
        targettext = [targetinfo.get('field'), newname, '重置', '无效']
        # 取列表的值
        targetsearchresult = ServiceSlaPage(self.driver).getsearchtarget()
        for i in range(0, 4):
            resulit = targetsearchresult[i].text
            self.assertEqual(resulit, targettext[i], msg='错误：编辑指标必填项失败，列表数据错误')

        time.sleep(2)
        ServiceSlaPage(self.driver).closetar()

    # 全填创建指标
    def test_014(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(2)
        targetinfo = ServiceSlaCommon(self.driver).targetfullcommon()
        ServiceSlaPage(self.driver).clicksubmittar()

        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))
        # 点击编辑按钮，进入编辑页面
        ServiceSlaPage(self.driver).targetedit()
        # 取开始出发事件和结束
        eventelemt = '.flex-start.indicator-events>span:nth-child(1)'
        events = ['TicketCreate', 'TicketDelete']
        for i in range(0, 2):
            getevents = self.driver.find_elements_by_css_selector(eventelemt)[i].text
            self.assertEqual(getevents, events[i], msg='错误：全填创建指标触发事件显示错误')

        ServiceSlaPage(self.driver).clicksubmittar()
        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))
        targettext = [targetinfo.get('field'), targetinfo.get('name'), '累计', '有效']
        # 取列表的值
        targetsearchresult = ServiceSlaPage(self.driver).getsearchtarget()
        for i in range(0, 4):
            resulit = targetsearchresult[i].text
            self.assertEqual(resulit, targettext[i], msg='错误：全填创建指标，列表数据错误')

        time.sleep(2)
        ServiceSlaPage(self.driver).closetar()

    # 编辑非必填项
    def test_015(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(10)
        targetinfo = ServiceSlaCommon(self.driver).targetfullcommon()
        ServiceSlaPage(self.driver).clicksubmittar()
        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))
        # 点击编辑按钮，进入编辑页面
        ServiceSlaPage(self.driver).targetedit()
        # 修改触发事件  clickdelevent
        ServiceSlaPage(self.driver).clickdelevent()
        ServiceSlaPage(self.driver).clickdelevent()
        ServiceSlaPage(self.driver).startcondition('NotificationAddNote')
        ServiceSlaPage(self.driver).endcondition('NotificationEscalation')

        # 提交，再次进入编辑页面
        ServiceSlaPage(self.driver).clicksubmittar()
        time.sleep(5)
        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))
        # 点击编辑按钮，进入编辑页面
        ServiceSlaPage(self.driver).targetedit()
        # 取开始出发事件和结束
        eventelemt = '.flex-start.indicator-events>span:nth-child(1)'
        events = ['NotificationAddNote', 'NotificationEscalation']
        for i in range(0, 2):
            getevents = self.driver.find_elements_by_css_selector(eventelemt)[i].text
            self.assertEqual(getevents, events[i], msg='错误：全填创建指标触发事件显示错误')

        ServiceSlaPage(self.driver).clicksubmittar()
        ServiceSlaPage(self.driver).searchtarget(targetinfo.get('name'))
        targettext = [targetinfo.get('field'), targetinfo.get('name'), '累计', '有效']
        # 取列表的值
        targetsearchresult = ServiceSlaPage(self.driver).getsearchtarget()
        for i in range(0, 4):
            resulit = targetsearchresult[i].text
            self.assertEqual(resulit, targettext[i], msg='错误：全填创建指标，列表数据错误')

        time.sleep(2)
        ServiceSlaPage(self.driver).closetar()

    # 指标字段校验 指标度量名称校验  指标字段输入类型校验
    def test_016(self):
        ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(2)
        targetinfo = ServiceSlaCommon(self.driver).targetrequiredcommon()
        ServiceSlaPage(self.driver).clicksubmittar()
        ServiceSlaPage(self.driver).clickaddtarget()
        ServiceSlaPage(self.driver).inputtargetfield(targetinfo.get('field'))
        ServiceSlaPage(self.driver).inputtargetname(targetinfo.get('name'))
        tarfieldtip = ServiceSlaPage(self.driver).gettarfieldtip()
        tarnametip = ServiceSlaPage(self.driver).gettarnametip()
        self.assertEqual(tarfieldtip, '当前字段已存在或是系统字段!', msg='错误：指标字段重名未提示')
        self.assertEqual(tarnametip, '当前字段已存在或是系统字段!', msg='错误：指标名称重名未提示')

        time.sleep(1)
        ServiceSlaPage(self.driver).inputtargetfield('这是中文输入')
        tarfieldtip2 = ServiceSlaPage(self.driver).gettarfieldtip()
        self.assertEqual(tarfieldtip2, '您当前输入值不符合要求，请检查', msg='错误：指标字段中文输入允许通过')

        time.sleep(1)
        ServiceSlaPage(self.driver).inputtargetfield('0987654321787')
        tarfieldtip3 = ServiceSlaPage(self.driver).gettarfieldtip()
        self.assertEqual(tarfieldtip3, '您当前输入值不符合要求，请检查', msg='错误：指标字段纯数字输入允许通过')

        time.sleep(1)
        ServiceSlaPage(self.driver).inputtargetfield('%##$#@+&*')
        tarfieldtip4 = ServiceSlaPage(self.driver).gettarfieldtip()
        self.assertEqual(tarfieldtip4, '您当前输入值不符合要求，请检查', msg='错误：指标字段特殊字符输入允许通过')

        time.sleep(1)
        ServiceSlaPage(self.driver).inputtargetfield('   ')
        tarfieldtip5 = ServiceSlaPage(self.driver).gettarfieldtip()
        self.assertEqual(tarfieldtip5, '数据格式错误,请重新输入!', msg='错误：指标字段空格输入允许通过')

        time.sleep(1)
        ServiceSlaPage(self.driver).inputtargetname('   ')
        tarnametip2 = ServiceSlaPage(self.driver).gettarnametip()
        self.assertEqual(tarnametip2, '数据格式错误,请重新输入!', msg='错误：指标度量名称空格输入允许通过')

        time.sleep(2)
        ServiceSlaPage(self.driver).closetar()

    # 检查指标度量名称必填、指标时长必填
    def test_017(self):
        ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicknewtarget()
        time.sleep(2)
        # 检查完成 完成添加
        complitestyle = ServiceSlaPage(self.driver).getcomplitestyle()
        compliteaddstyle = ServiceSlaPage(self.driver).getcompliteaddstyle()
        self.assertEqual(complitestyle, 'true', msg='错误：创建不填写任何值完成按钮可触发')
        self.assertEqual(compliteaddstyle, 'true', msg='错误：创建不填写任何值完成并提交按钮可触发')

        # 输入时长
        ServiceSlaPage(self.driver).inputtime('10')
        complitestyle = ServiceSlaPage(self.driver).getcomplitestyle()
        compliteaddstyle = ServiceSlaPage(self.driver).getcompliteaddstyle()
        self.assertEqual(complitestyle, 'true', msg='错误：创建指标仅输入时长完成按钮可触发')
        self.assertEqual(compliteaddstyle, 'true', msg='错误：创建指标进输入时长完成并提交按钮可触发')

    # 必填创建指标  查看指标详情
    def test_018(self):
        # EntranceAgentPage(self.driver).enter_sla()
        # 创建一个协议
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        time.sleep(3)
        ServiceSlaPage(self.driver).clickslanext()

        # 创建一个指标
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(1)
        targetinfo = ServiceSlaCommon(self.driver).targetfullcommon()
        ServiceSlaPage(self.driver).clicksubmittar()
        # 点击"×"关闭
        ServiceSlaPage(self.driver).closetar()


        ServiceSlaPage(self.driver).clicknewtarget()
        ServiceSlaPage(self.driver).inputtime('10')
        ServiceSlaPage(self.driver).chosetargetname(targetinfo.get('name'))
        time.sleep(3)
        tarlefttitle = ServiceSlaPage(self.driver).gettarlefttitle()
        # 断言一次左上角标题
        self.assertEqual(tarlefttitle, targetinfo.get('name')+'  指标时长 : 10 ( 分钟 )  计时类型 : 累计 ',
                         msg='错误：选择指标后左上角显示错误')

        # 查看详情
        ServiceSlaPage(self.driver).clickdetails()
        tarfield = ServiceSlaPage(self.driver).gettarfield()
        tarvalid = ServiceSlaPage(self.driver).getvalid()
        tarname = ServiceSlaPage(self.driver).gettarname()
        tartimetype = ServiceSlaPage(self.driver).gettimetype_add()
        self.assertEqual(tarfield, targetinfo.get('field'), msg='错误：指标详情指标字段显示错误')
        self.assertEqual(tarname, targetinfo.get('name'), msg='错误：指标详情度量名称显示错误')
        self.assertEqual(tarvalid, 'valid', msg='错误：指标详情有效性显示错误')
        self.assertEqual(tartimetype, 'ant-radio-wrapper ant-radio-wrapper-checked ng-star-inserted',
                         msg='错误：指标详情计时类型显示错误')
        eventelemt = '.flex-start.indicator-events>span:nth-child(1)'
        events = ['TicketCreate', 'TicketDelete']
        for i in range(0, 2):
            getevents = self.driver.find_elements_by_css_selector(eventelemt)[i].text
            self.assertEqual(getevents, events[i], msg='错误：全填创建指标触发事件显示错误')
        # 点击取消
        ServiceSlaPage(self.driver).targetcancle()

        # 点击完成，二次进入检查指标信息
        ServiceSlaPage(self.driver).clickcomplite()
        time.sleep(8)
        # 二次进入
        ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
        time.sleep(5)
        ServiceSlaPage(self.driver).clickserchresult()
        ServiceSlaPage(self.driver).clickslanext()
        # 取标题判断
        tarlefttitle = ServiceSlaPage(self.driver).gettarlefttitle()
        # print(tarlefttitle)
        self.assertEqual(tarlefttitle, targetinfo.get('name') + '  指标时长 : 10 ( 分钟 )  计时类型 : 累计 ',
                         msg='错误：选择指标后左上角显示错误')

    # 添加通知阈值 删除通知阈值 修改通知阈值  bug 2020120110000044
    # def test_019(self):
    #     EntranceAgentPage(self.driver).enter_sla()
    #     # # 进入
    #     # ServiceSlaPage(self.driver).inputserch('1112')
    #     # ServiceSlaPage(self.driver).clickserchresult()
    #     # ServiceSlaPage(self.driver).clickslanext()
    #
    #     # 创建一个协议
    #     slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
    #     ServiceSlaPage(self.driver).clickslanext()
    #
    #     # 创建一个指标
    #     ServiceSlaPage(self.driver).clicktarget()
    #     ServiceSlaPage(self.driver).clickaddtarget()
    #     time.sleep(1)
    #     targetinfo = ServiceSlaCommon(self.driver).targetfullcommon()
    #     ServiceSlaPage(self.driver).clicksubmittar()
    #     # 点击"×"关闭
    #     ServiceSlaPage(self.driver).closetar()
    #
    #     ServiceSlaPage(self.driver).clicknewtarget()
    #     ServiceSlaPage(self.driver).inputtime('10')
    #     ServiceSlaPage(self.driver).chosetargetname(targetinfo.get('name'))
    #     time.sleep(3)
    #
    #     # 添加阈值，并修改通知阈值
    #     ServiceSlaPage(self.driver).addthreshold()
    #     # ServiceSlaPage(self.driver).delthreshold()
    #     ServiceSlaPage(self.driver).inputthreshold1('10')
    #     # ServiceSlaPage(self.driver).inputthreshold2('90')
    #     # ServiceSlaPage(self.driver).inputthreshold3('90')
    #     ServiceSlaPage(self.driver).inputthreshold5('180')
    #
    #     # 上一步-下一步
    #     ServiceSlaPage(self.driver).clickBack2()
    #     ServiceSlaPage(self.driver).clickslanext()
    #
    #     time.sleep(3)
    #     thresholdinfo01 = ['10', '80', '100', '150', '180']
    #     getthreshold = ServiceSlaPage(self.driver).getthreshold()
    #     for i in range(0, len(getthreshold)):
    #         thresholdinfo = getthreshold[i].get_attribute('value')
    #         # print(thresholdinfo,thresholdinfo01[i])
    #         self.assertEqual(thresholdinfo, thresholdinfo01[i], msg='错误：阈值百分比显示错误')
    #
    #     # 删除通知阈值 ，修改通知阈值
    #     ServiceSlaPage(self.driver).delthreshold()
    #     ServiceSlaPage(self.driver).delthreshold()
    #     ServiceSlaPage(self.driver).inputthreshold1('30')
    #     ServiceSlaPage(self.driver).inputthreshold2('50')
    #     ServiceSlaPage(self.driver).inputthreshold3('70')
    #
    #     # 点击完成
    #     ServiceSlaPage(self.driver).clickcomplite()
    #     time.sleep(5)
    #     ServiceSlaPage(self.driver).inputserch(slainfo.get('slaname'))
    #     ServiceSlaPage(self.driver).clickserchresult()
    #     ServiceSlaPage(self.driver).clickslanext()
    #
    #     thresholdinfo01 = ['30', '50', '70']
    #     getthreshold = ServiceSlaPage(self.driver).getthreshold()
    #     for i in range(0, len(getthreshold)):
    #         thresholdinfo = getthreshold[i].get_attribute('value')
    #         self.assertEqual(thresholdinfo, thresholdinfo01[i], msg='错误：阈值百分比显示错误')
    #
    #     tarlefttitle = ServiceSlaPage(self.driver).gettarlefttitle()
    #     # 断言一次左上角标题
    #     self.assertEqual(tarlefttitle, targetinfo.get('name') + ' 指标时长 : 10 ( 分钟 )  计时类型 : 累计 ',
    #                      msg='错误：选择指标后左上角显示错误')

    # 触发开始计时条件选择多个、触发停止计时条件选择多个
    def test_020(self):
        slainfo = ServiceSlaCommon(self.driver).Serviceslarequiredcommon2()
        ServiceSlaPage(self.driver).clickslanext()
        ServiceSlaPage(self.driver).clicktarget()
        ServiceSlaPage(self.driver).clickaddtarget()
        time.sleep(5)


        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = str('多触发事件' + strnumber)
        field = str('field' + strnumber)
        ServiceSlaPage(self.driver).inputtargetfield(field)
        ServiceSlaPage(self.driver).inputtargetname(name)
        ServiceSlaPage(self.driver).clickaddup()

        ServiceSlaPage(self.driver).startcondition('TicketCreate')
        time.sleep(1)
        ServiceSlaPage(self.driver).startcondition('TicketCustomerOwnerUpdate')
        time.sleep(1)
        ServiceSlaPage(self.driver).startcondition('TicketCustomerUpdate')
        time.sleep(1)
        ServiceSlaPage(self.driver).endcondition('TicketDelete')
        time.sleep(1)
        ServiceSlaPage(self.driver).endcondition('NotificationAddNote')
        time.sleep(1)
        ServiceSlaPage(self.driver).endcondition('NotificationFollowUpInternal')
        ServiceSlaPage(self.driver).targetvalid()


        ServiceSlaPage(self.driver).clicksubmittar()
        # print(targetinfo.get('name'))
        ServiceSlaPage(self.driver).searchtarget(name)
        # time.sleep(1)
        targettext = [field, name, '累计', '有效']
        # 取列表的值
        targetsearchresult = ServiceSlaPage(self.driver).getsearchtarget()
        for i in range(0, 4):
            resulit = targetsearchresult[i].text
            self.assertEqual(resulit, targettext[i], msg='错误：添加指标必填项失败，列表数据错误')

        # 点击编辑进入
        ServiceSlaPage(self.driver).targetedit()
        eventelemt = '.flex-start.indicator-events>span:nth-child(1)'
        events = ['TicketCreate', 'TicketCustomerOwnerUpdate', 'TicketCustomerUpdate', 'TicketDelete',
                  'NotificationAddNote','NotificationFollowUpInternal']
        for i in range(0, 6):
            getevents = self.driver.find_elements_by_css_selector(eventelemt)[i].text
            self.assertEqual(getevents, events[i], msg='错误：全填创建指标触发事件显示错误')

        ServiceSlaPage(self.driver).closetar()
