"""
@author: DT_testing
@file:   servicesla_page.py
@desc:  【服务水平协议】
@step：
"""
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base import Base


class ServiceSlaPage(Base):
    # tab title 导航路径  div .nav-horizontal-active
    tabtitle_loc = (By.CSS_SELECTOR, 'div .nav-horizontal-active')
    bar_loc =(By.CSS_SELECTOR, '[class="ant-breadcrumb"]')
    addsla_loc = (By.ID, 'fieldCreateButton')
    search_loc = (By.ID, 'search-input')
    tableth_loc =(By.CSS_SELECTOR, 'th.ant-table-cell')
    # serchresult_loc = (By.CSS_SELECTOR, '#tableTbody .cursor td')
    serchresult_loc = (By.CSS_SELECTOR, 'Tbody .cursor td')
    #20211116调整
    #serchempty_loc = (By.CSS_SELECTOR, '[class="empty-text ng-star-inserted"] span')
    serchempty_loc = (By.CSS_SELECTOR, '.ant-empty p')

    # 20211116调整
    # 表格最左边列
    # tableleftcell_loc = (By.CSS_SELECTOR, 'td.ant-table-cell-fix-left-last')
    tableleftcell_loc = (By.CSS_SELECTOR, 'Tbody .cursor td')

    #  添加页面
    name_loc = (By.ID, 'Name')
    Validinout_loc =(By.ID, 'ValidID')
    # 0922修改
    Valid_loc = (By.CSS_SELECTOR, '[title="有效"]')
    inValid_loc = (By.CSS_SELECTOR, '[title="无效"]')
    comment_loc =(By.ID, 'Comment')
    backlist_loc = (By.ID, 'CalendarCancel')
    # 名称提示语：
    namemessage_loc = (By.ID, 'Name_errorServeMessage')
    # 下一步  提交并返回列表
    next_loc = (By.XPATH, '//*[@id="step1"]/form/nz-form-item/nz-form-control/div/div/button[1]')
    submitback_loc = (By.XPATH, '//*[@id="step1"]/form/nz-form-item/nz-form-control/div/div/button[2]')

    # 工作时间管理
    calendar_loc = (By.ID, 'Calendar')
    empty_loc = (By.CSS_SELECTOR, '.ant-empty-description')





    '''
        设置指标信息页面  步骤2
    '''
    # 完成 完成并添加 上一步 返回列表
    complete_loc = (By.XPATH, '//*[@id="step2"]/nz-form-item/nz-form-control/div/div/button[1]')
    completeadd_loc = (By.XPATH, '//*[@id="step2"]/nz-form-item/nz-form-control/div/div/button[2]')
    Back2_loc = (By.XPATH, '//*[@id="step2"]/nz-form-item/nz-form-control/div/div/button[3]')
    bastlist2_loc = (By.XPATH, '//*[@id="step2"]/nz-form-item/nz-form-control/div/div/button[4]')
    # 创建指标按钮 复制指标  #
    # 0118修改
    newtarget_loc = (By.CSS_SELECTOR, '.cursor.sla-indicator-add')
    # newtarget_loc = (By.CSS_SELECTOR, '[class="anticon anticon-plus"]')
    copytarget_loc = (By.CSS_SELECTOR, '[class="color-pormpt-text"]')
    # 删除指标  取消删除 确认删除
    deltarget_loc = (By.CSS_SELECTOR, '[class="color-red margin-L5"]')
    delconfirm_loc =(By.CSS_SELECTOR, '[class="ant-modal-confirm-btns"] button')

    # 取第一个创建指标框的元素： 指标度量名曾 指标时长
    tarname2_loc = (By.CSS_SELECTOR, '#slaIndicator0 .ant-select-selector')
    tartime_loc = (By.CSS_SELECTOR, '[class="ant-input-number-input-wrap"] input')

    # 通知阀值输入框 删除阀值 添加阀值
    inputthreshold_loc = (By.CSS_SELECTOR, '[class="ant-input-wrapper ant-input-group ng-star-inserted"] input')
    # 0118更新
    delthreshold_loc = (By.CSS_SELECTOR, '.anticon-minus-circle')
    # delthreshold_loc = (By.CSS_SELECTOR, '[class="anticon anticon-minus-circle"]')
    addthreshold_loc = (By.CSS_SELECTOR, 'button.ant-btn.ant-btn-sm')
    # 查看详情 取第一个框
    details_loc = (By.XPATH, '//*[@id="slaIndicator0"]/div[1]/div/nz-form-item/span')
    # 指标框左上角指标信息
    tartitle_loc = (By.CSS_SELECTOR, 'h4.flex-space-between div')


    '''
        指标度量管理页面 -指标度量管理-添加/编辑
    '''
    # 指标度量管理按钮
    target_loc= (By.CSS_SELECTOR, '[class="anticon anticon-pic-right"]')
    addtarget_loc = (By.CSS_SELECTOR, 'button.ant-btn.ant-btn-sm')

    # --------添加/编辑指标页-----
    targetfield_loc = (By.ID, 'IndicatorField')
    targetname_loc = (By.CSS_SELECTOR, '.ant-modal-body #Name')
    # 字段、名称提示信息
    fieldtip_loc = (By.ID, 'IndicatorField_errorServeMessage')
    nametip_loc = (By.ID, 'Name_errorServeMessage')
    closetar_loc = (By.CSS_SELECTOR, '[aria-label="Close"]')
    # 累计/重置
    # timetype_loc = (By.CSS_SELECTOR, '[class="ant-radio-input"]')
    addup_loc = (By.ID, 'add up')
    reset_loc = (By.ID, 'Reset')
    # 触发开始计时条件 触发通知计时条件
    # .padding-T5.padding-B5
    condition_loc = (By.CSS_SELECTOR, '.padding-T5.padding-B5 input')

    targetvalidinput_loc = (By.ID, 'Valid')
    targetvalid_loc = (By.CSS_SELECTOR, 'nz-option-item[title="有效"]')
    targetinvalid_loc = (By.CSS_SELECTOR, 'nz-option-item[title="无效"]')
    # targetinvalid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')
    # targetinvalid_loc = (By.CSS_SELECTOR, '[testvalue="无效"]')

    targetcancle_loc = (By.CSS_SELECTOR,'.ant-modal-body button:nth-child(2)')

    # 20211116调整变更
    # submittar_loc = (By.CSS_SELECTOR, '[class="margin-R10 ant-btn"]+button')
    submittar_loc = (By.CSS_SELECTOR, '.ant-modal-body button:nth-child(1)')

    # 删除事件按钮  [class="anticon anticon-minus-circle"]
    delevent_loc = (By.CSS_SELECTOR, '[class="anticon anticon-minus-circle"]')

    '''
            指标度量管理页面 -指标度量管理-页面（表格部分）
    '''
    # 搜索框 表格信息
    searchtarget_loc = (By.CSS_SELECTOR, '.modal-table-search input')
    # [class="ant-input-affix-wrapper ant-input-affix-wrapper-sm"] [placeholder="过滤"]
    # searchtarget_loc = (By.CSS_SELECTOR, '[class="ant-input-affix-wrapper ant-input-affix-wrapper-sm"] [placeholder="过滤"]')
    targetth_loc = (By.CSS_SELECTOR, '.metrics-modal-table th')
    # targettd_loc = (By.CSS_SELECTOR, 'td .ng-star-inserted')
    targettd_loc = (By.CSS_SELECTOR, '.metrics-modal-table td.ng-star-inserted')

    # targetedit_loc = (By.CSS_SELECTOR, '[class=" ng-fa-icon"]')
    targetedit_loc = (By.CSS_SELECTOR, 'td .operation-edit')







    # 添加
    def clickaddsla(self):
        # print('点击天机开始1')
        self.clickButton(self.addsla_loc)
        # print('点击天机开始2')
        # self.find_element(self.addsla_loc).click()

        time.sleep(3)

    def inputserch(self, text):
        self.clickButton(self.search_loc)
        self.send_keys(self.search_loc, text)
        time.sleep(2)

    def getserchresult(self):
        return self.find_elements(self.serchresult_loc)

    def clickserchresult(self):
        self.find_elements(self.serchresult_loc)[0].click()
        time.sleep(2)

    # 取搜索空结果
    def getserchempty(self):
        return self.find_element(self.serchempty_loc).text

    def gettabtitle(self):
        return self.find_element(self.tabtitle_loc).text

    def getbar(self):
        return self.find_element(self.bar_loc).text

    # 取表头列  tableth_loc
    def gettablehead(self):
        return self.find_elements(self.tableth_loc)

    # 取服务协议最左侧的名称列
    def getleftslaname(self):
        return self.find_elements(self.tableleftcell_loc)

    def inputslaname(self, text):
        self.send_keys(self.name_loc, text)

    def clickslavalid(self):
        self.find_element(self.Validinout_loc).click()
        self.find_element(self.Valid_loc).click()

    def clickslainvalid(self):
        self.find_element(self.Validinout_loc).click()
        self.find_element(self.inValid_loc).click()

    def clickslanext(self):
        self.clickButton(self.next_loc)
        # self.find_element(self.next_loc).click()

    def clickslasubmit(self):
        self.clickButton(self.submitback_loc)
        # self.find_element(self.submitback_loc).click()

    def clickslabacklist(self):
        self.find_element(self.backlist_loc).click()

    # 取下一步、提交并返回列表是否可点击
    def getnextstyle(self):
        return self.find_element(self.submitback_loc).get_attribute('disabled')

    def getsunmitbackstyle(self):
        return self.find_element(self.submitback_loc).get_attribute('disabled')

    # 取名称提示信息
    def getnamemessage(self):
        return self.find_element(self.namemessage_loc).text

    # 选择工作时间管理
    def chose_calendar(self, text):
        self.find_element(self.calendar_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()

    def get_empty_calendar(self):
        return self.find_element(self.empty_loc).text

    def esc_chose_calendar(self):
        ActionChains(self.driver).move_to_element(self.find_element(
            self.calendar_loc)).send_keys(Keys.ESCAPE).perform()

    '''
        设置指标信息页面事件 第二步
    '''
    # 点击 完成 完成并添加 上一步 返回列表
    def clickcomplite(self):
        self.clickButton(self.complete_loc)

    def clickcompliteadd(self):
        self.clickButton(self.completeadd_loc)

    def clickBack2(self):
        self.clickButton(self.Back2_loc)

    def clickbastlist2(self):
        self.clickButton(self.bastlist2_loc)

    def bastlist2enabled(self):
        return self.find_element(self.bastlist2_loc).is_enabled()

    # 取完成、完成并再添加一条的样式，判断必填
    def getcomplitestyle(self):
        return self.find_element(self.complete_loc).get_attribute('disabled')

    def getcompliteaddstyle(self):
        return self.find_element(self.completeadd_loc).get_attribute('disabled')

    # 点击创建指标
    def clicknewtarget(self):
        self.clickButton(self.newtarget_loc)

    # 输入时长
    def inputtime(self, text):
        self.find_element(self.tartime_loc).clear()
        self.send_keys(self.tartime_loc, text)

    def chosetargetname(self, text):
        # self.clickButton(self.tarname2_loc)
        self.driver.find_element(*self.tarname2_loc).click()
        time.sleep(2)
        ActionChains(self.driver).send_keys(text).perform()
        # self.driver.find_element_by_css_selector('[title="' + text + '"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[title="' + text + '"]').click()

    # 添加通知阈值 删除通知阈值 输入通知阈值百分比
    def addthreshold(self):
        self.clickButton(self.addthreshold_loc)

    def delthreshold(self):
        self.clickButton(self.delthreshold_loc)

    def inputthreshold1(self, text):
        element = self.find_elements(self.inputthreshold_loc)[0]
        element.clear()
        element.send_keys(text)
        # self.send_keys(self.inputthreshold_loc, text)

    def inputthreshold2(self, text):
        element = self.find_elements(self.inputthreshold_loc)[1]
        element.clear()
        element.send_keys(text)

    def inputthreshold3(self, text):
        element = self.find_elements(self.inputthreshold_loc)[2]
        element.clear()
        element.send_keys(text)

    def inputthreshold5(self, text):
        element = self.find_elements(self.inputthreshold_loc)[4]
        element.clear()
        element.send_keys(text)

    def getthreshold(self):
        return self.find_elements(self.inputthreshold_loc)

    # 点击查看详情按钮
    def clickdetails(self):
        # self.clickButton(self.details_loc)
        self.find_element(self.details_loc).click()

    # 指标框左上角指标信息
    def gettarlefttitle(self):
        return self.find_element(self.tartitle_loc).get_attribute('textContent')




    '''
        指标度量管理页面
    '''
    # 点击指标度量管理
    def clicktarget(self):
        time.sleep(1)
        self.find_element(self.target_loc).click()
        # self.clickButton(self.target_loc)

    def clickaddtarget(self):
        # self.find_element(self.addtarget_loc).click()
        time.sleep(3)
        self.clickButton(self.addtarget_loc)

    # 点击右上角×
    def closetar(self):
        self.clickButton(self.closetar_loc)

    # 点击取消
    def targetcancle(self):
        self.clickButton(self.targetcancle_loc)

    # 添加指标点击提交
    def clicksubmittar(self):
        self.clickButton(self.submittar_loc)
        time.sleep(8)

    # 取提交按钮样式
    def getsubmittar_style(self):
        return self.find_element(self.submittar_loc).get_attribute('disabled')

    # 添加、编辑指标部分
    def inputtargetfield(self, text):
        self.send_keys(self.targetfield_loc, text)

    def inputtargetname(self, text):
        # 查找到两个name id 取第二个
        # elm = self.driver.find_elements_by_id('Name')[1]
        elm = self.find_element(self.targetname_loc)
        elm.clear()
        elm.send_keys(text)

    # 指标编辑页面修改指标名称
    def edittargetname(self, loc, text):
        # 查找到两个name id 取第二个
        elem = self.driver.find_element_by_css_selector('[testvalue="' + loc + '"]')
        elem.clear()
        elem.send_keys(text)

    # 取指标字段、度量名称输入值
    def gettarfield(self):
        return self.find_element(self.targetfield_loc).get_attribute('testvalue')

    def gettarname(self):
        elm = self.driver.find_elements_by_id('Name')[1]
        return elm.get_attribute('testvalue')

    def getvalid(self):
        return self.find_element(self.targetvalidinput_loc).get_attribute('testvalue')

    # 取计时类型的样式
    def gettimetype_add(self):
        return self.find_element(self.addup_loc).get_attribute('class')

    def gettimetype_reset(self):
        return self.find_element(self.reset_loc).get_attribute('class')

    # 取指标字段、度量名称提示信息
    def gettarfieldtip(self):
        return self.find_element(self.fieldtip_loc).text

    def gettarnametip(self):
        return self.find_element(self.nametip_loc).text



    def clickaddup(self):
        self.clickButton(self.addup_loc)

    def clickreset(self):
        self.clickButton(self.reset_loc)

    # 触发开始计时条件 停止计时条件
    def startcondition(self, text):
        self.driver.find_elements(*self.condition_loc)[0].click()

        # self.find_elements(*self.condition_loc)[0].click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(text).perform()
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()
        # res = 0
        # resulut = ''
        # titl = '[title="' + text + '"]'
        # # 一开始还需要做一次判断。
        # # 此时必须使用滚动下拉框的滚动条操作
        # try:
        #     resulut = self.driver.find_element_by_css_selector(titl)
        # except:
        #     pass
        # while res < 15 and resulut == '':
        #     js = 'document.getElementsByClassName' \
        #          '("cdk-virtual-scroll-viewport cdk-virtual-scroll-orientation-vertical")[0].scrollBy(0,544)'
        #     self.driver.execute_script(js)
        #     try:
        #         resulut = self.driver.find_element_by_css_selector(titl)
        #     except:
        #         pass
        #     res = res + 1
        # self.driver.find_element_by_css_selector(titl).click()

    def endcondition(self, text):
        self.driver.find_elements(*self.condition_loc)[1].click()
        # self.find_elements(*self.condition_loc)[1].click()
        time.sleep(1)
        ActionChains(self.driver).send_keys(text).perform()
        self.driver.find_element_by_css_selector('[title="' + text + '"]').click()

        # self.find_elements(self.condition_loc)[1].click()
        # res = 0
        # resulut = ''
        # titl = '[title="' + text + '"]'
        # # 一开始还需要做一次判断。
        # # 此时必须使用滚动下拉框的滚动条操作
        # try:
        #     resulut = self.driver.find_element_by_css_selector(titl)
        # except:
        #     pass
        # while res < 15 and resulut == '':
        #     js = 'document.getElementsByClassName' \
        #          '("cdk-virtual-scroll-viewport cdk-virtual-scroll-orientation-vertical")[0].scrollBy(0,544)'
        #     self.driver.execute_script(js)
        #     try:
        #         resulut = self.driver.find_element_by_css_selector(titl)
        #     except:
        #         pass
        #     res = res + 1
        # self.driver.find_element_by_css_selector(titl).click()

    # 删除事件
    def clickdelevent(self):
        self.clickButton(self.delevent_loc)


    # 添加指标点击有效无效
    def targetvalid(self):
        self.find_element(self.targetvalidinput_loc).click()
        self.find_element(self.targetvalid_loc).click()
        # self.clickButton(self.targetvalidinput_loc)
        # self.clickButton(self.targetvalid_loc)

    def targetinvalid(self):
        self.find_element(self.targetvalidinput_loc).click()
        self.find_element(self.targetinvalid_loc).click()
        # self.clickButton(self.targetvalidinput_loc)
        # self.clickButton(self.targetinvalid_loc)

    # 搜索指标
    def searchtarget(self, text):
        self.clickButton(self.searchtarget_loc)
        time.sleep(2)
        self.send_keys(self.searchtarget_loc, text)
        time.sleep(1)

    # 取表格数据
    def getsearchtarget(self):
        return self.find_elements(self.targettd_loc)

    # 取表头列名
    def gettargettablehead(self):
        return self.find_elements(self.targetth_loc)

    # 点击编辑指标
    def targetedit(self):
        self.clickButton(self.targetedit_loc)



