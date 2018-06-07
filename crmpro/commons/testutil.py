# coding: utf-8
# @Date : 2018/4/15
import unittest
from .driver import browser


class TestUtil(unittest.TestCase):

    # def setUp(self):
    #     self.driver = browser()
    #     self.driver.implicitly_wait(20)
    #     self.driver.maximize_window()
    #
    # def tearDown(self):
    #     self.driver.quit()

    # driver = browser()

    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
