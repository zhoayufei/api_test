# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import unittest

#导入test.py里的EcTest测试类EcTest
from test import EcTest
#导入test.py里的test_user_login测试类LoginTest
from test_user_login import LoginTest


#使用TestLoader类，将得到指定测试文件中的所有测试方法，用TestSuite类创建测试套件，最后TestRunner类将通过调用测试套件来运行文件中的所有测试
ec_test=unittest.TestLoader().loadTestsFromTestCase(EcTest)
test_login=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
test_suite=unittest.TestSuite([ec_test,test_login])
#用TestRunner类来执行测试套件
unittest.TextTestRunner(verbosity=2).run(test_suite)














