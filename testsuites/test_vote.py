import time,unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.login_page import Login_HomePage
from pageobjects.main_page import Main_Homepage
from pageobjects.default_page import Default_Homepage
from pageobjects.vote_page import Vote_homepage

class Test_Vote(BaseTestCase):
    def test_vote(self):
        test_login = Login_HomePage(self.driver)
        test_main = Main_Homepage(self.driver)
        test_default = Default_Homepage(self.driver)
        test_vote=Vote_homepage(self.driver)

        test_login.login('admin','admin')
        test_main.click_moren()
        test_default.menu_loc()
        test_vote.publish_post()
        test_vote.vote()
        test_vote.get_name_ratio()
        test_vote.get_theme_name()

if __name__=="__main__":
    unittest.main()