# coding: utf-8
# @Date : 2018/4/15
from selenium.webdriver.common.by import By

from crmpro.commons.basepage import BasePage


class RegPage(BasePage):
    """注册页面"""

    _version = (By.XPATH, '//*[@id="payment_plan_id"]')
    first_name = (By.XPATH, '//*[@id="multipleForm"]/div[3]/input')
    last_name = (By.XPATH, '//*[@id="multipleForm"]/div[4]/input')
    email = (By.XPATH, '//*[@id="multipleForm"]/div[5]/input')
    confirm_email = (By.XPATH, '//*[@id="multipleForm"]/div[6]/input')
    _username = (By.XPATH, '//*[@id="username"]/input')
    password = (By.XPATH, '//*[@id="multipleForm"]/div[8]/input')
    confirm_password = (By.XPATH, '//*[@id="multipleForm"]/div[9]/input')
    agree_terms = (By.XPATH, '//*[@id="multipleForm"]/div[11]/div/label/input')
    reg_button = (By.XPATH, '//*[@id="multipleForm"]/div[12]/div')

    # 消息提示
    version_msg = (By.XPATH, '//*[@id="multipleForm"]/div[1]/small')
    username_too_short = (By.XPATH, '//*[@id="username"]/small[2]')

    # setp_2
    _company = (By.XPATH, '//*[@id="company_name"]')
    _phone = (By.XPATH, '//*[@id="phone"]')
    _fax = (By.XPATH, '//*[@id="fax"]')
    _website = (By.XPATH, '//*[@id="website"]')
    _email = (By.XPATH, '//*[@id="company_email"]')
    _description = (By.XPATH, '//*[@id="service"]')
    _address = (By.XPATH, '//*[@id="address"]')
    _city = (By.XPATH, '//*[@id="city"]')
    _state = (By.XPATH, '//*[@id="state"]')
    _postcode = (By.XPATH, '//*[@id="postcode"]')
    _country = (By.XPATH, '//*[@id="companyForm"]/div[11]/select')
    _checkbox = (By.XPATH, '//*[@id="companyForm"]/div[12]/label/input')
    __continue = (By.XPATH, '//*[@id="companyForm"]/div[13]/div/button')


    # Actions
    def select_version(self, value):
        self.select(self._version, value)

    def enter_first_name(self, name):
        self.send_keys(self.first_name, name)

    def enter_last_name(self, name):
        self.send_keys(self.last_name, name)

    def enter_email(self, email):
        self.send_keys(self.email, email)

    def enter_confirm_email(self, email):
        self.send_keys(self.confirm_email, email)

    def enter_username(self, username):
        self.send_keys(self._username, username)

    def enter_password(self, pwd):
        self.send_keys(self.password, pwd)

    def enter_confirm_password(self, pwd):
        self.send_keys(self.confirm_password, pwd)

    def click_agree_terms(self):
        self.click(self.agree_terms)

    def click_reg_button(self):
        self.click(self.reg_button)

    def get_version_msg(self):
        self.get_text(self.version_msg)

    def get_username_too_short_msg(self):
        return self.get_text(self.username_too_short)

    def clear_username(self):
        self.clear(self._username)

    # step_2
    def enter_company(self, company):
        self.send_keys(self._company, company)

    def enter_phone(self, phone):
        self.send_keys(self._phone, phone)

    def enter_fax(self, fax):
        self.send_keys(self._fax, fax)

    def enter_website(self, website):
        self.send_keys(self._website, website)

    def enter_email_at_setp2(self, email):
        self.send_keys(self._email, email)

    def enter_description(self, description):
        self.send_keys(self._description, description)

    def enter_address(self, address):
        self.send_keys(self._address, address)

    def enter_city(self, city):
        self.send_keys(self._city, city)

    def enter_state(self, state):
        self.send_keys(self._state, state)

    def enter_postcode(self, postcode):
        self.send_keys(self._postcode, postcode)

    def click_checkbox(self):
        self.click(self._checkbox)

    def select_country(self, value):
        self.select(self._country, value)

    def clisk_continue(self):
        self.click(self.clisk_continue())



    # 定义注册入口
    def reg(self, version, first_name, last_name, email, confirm_email, username, password, confirm_pwd):
        self.select_version(version)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_confirm_email(confirm_email)
        self.enter_username(username)
        self.enter_password(password)
        self.enter_confirm_password(confirm_pwd)
        self.click_agree_terms()
        self.click_reg_button()
