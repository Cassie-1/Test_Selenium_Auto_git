import time,unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.login_page import Login_HomePage
from pageobjects.main_page import Main_Homepage
from pageobjects.look_tie_page import Look_Tie_HomePage
from ddt import ddt,data,unpack

@ddt
class Test_Search_Tie(BaseTestCase):
    @unpack
    def test_search_tie(self):
        test_login = Login_HomePage(self.driver)
        test_main = Main_Homepage(self.driver)
        test_look_tie=Look_Tie_HomePage(self.driver)
        test_login.login('admin','admin')
        test_main.search('haotest')
        test_look_tie.enter_post()
        title=test_look_tie.check()
        try:
            self.assertEqual(title,'haotest',msg=title)
            print('断言结果:帖子标题和期望的一致')
        except:
            print('断言结果:帖子标题和期望的不一致')
        test_main.logout()


if __name__=='__main__':
    unittest.main()

