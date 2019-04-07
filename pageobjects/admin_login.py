from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Admin_Login_HomePage(BasePage):
    # 输入管理员密码
    home_page_password_loc = (By.CSS_SELECTOR, '.loginform .txt')
    home_page_submit_loc = (By.CSS_SELECTOR, '.btn')

    def enter_plate(self,password):
        time.sleep(1)
        self.sendkeys(password,*self.home_page_password_loc)
        time.sleep(1)
        self.click(*self.home_page_submit_loc)

