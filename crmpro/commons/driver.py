# coding: utf-8
# @Date : 2018/4/15
from selenium import webdriver
from selenium.webdriver.common.by import By


def browser():
    driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    driver = browser()
    driver.get('http://www.baidu.com')
    kw = (By.XPATH, '//*[@id="kw"]')
    a = driver.find_element_by_xpath('//*[@id="kw"]')
    print(a)
    b = (By.XPATH, '//*[@id="kw"]')
    print(type(b))
    print(b)
    print(*b)
    c = driver.find_element('xpath', '//*[@id="kw"]')
    print(c)
    print("==============")
    from crmpro.commons.basepage import BasePage

    po = BasePage(driver)
    e = po.find_element(kw).select_by_value("hs")
    print(e)
    print("************")
    po.send_keys(kw, text="hello world")

    driver.quit()
