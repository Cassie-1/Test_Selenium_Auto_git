import unittest,os,HTMLTestRunner
import sys
from page.test_search_tie import Test_Search_Tie

cur_path=os.path.dirname(os.path.realpath(__file__))

test_path=os.path.dirname(os.path.realpath('.'))+'/Test_Selenium_Auto/testsuites/'
suite=unittest.TestLoader().discover(test_path,pattern='test_*.py')
sys.path.append(os.path.dirname(os.path.realpath('.'))+'/Test_Selenium_Auto/')
report_path=os.path.join(test_path,"reports")

if not os.path.exists(report_path):
    os.mkdir(report_path)

if __name__=='__main__':
    html_report = report_path + r"\result.html"
    fp = open(html_report, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='单元测试报告', description='用例执行情况')
    runner.run(suite)



# 运行单个测试文件
# path=os.path.dirname(os.path.realpath('.'))+'/Test_Selenium_Auto/page/'
# suite_alone=unittest.TestLoader().discover(path,pattern='test_search_tie.py')
#
# report_path_alone=os.path.join(path,"reports")
# if not os.path.exists(report_path_alone):
#     os.mkdir(report_path_alone)
#
# if __name__ == '__main__':
#     html_report = report_path_alone + r"\result.html"
#     fp = open(html_report, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title='单元测试报告', description='用例执行情况')
#     runner.run(suite_alone)
