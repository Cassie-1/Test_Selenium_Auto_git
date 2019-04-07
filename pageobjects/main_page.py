from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Main_Homepage(BasePage):
    # 点击默认板块
    home_page_input_moren_loc = (By.CSS_SELECTOR, '.fl_tb h2 a')
    # 点击管理中心
    home_page_guanli_loc = (By.LINK_TEXT, '管理中心')
    # 点击新增的板块
    home_page_click_new_loc = (By.CSS_SELECTOR, '.fl_tb tbody tr:nth-last-child(2) td:nth-child(2) a')
    # 找到搜索文本框
    search_input_loc = (By.CSS_SELECTOR, '.cl form table tbody tr td:nth-child(2) input')
    # 找到搜索按钮
    search_button_loc = (By.CSS_SELECTOR, '.scbar_btn_td .pnc')
    # 退出
    home_page_input_logout_loc = (By.LINK_TEXT, '退出')

    def click_moren(self):
        time.sleep(1)
        self.click(*self.home_page_input_moren_loc)

    def enter_plate(self):
        time.sleep(1)
        self.click(*self.home_page_guanli_loc)
        time.sleep(1)
        self.change_window()

    def send_post_new(self):
        time.sleep(3)
        self.click(*self.home_page_click_new_loc)

    def search(self,content):
        self.clear(*self.search_input_loc)
        time.sleep(2)
        self.sendkeys(content,*self.search_input_loc)
        time.sleep(2)
        self.click(*self.search_button_loc)
        self.get_windows_img()
        time.sleep(2)

    def logout(self):
        time.sleep(1)
        self.click(*self.home_page_input_logout_loc)
        self.get_windows_img()