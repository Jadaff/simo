# coding: utf-8
# @Date : 2018/4/15
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    """页面基础类，封装所有页面的公用方法"""

    def __init__(self, driver, base_url='https://cn.crmpro.com/'):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 10

    def open(self, url=''):
        url = self.base_url + url
        self.driver.get(url)

    def find_element(self, locator):
        try:
            WebDriverWait(self.driver, self.timeout).until(ec.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except TimeoutException:
            print('{} Unable to locate element: {} after {} seconds!'.format(self, locator, self.timeout))
            raise

    def send_keys(self, locator, text):
        """
        Type text at the page element
        Before typing, try to clear existed text
        :param locator: locator - the element's xpath
        :param text: 	the input text
        """
        self.clear(locator)
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        """Click the web element"""
        self.find_element(locator).click()

    def select(self, locator, value):
        """Select an option by visible value from <select> web element."""
        Select(self.find_element(locator)).select_by_value(value)

    def get_text(self, locator):
        """Return text from specified web element"""
        return self.find_element(locator).text

    def clear(self, locator):
        """Clear existed text of web element"""
        self.find_element(locator).clear()

    def submit(self, locator):
        """Click the submit button"""
        self.find_element(locator).submit()

    def switch_to_frame(self, frame):
        """Switch current frame to specified frame"""
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def confirm_alert(self):
        """Confirm the alert dialog box"""
        WebDriverWait(self.driver, self.timeout).until(ec.alert_is_present())
        self.driver.switch_to.alert.accept()

    def hover_and_click(self, locator_hover, locator_click):
        """Hover on the web element, and then click the specified element"""
        ActionChains(self.driver).move_to_element(self.find_element(locator_hover)).perform()
        self.click(locator_click)

    def get_current_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def get_title(self):
        return self.driver.title
