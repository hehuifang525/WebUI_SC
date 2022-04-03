"""
@author: DT_testing
@file:   cmdb_overview_page.py
@desc:  【cmdb概览】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class CmdbOverviewPage(Base):

    # 添加、 导入导出、导出当前、打印、高级搜索
    bth_loc = (By.CSS_SELECTOR, '.flex-start.flex-wrap-row  button')
    add_loc = (By.XPATH, "//span[text()=' 添加 ']")
    # 右侧列表搜索
    Search_input_loc = (By.ID, 'Search-input')
    # 表头 0120修改表头元素变更
    # table_head_loc = (By.CSS_SELECTOR, '.ant-table-fixed thead th')
    table_head_loc = (By.CSS_SELECTOR, '.theadtr th')
    # 表格数据
    table_body_loc = (By.CSS_SELECTOR, 'td.ant-table-cell.ng-star-inserted')
    # 表格最左边列
    tableleftcell_loc = (By.CSS_SELECTOR, 'td.ant-table-cell-fix-left-last')
    # 路径、tab标题
    road_loc = (By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    tabtitle_loc = (By.CSS_SELECTOR, '.nav-horizontal-active [class="nav-horizontal-title ellipsis-row"]')
    # div.breadcrumb
    closetab_loc = (By.CSS_SELECTOR, '.nav-horizontal-active .delete')
    empty_loc = (By.CSS_SELECTOR, '[class="empty-text ng-star-inserted"] span')

    # 左侧树形结构的全部  [class="ant-tree-node-content-wrapper ant-tree-node-selected"]
    left_all_loc = (By.CSS_SELECTOR,'[class="ant-tree-node-content-wrapper ant-tree-node-selected"]')

    # 取列表中的“全部（*）”
    totaltab_loc = (By.CSS_SELECTOR, '.simple-site.list-tabList-detail.flex-space-between div:nth-child(1)')  # 32版本该元素被删除

    table_tr_loc = (By.CSS_SELECTOR, '#tableTbody .tbody-tr')
    # 2021-12-20 tab被删除，调整搜索后无数据的定位

    empty_text_loc = (By.CSS_SELECTOR, '.empty-text span')
    # 删除  #Delete

    delete_loc = (By.ID, 'Delete')
    # 删除弹框确认、删除
    delete_cancle_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-body-wrapper button:nth-child(1)')
    delete_comfire_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-body-wrapper button:nth-child(2)')

    # 第二排按钮
    btn2_loc = (By.CSS_SELECTOR, '[class="flex-start flex-wrap-row"] button')
    # 类
    select_class_loc = (By.CSS_SELECTOR, '[class="ant-form-item-control-input-content"] input')
    # 新建模板
    template_loc = (By.CSS_SELECTOR, '[class="flex-wrap-row itsm-template ng-star-inserted"]>li')
    # 资产名称、资产生命周期
    name_loc = (By.ID, 'Name')
    DeplState_loc = (By.CSS_SELECTOR, '#DeplState')
    # 已计划 、已过期
    Expired_loc = (By.ID, 'Expired')
    Planned_loc = (By.ID, 'Planned')

    # 资产状态
    InciState_loc = (By.CSS_SELECTOR, '#InciState')
    # 事件、正常
    Incident_loc = (By.ID, 'Incident')
    Operational_loc = (By.ID, 'Operational')
    CustomerCompany_loc = (By.ID, 'CustomerCompany')
    # 资产--日期
    cmdb_se_data_loc = (By.CSS_SELECTOR, '[placeholder="请选择日期"]')
    commit_loc = (By.ID, 'commit')
    backlist_loc = (By.CSS_SELECTOR, '#commit+button')

    # 返回概览
    back_overview_loc = (By.CSS_SELECTOR, '[class="ant-breadcrumb-link ng-star-inserted"]')
    # cmdb 编辑
    cmdb_edit_loc = (By.CSS_SELECTOR,'div.itsm-detail-template .itsm-detail-template-btn:nth-child(1)')
    # cmdb 链接
    link_loc = (By.CSS_SELECTOR, 'div.itsm-detail-template .itsm-detail-template-btn:nth-child(3)')

    # --------------高级搜索页面------------------
    # 资产编号 资产名称
    height_search_input_loc = (By.CSS_SELECTOR, '.ant-form-item-control-input-content')
    # 搜索按钮
    height_search_btn_loc = (By.CSS_SELECTOR, '[class="searchBtn ant-btn ant-btn-primary ant-btn-block"]')
    # 搜索结果tab
    height_search_resulttab_loc = (By.CSS_SELECTOR, '.simple-site.list-tabList-detail.flex-space-between div:nth-child(1)')

    # -----------点击链接，进入的链接页面---------------
    # 创建新链接 、管理现有链接
    createlink_loc = (By.CSS_SELECTOR,'.ant-tabs-tab.ng-star-inserted:nth-child(1)')
    managelink_loc = (By.CSS_SELECTOR, '.ant-tabs-tab.ng-star-inserted:nth-child(2)')
    # 链接到
    link_to_loc = (By.ID, 'TargetIdentifier')
    # 链接到：配置项
    # 0922修改
    # link_tocmdb_loc = (By.ID, 'ITSMConfigItem')
    link_tocmdb_loc = (By.CSS_SELECTOR, '[title="配置项"]')
    # 增加搜索条件
    FilterCondition_loc = (By.ID, 'FilterCondition')
    # 搜索条件下拉项：如资产编号
    choose_Condition_loc = (By.CSS_SELECTOR, '[class="ant-select-item-option-content"]')
    # 资产编号输入框
    cmdbnumber_loc = (By.ID, 'Number')
    # 链接关系
    link_relationship_loc = (By.CSS_SELECTOR, '.ant-form-item-control-input-content')
    # 链接关系选项
    relationship_options_loc = (By.CSS_SELECTOR, '[class="ant-select-item-option-content"]')
    # 添加链接按钮
    addlinkbtn_loc = (By.CSS_SELECTOR, '.flex-align-start button')
    # 管理链接的-搜索按钮
    link_search_loc = (By.ID, 'runSearch')

    # 列表选择框  [class="ant-  ]
    choose_cmdb_loc = (By.CSS_SELECTOR, '.ant-modal-content .ant-table-tbody .ant-table-row .ant-table-cell-fix-left')
    # choose_cmdb_loc = (By.CSS_SELECTOR, "td[id='1']")
    # 删除链接，取消删除、确认删除
    deletelink_loc =(By.CSS_SELECTOR, 'button.ant-btn.ant-btn-primary.ng-star-inserted')
    cancel_delete_link_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-body-wrapper button:nth-child(1)')
    confirm_delete_link_loc = (By.CSS_SELECTOR, '.ant-modal-confirm-body-wrapper button:nth-child(2)')
    # 关闭链接弹窗
    closelink_loc = (By.CSS_SELECTOR, '[class="ant-modal-close-x"]')

    # 管理现有链接页面，无链接提示语.ant-empty-description
    link_empty_description_loc = (By.CSS_SELECTOR,'.ant-empty-description')

    # -----cmdb详情页面----
    # 取链接资产的表格数据 ,最左侧的资产编号
    link_cmdb_number = (By.CSS_SELECTOR,
                        '.ant-table-body tbody.ant-table-tbody .ant-table-row td.ant-table-cell-fix-left')
    # 取基本信息中资产名称、资产生命周期、资产状态
    detail_name_loc = (By.CSS_SELECTOR,'div#itsm-baseInfo .itsm-detail-content:nth-child(2) .itsm-content-text')
    detail_cycle_loc = (By.CSS_SELECTOR, 'div#itsm-baseInfo .itsm-detail-content:nth-child(3) .itsm-content-text')
    detail_status_loc = (By.CSS_SELECTOR, 'div#itsm-baseInfo .itsm-detail-content:nth-child(4) .itsm-content-text')

    # 关闭当前tab
    close_active_tab_loc = (By.CSS_SELECTOR, '.cursor.ng-star-inserted.nav-horizontal-active .anticon.anticon-close')

    # --------添加界面------------------
    # cmdb_class_loc = (By.CSS_SELECTOR, ".ant-form-item-control-input")
    cmdb_class_loc = (By.CSS_SELECTOR, ".itsm-template-all input")
    cmdb_class_option_loc = (By.CSS_SELECTOR, ".cdk-virtual-scroll-content-wrapper  nz-option-item")

    def click_add(self):
        """
            点击添加按钮
        """
        self.clickButton(self.add_loc)

    # 点击添加、导入导出、导出当前、打印、高级搜索
    # def click_add(self):
    #     Base(self.driver).check_loading()
    #     # time.sleep(10)
    #     self.find_elements(self.bth_loc)[0].click()
    #     time.sleep(3)

    def click_import(self):
        self.find_elements(self.bth_loc)[1].click()

    def click_export_current(self):
        self.find_elements(self.bth_loc)[2].click()

    def click_print(self):
        self.find_elements(self.bth_loc)[3].click()

    def click_high_search(self):
        self.find_elements(self.bth_loc)[4].click()

    def clickleftall(self):
        '''点击左侧的全部'''
        self.clickButton(self.left_all_loc)

    def gettable_head(self):
        '''
        :return: 返回表头数据
        '''
        return self.find_elements(self.table_head_loc)

    def gettable_body(self):
        return self.find_elements(self.table_body_loc)

    def getleftslaname(self):
        return self.find_elements(self.tableleftcell_loc)

    def gettabTitle(self):
        '''

        :return: tab标题
        '''
        return self.find_element(self.tabtitle_loc).text

    def get_empty_tip(self):
        return self.find_element(self.empty_loc).text

    def getroadText(self):
        '''
        :return: 左上角的路径名称
        '''
        return self.find_element(self.road_loc).text

    # def click_add(self):
    #     self.clickButton(self.addbth_loc)
    #     time.sleep(2)

    def search_input(self, text):
        self.clickButton(self.Search_input_loc)
        self.send_keys(self.Search_input_loc, text)
        time.sleep(2)

    def click_search_relust(self):
        self.find_elements(self.tableleftcell_loc)
        self.find_elements(self.tableleftcell_loc)[0].click()
        time.sleep(2)

    def get_total(self):
        return self.find_element(self.totaltab_loc).text

    def table_tr(self):
        """
            取搜索后的记录数
        """
        return self.find_elements(self.table_tr_loc)

    # 点击列表全选按钮
    def click_all_select(self):
        self.clickButton(self.table_head_loc)
        time.sleep(1)

    def delete_cmdb(self):
        self.clickButton(self.delete_loc)
        time.sleep(3)

    def delete_cancel(self):
        self.clickButton(self.delete_cancle_loc)
        time.sleep(1)

    def delete_comfire(self):
        self.find_element(self.delete_comfire_loc).click()
        # self.clickButton(self.delete_comfire_loc)
        time.sleep(1)

    def detele_all(self):
        elm = self.find_elements(self.btn2_loc)[1]
        elm.click()

    def empty_text(self):
        """
            取无数据时报错
        """
        return self.find_element(self.empty_text_loc).text


    # ------添加页面------
    def choose_class(self, text):
        self.driver.find_element_by_css_selector \
            ('[class="ant-form-item-control-input-content"] input').click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        time.sleep(1)
        self.driver.find_element_by_css_selector('nz-option-item>div').click()

    def click_create_template(self):
        self.clickButton(self.template_loc)

    def input_name(self, text):
        self.send_keys(self.name_loc, text)

    def choose_DeplState(self, text):
        '''
            选择资产生命周期
        '''
        # self.driver.find_element_by_css_selector('#DeplState input').click()
        # if text == '已计划':
        #     self.driver.find_element_by_css_selector('#Planned').click()
        # elif text == '已过期':
        #     self.driver.find_element_by_css_selector('#Expired').click()

        self.driver.find_element(*self.DeplState_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()
        time.sleep(1)

    def choose_InciState(self, text):
        '''
            选择资产状态
        '''
        # self.driver.find_element_by_css_selector('#InciState input').click()
        # if text == '事件':
        #     self.driver.find_element_by_css_selector('#Incident').click()
        # elif text == '正常':
        #     self.driver.find_element_by_css_selector('#Operational').click()

        self.driver.find_element(*self.InciState_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()

    def click_commit(self):
        self.clickButton(self.commit_loc)
        time.sleep(4)

    def click_backlist(self):
        self.clickButton(self.backlist_loc)

    def close_edit_tab(self):
        '''
         关闭编辑tab
        :return:
        '''
        self.clickButton(self.closetab_loc)
        time.sleep(2)

    def back_overview(self):
        # 等待元素
        self.find_element(self.cmdb_edit_loc)
        self.find_elements(self.back_overview_loc)[2].click()
        time.sleep(3)

    def click_cmdb_edit(self):
        '''点击编辑'''
        self.clickButton(self.cmdb_edit_loc)

    def click_link(self):
        '''点击链接'''
        self.clickButton(self.link_loc)
        time.sleep(1)

    # 资产基本信息 分别取资产名称、资产生命周期、资产状态值
    def detail_name(self):
        return self.find_element(self.detail_name_loc).text

    def detail_cycle(self):
        return self.find_element(self.detail_cycle_loc).text

    def detail_status(self):
        return self.find_element(self.detail_status_loc).text

    # 关闭当前tab
    def close_active_tab(self):
        self.find_element(self.close_active_tab_loc).click()


    # -----高级搜索页面-----
    # 点击高级搜索
    def click_height_search(self):
        self.find_elements(self.bth_loc)[4].click()
        time.sleep(3)

    def input_cmdb_id2(self, text):
        '''
            高级搜索页面：输入资产编号
        '''

        self.driver.find_elements_by_css_selector('.ant-form-item-control-input-content')[1].click()
        ActionChains(self.driver).send_keys(text).perform()
        # self.send_keys(elm, text)

    def input_cmdb_name2(self, text):
        '''
            高级搜索页面：输入资产名称
        '''
        self.driver.find_elements_by_css_selector('.ant-form-item-control-input-content')[2].click()
        ActionChains(self.driver).send_keys(text).perform()

    def click_height_search2(self):
        '''
            高级搜索页面：点击搜素按钮
        '''
        self.find_element(self.height_search_btn_loc).click()
        # self.send_keys(elm, text)

    def get_height_search_result(self):
        return self.find_element(self.height_search_resulttab_loc).text

    # -------详情中 点击链接，进入链接页面-----------
    def createlink(self):
        ''' 点击创建新链接'''
        self.clickButton(self.createlink_loc)

    def managelink(self):
        ''' 点击管理现有链接'''
        self.clickButton(self.managelink_loc)

    def linkto(self):
        '''链接到'''
        self.clickButton(self.link_to_loc)

    def linktocmdb(self):
        '''链接到配置项'''
        self.clickButton(self.link_to_loc)
        time.sleep(1)
        self.clickButton(self.link_tocmdb_loc)

    def addsearchcondition(self, title):
        '''增加搜索条件'''
        # 原生方法点击按钮
        # self.find_element(self.FilterCondition_loc)
        self.driver.find_element_by_css_selector('#FilterCondition').click()
        # self.driver.find_elements_by_css_selector('[class="ant-form-item-control-input"]')[3].click()
        # [class="ant-form-item-control-input"]
        # 输入
        ActionChains(self.driver).send_keys(title).perform()
        # 点击

        menuname = '[title="' + title + '"]'
        common_title_loc = (By.CSS_SELECTOR, menuname)
        self.find_element(common_title_loc).click()

        # self.find_elements(self.choose_Condition_loc)[0].click()

    def input_cmdb_number(self, text):
        self.send_keys(self.cmdbnumber_loc, text)

    def link_search(self):
        self.clickButton(self.link_search_loc)

    def addlink(self):
        '''点击添加链接'''
        self.find_element(self.addlinkbtn_loc).click()
        #  self.clickButton(self.addlinkbtn_loc)

    def choose_link_relationship(self):
        '''链接关系选择-连接到'''
        self.find_elements(self.link_relationship_loc)[5].click()
        # self.clickButton(self.link_relationship_loc)
        self.find_elements(self.relationship_options_loc)[1].click()

    def chose_cmdb_option(self):
        '''选择查找出来的资产项'''
        self.find_elements(self.choose_cmdb_loc)[0].click()

    def deletelink(self):
        '''点击删除链接'''
        self.clickButton(self.deletelink_loc)

    def cancel_deletelink(self):
        self.clickButton(self.cancel_delete_link_loc)

    def confirm_deletelink(self):
        self.clickButton(self.confirm_delete_link_loc)

    def closelink(self):
        '''关闭链接弹框'''
        self.clickButton(self.closelink_loc)
        time.sleep(2)

    def link_empty_description(self):
        return self.find_element(self.link_empty_description_loc).text

    # -------资产详情页面--------------
    def getlink_cmdbnumber(self):
        '''资产详情页面，取下方链接的资产编号'''
        return self.find_elements(self.link_cmdb_number)

    def chose_cmdb_class(self,cmdb_class):
        """
        选择一个资产蕾
        """
        btn = self.find_element(self.cmdb_class_loc)
        self.driver.execute_script("arguments[0].click();", btn)

        # self.find_element(self.cmdb_class_loc).click()
        # 输入值
        ActionChains(self.driver).send_keys(cmdb_class).perform()
        self.find_elements(self.cmdb_class_option_loc)[0].click()

    def get_name(self):
        """返回新增界面名称，主要拥于默认值检查"""
        return self.find_element(self.name_loc).get_attribute('value')

    def get_depl_state(self):
        """返回新增界面资产生命周期值"""
        return self.find_element(self.DeplState_loc).text

    def get_incitate(self):
        """返回新增界面资产状态值"""
        return self.find_element(self.InciState_loc).text

    def get_customer_company(self):
        """返回使用科室"""
        return self.find_element(self.CustomerCompany_loc).text

    def get_stsrt_data(self):
        """返回资产开始日期"""
        return self.find_elements(self.cmdb_se_data_loc)[0].text





