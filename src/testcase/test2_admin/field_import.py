# """
# @author: DT_testing
# @file:   field_import.py
# @desc:  【】
# @step：
# """
# from src.page.pagecommon.import_common import ImportCommon
# from src.page.agent.field_page import FieldPage
# from src.page.agent.entrance_agent_page import EntranceAgentPage
# import time
# from src.testcase.testcase_base.basecase_user import BaseCaseUser
#
#
# class FieldImport(BaseCaseUser):
#
#     def test_fieldImport(self):
#         EntranceAgentPage(self.driver).enter_filed()
#         # 进入导入页面
#         FieldPage(self.driver).import_export()
#         time.sleep(2)
#         # 点击导入按钮
#         FieldPage(self.driver).uploadFile()
#         # 调用导入公共方法上传文件
#         ImportCommon(self.driver).importCommon('D:\桌面\Fields_2020-06-15_15-50.yml')
#         time.sleep(2)
#         #导入
#         ImportCommon(self.driver).checkImport()
