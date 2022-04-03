# """
# @author: DT_testing
# @file:   agent_import.py
# @desc:  【】
# @step：
# """
# from src.page.pagecommon.import_common import ImportCommon
# from src.page.agent.agent_page import AgentPage
# from src.page.agent.entrance_agent_page import EntranceAgentPage
# import time
# from src.testcase.testcase_base.basecase_user import BaseCaseUser
#
#
# class AgentImport(BaseCaseUser):
#
#     def test_agentImport(self):
#         EntranceAgentPage(self.driver).enter_agent()
#         # 进入导入页面
#         AgentPage(self.driver).upload()
#         time.sleep(2)
#         # 点击导入按钮
#         AgentPage(self.driver).uploadFile()
#         # 调用导入公共方法上传文件
#         ImportCommon(self.driver).importCommon('D:\桌面\Export_2020-06-12 15_39_41.xlsx')
#         # 上传文件后导入
#         ImportCommon(self.driver).checkImport()