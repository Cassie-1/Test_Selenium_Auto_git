from pageobjects.base import BasePage
from selenium.webdriver.common.by import By
from pageobjects.login_page import Login_HomePage
from pageobjects.main_page import Main_Homepage
import time

class Management_Center_HomePage(BasePage):
    # 点击论坛
    home_page_click_luntan_loc = (By.CSS_SELECTOR, '.nav ul li:nth-child(7)')
    # 点击添加新版块
    home_page_click_new_border_loc = (By.CSS_SELECTOR, '.lastboard .addtr')
    # 找到新模块文本框
    home_page_new_txt_loc = (By.CSS_SELECTOR, 'form .tb2 tbody:nth-last-child(2) .board .txt')
    # 找到提交按钮
    home_page_submit_new_loc = (By.CSS_SELECTOR, '.fixsel .btn')

    def enter_plate(self):
        time.sleep(1)
        self.click(*self.home_page_click_luntan_loc)


    def new_plate(self,name):
        self.testone = Main_Homepage(self.driver)
        time.sleep(1)
        self.change_window()
        self.enter_iframe()
        time.sleep(2)
        self.click(*self.home_page_click_new_border_loc)
        print('点击新增版块按钮成功')
        time.sleep(1)
        self.clear(*self.home_page_new_txt_loc)
        time.sleep(1)
        print('清除新板块的名字成功')
        self.sendkeys(name,*self.home_page_new_txt_loc)
        print('输入新板块的名字成功')
        time.sleep(1)
        self.click(*self.home_page_submit_new_loc)
        self.get_windows_img()
        # 退出管理中心
        time.sleep(2)
        self.change_window()
        self.testone.logout()
