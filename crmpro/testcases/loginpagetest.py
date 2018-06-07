# coding: utf-8
# @Date : 2018/4/18
import unittest
from crmpro.commons.testutil import TestUtil
from crmpro.pages.loginpage import LoginPage


class LoginPageTest(TestUtil):

    def test_0010_invalid_username(self):
        po = LoginPage(self.driver)
        po.open()
        po.login("", "")
        self.assertIn("?e=1", self.driver.current_url)

    def test_0020_invalid_passwd(self):
        po = LoginPage(self.driver)
        po.login("sdfsdf", "sdf")
        self.assertIn("?e=1", self.driver.current_url)

    def test_0030_valid_username_and_passwd(self):
        po = LoginPage(self.driver)
        po.open()
        po.login("Jadaff", "1990_po_test")
        self.assertIn("index.cfm?CFID=", self.driver.current_url)


if __name__ == '__main__':
    unittest.main()
