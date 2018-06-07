# coding: utf-8
# @Date : 2018/4/15
import unittest
from crmpro.commons.testutil import TestUtil
from crmpro.pages.regpage import RegPage
import time


class RegPageTest(TestUtil):
    """用户注册页面测试"""

    def test_0010_ret_without_select_version(self):
        po = RegPage(self.driver)
        po.open("register")
        po.enter_username("1")
        self.assertEqual(po.get_username_too_short_msg(), 'Username must be at least 6 characters long')

    def test_0020_reg(self):
        po = RegPage(self.driver)
        po.clear_username()
        po.reg('1', 'Jadaff', 'Bob', 'potest@qq.com', 'potest@qq.com',
               'Jadaff', '1990_po_test', '1990_po_test')
        time.sleep(1)
        self.assertIn("step=2", self.driver.current_url)

    def test_0030_reg_setp_2(self):
        po = RegPage(self.driver)
        po.confirm_alert()
        po.enter_company("Infocare")
        po.enter_phone("123456")
        po.enter_fax('123456')
        po.enter_website("http://www.baidu.com")
        po.enter_email_at_setp2('potest@qq.com')
        po.enter_description("Description!")
        po.enter_address("Address")
        po.select_country("China")
        po.click_checkbox()
        po.clisk_continue()


if __name__ == '__main__':
    unittest.main()
