"""
@author: DT_testing
@file:   tickettemplate_common.py
@desc:  【工单模板】
@step： templateRequiredCommon： 填写必填，创建服务人员工单模板
        gettemplateinfo：二次打开模板编辑页面，取值
        templatefullCommon：全填信息，创建服务人员工单模板
        fullSelectFieldCommon：工单模板页面添加下拉类型的自定义字段
"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.template_page import TemplatePage
from src.page.agent.field_page import FieldPage
from src.page.pagecommon.get_time_common import GetTimeCommon
import random
class TicketTemplateCommon(TemplatePage):
    def templateRequiredCommon(self):
        EntranceAgentPage(self.driver).enter_tickettemplate()
        time.sleep(8)
        TemplatePage(self.driver).addtemplate()
        templatename = '工单模板必填' + time.strftime('%Y%m%d%M%S', time.localtime())
        TemplatePage(self.driver).inputname(templatename)
        TemplatePage(self.driver).clickagent()
        TemplatePage(self.driver).clickshowLocation()
        TemplatePage(self.driver).clickselectall()
        TemplatePage(self.driver).clickcloseOption()
        TemplatePage(self.driver).chosecreateticket()
        time.sleep(2)
        # TemplatePage(self.driver).chosevaild()
        TemplatePage(self.driver).commit()
        # 此处必须加强制等待，否则点击不到查询的数据
        time.sleep(4)
        templateinfo = {'name': templatename}
        return templateinfo
    def templateRequiredCommon3(self):
        TemplatePage(self.driver).addtemplate()
        templatename = '工单模板必填' + time.strftime('%Y%m%d%M%S', time.localtime())
        TemplatePage(self.driver).inputname(templatename)
        TemplatePage(self.driver).clickagent()
        TemplatePage(self.driver).clickshowLocation()
        TemplatePage(self.driver).clickselectall()
        TemplatePage(self.driver).clickcloseOption()
        TemplatePage(self.driver).chosecreateticket()
        time.sleep(2)
        # TemplatePage(self.driver).chosevaild()
        TemplatePage(self.driver).commit()
        # 此处必须加强制等待，否则点击不到查询的数据
        time.sleep(4)
        templateinfo = {'name': templatename}
        return templateinfo

    def gettemplateinfo(self):
        name = TemplatePage(self.driver).getname()
        role = TemplatePage(self.driver).getrole()
        showloaction = TemplatePage(self.driver).getshowLocation()
        templatetype = TemplatePage(self.driver).gettemplatetype()
        displaytype = TemplatePage(self.driver).getdisplaytype()
        describe = TemplatePage(self.driver).getdescribe()
        relationfaqtype = TemplatePage(self.driver).getrelationfaqtype()
        relationfaqcontent = TemplatePage(self.driver).getrelationfaqcontent()
        ticketcolor = TemplatePage(self.driver).getticketcolor()
        valid = TemplatePage(self.driver).getvalid()
        templateinfo = {'name': name, 'role': role, 'showloaction': showloaction, 'templatetype': templatetype,
                        'displayType':  displaytype, 'describe': describe, 'relationFaqType': relationfaqtype,
                        'relationFaqContent': relationfaqcontent, 'ticketColor': ticketcolor, 'valid': valid}
        return templateinfo

    def templatefullCommon(self, type1):
        EntranceAgentPage(self.driver).enter_tickettemplate()
        time.sleep(6)
        TemplatePage(self.driver).addtemplate()
        templatename = '工单模板全填' + time.strftime('%Y%m%d%M%S', time.localtime())
        TemplatePage(self.driver).inputname(templatename)
        TemplatePage(self.driver).clickagent()
        # TemplatePage(self.driver).choserole('Junk')   # 角色跳过选择 0803
        TemplatePage(self.driver).clickshowLocation()
        TemplatePage(self.driver).clickselectall()
        TemplatePage(self.driver).clickcloseOption()
        time.sleep(2)
        if type1 == 'create':
            TemplatePage(self.driver).chosecreateticket()
        else:
            TemplatePage(self.driver).choseprocessticket()
        # 选择显示类型、描述、关联知识库类型、关联知识库内容
        TemplatePage(self.driver).chosecommonform()
        TemplatePage(self.driver).inputdescribe('全填创建模板')
        TemplatePage(self.driver).chosecategory()
        # TemplatePage(self.driver).chosemisc()    # 关联知识库内容跳过选择 0803
        TemplatePage(self.driver).inputcolor('#666')
        TemplatePage(self.driver).clickimg()
        # TemplatePage(self.driver).chosevaild()
        TemplatePage(self.driver).commit()
        # 此处必须加强制等待，否则点击不到查询的数据
        time.sleep(2)
        templateinfo = {'name': templatename}
        return templateinfo

    # 填写必填，不提交信息
    def templateRequiredCommon2(self,type1):
        EntranceAgentPage(self.driver).enter_tickettemplate()
        time.sleep(6)
        TemplatePage(self.driver).addtemplate()
        templatename = '必填' + time.strftime('%Y%m%d%M%S', time.localtime())
        TemplatePage(self.driver).inputname(templatename)
        TemplatePage(self.driver).clickweb()
        if type1 == 'create':
            TemplatePage(self.driver).chosecreateticket()
        else:
            TemplatePage(self.driver).choseprocessticket()
        # TemplatePage(self.driver).chosecreateticket()
        templateinfo = {'name': templatename}
        return templateinfo

    # 添加自定义字段--下拉类型
    def fullSelectFieldCommon(self):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        sysField = str('sys' + strnumber)
        name = str('name' + strnumber)
        TemplatePage(self.driver).clickaddfield()

        # TemplatePage(self.driver).fieldType()
        # TemplatePage(self.driver).selectType()
        # TemplatePage(self.driver).sysField(sysField)
        # TemplatePage(self.driver).fieldName(name)
        # TemplatePage(self.driver).addFieldBtn()
        # TemplatePage(self.driver).addFieldBtn()
        # TemplatePage(self.driver).addFieldBtn()
        # TemplatePage(self.driver).fileTypeKey0('key0')
        # TemplatePage(self.driver).fileTypeValue0('value0')
        # TemplatePage(self.driver).fileTypeKey1('key1')
        # TemplatePage(self.driver).fileTypeValue1('value1')
        # TemplatePage(self.driver).fileTypeKey2('key2')
        # TemplatePage(self.driver).fileTypeValue2('value2')

        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).selectType()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        FieldPage(self.driver).addFieldBtn()
        FieldPage(self.driver).addFieldBtn()
        FieldPage(self.driver).addFieldBtn()
        FieldPage(self.driver).fileTypeKey0('key0')
        FieldPage(self.driver).fileTypeValue0('value0')
        FieldPage(self.driver).fileTypeKey1('key1')
        FieldPage(self.driver).fileTypeValue1('value1')
        FieldPage(self.driver).fileTypeKey2('key2')
        FieldPage(self.driver).fileTypeValue2('value2')

        TemplatePage(self.driver).fieldsubmi()
        fieldInfo = {'sysField': sysField, 'name': name}
        return fieldInfo

    # 添加自定义的字段--日期/日期时间，复选类字段
    def  fullSelectFieldCommon02(self, type = 'date'):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        sysField = str('sys' + strnumber)
        name = str('name' + strnumber)
        TemplatePage(self.driver).clickaddfield()
        FieldPage(self.driver).fieldType()
        if type == 'date':
            # TemplatePage(self.driver).clickaddfield()
            # FieldPage(self.driver).fieldType()
            TemplatePage(self.driver).dateType()
            FieldPage(self.driver).sysField(sysField)
            FieldPage(self.driver).fieldName(name)
            TemplatePage(self.driver).fieldsubmi()

        elif type == 'datetime':
            # TemplatePage(self.driver).clickaddfield()
            # FieldPage(self.driver).fieldType()
            TemplatePage(self.driver).datetimeType()
            FieldPage(self.driver).sysField(sysField)
            FieldPage(self.driver).fieldName(name)
            TemplatePage(self.driver).fieldsubmi()

        else:
            # TemplatePage(self.driver).clickaddfield()
            # FieldPage(self.driver).fieldType()
            TemplatePage(self.driver).checkboxType()
            FieldPage(self.driver).sysField(sysField)
            FieldPage(self.driver).fieldName(name)
            FieldPage(self.driver).addFieldBtn()
            FieldPage(self.driver).addFieldBtn()
            FieldPage(self.driver).addFieldBtn()
            FieldPage(self.driver).fileTypeKey0('key0')
            FieldPage(self.driver).fileTypeValue0('value0')
            FieldPage(self.driver).fileTypeKey1('key1')
            FieldPage(self.driver).fileTypeValue1('value1')
            FieldPage(self.driver).fileTypeKey2('key2')
            FieldPage(self.driver).fileTypeValue2('value2')
            TemplatePage(self.driver).fieldsubmi()

        fieldInfo = {'sysField': sysField, 'name': name}
        return fieldInfo







