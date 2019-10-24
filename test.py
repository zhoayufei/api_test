# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import unittest
from PIL import Image
import pytesseract


class EcTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        #输入网址
        cls.driver.get("http://echuang.innotree.com/home")
        time.sleep(3)
        #全屏
        cls.driver.maximize_window()
        time.sleep(3)

    def test_login(self):
        #点击登陆按钮
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/header/div[3]/div/div/div/a[1]/span').click()
        time.sleep(3)
        #点击输入用户名
        self.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/form/div[1]/div/div[1]/input').send_keys("zhaoyufei001")
        time.sleep(3)
        #点击输入密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/form/div[2]/div/div[1]/input').send_keys("123456")
        time.sleep(3)
        #点击输入验证码
        self.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/form/div[3]/div/div[1]/div/input').send_keys("1234")
        time.sleep(3)
        #点击登陆按钮
        self.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div[2]/form/button/span').click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
