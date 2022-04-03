"""
@author: DT_testing
@file:   agent_common.py
@desc:  【】
@step：
"""
import time

from src.page.agent.agent_page import AgentPage
from src.page.agent.entrance_agent_page import EntranceAgentPage
import random


class AgentCommon(AgentPage):

    # 添加服务人员，填写必填项
    def agentRequiredCommon(self):
        string=time.strftime('%M%S', time.localtime())
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        fullname=str('杨航' + string)
        password='123456'
        userlogin=str('YangHang' + string)
        # 0805修改手机号格式需要严格校验
        #usermobile=str(strnumber)
        #usermobile = '138'+str(random.randint(10000000, 99999999))
        usermobile = ''
        #useremail=str(strnumber + '@a123.com')
        useremail = ''
        EntranceAgentPage(self.driver).enter_agent()
        time.sleep(1)
        # 进入添加agent界面
        AgentPage(self.driver).addagent()
        time.sleep(2)
        AgentPage(self.driver).fullname(fullname)
        # AgentPage(self.driver).lastname(lastname)
        AgentPage(self.driver).userlogin(str(userlogin))
        AgentPage(self.driver).userpw(password)
        # 0814修改填写的必填项
        # AgentPage(self.driver).usermobile(str(usermobile))
        # AgentPage(self.driver).useremail(str(useremail))
        AgentPage(self.driver).comandre()
        time.sleep(10)
        userInfo={'fullname': fullname, 'userlogin': userlogin, 'usermobile': usermobile, 'useremail': useremail}
        return userInfo

    def agentRequiredCommon2(self):
        string = time.strftime('%M%S', time.localtime())
        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        fullname = str('杨航' + string)
        password = '123456'
        userlogin = str('yanghang' + string)
        usermobile = ''
        useremail = ''
        time.sleep(1)
        # 进入添加agent界面
        # AgentPage(self.driver).addagent()
        time.sleep(2)
        AgentPage(self.driver).fullname(fullname)
        # AgentPage(self.driver).lastname(lastname)
        AgentPage(self.driver).userlogin(str(userlogin))
        userInfo = {'fullname': fullname, 'userlogin': userlogin, 'usermobile': usermobile, 'useremail': useremail}
        return userInfo

    # 必填创建服务人员，填写密码，可登陆,密码123456
    def agentRequiredCommon3(self):
        string=time.strftime('%M%S', time.localtime())
        fullname=str('杨航' + string)
        password='123456'
        userlogin=str('yanghang' + string)
        EntranceAgentPage(self.driver).enter_agent()
        time.sleep(1)
        # 进入添加agent界面
        AgentPage(self.driver).addagent()
        time.sleep(2)
        AgentPage(self.driver).fullname(fullname)
        AgentPage(self.driver).userlogin(str(userlogin))
        AgentPage(self.driver).userpw(password)
        AgentPage(self.driver).comandre()
        time.sleep(3)
        userInfo={'fullname': fullname, 'userlogin': userlogin}
        return userInfo


    # 添加服务人员，字段全部填写
    def fullAgentCommon(self):
        string=time.strftime('%M%S', time.localtime())
        strnumber=time.strftime('%y%m%d%M%S', time.localtime())
        position=str('职位' + string)
        fullname=str('杨航' + string)
        firstname='杨'
        lastname='航'
        jobnumber=str('A' + strnumber)
        password='123456'
        userlogin=str('yanghang' + string)
        # usermobile=str(strnumber)
        usermobile = '138' + str(random.randint(10000000, 99999999))
        useremail=str(strnumber + '@a123.com')
        city=string
        EntranceAgentPage(self.driver).enter_agent()
        time.sleep(3)
        # 进入添加agent界面
        time.sleep(3)
        AgentPage(self.driver).addagent()
        time.sleep(3)
        AgentPage(self.driver).position(position)
        AgentPage(self.driver).fullname(fullname)
        # AgentPage(self.driver).lastname(lastname)
        AgentPage(self.driver).jobnumber(jobnumber)
        AgentPage(self.driver).userlogin(userlogin)
        AgentPage(self.driver).userpw(password)
        AgentPage(self.driver).usermobile(usermobile)
        AgentPage(self.driver).useremail(useremail)
        AgentPage(self.driver).usercity(city)
        time.sleep(4)
        AgentPage(self.driver).comandre()
        # AgentPage(self.driver).next01()
        # AgentPage(self.driver).group01()
        # AgentPage(self.driver).groupValue01()
        # AgentPage(self.driver).regruop01()
        # AgentPage(self.driver).commit()
        # time.sleep(2)
        # AgentPage(self.driver).goback()
        time.sleep(5)
        userInfo={'position': position, 'fullname': fullname, 'jobnumber': jobnumber, 'userlogin': userlogin,
                  'usermobile': usermobile, 'useremail': useremail, 'city': city}
        return userInfo
