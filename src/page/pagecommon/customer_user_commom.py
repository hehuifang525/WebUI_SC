"""
@author: DT_testing
@file:   customer_user_common.py
@desc:  【创建必填值填写的客户、用户 及 全部填写字段的组】
@step：  都是客户用户页面内部的值填写
"""
import time
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.customer_user_page import CustomerUserPage
from src.page.pagecommon.get_time_common import GetTimeCommon
import random


class CustomerUserCommon(CustomerUserPage):

    # 填写必填值，创建客户
    def Companyrequiredcommon(self):
        EntranceAgentPage(self.driver).enter_customer_user()
        time.sleep(15)
        CustomerUserPage(self.driver).AddCompany()

        now_time = GetTimeCommon(self.driver).get_time()

        com_id = now_time[0:4]+now_time[5:7]+now_time[8:10]+now_time[11:13]+now_time[14:16]+now_time[17:]

        name = "company必填_" + com_id
        time.sleep(5)
        # 客户编号
        CustomerUserPage(self.driver).CustomerID(com_id)
        # 客户名称
        CustomerUserPage(self.driver).CompanyName(name)
        # 选择有效
        CustomerUserPage(self.driver).valid()
        return name, com_id
    # 填写必填，连续创建客户
    def Companyrequiredcommon2(self):

        CustomerUserPage(self.driver).AddCompany()
        now_time = GetTimeCommon(self.driver).get_time()
        com_id = now_time[0:4]+now_time[5:7]+now_time[8:10]+now_time[11:13]+now_time[14:16]+now_time[17:]
        name = "company必填_" + com_id
        # 客户编号
        CustomerUserPage(self.driver).CustomerID(com_id)
        # 客户名称
        CustomerUserPage(self.driver).CompanyName(name)
        # 选择有效
        CustomerUserPage(self.driver).valid()
        return name, com_id

    # 填写必填创建一个无效客户
    def Companyinvalidcommon(self):
        EntranceAgentPage(self.driver).enter_customer_user()
        time.sleep(10)
        CustomerUserPage(self.driver).AddCompany()

        now_time = GetTimeCommon(self.driver).get_time()

        com_id = now_time[0:4]+now_time[5:7]+now_time[8:10]+now_time[11:13]+now_time[14:16]+now_time[17:]

        name = "company必填_" + com_id
        # 客户编号
        CustomerUserPage(self.driver).CustomerID(com_id)
        # 客户名称
        CustomerUserPage(self.driver).CompanyName(name)
        # 选择有效
        CustomerUserPage(self.driver).invalid()
        return name, com_id


    # 取客户页面的搜索值
    def get_company_alltext(self):
        Companynum = CustomerUserPage(self.driver).CustomerID_text()
        # Responsible = CustomerUserPage(self.driver).Responsible_text()
        Companyname = CustomerUserPage(self.driver).CompanyName_text()
        ParentCustomer = CustomerUserPage(self.driver).ParentCustomer_text()
        District = CustomerUserPage(self.driver).CompanyDistrict_text()
        Street = CustomerUserPage(self.driver).CompanyStreet_text()
        ZIP = CustomerUserPage(self.driver).CompanyZIP_text()
        city = CustomerUserPage(self.driver).CompanyCity_text()
        Country = CustomerUserPage(self.driver).CompanyCountry_text()
        URL = CustomerUserPage(self.driver).CompanyURL_text()
        Comment = CustomerUserPage(self.driver).CompanyComment_text()
        valid = CustomerUserPage(self.driver).valid_text()
        return Companynum,Companyname,ParentCustomer,District,Street,ZIP,city,Country,URL,Comment,valid


    # 填写必填项添加用户
    def userrequiredcommom(self):
        # 需要新创建一个客户
        #EntranceAgentPage(self.driver).enter_customer_user()

        str1 = CustomerUserCommon(self.driver).Companyrequiredcommon()
        name = str1[0]
        login_num = str1[1]
        # time.sleep(3)
        # 提交
        CustomerUserPage(self.driver).Companysub()
        time.sleep(5)
        CustomerUserPage(self.driver).associate_GoBack()
        time.sleep(2)
        # 点击点击用户
        CustomerUserPage(self.driver).adduser()
        # CustomerUserPage(self.driver).click_usercustomerid()
        # time.sleep(2)
        # CustomerUserPage(self.driver).selectcustomer(name)
        time.sleep(3)
        CustomerUserPage(self.driver).userfullname('何必填')
        #CustomerUserPage(self.driver).userlastname('何')
        #CustomerUserPage(self.driver).userfirstname('大大')
        CustomerUserPage(self.driver).userlogin(login_num)
        # 选择有效性
        CustomerUserPage(self.driver).uservaild()
        time.sleep(2)
        CustomerUserPage(self.driver).click_adduser_Submit()
        time.sleep(2)
        return  login_num ,name

    # 连续创建用户
    def userrequiredcommom2(self):
        CustomerUserPage(self.driver).adduser()
        login_num = 'diantong'+ str(random.randint(1, 100000))
        time.sleep(3)
        namenum = random.randint(1, 100)
        userfullname = '何必填'+ str(namenum)
        userfirstname = '必填'+ str(namenum)
        CustomerUserPage(self.driver).userfullname(userfullname)
        CustomerUserPage(self.driver).userlastname('何')
        CustomerUserPage(self.driver).userfirstname(userfirstname)
        CustomerUserPage(self.driver).userlogin(login_num)
        CustomerUserPage(self.driver).uservaild()
        time.sleep(2)
        CustomerUserPage(self.driver).click_adduser_Submit()
        time.sleep(2)
        return login_num, userfullname


    # 填写全填项添加用户
    def userfullcommom(self):
        # 需要新创建一个客户
        #EntranceAgentPage(self.driver).enter_customer_user()
        str1 = CustomerUserCommon(self.driver).Companyrequiredcommon()
        name = str1[0]
        login_num = str1[1]
        Mobile0 = random.randint(1000, 9999)
        Mobile = '138' + str(Mobile0) + str(Mobile0)
        email = login_num+'@qq.com'
        # time.sleep(3)
        # 提交
        CustomerUserPage(self.driver).Companysub()
        time.sleep(5)
        CustomerUserPage(self.driver).associate_GoBack()
        time.sleep(2)
        # 点击点击用户
        CustomerUserPage(self.driver).adduser()
        time.sleep(2)
        # CustomerUserPage(self.driver).click_usercustomerid()
        # time.sleep(2)
        # CustomerUserPage(self.driver).selectcustomer(name)

        CustomerUserPage(self.driver).uservaild()
        time.sleep(2)
        CustomerUserPage(self.driver).usertitle('全填标题')
        CustomerUserPage(self.driver).userfullname('何全填')
        # CustomerUserPage(self.driver).userlastname('何')
        # CustomerUserPage(self.driver).userfirstname('全填')
        CustomerUserPage(self.driver).userlogin(login_num)
        CustomerUserPage(self.driver).userpwd('123')
        CustomerUserPage(self.driver).useremail(email)
        CustomerUserPage(self.driver).userphone('全填电话')
        CustomerUserPage(self.driver).userfax('全填传真')
        CustomerUserPage(self.driver).usermobile(Mobile)

        CustomerUserPage(self.driver).userstreet('全填街道')

        CustomerUserPage(self.driver).userzip('全填邮编')

        CustomerUserPage(self.driver).usercity('全填城市')

        CustomerUserPage(self.driver).usercountry('全填国家')

        CustomerUserPage(self.driver).usercommom('全填备注')
        time.sleep(3)
        CustomerUserPage(self.driver).click_adduser_Submit()
        time.sleep(2)
        return login_num , name , Mobile , email

    def getuser_alltext(self):
        # 取用户页面的所有值
        usertitle = CustomerUserPage(self.driver).usertitle_text()
        userfullname = CustomerUserPage(self.driver).userfullname_text()
        userfirstname = CustomerUserPage(self.driver).userfirstname_text()
        userlastname =  CustomerUserPage(self.driver).userlastname_text()
        userlogin = CustomerUserPage(self.driver).userlogin_text()
        userpwd = CustomerUserPage(self.driver).userpwd_text()
        useremail = CustomerUserPage(self.driver).useremail_text()
        usercustomerid = CustomerUserPage(self.driver).usercustomerid_text()
        userdistrict = CustomerUserPage(self.driver).userdistrict_text()
        userphone = CustomerUserPage(self.driver).userphone_text()
        userfax = CustomerUserPage(self.driver).userfax_text()
        usermobile = CustomerUserPage(self.driver).usermobile_text()
        userstreet = CustomerUserPage(self.driver).userstreet_text()
        userzip = CustomerUserPage(self.driver).userzip_text()
        usercity = CustomerUserPage(self.driver).usercity_text()
        usercountry = CustomerUserPage(self.driver).usercountry_text()
        usercommom = CustomerUserPage(self.driver).usercommom_text()
        uservaild = CustomerUserPage(self.driver).uservaild_text()
        return  usertitle,userfullname,userlastname,userfirstname,userlogin,userpwd,useremail,usercustomerid ,\
        userdistrict,userphone,userfax,usermobile,userstreet,userzip,usercity,usercountry,usercommom,uservaild
