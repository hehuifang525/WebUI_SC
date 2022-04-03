"""
@author: DT_testing
@file:   agent_case.py
@desc:  【】
@step： 001. 检查角色面包屑（路径）、服务人员默认列表头、url title（SC_User_1，SC_User_5）
        002. 检查添加页面的“返回”按钮（SC_User_16，SC_User_17）
        003. 只填写必填项新增组检查（SC_User_18）
        004. 填写所有值 b.二次进入页面检查已填写内容（SC_User_19）
        005. 添加无效的服务人员(SC_User_77，SC_User_78)
        006. 编辑服务人员关联的角色，二次进入查看
        007. 编辑，不修改内容直接提交（SC_User_20）
        008. 更新必填项,查看（SC_User_21）
        009. 更新非必填项，查看（SC_User_22）
        010. 必填项不填写时，下一步按钮，提交并返回按钮检验(SC_User_23)
        011. 必填项输入空格时，下一步按钮，提交并返回按钮检验(SC_User_24，SC_User_36)
        012. 验证姓名，账号输入框特殊字符（SC_User_25，SC_User_29）
        013. 验证输入框字符长度（SC_User_26，SC_User_30）
        014. 重复检验（SC_User_28）
        015. 正确手机号检验（SC_User_32）
        016. 输入10位 ，12位号码检验（SC_User_33，SC_User_34）
        017. 验证手机号重复（SC_User_35）
        018. 验证手机号特殊字符不能成功提交（SC_User_38，SC_User_39）
        019. 验证邮箱重复（SC_User_42）
        020. 验证邮箱格式（SC_User_41，SC_User_43，SC_User_44，SC_User_45，SC_User_46，SC_User_47，SC_User_48，SC_User_49，SC_User_50，SC_User_51）
        021. 验证密码输入字符(SC_User_54)
        022. 验证修改密码(SC_User_55)
        023. 验证输入已存在工号（SC_User_57）
        024. 导入
        025. 检查服务人员列表左侧角色搜索(SC_User_80)

"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.agent_page import AgentPage
from src.page.pagecommon.get_time_common import GetTimeCommon
from src.testcase.testcase_base.basecase_user import BaseCaseUser
from common.base import Base
from common.logger import Logger
from src.page.pagecommon.agent_common import AgentCommon
from src.page.agent.agent_login_page import AgentLoginPage
from src.page.pagecommon.role_common import RoleCommon
from src.page.agent.role_page import RolePage
import random


class Agent(BaseCaseUser, Base):
    # logger=Logger(logname='log.txt', loglevel=1, logger="fox").getlog()
    # logger=Logger(logger="BasePage").getlog()

    # 1.检查列表页面
    def test_001_userlist(self):
        try:
            EntranceAgentPage(self.driver).enter_agent()
            # 打开页面过慢必须增加等待，否则数据取错
            time.sleep(10)
            # 检查页面路径
            roadText=AgentPage(self.driver).getroadText()
            roadText = str.replace(roadText,' ','')
            time.sleep(3)
            # 检查页面title
            titleText=AgentPage(self.driver).get_title()
            # 检查列表表头
            for listheader01 in ['.ant-table-thead th']:
                for i in range(0, 8):
                    time.sleep(2)
                    text=self.driver.find_elements_by_css_selector(listheader01)[i].text
                    if text != '工号' and text != '账号' and text != '姓名' and text != '姓' and text != '名' and text != '手机' \
                            and text != '邮件' and text != '有效性':
                        print("服务人员列表表头显示不正确！---- " + text)
            assert roadText == '/系统管理/服务人员', '服务人员列表路径显示不正确'
            assert titleText == '服务人员', '服务人员列表当前窗口 title 显示不正确'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('路径错误' + str(msg))

    # 2.检查添加页面返回按钮
    def test_002_returnAgent(self):
        try:
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(3)
            AgentPage(self.driver).addagent()
            time.sleep(5)
            AgentPage(self.driver).returnAg()
            time.sleep(3)
            # 返回页面后，搜索root@localhost
            addValue=str.replace(AgentPage(self.driver).getAdd(),' ','')
            assert addValue == '添加', '返回服务人员列表页面错误'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('返回服务人员列表页面错误' + str(msg))

    # 3.只填写必填项
    def test_003_addAgent(self):
        # 进入agent界面
        try:
            userInfo=AgentCommon(self.driver).agentRequiredCommon()
            # 判断添加后，列表中的服人员数据是否正确
            # 先搜索出来添加的数据
            # 提交后loading时间过长，导致输入搜索内容失败
            AgentPage(self.driver).search(str(userInfo.get('userlogin')))
            time.sleep(10)
            userInfolist = ['', str(userInfo.get('userlogin')), userInfo.get('fullname'), userInfo.get('fullname'), '航', str(userInfo.get('usermobile'))
                            , str(userInfo.get('useremail')), '有效']
            for FiledList01 in ['.ant-table-row.ng-star-inserted td']:
                for i in range(0, 8):
                    text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
                    text_zoom_01=''.join(text_zoom_01.split())
                    # print(i , userInfolist[i],'1', text_zoom_01)
                    # self.assertEqual(text_zoom_01, userInfolist[i], msg='添加服务人员数据列表展示不正确')
                    if text_zoom_01 != '' and text_zoom_01 != str(
                            userInfo.get('userlogin')) and text_zoom_01 != userInfo.get(
                        'fullname') and text_zoom_01 != userInfo.get('fullname') and text_zoom_01 != '航' \
                            and text_zoom_01 != str(userInfo.get('usermobile')) and text_zoom_01 != str(
                        userInfo.get('useremail')) and text_zoom_01 != '有效':
                        print("添加服务人员数据列表展示不正确！---- " + text_zoom_01)
        except Exception as msg:
            # Base.get_windows_img(self)
            Base.get_windows_img(self)
            self.logger.error('服务人员添加不成功:' + str(msg))


    # 4.字段全部填写
    # def test_004_addAgent(self):
    #     try:
    #         userInfo=AgentCommon(self.driver).fullAgentCommon()
    #         # 判断添加后，列表中的服人员数据是否正确
    #         AgentPage(self.driver).search(userInfo.get('userlogin'))
    #         for FiledList01 in ['.ant-table-tbody  td']:
    #             for i in range(0, 8):
    #                 text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
    #                 text_zoom_01=''.join(text_zoom_01.split())
    #                 if text_zoom_01 != userInfo.get('position') and text_zoom_01 != userInfo.get(
    #                         'userlogin') and text_zoom_01 != userInfo.get(
    #                     'fullname') and text_zoom_01 != '' and text_zoom_01 != '' \
    #                         and text_zoom_01 != userInfo.get('usermobile') and text_zoom_01 != userInfo.get(
    #                     'useremail') and text_zoom_01 != '有效':
    #                     print("添加服务人员数据列表展示不正确！---- " + text_zoom_01)
    #         # 检验添加时选择的角色
    #         AgentPage(self.driver).details()
    #         AgentPage(self.driver).next01()
    #         # 获取添加的角色
    #         group_text=AgentPage(self.driver).groupText()
    #         assert group_text == 'Postmaster', '服务人员没有成功关联组' + group_text
    #     except Exception as msg:
    #         Base.get_windows_img(self)
    #         self.logger.error('服务人员没有成功关联组' + str(msg))

    # 0814 无效tab id被丢弃  0818修改恢复
    def test_005_addAgent(self):
        """添加无效的服务人员"""
        try:
            # 填写必填项
            userInfo=AgentCommon(self.driver).agentRequiredCommon()
            AgentPage(self.driver).search(userInfo.get('userlogin'))
            AgentPage(self.driver).details()
            time.sleep(0.5)
            AgentPage(self.driver).vaild()
            time.sleep(1)
            AgentPage(self.driver).selectInvaild()
            time.sleep(2)
            AgentPage(self.driver).comandre()
            time.sleep(3)
            AgentPage(self.driver).invalidList()
            time.sleep(10)
            AgentPage(self.driver).search(userInfo.get('userlogin'))
            # 必须添加
            time.sleep(5)
            new_user_info = ['',userInfo.get('jobnumber'),userInfo.get('userlogin'),userInfo.get('fullname'),userInfo.get('usermobile'),
                              userInfo.get('useremail'),"航","切换到服务人员","无效"]
            list_td =AgentPage(self.driver).list_td()
            for i in range(0, len(list_td)):
                text_zoom_01=list_td[i].text
                text_zoom_01=''.join(text_zoom_01.split())
                # print(text_zoom_01)
                with self.subTest(i=i):
                    self.assertIn(text_zoom_01,new_user_info,msg="无效列表数据展示错误")
            AgentPage(self.driver).details()
            time.sleep(2)
            AgentPage(self.driver).selectvaild()
            time.sleep(0.5)
            AgentPage(self.driver).comandre()
            time.sleep(4)
            AgentPage(self.driver).validList()
            time.sleep(2)
            AgentPage(self.driver).search(userInfo.get('userlogin'))
            time.sleep(5)
            new_user_info02 = ['', userInfo.get('jobnumber'), userInfo.get('userlogin'), userInfo.get('fullname'),
                             userInfo.get('usermobile'),"航",
                             userInfo.get('useremail'), "切换到服务人员", "有效"]
            list_td02 = AgentPage(self.driver).list_td()
            for i in range(0, len(list_td)):
                text_zoom_02 = list_td02[i].text
                text_zoom_02 = ''.join(text_zoom_02.split())
                with self.subTest(i=i):
                    self.assertIn(text_zoom_02, new_user_info02, msg="无效切换到有效列表数据展示错误")

            # for FiledList01 in ['.ant-table-row.ng-star-inserted td']:
            #     for i in range(0, 7):
            #         text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
            #         text_zoom_01=''.join(text_zoom_01.split())
            #         if text_zoom_01 != str(userInfo.get('jobnumber')) and text_zoom_01 != str(userInfo.get('userlogin')) \
            #                 and text_zoom_01 != userInfo.get('fullname') and text_zoom_01 != '' and text_zoom_01 != '航' \
            #                 and text_zoom_01 != str(userInfo.get('usermobile')) and text_zoom_01 != str(
            #             userInfo.get('useremail')) \
            #                 and text_zoom_01 != '有效':
            #             print("添加服务人员数据列表展示不正确！---- " + text_zoom_01)
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('添加服务人员数据列表展示不正确' + str(msg))

    # 6.编辑角色，二次进入查看
    # def test_006_editAgent(self):
    #     now_time=GetTimeCommon(self.driver).get_time()
    #     phone=str(GetTimeCommon(self.driver).get_number())
    #     name='姓名' + str(now_time)
    #     login='u' + str(phone)
    #     email=str(phone + '@123.com')
    #     EntranceAgentPage(self.driver).enter_agent()
    #     AgentPage(self.driver).addagent()
    #     AgentPage(self.driver).fullname(name)
    #     AgentPage(self.driver).userlogin(login)
    #     AgentPage(self.driver).userpw('123456')
    #     AgentPage(self.driver).usermobile(phone)
    #     AgentPage(self.driver).useremail(email)
    #     AgentPage(self.driver).next01()
    #     AgentPage(self.driver).group01()
    #     AgentPage(self.driver).groupValue01()
    #     AgentPage(self.driver).group01()
    #     AgentPage(self.driver).commit()
    #     time.sleep(2)
    #     AgentPage(self.driver).search(login)
    #     AgentPage(self.driver).details()
    #     AgentPage(self.driver).next01()
    #     AgentPage(self.driver).group01()
    #     AgentPage(self.driver).groupValue01()
    #     AgentPage(self.driver).groupValue02()
    #     AgentPage(self.driver).group01()
    #     AgentPage(self.driver).commit()
    #     time.sleep(2)
    #     AgentPage(self.driver).search(login)
    #     AgentPage(self.driver).details()
    #     AgentPage(self.driver).next01()
    #     group_text=AgentPage(self.driver).groupText()
    #     assert group_text == 'Raw', '服务人员没有成功编辑角色' + group_text

    # 7.编辑，不修改内容直接提交  -关联角色未处理
    # def test_007_editAgent(self):
    #     userInfo=AgentCommon(self.driver).fullAgentCommon()
    #     AgentPage(self.driver).search(userInfo.get('userlogin'))
    #     AgentPage(self.driver).details()
    #     AgentPage(self.driver).comandre()
    #     AgentPage(self.driver).search(userInfo.get('userlogin'))
    #     for FiledList01 in ['.ant-table-tbody  td']:
    #         for i in range(0, 8):
    #             text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
    #             text_zoom_01=''.join(text_zoom_01.split())
    #             if text_zoom_01 != userInfo.get('jobnumber') and text_zoom_01 != userInfo.get(
    #                     'userlogin') and text_zoom_01 != userInfo.get('fullname') and \
    #                     text_zoom_01 != '' and text_zoom_01 != '航' and text_zoom_01 != userInfo.get('usermobile') and \
    #                     text_zoom_01 != userInfo.get('useremail') and text_zoom_01 != '有效':
    #                 print("添加服务人员数据列表展示不正确！---- " + text_zoom_01)

    # 8.更新必填项
    def test_008_editAgent(self):
        try:
            phone=GetTimeCommon(self.driver).get_mobile()
            email=str(phone + '@123.com')
            userlogin=str('login' + phone)
            fullname=str('name' + phone)
            userInfo=AgentCommon(self.driver).agentRequiredCommon()
            # print(userInfo,'1111')
            AgentPage(self.driver).search(userInfo.get('userlogin'))
            AgentPage(self.driver).details()
            time.sleep(5)
            # 编辑输入信息
            AgentPage(self.driver).userlogin(userlogin)
            AgentPage(self.driver).fullname(fullname)
            # 邮箱，手机号的输入，校验异常慢，屏蔽输入20220104
            # AgentPage(self.driver).usermobile(phone)
            # AgentPage(self.driver).useremail(email)
            AgentPage(self.driver).comandre()
            time.sleep(2)
            AgentPage(self.driver).search(userlogin)
            new_user_info = ['', userInfo.get('jobnumber'), userlogin, fullname,
                             phone,email, "航", "切换到服务人员", "有效"]
            time.sleep(1)
            list_td = AgentPage(self.driver).list_td()
            for i in range(0, len(list_td)):
                text_zoom_01 = list_td[i].text
                text_zoom_01 = ''.join(text_zoom_01.split())
                with self.subTest(i=i):
                    self.assertIn(text_zoom_01, new_user_info, msg="编辑必填后列表数据展示错误")
            # for FiledList01 in ['.ant-table-row.ng-star-inserted td']:
            #     for i in range(0, 8):
            #         text_zoom_01=self.driver.find_elements_by_css_selector(FiledList01)[i].text
            #         text_zoom_01=''.join(text_zoom_01.split())
            #         if text_zoom_01 != '' and text_zoom_01 != userlogin and text_zoom_01 != fullname and text_zoom_01 != '' \
            #                 and text_zoom_01 != ''  and text_zoom_01 != '有效':
            #             print("添加服务人员数据列表展示不正确！---- " + text_zoom_01)
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('更新必填项出错' + str(msg))

    # 9.更新非必填项  --关联角色未处理
    # def test_009_editAgent(self):
    #     phone=GetTimeCommon(self.driver).get_number()
    #     position='pos' + phone
    #     jobnumber='job' + phone
    #     city='city' + phone
    #     userInfo=AgentCommon(self.driver).fullAgentCommon()
    #     time.sleep(3)
    #     AgentPage(self.driver).search(userInfo.get('userlogin'))
    #     AgentPage(self.driver).details()
    #     AgentPage(self.driver).position(position)
    #     AgentPage(self.driver).jobnumber(jobnumber)
    #     AgentPage(self.driver).usercity(city)
    #     AgentPage(self.driver).comandre()
    #     AgentPage(self.driver).search(userInfo.get('userlogin'))
    #     AgentPage(self.driver).details()
    #     userTitle=AgentPage(self.driver).getPosition()
    #     print(userTitle)
    #     jobNumber=AgentPage(self.driver).getJobnumber()
    #     city=AgentPage(self.driver).getCity()
    #     assert userTitle == position, '编辑服务人员职位不正确'
    #     assert jobNumber == jobnumber, '编辑服务人员工号不正确'
    #     assert city == city, '编辑服务人员城市不正确'

    # 10.必填项不填写时，下一步按钮，提交并返回按钮检验
    # 0730检查发现该模块必填项发生变更:必填项为姓名、姓、名、账号、有效性
    def test_010_editAgent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            phone=GetTimeCommon(self.driver).get_number()
            email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(3)
            AgentPage(self.driver).addagent()  # 进入添加agent界面
            time.sleep(3)
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：不填写必填项时，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：不填写必填项时，提交并返回列表按钮可点击'
            AgentPage(self.driver).fullname(name)
            time.sleep(2)
            nextColor1=AgentPage(self.driver).getNextColor()
            comColor1=AgentPage(self.driver).getComColor()
            assert str(nextColor1) == 'true', '错误：只填写姓名时，下一步按钮可点击'
            assert str(comColor1) == 'true', '错误：只填写姓名时，提交并返回列表按钮可点击'
            AgentPage(self.driver).userlogin(login)
            # time.sleep(2)
            # nextColor2=AgentPage(self.driver).getNextColor()
            # comColor2=AgentPage(self.driver).getComColor()
            # assert str(nextColor2) == 'background-color: rgb(191, 191, 191);', '错误：只填写姓名和账号时，下一步按钮可点击'
            # assert str(comColor2) == 'background-color: rgb(191, 191, 191);', '错误：只填写姓名和账号时，提交并返回列表按钮可点击'
            # AgentPage(self.driver).usermobile(phone)
            # nextColor3=AgentPage(self.driver).getNextColor()
            # comColor3=AgentPage(self.driver).getComColor()
            # assert str(nextColor3) == 'background-color: rgb(191, 191, 191);', '错误：不填写邮箱时，下一步按钮可点击'
            # assert str(comColor3) == 'background-color: rgb(191, 191, 191);', '错误：不填写邮箱时，提交并返回列表按钮可点击'
            # AgentPage(self.driver).useremail(email)
            # 1124 样式变更，屏幕该颜色取值
            # nextColor4=AgentPage(self.driver).getNextColor()
            # comColor4=AgentPage(self.driver).getComColor()
            # assert str(nextColor4) == 'background-color: rgb(52, 152, 166);', '错误：填写所有必填项时，下一步按钮不可点击'
            # assert str(comColor4) == 'background-color: rgb(52, 152, 166);', '错误：填写所有必填项时，提交并返回列表按钮不可点击'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('必填项不填写时，下一步按钮，提交并返回出错' + str(msg))

    # 11.必填项输入空格时，下一步按钮，提交并返回按钮检验
    def test_011_editAgent(self):
        try:
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(3)
            # 进入添加agent界面
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).fullname('      ')
            AgentPage(self.driver).lastname('      ')
            AgentPage(self.driver).firstname('     ')
            AgentPage(self.driver).userlogin('     ')
            AgentPage(self.driver).usermobile('    ')
            AgentPage(self.driver).useremail('     ')
            time.sleep(3)
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误:必填项输入空格时，下一步按钮可点击'
            assert str(comColor) == 'true', '错误:必填项输入空格时，提交并返回列表按钮可点击'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('必填项输入空格时，下一步按钮，提交并返回按钮检验错误' + str(msg))

    # 12.验证姓名，账号输入框特殊字符  OK
    def test_012_editAgent(self):
        try:
            name=str(GetTimeCommon(self.driver).get_number() + 'abc !@#$%^&*_=[]{}')
            login=str(GetTimeCommon(self.driver).get_number() + 'abc !@#$%^&*_=[]{}')
            # phone=GetTimeCommon(self.driver).get_number()
            # email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(8)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            # 出现账号校验时间过长，提交按钮无法触发
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            # AgentPage(self.driver).usermobile(phone)
            # AgentPage(self.driver).useremail(email)
            time.sleep(4)
            AgentPage(self.driver).comandre()
            time.sleep(6)
            AgentPage(self.driver).search(login)
            time.sleep(2)
            AgentPage(self.driver).details()
            time.sleep(3)
            fullName=AgentPage(self.driver).getFullname()
            time.sleep(1)
            userLogin=AgentPage(self.driver).getUserLogin()
            time.sleep(1)
            self.assertEqual(name, fullName, msg='错误：姓名输入特殊字符验证不通过')
            self.assertEqual(login, userLogin, msg='错误：用户名输入特殊字符验证不通过')

        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('姓名，账号特殊字符验证错误' + str(msg))

    # 13.验证姓名，账号输入框字符长度 # 0723修改ok
    def test_013_editAgent(self):
        try:
            name=str(GetTimeCommon(self.driver).get_number())
            for i in range(0, 3):
                name+=name
            login=str(GetTimeCommon(self.driver).get_number())
            for i in range(0, 3):
                login+=login
            phone=GetTimeCommon(self.driver).get_number()
            email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(10)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            # AgentPage(self.driver).usermobile(phone)
            # AgentPage(self.driver).useremail(email)
            AgentPage(self.driver).comandre()
            time.sleep(2)
            AgentPage(self.driver).search(login)
            AgentPage(self.driver).details()
            # 打开编辑页面后，必须增加强制等待
            time.sleep(2)
            fullName=AgentPage(self.driver).getFullname()
            userLogin=AgentPage(self.driver).getUserLogin()
            assert name == fullName, '错误：姓名最大字符数200验证未通过'
            assert login == userLogin, '错误：用户名最大字符数200验证不通过'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('验证姓名，账号输入框字符长度错误' + str(msg))

    # 14.重复检验
    # 0809 数据校验耗时过长暂时屏蔽该用例  0814检查重复的id被丢弃  0828检查恢复
    def test_014_editAgent(self):
        try:
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(3)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).userlogin('root@localhost')
            time.sleep(5)
            loginMessage=AgentPage(self.driver).getLoginMessage()

            assert loginMessage == '数据校验不通过，该值已存在，请重新输入！', '服务人员账号重复校验功能不正确'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('账号重复校验出错' + str(msg))

    # 15.正确手机号检验--以13、14、15、16、17、18、19开头11位号码
    # #0814 手机号验证规则修改需要调整测试例子
    def test_015_editAgent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            phone=GetTimeCommon(self.driver).get_mobile()
            # email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(3)
            AgentPage(self.driver).addagent()
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            AgentPage(self.driver).usermobile(phone)
            # AgentPage(self.driver).useremail(email)
            time.sleep(2)
            AgentPage(self.driver).comandre()
            time.sleep(3)
            AgentPage(self.driver).search(login)
            AgentPage(self.driver).details()
            time.sleep(3)
            mobile01=AgentPage(self.driver).getUsermobile()
            mobile01=''.join(mobile01.split())
            assert phone == mobile01, '正确手机号不能够添加成功'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('手机格式验证错误' + str(msg))

    # 16.输入10位 ，12位号码检验
    def test_016_editAgent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            phone=GetTimeCommon(self.driver).get_mobile()
            phone1=phone[0:10]
            email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(10)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            AgentPage(self.driver).usermobile(phone1)
            time.sleep(6)
            AgentPage(self.driver).useremail(email)
            time.sleep(3)
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：手机号为10位时，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：手机号为10位时，提交并返回列表按钮可点击'
            AgentPage(self.driver).usermobile('23')
            time.sleep(3)
            nextColor1=AgentPage(self.driver).getNextColor()
            comColor1=AgentPage(self.driver).getComColor()
            assert str(nextColor1) == 'true', '错误：手机号为12位时，下一步按钮可点击'
            assert str(comColor1) == 'true', '错误：手机号为12位时，提交并返回列表按钮可点击'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('10位 ，12位号码检验错误' + str(msg))

    # 17.验证手机号重复
    # 0814 检查发现不对数据进行重复校验？？  0828恢复
    def test_017_editAgent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            # phone=GetTimeCommon(self.driver).get_mobile()
            phone = '138' + str(random.randint(10000000, 99999999))
            email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(10)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            AgentPage(self.driver).usermobile(phone)
            # AgentPage(self.driver).useremail(email)
            # 必须强制等待，等待检验结束
            time.sleep(2)
            AgentPage(self.driver).comandre()
            time.sleep(5)
            AgentPage(self.driver).addagent()
            name01=str('name' + GetTimeCommon(self.driver).get_number())
            login01=str('user' + GetTimeCommon(self.driver).get_number())
            phone01=GetTimeCommon(self.driver).get_mobile()
            email01=str(phone01 + '@123.com')
            AgentPage(self.driver).fullname(name01)
            AgentPage(self.driver).userlogin(login01)
            AgentPage(self.driver).usermobile(phone)
            time.sleep(6)
            # AgentPage(self.driver).useremail(email01)
            # time.sleep(5)
            mobileMessage=AgentPage(self.driver).getMobileMessage()
            assert mobileMessage == '数据校验不通过，该值已存在，请重新输入！', '手机号重复校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：手机号重复时，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：手机号重复时，提交并返回列表按钮可点击'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('验证手机号重复失败' + str(msg))

    # 18.验证手机号特殊字符不能成功提交
    def test_018_Agent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            phone='1a!@#$%^&*('
            email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            # time.sleep(10)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            AgentPage(self.driver).usermobile(phone)
            time.sleep(6)
            AgentPage(self.driver).useremail(email)
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            # print(nextColor , nextColor)
            assert str(nextColor) == 'true', '错误：手机号为特殊字符时，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：手机号为特殊字符时，提交并返回列表按钮可点击'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('验证手机号特殊字符不能成功提交失败' + str(msg))

    # 19.验证邮箱重复
    # 0809 邮箱校验时间过长，暂时屏蔽该用例  0828恢复
    def test_019_Agent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            # phone=GetTimeCommon(self.driver).get_mobile()
            phone= '138' + str(random.randint(10000000, 99999999))
            email=str(phone + '@123.com')
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(10)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            AgentPage(self.driver).usermobile(phone)
            AgentPage(self.driver).useremail(email)
            AgentPage(self.driver).comandre()
            time.sleep(8)
            AgentPage(self.driver).addagent()

            name01=str('name' + GetTimeCommon(self.driver).get_number())
            login01=str('user' + GetTimeCommon(self.driver).get_number())
            phone01= '138' + str(random.randint(10000000, 99999999))
            AgentPage(self.driver).fullname(name01)
            AgentPage(self.driver).userlogin(login01)
            AgentPage(self.driver).usermobile(phone01)
            AgentPage(self.driver).useremail(email)
            time.sleep(8)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            emailMessage = str.replace(emailMessage,' ','')
            # print(emailMessage,'4')
            self.assertEqual(emailMessage,'数据校验不通过，该值已存在，请重新输入！',msg='服务人员邮箱重复校验失败')
            #assert emailMessage == '数据校验不通过，该值已存在，请重新输入！', '邮箱重复校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱重复时，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱重复时，提交并返回列表按钮可点击'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('验证邮箱重复失败' + str(msg))

    # 20.验证邮箱格式
    # 0809  邮箱校验时间过长，暂时屏蔽该用例  0828恢复
    def test_020_Agent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            # phone=GetTimeCommon(self.driver).get_mobile()
            # phone= '138' + str(random.randint(10000000, 99999999))
            email='2邮箱123 abc'
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(10)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            # AgentPage(self.driver).usermobile(phone)
            AgentPage(self.driver).useremail(email)
            time.sleep(6)

            emailMessage=AgentPage(self.driver).getEmailMessage()
            # print(emailMessage,'1')
            self.assertEqual(emailMessage, '邮件格式错误。 请检查！', msg='邮箱格式校验功能不正确')
            # assert emailMessage == '数据格式错误,请重新输入！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)
            email='123abc.edf'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            # assert emailMessage == '数据格式错误,请重新输入!', '邮箱格式校验功能不正确'
            self.assertEqual(emailMessage, '邮件格式错误。 请检查！', msg='邮箱格式校验功能不正确')
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)

            email='abc123@ooo'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            assert emailMessage == '邮件格式错误。 请检查！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)

            email='@abc123'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            assert emailMessage == '邮件格式错误。 请检查！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)

            email='abc@.123opl'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            assert emailMessage == '邮件格式错误。 请检查！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)

            email='%q$ab@c.d'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            assert emailMessage == '邮件格式错误。 请检查！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)

            email='中国ab@c.d'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            assert emailMessage == '邮件格式错误。 请检查！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)

            email='w@e@ab@c.d'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            assert emailMessage == '邮件格式错误。 请检查！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
            AgentPage(self.driver).clearEmail()
            time.sleep(2)

            email='e.ab@c.d'
            AgentPage(self.driver).useremail(email)
            emailMessage=AgentPage(self.driver).getEmailMessage()
            assert emailMessage == '邮件格式错误。 请检查！', '邮箱格式校验功能不正确'
            nextColor=AgentPage(self.driver).getNextColor()
            comColor=AgentPage(self.driver).getComColor()
            assert str(nextColor) == 'true', '错误：邮箱格式不正确，下一步按钮可点击'
            assert str(comColor) == 'true', '错误：邮箱格式不正确，提交并返回列表按钮可点击'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('验证邮箱格式失败' + str(msg))

    # 21.验证密码输入字符
    def test_021_Agent(self):
        try:
            name=str('name' + GetTimeCommon(self.driver).get_number())
            login=str('user' + GetTimeCommon(self.driver).get_number())
            phone=GetTimeCommon(self.driver).get_mobile()
            email=str(phone + '@123.com')
            password='pw中文！@#!@#$%* '
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(10)
            AgentPage(self.driver).addagent()
            time.sleep(3)
            AgentPage(self.driver).userpw(password)
            AgentPage(self.driver).fullname(name)
            AgentPage(self.driver).userlogin(login)
            # AgentPage(self.driver).usermobile(phone)
            # AgentPage(self.driver).useremail(email)
            AgentPage(self.driver).comandre()
            time.sleep(2)
            EntranceAgentPage(self.driver).enter_home()
            time.sleep(2)
            AgentLoginPage(self.driver).logout_button()
            AgentLoginPage(self.driver).input_username(login)
            AgentLoginPage(self.driver).input_passwd(password)
            AgentLoginPage(self.driver).login_button()
            time.sleep(10)
            result=Base(self.driver).get_userLoginName()
            assert result == name, '密码中有特殊字符时登录失败'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('验证密码输入字符失败' + str(msg))

    # # 22.验证修改密码
    # def test_022_Agent(self):
    #     try:
    #         name=str('name' + GetTimeCommon(self.driver).get_number())
    #         login=str('user' + GetTimeCommon(self.driver).get_number())
    #         phone=GetTimeCommon(self.driver).get_mobile()
    #         email=str(phone + '@123.com')
    #         password='pw中文！@#!@#$%* '
    #         EntranceAgentPage(self.driver).enter_agent()
    #         time.sleep(10)
    #         AgentPage(self.driver).addagent()
    #         time.sleep(3)
    #         AgentPage(self.driver).userpw(password)
    #         AgentPage(self.driver).fullname(name)
    #         AgentPage(self.driver).userlogin(login)
    #         # AgentPage(self.driver).usermobile(phone)
    #         # AgentPage(self.driver).useremail(email)
    #         AgentPage(self.driver).comandre()
    #         time.sleep(2)
    #         AgentPage(self.driver).search(login)
    #         AgentPage(self.driver).details()
    #         time.sleep(3)
    #         AgentPage(self.driver).clearPassWord()
    #         password='123456'
    #         AgentPage(self.driver).userpw(password)
    #         AgentPage(self.driver).comandre()
    #         time.sleep(2)
    #         AgentLoginPage(self.driver).logout_button()
    #         AgentLoginPage(self.driver).input_username(login)
    #         AgentLoginPage(self.driver).input_passwd(password)
    #         AgentLoginPage(self.driver).login_button()
    #         time.sleep(8)
    #         result=Base(self.driver).get_userLoginName()
    #
    #         assert result == name, '更改密码失败'
    #     except Exception as msg:
    #         Base.get_windows_img(self)
    #         self.logger.error('更改密码失败' + str(msg))

    # 23.验证输入已存在工号  校验时间过长  0828恢复
    def test_023_Agent(self):
        userInfo=AgentCommon(self.driver).fullAgentCommon()
        AgentPage(self.driver).addagent()
        time.sleep(2)
        AgentPage(self.driver).jobnumber(userInfo.get('jobnumber'))
        time.sleep(2)
        JobNumMessage=AgentPage(self.driver).getJobNumMessage()
        assert JobNumMessage == '数据校验不通过，该值已存在，请重新输入！', '工号重复校验功能不正确'

        name=str('name' + GetTimeCommon(self.driver).get_number())
        login=str('user' + GetTimeCommon(self.driver).get_number())
        # phone=GetTimeCommon(self.driver).get_mobile()
        # email=str(phone + '@123.com')
        AgentPage(self.driver).fullname(name)
        AgentPage(self.driver).userlogin(login)
        # AgentPage(self.driver).usermobile(phone)
        # AgentPage(self.driver).useremail(email)
        time.sleep(2)
        nextColor=AgentPage(self.driver).getNextColor()
        comColor=AgentPage(self.driver).getComColor()
        assert str(nextColor) == 'true', '错误：工号重复，下一步按钮可点击'
        assert str(comColor) == 'true', '错误：工号重复，提交并返回列表按钮可点击'

    # #024.导入
    # def test_024_Agent(self):
    #     EntranceAgentPage(self.driver).enter_agent()
    #     AgentPage(self.driver).upload()
    #     time.sleep(2)
    #     AgentPage(self.driver).uploadFile('D:\桌面\Export_2020-06-12 15_39_41.xlsx')
    #     AgentPage(self.driver).agentImport()
    #     print(AgentPage(self.driver).getUploadResult())

    # 025. 检查服务人员列表左侧角色搜索  # 0723 ok
    def test_25_Agent(self):
        try:
            # name = RoleCommon(self.driver).rolerequiredcommon()
            # RolePage(self.driver).savereturnbtn()
            # time.sleep(2)
            EntranceAgentPage(self.driver).enter_agent()
            time.sleep(8)
            AgentPage(self.driver).searchRole('Postmaster')
            # AgentPage(self.driver).searchRole(name)
            time.sleep(5)
            role = str(AgentPage(self.driver).getSearchRole('Postmaster'))
            # role = str(AgentPage(self.driver).getSearchRole(name)).replace(' ','')
            # print(role)
            # print(name)
            time.sleep(3)
            # assert role == ' Postmaster ','服务人员页面，左侧搜索角色后显示不正确'
            self.assertEqual(role, ' Postmaster ', msg='服务人员页面，左侧搜索角色后显示不正确')
            #assert role == name, '服务人员页面，左侧搜索角色后显示不正确'
        except Exception as msg:
            Base.get_windows_img(self)
            self.logger.error('左侧搜索角色后显示不正确' + str(msg))