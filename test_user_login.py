# -*- coding: utf-8 -*-
#导入requests包
import unittest
import requests
import json
import xlrd

class LoginTest(unittest.TestCase):

    @classmethod
    def test_login(self):
        wb = xlrd.open_workbook("test_user_data.xlsx")  # 打开excel
        sh = wb.sheet_by_name("TestUserLogin")  # 按工作簿名定位工作表
        print(sh.nrows)  # 有效数据行数
        print(sh.ncols)  # 有效数据列数
        print(sh.cell(0, 0).value)  # 输出第一行第一列的值`case_name`
        print(sh.row_values(0))  # 输出第1行的所有值（列表格式）

        # 将数据和标题组装成字典，使数据更清晰
        print(dict(zip(sh.row_values(0), sh.row_values(1))))

        # 遍历excel,打印所有的数据
        for i in range(sh.nrows):
            print(sh.row_values(i))










#class TestUserLogin(unittest.TestCase):
         #url="http://test-api.innotree.com/gateway/user/login"
        #
        # def test_user_login_normal(self):
        #         data = {
        #                 "accountName":"zhaoyufei001",
        #                 "accountPassword":"123456",
        #                 "verifyCaptcha":"1234",
        #                 "encryptCaptcha":"553268e01b2906813dfbe18a8485bcaf85af8777205e1ae4cbc5369c5c483fe0",
        #                 "appId":"IT8e5798252c7d3294a492aced6aa9",
        #                 "subAppId":18000016
        #         }
        #         headers = {"Content-Type":"application/json"}
        #         res = requests.post(url=self.url, data=json.dumps(data), headers=headers)
        #         print (res.text)
        #         self.assertIn("ok",res.text)#断言
        #
        # def test_user_login_passwordwrong(self):
        #         data = {
        #                 "accountName":"zhaoyufei001",
        #                 "accountPassword":"1234567",
        #                 "verifyCaptcha":"1234",
        #                 "encryptCaptcha":"553268e01b2906813dfbe18a8485bcaf85af8777205e1ae4cbc5369c5c483fe0",
        #                 "appId":"IT8e5798252c7d3294a492aced6aa9",
        #                 "subAppId":18000016
        #         }
        #         headers = {"Content-Type":"application/json"}
        #         res = requests.post(url=self.url, data=json.dumps(data), headers=headers)
        #         print (res.text)
        #         self.assertIn("1006",res.text)#断言
        #
        # def test_user_login_userwrong(self):
        #         data = {
        #                 "accountName": "zhaoyufei",
        #                 "accountPassword": "123456",
        #                 "verifyCaptcha": "1234",
        #                 "encryptCaptcha": "553268e01b2906813dfbe18a8485bcaf85af8777205e1ae4cbc5369c5c483fe0",
        #                 "appId": "IT8e5798252c7d3294a492aced6aa9",
        #                 "subAppId": 18000016
        #         }
        #         headers = {"Content-Type": "application/json"}
        #         res = requests.post(url=self.url, data=json.dumps(data), headers=headers)
        #         print (res.text)
        #         self.assertIn("1001", res.text)  # 断言






        # res_dict = res.json() # 将响应转为json对象（字典）等同于`json.loads(res.text)
        # print(json.dumps(res_dict, indent=2, sort_keys=True, ensure_ascii=False)) # 重新转为文本

#if __name__ == '__main__':  # 如果是直接从当前模块执行（非别的模块调用本模块）
      #  unittest.main(verbosity=2)  # 运行本测试类所有用例,verbosity为结果显示级别