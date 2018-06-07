# coding: utf-8
# @Date : 2018/4/19
import unittest
from HtmlTestRunner import HTMLTestRunner
import time


def main():
    now = time.strftime('%Y%m%d_%H%M%S')
    filename = now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(output=filename, report_title='Simo2.0自动化测试报告',
                            descriptions='运行环境：windows 10, Chrome')
    test_suite = unittest.defaultTestLoader.discover('./', pattern='*test.py')
    runner.run(test_suite)
    fp.close()


if __name__ == '__main__':
    main()
