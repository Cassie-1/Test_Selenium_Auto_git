from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
import time

class Default_Homepage(BasePage):
    # 发帖子
    home_page_input_title_loc = (By.NAME, 'subject')
    home_page_input_content_loc = (By.NAME, 'message')
    home_page_input_send_loc = (By.CSS_SELECTOR, '.pnpost .pn strong')
    # 回复帖子
    home_page_input_reply_kuang_loc = (By.CSS_SELECTOR, '.pt')
    home_page_input_reply_button_loc = (By.CSS_SELECTOR, '.vm strong')
    # 选择要删除的选项
    home_page_select_loc = (By.CSS_SELECTOR, '.o input')
    home_page_delete_loc = (By.XPATH, '//div[@id="mdly"]/p[1]/strong[1]/a')
    home_page_delete_enter_loc = (By.CSS_SELECTOR, '.pns .pnc span')
    # 下拉选项发帖
    menu_loc = (By.CSS_SELECTOR, '.pgs img ')
    # 退出
    home_page_input_logout_loc = (By.LINK_TEXT, '退出')


    def send_post(self,title,content):
        time.sleep(1)
        self.sendkeys(title, *self.home_page_input_title_loc)
        self.sendkeys(content, *self.home_page_input_content_loc)
        self.click(*self.home_page_input_send_loc)
        self.get_windows_img()

    def reply_post(self,content):
        self.sendkeys(content, *self.home_page_input_reply_kuang_loc)
        self.click(*self.home_page_input_reply_button_loc)
        self.get_windows_img()

    def delete(self):
        time.sleep(1)
        self.click(*self.home_page_select_loc)
        time.sleep(1)
        self.click(*self.home_page_delete_loc)
        time.sleep(2)
        self.click(*self.home_page_delete_enter_loc)
        self.get_windows_img()
        time.sleep(2)

    def menu_loc(self):
        time.sleep(2)
        self.click(*self.menu_loc)

    def logout(self):
        time.sleep(1)
        self.click(*self.home_page_input_logout_loc)
        self.get_windows_img()