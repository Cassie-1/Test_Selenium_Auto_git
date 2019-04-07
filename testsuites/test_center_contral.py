import time,unittest
from testsuites.base_testcase import BaseTestCase

from pageobjects.login_page import Login_HomePage
from pageobjects.main_page import Main_Homepage
from pageobjects.default_page import Default_Homepage
from pageobjects.admin_login import Admin_Login_HomePage
from pageobjects.management_center import Management_Center_HomePage
from pageobjects.new_bankuai_page import New_Bankuai_Homepage

class Test_Center_Contral_test(BaseTestCase):
    def test_center_contral(self):
        test_login = Login_HomePage(self.driver)
        test_main = Main_Homepage(self.driver)
        test_default = Default_Homepage(self.driver)
        test_admin_login=Admin_Login_HomePage(self.driver)
        test_management_center=Management_Center_HomePage(self.driver)
        test_new_bankuai=New_Bankuai_Homepage(self.driver)

        # 登录
        test_login.login('admin','admin')
        # 点击默认板块
        test_main.click_moren()
        # 删除帖子
        test_default.delete()
        # 点击管理中心
        test_main.enter_plate()
        # 进入版块管理(管理中心 - -论坛)
        test_admin_login.enter_plate('admin')
        # 点击论坛
        test_management_center.enter_plate()
        # 创建新的版块
        test_management_center.new_plate('自动化测试')
        # 管理员退出
        test_main.logout()
        # 普通用户登录
        test_login.login('lucky ','lucky')
        # 在新的版块下发帖
        test_main.send_post_new()
        test_new_bankuai.send_post_new('你好呀','今天也要加油鸭！！！')
        # 回复帖子
        test_new_bankuai.reply_post('是的呀,加油鸭，加油鸭')

if __name__=='__main__':
    unittest.main()