from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from pageobjects.default_page import Default_Homepage
import time


class New_Bankuai_Homepage(BasePage):

    # 发帖子
    home_page_input_title_loc = (By.NAME, 'subject')
    home_page_input_content_loc = (By.NAME, 'message')
    home_page_input_send_loc = (By.CSS_SELECTOR, '.pnpost .pn strong')

    def send_post_new(self, title, content):
        time.sleep(1)
        self.sendkeys(title, *self.home_page_input_title_loc)
        self.sendkeys(content, *self.home_page_input_content_loc)
        self.click(*self.home_page_input_send_loc)

    def reply_post(self, content):
        self.testone = Default_Homepage(self.driver)
        time.sleep(1)
        self.testone.reply_post(content)