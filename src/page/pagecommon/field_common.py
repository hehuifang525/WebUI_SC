"""
@author: DT_testing
@file:   field_common.py
@desc:  【】
@step：
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.field_page import FieldPage
import time
from common.base import Base


class FieldCommon(FieldPage):

    # 添加自定义字段--只填写必填项   # 0723修改ok
    def fieldRequiredCommon(self, objectType):
        strnumber=time.strftime('%Y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()   # 0723修改
        FieldPage(self.driver).objectType()
        time.sleep(2)
        if objectType == 'Ticket':
            FieldPage(self.driver).objectTicket()
        elif objectType == 'ITSM':
            FieldPage(self.driver).objectITSM()
        elif objectType == 'FAQ':
            FieldPage(self.driver).objectFAQ()
        elif objectType == 'CustomerUser':
            FieldPage(self.driver).objectComuser()
        elif objectType == 'Customer':
            FieldPage(self.driver).objectCompany()
        elif objectType == 'Contract':
            FieldPage(self.driver).objectContract()
        elif objectType == 'Article':
            FieldPage(self.driver).objectArticle()
        else:
            FieldPage(self.driver).objectTicket()

        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        FieldPage(self.driver).submit()
        fieldInfo={'sysField': sysField, 'name': name}
        return fieldInfo

    # 添加自定义字段--文本类型
    def fullTextFieldCommon(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).textType()
        # FieldPage(self.driver).choiceTextType()
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        # FieldPage(self.driver).userInvisible()
        FieldPage(self.driver).regex('^[0-9]*$')
        FieldPage(self.driver).regexHint('只能输入数字')
        FieldPage(self.driver).hintType()
        FieldPage(self.driver).hintTypeValue03()
        FieldPage(self.driver).hintContent('请填写')
        FieldPage(self.driver).formula('12')
        FieldPage(self.driver).submit()
        fieldInfo={'sysField': sysField, 'name': name}
        return fieldInfo

    # 添加自定义字段--下拉类型
    def fullSelectFieldCommon(self):
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        sysField=str('sys' + strnumber)
        name=str('name' + strnumber)
        EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()
        FieldPage(self.driver).fieldType()
        FieldPage(self.driver).selectType()
        FieldPage(self.driver).objectType()
        FieldPage(self.driver).objectTicket()
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)
        # FieldPage(self.driver).userInvisible()
        Base(self.driver).move_to_pagebottom()
        FieldPage(self.driver).addFieldBtn()
        FieldPage(self.driver).addFieldBtn()
        Base(self.driver).move_to_pagebottom()
        FieldPage(self.driver).addFieldBtn()
        FieldPage(self.driver).fileTypeKey0('key0')
        FieldPage(self.driver).fileTypeValue0('value0')
        FieldPage(self.driver).fileTypeKey1('key1')
        FieldPage(self.driver).fileTypeValue1('value1')
        FieldPage(self.driver).fileTypeKey2('key2')
        FieldPage(self.driver).fileTypeValue2('value2')
        time.sleep(2)
        # 0819屏蔽，只有文本类字段才有正则
        # FieldPage(self.driver).regex('^[0-9]*$')
        # FieldPage(self.driver).regexHint('只能输入数字')
        # FieldPage(self.driver).hintType()
        # FieldPage(self.driver).hintTypeValue03()
        # FieldPage(self.driver).hintContent('请填写')
        # FieldPage(self.driver).formula('12')
        FieldPage(self.driver).submit()
        fieldInfo={'sysField': sysField, 'name': name}
        return fieldInfo

    # 创建字段，输入值，类型/对象为变量
    def createFieldCommon(self,fieldType='文本',objectType='Ticket'):
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        sysField = str('sys' + strnumber)
        name = str('name' + strnumber)
        # EntranceAgentPage(self.driver).enter_filed()
        FieldPage(self.driver).add()

        # 选择类型
        if fieldType == '下拉选择框':
            # 点击类型
            FieldPage(self.driver).fieldType()
            FieldPage(self.driver).selectType()
        elif fieldType == '字段组':
            FieldPage(self.driver).FieldGroup()

        else:
            # 点击类型,默认是文本
            FieldPage(self.driver).fieldType()
            FieldPage(self.driver).textType()

        # 点击对象
        FieldPage(self.driver).objectType()
        # 选择对象
        if objectType == 'Ticket':
            FieldPage(self.driver).objectTicket()
        elif objectType == 'ITSM':
            FieldPage(self.driver).objectITSM()
        elif objectType == 'FAQ':
            FieldPage(self.driver).objectFAQ()
        elif objectType == 'CustomerUser':
            FieldPage(self.driver).objectComuser()
        elif objectType == 'Customer':
            FieldPage(self.driver).objectCompany()
        elif objectType == 'Contract':
            FieldPage(self.driver).objectContract()
        elif objectType == 'Article':
            FieldPage(self.driver).objectArticle()
        else:
            FieldPage(self.driver).objectTicket()

        # 输入系统字段/字段名称
        FieldPage(self.driver).sysField(sysField)
        FieldPage(self.driver).fieldName(name)

        fieldInfo = {'sysField': sysField, 'name': name}
        return fieldInfo

