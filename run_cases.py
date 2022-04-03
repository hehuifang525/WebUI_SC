"""
@author: QianJingjing
@file:   run_cases.py
@desc:  【批量执行测试用例，生成测试报告】
@step：  
"""
import sys

import unittest2

from common.HTMLTestRunner import HTMLTestRunner

# if __name__ == '__main__':
#     # suite = unittest2.defaultTestLoader.discover("./src/testcase", pattern="*.py")  # --运行了所有
#     # # 参数化
#     path = sys.argv[2]
#     file = sys.argv[3]
#     suite = unittest2.defaultTestLoader.discover(path, pattern=file)
#
#     # unittest2.TextTestRunner().run(suite)
#     print(suite)
#     # 指定测试报告的位置
#     path = "test_report/TestReport.html"
#
#     # 生成测试报告
#
#     with open(path, 'wb') as file:  # w表示写，b表示二进制
#         HTMLTestRunner(stream=file, # 文件名
#                        verbosity=1, # 日志详细级别 无需修改
#                        title="ServiceCool 自动化测试报告",
#                        description="测试环境：Chrome",
#                        tester="DT_testing").run(suite)
# import os
# import sys
# import unittest2
#
# from common.BeautifulReport import BeautifulReport
#
# proDir = os.path.split(os.path.realpath(__file__))[0]
# report_path = os.path.join(proDir, r'test_report')
# #print(report_path)
#
# if __name__ == '__main__':
#     root_dir = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
#
#     # test_dir = root_dir + '/src/testcase/test2_admin'
#     #file='role_case.py'
#
#     test_dir = sys.argv[2]
#     print('test_dir---------------'+test_dir)
#     file = sys.argv[3]
#
#     suite = unittest2.defaultTestLoader.discover(test_dir, pattern=file,top_level_dir=None)
#
#
#     filename = "TestReport.html"
#     desc = '自动化测试报告（测试环境：Chrome）'
#
#     run = BeautifulReport(suite)
#     run.report(description=desc, filename=filename, report_dir=report_path)

# 本地运行修改
if __name__ == '__main__':
    # suite = unittest2.defaultTestLoader.discover("src/testcase", pattern="*.py")  # --运行了所有
    suite = unittest2.defaultTestLoader.discover("src/testcase/test1_login", pattern="*.py")  # --运行了所有
    # # 参数化
    # path = sys.argv[2]
    # file = sys.argv[3]
    # suite = unittest2.defaultTestLoader.discover(path, pattern=file)

    # unittest2.TextTestRunner().run(suite)
    print(suite)
    # 指定测试报告的位置
    path = "test_report/TestReport.html"

    # 生成测试报告

    with open(path, 'wb') as file:  # w表示写，b表示二进制
        HTMLTestRunner(stream=file, # 文件名
                       verbosity=1, # 日志详细级别 无需修改
                       title="ServiceCool 自动化测试报告",
                       description="测试环境：Chrome",
                       tester="DT_testing").run(suite)