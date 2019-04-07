import time,unittest
from testsuites.base_testcase import BaseTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pageobjects.login_page import Login_HomePage
from pageobjects.main_page import Main_Homepage
from pageobjects.default_page import Default_Homepage
from ddt import ddt,data,unpack

@ddt
class Test_Send_Tie(BaseTestCase):

    @unpack
    def test_send_tie(self):
        test_login=Login_HomePage(self.driver)
        test_main = Main_Homepage(self.driver)
        test_default = Default_Homepage(self.driver)

        test_login.login('admin','admin')
        test_main.click_moren()
        test_default.send_post('搭建框架','今天学习搭建自动化测试框架')
        test_default.reply_post('好好努力，加油鸭')
        test_default.logout()

if __name__=='__main__':
    unittest.main()