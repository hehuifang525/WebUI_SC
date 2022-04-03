"""
@author: DT_testing
@file:   entrance_agent_page.py
@desc:  【进入各个入口】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base import Base


class EntranceAgentPage(Base):
    '''
    系统左侧方及隐藏的所有按钮
    '''
    # 主菜单menu
    menu_loc = (By.ID, 'submenu')
    # 合起菜单
    closemenu_loc = (By.CSS_SELECTOR, '[class="subClose"]')

    # my tickets
    mytickets_loc=(By.CSS_SELECTOR, '.subNavigation [title="我的工单"]')

    # 组--现在该名称为“角色”
    role_loc=(By.CSS_SELECTOR, '.subNavigation [title="角色"]')

    agent_loc=(By.CSS_SELECTOR, '.subNavigation [title="服务人员"]')
    # 字段库
    field_loc=(By.CSS_SELECTOR, '.subNavigation [title="字段库"]')

    # 菜单权限管理
    menuset_loc=(By.CSS_SELECTOR, 'div.subNavigation [title="菜单权限管理"]')
    # # KPI
    # kpi_loc = (By.ID, 'nav-KPIDashboard')
    # 主页
    dashboard_loc=(By.CSS_SELECTOR, '[title="主页"]')

    # 客户
    # 客户用户
    customer_user_loc=(By.CSS_SELECTOR, '.subNavigation [title="客户用户管理"]')

    # 新建工单
    ticketcreate_loc = (By.CSS_SELECTOR, '[title="TESTBED_测试流程"]')
    ticketcreate2_loc = (By.CSS_SELECTOR, '[title="不同角色使用"]')

    # 工单搜索
    ticketsearch_loc = (By.CSS_SELECTOR, '.subNavigation [title="工单搜索"]')

    # 服务水平协议
    servicesla_loc = (By.CSS_SELECTOR, '.subNavigation [title="服务水平协议"]')

    # cmdb配置 概览
    cmdb_configure_loc = (By.CSS_SELECTOR, '.subNavigation [title="CMDB 配置"]')
    cmdb_overview_loc = (By.CSS_SELECTOR, '.subNavigation [title="CMDB 概览"]')

    # 工作时间管理
    slacalendar_loc = (By.CSS_SELECTOR, '.subNavigation [title="工作时间管理"]')
    # 邮件过滤器
    postmasterfilter_loc = (By.CSS_SELECTOR, '.subNavigation [title="邮件过滤器"]')

    # customers_loc = (By.ID, 'nav-Customers')
    # # 值班
    # duty_loc = (By.ID, 'nav-OnDutyCalendar')
    # # 工单
    # ticket_loc = (By.ID, 'nav-Tickets')
    # # 知识库
    # faq_loc = (By.ID, 'nav-FAQ')

    # # AgentRelated_loc = (By.ID, 'nav-KPIDashboard') 服务人员管理
    # # 合同
    # contract_loc = (By.ID, 'nav-Contract')
    # # 资产
    # cmdb_loc = (By.ID, 'nav-CMDB')
    # # 调查
    # survey_loc = (By.ID, 'nav-Satisfactionsurvey')
    # # 报表
    # report_loc = (By.ID, 'nav-Reports')
    #
    # # 系统管理
    # sys_loc = (By.LINK_TEXT, '系统管理')
    # # 系统管理--工单模板
    tickettemplate_loc = (By.CSS_SELECTOR, '.subNavigation [title="工单模板"]')
    district_loc = (By.CSS_SELECTOR, '.subNavigation [title="区域"]')
    # 新建cmdb -网络
    newcmdb_network_loc = (By.CSS_SELECTOR, '[title="网络"]')
    # 工单通知
    notificationevent_loc = (By.CSS_SELECTOR, '.subNavigation [title="工单通知"]')
    # 流程管理
    processmanagement_loc = (By.CSS_SELECTOR, '.subNavigation [title="流程管理"]')
    # 工单分组
    ticketgroup_loc = (By.CSS_SELECTOR,'.subNavigation [title="工单分组"]')
    # 自动任务
    generic_loc =(By.CSS_SELECTOR,'.subNavigation [title="自动任务"]')
    # 会话
    session_loc = (By.CSS_SELECTOR, '.subNavigation [title="会话"]')
    # 知识库类别管理
    faq_loc = (By.CSS_SELECTOR, '.subNavigation [title="知识库类别管理"]')
    # 邮箱
    mailmanagement_loc = (By.CSS_SELECTOR, '.subNavigation [title="邮箱"]')
    # 工单搜索
    search_loc = (By.CSS_SELECTOR, '.subNavigation [title="工单搜索"]')
    # 知识库概览
    faq_overview_loc = (By.CSS_SELECTOR, '.subNavigation [title="知识库概览"]')
    # 服务
    service_loc = (By.CSS_SELECTOR, '.subNavigation [title="服务"]')
    # 统计管理
    stats_loc = (By.CSS_SELECTOR, '.subNavigation [title="统计管理"]')
    # 统计组合管理
    statscombine_loc = (By.CSS_SELECTOR, '.subNavigation [title="统计组合管理"]')
    # 内容模板
    contenttemplate_loc = (By.CSS_SELECTOR, '.subNavigation [title="内容模板"]')
    # 管理员通知
    messagecool_loc = (By.CSS_SELECTOR, '.subNavigation [title="管理员通知"]')
    # 服务岛
    island_loc = (By.CSS_SELECTOR, '.subNavigation [title="服务岛"]')
    # 软件包管理
    packagemanager_loc = (By.CSS_SELECTOR, '.subNavigation [title="软件包管理"]')

    # 字段影响关系
    fieldimpact_loc = (By.CSS_SELECTOR, '.subNavigation [title="自定义字段影响关系"]')

    # 菜单栏面板搜索框
    menu_search_loc = (By.CSS_SELECTOR, '.product-search input')

    # 工作台
    workbench_loc = (By.CSS_SELECTOR,'.subNavigation [title="工作台"]')
    # 工作台管理
    workbenchmanage_loc = (By.CSS_SELECTOR, '.subNavigation [title="工作台管理"]')
    # kpi
    KPI_loc = (By.CSS_SELECTOR, ' [title="KPI DashBorad"]')
    # 通信日志
    communicationlog_loc = (By.CSS_SELECTOR, '.subNavigation [title="通信日志"]')
    # 系统日志
    systemlog_loc = (By.CSS_SELECTOR, '.subNavigation [title="系统日志"]')

    # 公共参数设置
    paramsetting_loc = (By.CSS_SELECTOR, '.subNavigation [title="公共参数设置"]')
    # sql屏幕查询
    selectbox_loc = (By.CSS_SELECTOR, '.subNavigation [title="SQL查询屏幕"]')

    # 偏好设置
    Preferences_loc = (By.ID, 'EditPreferences')
    # 服务台
    cti_loc = (By.CSS_SELECTOR, '.subNavigation [title="服务台"]')

    # 标签管理
    tagmanagement_loc = (By.CSS_SELECTOR, '.subNavigation [title="标签管理"]')
    # 标签规则管理
    tagmanagement_rule_loc = (By.CSS_SELECTOR, '.subNavigation [title="标签规则管理"]')
    # 到期提醒管理
    serviceremind_loc = (By.CSS_SELECTOR, '.subNavigation [title="到期提醒管理"]')
    # 小程序配置管理
    wechat_config_loc = (By.CSS_SELECTOR, '.subNavigation [title="小程序配置管理"]')
    # 值班概览
    duty_loc = (By.CSS_SELECTOR, '.subNavigation [title="值班概览"]')



    # 点击开始菜单按钮
    def openmenu(self):
        self.find_element(self.menu_loc).click()
        time.sleep(2)

    # 点击关闭菜单按钮
    def closemenu(self):
        self.find_element(self.closemenu_loc).click()
        time.sleep(2)



    # 点击菜单---主页
    def enter_home(self):
        self.clickButton(self.menu_loc)
        self.clickButton(self.dashboard_loc)


    # 点击菜单--角色
    def enter_role(self):
        # 0717修改
        # time.sleep(6)
        # try:
        #     submenu_text = self.driver.find_element_by_id('submenu').get_attribute('textContent')
        #     # print(submenu_text)
        #     n = 0
        #     while (submenu_text == '' and n <20):
        #         #print('2')
        #         submenu_text = self.driver.find_element_by_id('submenu').get_attribute('textContent')
        #         n = n+1
        # except Exception as msg:
        #     print('无法获取开始按钮的元素', msg)

        self.clickButton(self.menu_loc)
        # self.find_element(self.menu_loc).click()
        time.sleep(2)
        self.clickButton(self.role_loc)
        # self.find_element(self.agent_loc).click()
        time.sleep(4)
        #
        # self.find_element(self.menu_loc).click()
        # time.sleep(2)
        # self.find_element(self.role_loc).click()
        # time.sleep(4)

    # 点击菜单--服务人员
    def enter_agent(self):
        self.clickButton(self.menu_loc)
        # self.find_element(self.menu_loc).click()
        time.sleep(2)
        self.clickButton(self.agent_loc)
        # self.find_element(self.agent_loc).click()
        time.sleep(4)

    # 进入流程管理processmanagement_loc
    def enter_processmanagement(self):
        self.find_element(self.menu_loc).click()
        time.sleep(2)
        self.find_element(self.processmanagement_loc).click()
        time.sleep(4)

    # 点击菜单--菜单权限管理
    def enter_menuset(self):
        self.find_element(self.menu_loc).click()
        time.sleep(4)
        # self.find_element(self.menuset_loc).click()
        # time.sleep(4)
        element = self.find_element(self.menuset_loc)
        self.driver.execute_script("arguments[0].click();", element)


    # 点击菜单--字段库
    def enter_filed(self):
        # self.find_element(self.menu_loc).click()
        # time.sleep(2)
        # self.find_element(self.field_loc).click()
        # time.sleep(4)

        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.field_loc)
        time.sleep(4)

    # 点击进入菜单--进入客户用户管理
    def enter_customer_user(self):
        self.clickButton(self.menu_loc)
        # self.find_element(self.menu_loc).click()
        time.sleep(2)
        self.clickButton(self.customer_user_loc)
        # self.find_element(self.customer_user_loc).click()
        time.sleep(4)

    # 新建工单：进入工单模板使用页面--使用“TESTBED_测试流程”
    def enter_templateuse(self):
        # 点击“系统管理”
        self.find_element(self.menu_loc).click()
        time.sleep(2)
        # 点击使用“TESTBED_测试流程”
        self.find_element(self.ticketcreate_loc).click()
        time.sleep(4)
    # 流程2：角色--服务人员使用的流程
    def enter_templateuse2(self):
        # 点击“系统管理”
        self.find_element(self.menu_loc).click()
        time.sleep(2)
        # 点击使用“不同角色使用”
        self.find_element(self.ticketcreate2_loc).click()
        time.sleep(4)

    def enter_tickettemplate(self):
        # self.find_element(self.menu_loc).click()
        # time.sleep(2)
        # self.find_element(self.tickettemplate_loc).click()
        # time.sleep(4)

        self.clickButton(self.menu_loc)
        # self.find_element(self.menu_loc).click()
        time.sleep(2)
        self.clickButton(self.tickettemplate_loc)

    # 进入服务水平协议
    def enter_sla(self):
        self.clickButton(self.menu_loc)
        # self.find_element(self.menu_loc).click()
        time.sleep(2)
        self.clickButton(self.servicesla_loc)
        # self.find_element(self.servicesla_loc).click()
        time.sleep(6)

    def enter_district(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.district_loc)
        time.sleep(4)

    # 进入cmdb配置
    def enter_cmdb_configure(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.cmdb_configure_loc)
        time.sleep(4)

    # 进入cmdb概览
    def enter_cmdb_overview(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        # self.find_element(self.menu_search_loc).clear()
        # self.send_keys(self.menu_search_loc, Keys.CONTROL+"A")
        # self.send_keys(self.menu_search_loc, Keys.BACKSPACE)
        self.clickButton(self.cmdb_overview_loc)
        time.sleep(4)

    def enter_newcodb_network(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.newcmdb_network_loc)
        time.sleep(4)

    def enter_slacalendar(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.slacalendar_loc)
        time.sleep(4)

    def enter_postmasterfilter(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.postmasterfilter_loc)
        time.sleep(4)

    def enter_notificationevent(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.notificationevent_loc )
        time.sleep(4)

    def enter_processmanagement(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.processmanagement_loc )
        time.sleep(4)

    # 工单分组
    def enter_ticketgroup(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.ticketgroup_loc)
        time.sleep(4)

    # 自动任务
    def enter_generic(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.generic_loc )
        time.sleep(4)

    # 会话
    def enter_session(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.session_loc )
        time.sleep(4)

    # 知识库类别管理
    def enter_faq(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.faq_loc )
        time.sleep(4)

    # 邮箱
    def enter_mailmanagement(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.mailmanagement_loc )
        time.sleep(4)

    # 工单搜索
    def enter_search(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.search_loc)
        time.sleep(4)

    # 知识库概览
    def enter_faq_overview(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.faq_overview_loc)
        time.sleep(4)

    # 服务
    def enter_service(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.service_loc )
        time.sleep(4)

    # 统计管理
    def enter_stats(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.stats_loc)
        time.sleep(4)

    # 统计组合管理
    def enter_statscombine(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.statscombine_loc)
        time.sleep(4)

    # 内容模板
    def enter_contenttemplate(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.contenttemplate_loc)
        time.sleep(4)

    # 管理员通知
    def enter_messagecool(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.messagecool_loc)
        time.sleep(4)

    # 服务岛
    def enter_island(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.island_loc)
        time.sleep(4)


    # 软件包管理
    def enter_packagemanager(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.packagemanager_loc)
        time.sleep(4)


    # 字段影响关系

    def enter_fieldimpact(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.fieldimpact_loc)
        time.sleep(4)

    # 搜索后点击进入菜单
    def enter_relust(self, text):
        self.clickButton(self.menu_loc)
        time.sleep(4)
        self.send_keys(self.menu_search_loc, text)
        menuname = '.menu-navigation [title="' + text + '"]'
        common_title_loc = (By.CSS_SELECTOR, menuname)
        time.sleep(4)
        self.find_element(common_title_loc).click()
        # 如下这种方式的定位，没有走显示等待，一找不到元素程序直接中断
        # self.driver.find_element_by_css_selector(menuname).click()
        time.sleep(4)
        # self.find_element(common_title_loc)

    # 工作台
    def enter_workbench(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.workbench_loc)
        time.sleep(4)

    # 工作台管理
    def enter_workbenchmanage(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.workbenchmanage_loc)
        time.sleep(4)

    # kpi
    def enter_kpi(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.KPI_loc)
        time.sleep(4)

    # 通信日志
    def enter_communicationlog(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.communicationlog_loc)
        time.sleep(4)

    # 系统日志
    def enter_systemlog(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.systemlog_loc)
        time.sleep(4)

    # 公共参数设置
    def enter_paramsetting(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.paramsetting_loc)
        time.sleep(4)

    # sql屏幕查询
    def enter_selectbox(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.selectbox_loc)
        time.sleep(4)

    # 偏好设置
    def enter_preferences(self):
        # self.clickButton(self.menu_loc)
        # time.sleep(2)
        self.clickButton(self.Preferences_loc)
        time.sleep(4)

    # 服务台
    def enter_cti(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.cti_loc)
        time.sleep(4)

    # 我的工单  mytickets_loc
    def enter_mytickets(self):
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.mytickets_loc)
        time.sleep(4)

    def entre_tagmanagement(self):
        """
            点击进入标签管理tab
        """
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.tagmanagement_loc)
        time.sleep(4)

    def enter_tagmanagement_rule(self):
        """
            点击进入标签规则管理tab
        """
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.tagmanagement_rule_loc)
        time.sleep(4)

    def entre_serviceremind(self):
        """
            点击进入到期提醒管理tab
        """
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.serviceremind_loc)
        time.sleep(4)

    def entre_wechat_config(self):
        """
            点击进入小程序配置tab
        """
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.wechat_config_loc)
        time.sleep(4)

    def enter_duty(self):
        """
            点击进入值班概览
        """
        self.clickButton(self.menu_loc)
        time.sleep(2)
        self.clickButton(self.duty_loc)
        time.sleep(4)
