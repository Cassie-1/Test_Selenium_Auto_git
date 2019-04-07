from pageobjects.base import BasePage
from pageobjects.main_page import Main_Homepage
import time
from selenium.webdriver.common.by import By

class Look_Tie_HomePage(BasePage):
    # 查看帖子
    look_post_loc=(By.CSS_SELECTOR,'.xs3 a')
    # 打开帖子
    open_post_loc=(By.CSS_SELECTOR,'.ts')

    def enter_post(self):
        self.change_window()
        time.sleep(1)
        self.click(*self.look_post_loc)
        self.get_windows_img()
        time.sleep(1)
    def check(self):
        self.change_window()
        time.sleep(1)
        title=self.get_text(*self.open_post_loc)
        self.get_windows_img()
        return title

    def logout(self):
        self.testone = Main_Homepage(self.driver)
        self.close()
        self.change_window()
        self.close()
        self.change_window()
        self.testone.logout()
        time.sleep(1)