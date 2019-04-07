from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Login_HomePage(BasePage):
    # 登录
    home_page_input_username_loc = (By.NAME, 'username')
    home_page_input_password_loc = (By.NAME, 'password')
    home_page_input_login_loc = (By.CSS_SELECTOR, '.vm em')

    def login(self,username,password):
        self.clear(*self.home_page_input_username_loc)
        self.sendkeys(username,*self.home_page_input_username_loc)
        self.clear(*self.home_page_input_password_loc)
        self.sendkeys(password, *self.home_page_input_password_loc)
        self.click(*self.home_page_input_login_loc)
        self.get_windows_img()