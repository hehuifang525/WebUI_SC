"""
@author: DT_testing
@file:   cmdb_configure_page.py
@desc:  【cmdb配置】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from common.base import Base


class CmdbConfigurePage(Base):

    addbth_loc = (By.ID, 'fieldCreateButton')
    Search_input_loc = (By.ID, 'Search-input')
    # 表头
    table_head_loc = (By.CSS_SELECTOR, '.ant-table-fixed thead th')
    # 表格数据
    table_body_loc = (By.CSS_SELECTOR, 'td.ant-table-cell.ng-star-inserted')
    # 表格最左边列
    tableleftcell_loc = (By.CSS_SELECTOR, 'td.ant-table-cell-fix-left-last')
    # 路径、tab标题
    road_loc = (By.CSS_SELECTOR, "[class='breadcrumb-overflow']")
    tabtitle_loc = (By.CSS_SELECTOR, '.nav-horizontal-active [class="nav-horizontal-title ellipsis-row"]')
    empty_loc = (By.CSS_SELECTOR, '[class="empty-text ng-star-inserted"] span')
    copy_loc = (By.ID, 'Copy')
    # 取列表中的“全部（*）”
    totaltab_loc = (By.CSS_SELECTOR, '[class="simple-site flex-space-between"] div')

    # -------填写基本类的信息页面01---------
    name_loc = (By.ID, 'Class')
    repeat_nametip_loc = (By.CSS_SELECTOR, '.ng-trigger-helpMotion')
    # 可见组权限
    # 有效无效
    valid_input_loc = (By.ID, 'ValidID')
    valid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(1)')
    invalid_loc = (By.CSS_SELECTOR, '.cdk-virtual-scroll-content-wrapper nz-option-item:nth-child(2)')
    valid_clear_loc = (By.CSS_SELECTOR, '#ValidID .ant-select-clear.ng-star-inserted')

    # 上传图片
    # 备注
    Comments_loc = (By.ID, 'Comments')
    next_loc = (By.ID, 'nextbtn')
    # 返回列表
    backlist1_loc = (By.ID, 'cancelbtn1')

    # ------填写表单字段信息02----------
    # 提交
    submit2_loc = (By.CSS_SELECTOR, '#step2 button.ant-btn.ant-btn-primary')
    # 上一步
    Backbtn2_loc = (By.CSS_SELECTOR, '#step2 button:nth-child(2)')
    # 返回列表
    cancelbtn2_loc = (By.ID, 'cancelbtn2')

    # 选择显示字段
    selectfield_loc = (By.CSS_SELECTOR,
                       '[class="margin-L10 ant-form-item ant-row"] .ant-select-selection-search input]')
    # 页面显示的字段  [class="ant-form-item-label ant-col"] label
    # showfield_loc = (By.CSS_SELECTOR, '[class="ant-form-item-label ant-col"] label')
    showfield_loc = (By.CSS_SELECTOR, '.dynamic-formgroup label') # 2022-01-06
    # 添加字段

    # -------定制模板03-----
    template_loc = (By.CSS_SELECTOR, '.module-item.cursor.flex-align-center.ng-star-inserted')
    # edit_loc = (By.CSS_SELECTOR, '#step3 .module-item:nth-child(2)')
    # details_loc = (By.CSS_SELECTOR, '#step3 .module-item:nth-child(3)')
    # import_loc = (By.CSS_SELECTOR, '#step3 .module-item:nth-child(4)')
    # 完成 继续新建资产类 上一步 返回列表
    complete_loc = (By.CSS_SELECTOR, '#step3 button:nth-child(1)')
    createagainbtn_loc = (By.ID, 'createagainbtn')
    Backbtn3_loc = (By.CSS_SELECTOR, '#step3 button:nth-child(3)')
    cancelbtn3_loc = (By.ID, 'cancelbtn3')

    # 创建模板页面
    FormName_loc = (By.ID, 'FormName')

    # 提交 取消
    submit3_loc = (By.CSS_SELECTOR, '#step3 button:nth-child(1)')
    cancel_template_loc = (By.CSS_SELECTOR, '#step3 button:nth-child(2)')

    # -----完成04-----
    backlist4_loc = (By.ID, 'Backtolist')
    newciitembtn = (By.ID, 'toaddnewciitembtn')

    # --------定制模板--下方自定义模块---------
    # 名称
    field_name_loc = (By.CSS_SELECTOR,".cdk-drop-list #Name")
    # 资产生命周期
    depl_state_loc = (By.CSS_SELECTOR, ".cdk-drop-list #DeplState")
    # 资产状态
    incistate_loc = (By.CSS_SELECTOR, ".cdk-drop-list #InciState")
    # 使用科室
    customer_company_loc = (By.CSS_SELECTOR, ".cdk-drop-list #CustomerCompany")
    # 资产开始日期
    start_date_loc = (By.CSS_SELECTOR, ".cdk-drop-list #StartDate")


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

    def click_add(self):
        self.clickButton(self.addbth_loc)
        time.sleep(2)

    def checkadd(self):
        return self.find_element(self.addbth_loc).is_enabled()

    def click_copy(self):
        self.clickButton(self.copy_loc)
        time.sleep(2)

    def search_input(self, text):
        self.send_keys(self.Search_input_loc, text)
        time.sleep(2)

    def gettemnuber(self):
        """取当前显示的记录条数"""
        elem = self.driver.find_elements(By.CSS_SELECTOR, "tbody tr.cursor")
        return len(elem)

    def click_search_relust(self):
        self.find_elements(self.tableleftcell_loc)[0].click()
        time.sleep(2)

    def check_td(self):
        """" 检查页面指定元素是否存在"""
        self.find_element_10(self.tableleftcell_loc)

    def get_total(self):
        return self.find_element(self.totaltab_loc).text

    # ------添加页面01--------
    def inputname(self, text):
        self.send_keys(self.name_loc, text)

    def get_name_tip(self):
        return self.find_element(self.repeat_nametip_loc).text

    def choose_valid(self):
        self.clickButton(self.valid_input_loc)
        time.sleep(1)
        self.clickButton(self.valid_loc)

    def choose_invalid(self):
        self.clickButton(self.valid_input_loc)
        # time.sleep(1)
        self.clickButton(self.invalid_loc)

    # 删除有效性
    def delete_valid(self):
        elenmt = self.find_element(self.valid_input_loc)
        ActionChains(self.driver).move_to_element(elenmt).perform()
        time.sleep(1)
        self.clickButton(self.valid_clear_loc)

    def input_coment(self, text):
        self.send_keys(self.Comments_loc, text)

    def click_next(self):
        """
            填写类的基本信息-下一步
        """
        self.clickButton(self.next_loc)
        time.sleep(2)

    def checknext(self):
        '''
            检查基本信息页的下一步按钮是否可用
        '''
        return self.find_element(self.next_loc).is_enabled()

    def getnext(self):
        '''
            取基本信息页下一步按钮的文本值
        '''
        return self.find_element(self.next_loc).text

    def click_backlist(self):
        '''
            点击返回列表
        '''
        self.clickButton(self.backlist1_loc)

    # ------填写表单字段信息页面02---------------

    def click_submit2(self):
        """
            填写表单字段信息页面-提交
        """
        self.clickButton(self.submit2_loc)
        time.sleep(2)

    def click_backbtn2(self):
        '''
            点击上一步
        '''
        self.clickButton(self.Backbtn2_loc)
        time.sleep(2)

    def click_backlist2(self):
        '''
            点击返回列表
        '''
        self.clickButton(self.cancelbtn2_loc)

    # -------- 定制模板03-----------
    def create_tempalte(self):
        self.find_elements(self.template_loc)[0].click()
        # self.clickButton(self.create_loc)
        time.sleep(5)

    def edit_tempalte(self):
        self.find_elements(self.template_loc)[1].click()
        #self.clickButton(self.edit_loc)
        time.sleep(5)

    def details_tempalte(self):
        # self.clickButton(self.details_loc)
        self.find_elements(self.template_loc)[2].click()
        time.sleep(5)

    def import_tempalte(self):
        # self.clickButton(self.import_loc)
        self.find_elements(self.template_loc)[2].click()
        time.sleep(5)

    def input_tempalte_name(self, text):
        self.send_keys(self.FormName_loc, text)

    def clicksubmit3(self):
        '''
                    模板内点击取消
                :return:
                '''
        self.clickButton(self.submit3_loc)
        time.sleep(1)

    def clickcancle3(self):
        '''
            模板内点击取消
        :return:
        '''
        self.clickButton(self.cancel_template_loc)
        time.sleep(3)

    def clickcomplete(self):
        '''
            定制模板点击完成
        :return:
        '''
        self.clickButton(self.complete_loc)

    def backlist3(self):
        '''
            定制模板返回列表
        :return:
        '''
        self.clickButton(self.cancelbtn3_loc)
        time.sleep(3)

    def Backbtn3(self):
        '''
            定制模板 上一步
        :return:
        '''
        self.clickButton(self.Backbtn3_loc)

    def createagain(self):
        '''
            定制模板  点击继续添加
        '''
        self.clickButton(self.createagainbtn_loc)
        time.sleep(3)

    def select_field(self, text):
        self.driver.find_elements_by_css_selector\
            ('[class="margin-L10 ant-form-item ant-row"] .ant-select-selection-search input')[0].click()
        ActionChains(self.driver).send_keys(text).perform()
        self.driver.find_element_by_css_selector('nz-option-item>div').click()

    def getshow_field(self):
        return self.find_elements(self.showfield_loc)

    # ----完成04----
    def backlist4(self):
        '''
            第四步完成页面点击返回列表
        '''
        self.clickButton(self.backlist4_loc)
        time.sleep(2)

    def newciitem(self):
        self.clickButton(self.newciitembtn)

    def temp_click(self, temp_name):
        """
            定制模板页面，点击指定名称的模板
        """
        temp_name = '[title="' + temp_name +'"]'
        tem_name_loc = (By.CSS_SELECTOR, temp_name)
        self.clickButton(tem_name_loc)

    def field_name(self, text):
        """ 定制模板，自定义模块下输入名称 """
        self.send_keys(self.field_name_loc,text)

    def depl_state(self, depl_state):
        """ 定制模板，选择生命周期 """
        self.clickButton(self.depl_state_loc)
        depl_state_title = '.cdk-virtual-scroll-content-wrapper [title="' + depl_state +'"]'
        depl_state_title_loc = (By.CSS_SELECTOR, depl_state_title)
        # btn = self.find_element(depl_state_title_loc)
        # self.driver.execute_script("arguments[0].click();", btn)
        self.clickButton(depl_state_title_loc)

    def incistate(self, incistate):
        """ 定制模板，选择状态 """
        self.clickButton(self.incistate_loc)
        incistate_title = '.cdk-virtual-scroll-content-wrapper [title="' + incistate + '"]'
        incistate_title_loc = (By.CSS_SELECTOR, incistate_title)
        self.clickButton(incistate_title_loc)

    def customer_company(self, customer_company):
        """ 定制模板，选择客户 """
        self.find_element(self.customer_company_loc).click()
        # 输入值需要修改输入方式actioncharm
        ActionChains(self.driver).send_keys(customer_company).perform()
        time.sleep(3)
        customer_company_title = '.cdk-virtual-scroll-content-wrapper [title="' + customer_company + '"]'
        customer_company_title_loc = (By.CSS_SELECTOR, customer_company_title)
        self.clickButton(customer_company_title_loc)

    def start_date(self):
        """ 定制模板，选择资产开始日期（选择今日）"""
        self.clickButton(self.start_date_loc)
        time.sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR, ".ant-picker-today-btn").click()





