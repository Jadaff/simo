# coding: utf-8
# @Date : 2018/4/18
import unittest

from crmpro.commons import driver
from crmpro.commons.testutil import TestUtil
from crmpro.pages.homepage import HomePage
from crmpro.pages.loginpage import LoginPage


class HomePageTest(TestUtil):

    @classmethod
    def setUpClass(cls):
        super(HomePageTest, cls).setUpClass()
        cls.po = HomePage(cls.driver)

    def test_0010_add_boxes(self):
        self.po.open()
        LoginPage(self.driver).login('Jadaff', '1990_po_test')
        self.po.switch_to_frame('mainpanel')
        self.po.click_add_boxes()
        self.assertEqual(self.po.get_add_boxes_title(), 'Add Home Boxes')
        self.po.close_add_boxes()

    def test_0020_new_company(self):
        po = HomePage(self.driver)
        po.click_new_company()

    def test_0030_new_company(self):
        po = HomePage(self.driver)
        po.click_full_search_form()


if __name__ == '__main__':
    unittest.main()
