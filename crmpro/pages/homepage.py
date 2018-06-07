# coding: utf-8
# @Date : 2018/4/18
from selenium.webdriver.common.by import By

from crmpro.commons.basepage import BasePage


class HomePage(BasePage):
    add_boxes = (By.XPATH, '//*[@id="navMenu"]/ul/li[2]/a')
    close_boxes = (By.XPATH, '//*[@id="ibox_footer_wrapper"]/a')
    add_boxes_title = (By.XPATH, '//*[@id="ibox_footer"]')
    new_company = (By.XPATH, '//*[@id="navmenu"]/ul/li[3]/ul/li[1]/a')
    company = (By.XPATH, '//*[@id="navmenu"]/ul/li[3]/a')
    contacts = (By.XPATH, '//*[@id="navmenu"]/ul/li[4]/a')
    contacts_full_search_form = (By.XPATH, '//*[@id="navmenu"]/ul/li[4]/ul/li[3]/a')

    def click_add_boxes(self):
        self.click(self.add_boxes)

    def close_add_boxes(self):
        self.click(self.close_boxes)

    def get_add_boxes_title(self):
        return self.get_text(self.add_boxes_title)

    def click_new_company(self):
        self.hover_and_click(self.company, self.new_company)

    def click_full_search_form(self):
        self.hover_and_click(self.contacts, self.contacts_full_search_form)
