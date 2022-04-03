"""
@author: DT_testing
@file:   district_common.py
@desc:  【区域】
@step：
"""
from src.page.agent.entrance_agent_page import EntranceAgentPage
from src.page.agent.district_page import DistrictPage
import time


class DistrictCommon(DistrictPage):
    def DistrictRequiredCommon(self):

        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "区域必填" + strnumber
        EntranceAgentPage(self.driver).enter_district()
        time.sleep(2)
        DistrictPage(self.driver).click_add()
        time.sleep(3)
        DistrictPage(self.driver).input_name(name)
        DistrictPage(self.driver).choose_valid()
        DistrictPage(self.driver).addsubmit()
        return name

    def DistrictRequiredCommon2(self):

        strnumber = time.strftime('%y%m%d%M%S', time.localtime())
        name = "区域必填" + strnumber
        time.sleep(2)
        DistrictPage(self.driver).click_add()
        time.sleep(3)
        DistrictPage(self.driver).input_name(name)
        DistrictPage(self.driver).choose_valid()
        DistrictPage(self.driver).addsubmit()
        return name

    # 创建无效区域
    def DistrictinvalidCommon(self):

        strnumber = time.strftime('%Y%m%d%M%S', time.localtime())
        name = "区域必填" + strnumber
        EntranceAgentPage(self.driver).enter_district()
        time.sleep(2)
        DistrictPage(self.driver).click_add()
        time.sleep(3)
        DistrictPage(self.driver).input_name(name)
        DistrictPage(self.driver).choose_invalid()
        DistrictPage(self.driver).addsubmit()
        return name


    def DistrictFullCommon(self):
        strnumber = time.strftime('%y%m%d%H%M%S', time.localtime())
        name = "区域全填" + strnumber
        coment = "备注" + strnumber
        time.sleep(2)
        parentdistrict = DistrictCommon(self.driver).DistrictRequiredCommon()
        DistrictPage(self.driver).click_add()
        DistrictPage(self.driver).input_name(name)
        DistrictPage(self.driver).choose_parent_district(parentdistrict)
        DistrictPage(self.driver).input_coment(coment)
        DistrictPage(self.driver).choose_valid()
        time.sleep(1)
        DistrictPage(self.driver).addsubmit()
        return name, coment, parentdistrict

    def GetDistrictInfo(self):
        name = DistrictPage(self.driver).get_name()
        parent_district = DistrictPage(self.driver).get_parent_district()
        valid = DistrictPage(self.driver).get_valid()
        coment = DistrictPage(self.driver).get_coment()
        return name, parent_district, valid, coment
