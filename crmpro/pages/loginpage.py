# coding: utf-8
# @Date : 2018/4/18
from selenium.webdriver.common.by import By

from crmpro.commons.basepage import BasePage


class LoginPage(BasePage):
    username = (By.XPATH, '//*[@id="loginForm"]/div/input[1]')
    passwd = (By.XPATH, '//*[@id="loginForm"]/div/input[2]')
    _login = (By.XPATH, '//*[@id="loginForm"]/div/div/input')

    def enter_username(self, username):
        self.send_keys(self.username, username)

    def clear_username(self):
        self.clear(self.username)

    def enter_passwd(self, passwd):
        self.send_keys(self.passwd, passwd)

    def clear_passwd(self):
        self.clear(self.passwd)

    def submit_login(self):
        self.submit(self._login)

    def login(self, username='Jadaff', passwd='1990_po_test'):
        self.clear_username()
        self.enter_username(username)
        self.clear_passwd()
        self.enter_passwd(passwd)
        self.submit_login()
