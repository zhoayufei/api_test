
# -*- coding: utf-8 -*- 

import sys,os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import random


from selenium.webdriver.common.action_chains import ActionChains

reload(sys)
sys.setdefaultencoding('utf-8')


from selenium import webdriver 
import random,time
global driver,rint


pwd="123456"
dxyzm="8756"
picyzm="1234"


#输入框输入内容方法
def xpah_sendk(xpath,keystring):
	xname=driver.find_element_by_xpath(xpath)
	xname.send_keys(keystring)
#点击方法
def xpath_click(xpath):
	xname=driver.find_element_by_xpath(xpath)
	xname.click()
#清除方法
def xpath_clear(xpath):
	xname=driver.find_element_by_xpath(xpath)
	xname.clear()

driver = webdriver.Chrome()
for i in range(1):
	rint=random.randint(99999,1000000)
	name='wxj'+str(rint)
	# phone="14000"+str(rint)
	phone="13000"+str(rint)
	print '------------------'
	print name
	rstr=str(rint)

	#E创注册
	driver.get("http://echuang.innotree.com/register")
	driver.maximize_window()	
	time.sleep(1)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input',name)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[3]/div/div[1]/input',phone)
	xpath_click('//*[@id="app"]/div[3]/div/div/div[2]/form/div[4]/div/div/div[2]/a')
	time.sleep(1)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[4]/div/div[1]/div/input',dxyzm)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input',pwd)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[6]/div/div[1]/input',pwd)
	xpath_click('//*[@id="app"]/div[3]/div/div/div[2]/form/button')
	time.sleep(2)

	#E创登录
	driver.get("http://echuang.innotree.com/login")
	xpah_sendk('//*[@id="app"]/div[3]/div/div[2]/form/div[1]/div/div[1]/input',phone)
	xpah_sendk('//*[@id="app"]/div[3]/div/div[2]/form/div[2]/div/div[1]/input',pwd)
	xpah_sendk('//*[@id="app"]/div[3]/div/div[2]/form/div[3]/div/div[1]/div/input','1234')
	xpath_click('//*[@id="app"]/div[3]/div/div[2]/form/button')
	time.sleep(2)


	#需求分发布
	driver.get("http://echuang.innotree.com/demand/publish")
	time.sleep(1)

	driver.maximize_window()	
	time.sleep(1)
	#需求名称
	def xqname():		
		xpah_sendk('//*[@id="app"]/div[3]/form/div[1]/div[1]/div/div[1]/input',u'需求名称'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[1]/div[2]/div/div[1]/input',u"2019-08-25")
		xpah_sendk('//*[@id="app"]/div[3]/form/div[1]/div[3]/div/div[1]/textarea',u'需求描述'+rstr)

	#需求类型
	xqtype=['//*[@id="app"]/div[3]/form/div[2]/div[2]/a[1]/span[1]','//*[@id="app"]/div[3]/form/div[2]/div[2]/a[2]/span[1]','//*[@id="app"]/div[3]/form/div[2]/div[2]/a[3]/span[1]','//*[@id="app"]/div[3]/form/div[2]/div[2]/a[4]/span[1]','//*[@id="app"]/div[3]/form/div[2]/div[2]/a[5]/span[1]']
	#需求内容
	def xqcontent():
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[1]/div/div[1]/input',u'期望解决的难题'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[2]/div/div[1]/input',u'预期达到的目标'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[3]/div/div/textarea',u'需求描述'+rstr)
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[4]/div/div/div[1]/div/div/span[2]')
		#os.system("F:\\py\\pysele\\autoJpg.exe")
		os.system("D:\\image\\jpg.exe")
		time.sleep(2)

	#联系方式
	def lxfs():
		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[1]/div/div[1]/input',u'企业名称'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[2]/div/div/textarea',u'企业简介'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[3]/div/div/input',u'http://www.baidu.com')
		xpath_click('//*[@id="app"]/div[3]/form/div[4]/div/div[4]/div/div[1]/label[1]/span')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[5]/div/div[1]/input',u'联系人'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[6]/div[1]/div/div[1]/input',u'13500000000')
		xpath_click('//*[@id="app"]/div[3]/form/div[4]/div/div[6]/div[3]/a')
		time.sleep(2)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[6]/div[2]/div/div[1]/input','8756')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[7]/div/div[1]/input',u'1@1.com')

		xpath_click('//*[@id="app"]/div[3]/form/div[4]/div/div[8]/div[1]/div/div/div/input')
		time.sleep(1)
		xpath_click('/html/body/div[9]/div[1]/div[1]/ul/li[3]')
		time.sleep(1)

		xpath_click('//*[@id="app"]/div[3]/form/div[4]/div/div[8]/div[2]/div/div/div/span/span/i')
		time.sleep(1)
		xpath_click('/html/body/div[4]/div[1]/div[1]/ul/li[3]')
		time.sleep(1)

		xpath_click('//*[@id="app"]/div[3]/form/div[4]/div/div[8]/div[3]/div/div/div/input')
		time.sleep(1)
		xpath_click('/html/body/div[5]/div[1]/div[1]/ul/li[3]')
		time.sleep(1)

		xpah_sendk('//*[@id="app"]/div[3]/form/div[4]/div/div[9]/div/div[1]/input',u'联系地址'+rstr)

	FLAG=2
	XQ=[u'技术需求',u'服务需求',u'股权融资',u'债权融资',u'其它需求']
	print XQ[FLAG]
	if FLAG==0:
		xqname()
		xpath_click(xqtype[FLAG])
		xqcontent()
		lxfs()
	elif FLAG==1:
		xqname()
		xpath_click(xqtype[FLAG])
		xqcontent()
		lxfs()
	elif FLAG==2:
		xqname()
		xpath_click(xqtype[FLAG])
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[1]/div/div/input',u'项目名称-股权融资'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[2]/div[1]/div/div/input',rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[2]/div[2]/div/div/input',rstr)
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[3]/div/div/div/input')
		time.sleep(0.5)
		xpath_click('/html/body/div[3]/div[1]/div[1]/ul/li[2]')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[4]/div[1]/div/div/input',u'2019-08-25')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[4]/div[2]/div/div/input',u'2019-08-28')
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[5]/div/div/div/input')
		time.sleep(0.5)
		xpath_click('/html/body/div[6]/div[1]/div[1]/ul/li[2]')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[6]/div[1]/div/div/input',rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[6]/div[3]/div/div/input',rstr)
		#出让比例
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[7]/div[1]/div/div/input',rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[7]/div[3]/div/div/input',rstr)

		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[8]/div[1]/div/div/div[1]/input')
		time.sleep(0.5)
		xpath_click('/html/body/div[7]/div[1]/div[1]/ul/li[3]')
		time.sleep(0.5)

		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[8]/div[2]/div/div/div[1]/input')
		time.sleep(0.5)
		xpath_click('/html/body/div[8]/div[1]/div[1]/ul/li[3]')
		time.sleep(0.5)
		
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[9]/div/div/input',u'河北省秦皇岛'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[10]/div/div/input',rstr)
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[11]/div/div/label[2]/span[1]/span')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[12]/div/div/textarea',u'资金用途'+rstr)
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[13]/div/div/div[1]/div/div/span[2]')
		os.system("D:\\image\\jpg.exe")
		#os.system("F:\\py\\pysele\\autoJpg.exe")
		time.sleep(20)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[14]/div/div/textarea',u'项目介绍'+rstr)
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[15]/div/div/div[1]/div/div')
		os.system("F:\\py\\pysele\\autoJpg.exe")
		time.sleep(2)				
		lxfs()				
	elif FLAG==3:
		xqname()
		xpath_click(xqtype[FLAG])
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[1]/div/div/input',u'项目名称-债权融资'+rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[2]/div/div/input',rstr)
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[3]/div/div/div[1]/div/div/span[2]')
		os.system("F:\\py\\pysele\\autoJpg.exe")
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[4]/div/div/textarea',u'项目介绍'+rstr)
		time.sleep(2)	
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[5]/div/div/div[1]/div/div/span[2]')
		os.system("F:\\py\\pysele\\autoJpg.exe")
		time.sleep(2)	
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[6]/div[1]/div/div/input',rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[6]/div[3]/div/div/input',rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[7]/div/div/input',rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[8]/div/div/input',rstr)
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[9]/div[1]/div/div/input',u'2019-08-25')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[9]/div[2]/div/div/input',u'2019-08-28')
		#风控类型
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[10]/div/div/label[2]/span[1]/span')
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[10]/div/div/label[3]/span[2]')
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[11]/div[1]/div/div/div[1]/input')
		time.sleep(1)
		xpath_click('/html/body/div[7]/div[1]/div[1]/ul/li[3]')
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[11]/div[2]/div/div/div[1]/input')
		time.sleep(1)
		xpath_click('/html/body/div[8]/div[1]/div[1]/ul/li[3]')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[12]/div/div/input',u'河北-秦皇岛'+rstr)
		xpath_click('//*[@id="app"]/div[3]/form/div[3]/div/div[13]/div/div/div/input')
		time.sleep(1)
		xpath_click('/html/body/div[9]/div[1]/div[1]/ul/li[2]')
		xpah_sendk('//*[@id="app"]/div[3]/form/div[3]/div/div[14]/div/div/textarea',u'资金用途'+rstr)
		xpah_sendk('',u''+rstr)
		lxfs()
	elif FLAG==4:
		xqname()
		xpath_click(xqtype[FLAG])
		xqcontent()
		lxfs()



	xpah_sendk('',u''+rstr)
	xpah_sendk('',u''+rstr)
	xpah_sendk('',)
	xpah_sendk('',)




	xpath_click('//*[@id="app"]/div/div/div[2]/div/div/form/div[3]/div/div[1]/button/span')
	xpah_sendk('//*[@id="app"]/div/div/div[2]/div/div/form/div[3]/div/div[1]/div/input',dxyzm)
	xpah_sendk('//*[@id="app"]/div/div/div[2]/div/div/form/div[4]/div/div[1]/input',pwd)
	xpah_sendk('//*[@id="app"]/div/div/div[2]/div/div/form/div[5]/div/div[1]/input',pwd)
	xpah_sendk('//*[@id="app"]/div/div/div[2]/div/div/form/div[6]/div/div[1]/div/input',picyzm)
	time.sleep(1)
	xpath_click('//*[@id="app"]/div/div/div[2]/div/div/form/button')
	time.sleep(5)





	driver.get("http://echuang.innotree.com/register")
	driver.maximize_window()	
	time.sleep(1)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input',name)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[3]/div/div[1]/input',phone)
	xpath_click('//*[@id="app"]/div[3]/div/div/div[2]/form/div[4]/div/div/div[2]/a')
	time.sleep(1)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[4]/div/div[1]/div/input',dxyzm)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input',pwd)
	xpah_sendk('//*[@id="app"]/div[3]/div/div/div[2]/form/div[6]/div/div[1]/input',pwd)
	xpath_click('//*[@id="app"]/div[3]/div/div/div[2]/form/button')
	time.sleep(2)

	#E创登录
	driver.get("http://echuang.innotree.com/login")
	xpah_sendk('//*[@id="app"]/div[3]/div/div[2]/form/div[1]/div/div[1]/input',phone)
	xpah_sendk('//*[@id="app"]/div[3]/div/div[2]/form/div[2]/div/div[1]/input',pwd)
	xpah_sendk('//*[@id="app"]/div[3]/div/div[2]/form/div[3]/div/div[1]/div/input','1234')
	xpath_click('//*[@id="app"]/div[3]/div/div[2]/form/button')
	time.sleep(2)



	#立即认证
	driver.get("http://echuang.innotree.com/certificate")
	driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
	time.sleep(1)
	xpath_click('//*[@id="app"]/div[3]/div[2]/div[2]/button')
	time.sleep(1)
	corptt=str(rint)+u"基础认证因果树树树树树树树树树"
	xydm='012345678901'+str(rint)
	# corptt=u'现代农装科技股份有限公司'
	# xydm='91110114726362764L'
	# corptt=u"深圳市拓勤进出口有限公司"
	#企业类型贸易型
	# xpath_click('//*[@id="app"]/div/div/form/div[2]/div/div[1]/div/div/label[2]/span[1]/span')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/div[2]/div[2]/div/form/div/div[1]/div/div[1]/input',corptt)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/div[2]/div[2]/div/form/div/div[2]/div/div[1]/input',xydm)
	xpath_click('//*[@id="app"]/div[3]/div[2]/div[2]/div[3]/div')
	xpath_click('//*[@id="app"]/div[3]/div[2]/div[3]/button')
	time.sleep(1)



	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[1]/div[1]/div/div[1]/input',corptt)

	
	# xydm='914403006955788289'

	xpath_clear('//*[@id="app"]/div/div[2]/form/div[1]/div[2]/div/div[1]/input')
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[2]/div/div[1]/input',xydm)
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[3]/div/div/div[1]/div/div[1]/input',100)
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[4]/div/div/div[1]/div/div/input',100)

	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[1]/div[5]/div/div/input',u"2019-06-09")
	time.sleep(2)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[1]/div[5]/div/div/input')
	xpath_click('//*[@id="app"]/div/div[2]/form/div[1]/div[6]/div/div/div[1]/div/div/div/input')
	for i in range(5):
		xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[6]/div/div/div[1]/div/div/div/input',Keys.DOWN)
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[6]/div/div/div[1]/div/div/div/input',Keys.ENTER)
	xpath_click('//*[@id="app"]/div/div[2]/form/div[1]/div[6]/div/div/div[2]/div/div/div/input')
	time.sleep(1)
	for i in range(4):
		xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[6]/div/div/div[2]/div/div/div/input',Keys.DOWN)
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[6]/div/div/div[2]/div/div/div/input',Keys.ENTER)
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[7]/div/div[1]/input',u"注册地区内蒙")
	xpath_click('//*[@id="app"]/div/div[2]/form/div[1]/div[8]/div/div/div/div/div/div/input')
	time.sleep(1)
	for i in range(4):
		xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[8]/div/div/div/div/div/div/input',Keys.DOWN)
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[8]/div/div/div/div/div/div/input',Keys.ENTER)
	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/div[9]/div/div[1]/textarea',u"经营范围")
	time.sleep(1)



	# //*[@id="app"]/div/div[2]/form/div[1]/div[10]/div/div/div[1]/div/button/span

	#营业执照
	xpath_click('//*[@id="app"]/div/div[2]/form/div[1]/div[10]/div/div/div[1]/div/button')
	os.system("F:\\py\\pysele\\autoJpg.exe")
	time.sleep(3)
	for i in range(random.randint(1,5)):
		xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[1]/div[11]/div/div/div[1]/div/button/span')
		os.system("F:\\py\\pysele\\autoJpg.exe")
		time.sleep(2)


	time.sleep(3)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[1]/div[12]/div/div/div[1]/div/button/span')
	os.system("F:\\py\\pysele\\autoJpg.exe")
	time.sleep(3)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[1]/div[13]/div/div[1]/textarea',u"公司介绍")
	time.sleep(3)

	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[1]/div[14]/div/div/div[1]/div/button/span')
	os.system("F:\\py\\pysele\\autoJpg.exe")
	time.sleep(4)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[2]/button')

	#--------------------核心成员

	# for i in range(4):
	# 	xpah_sendk('//*[@id="app"]/div/div[2]/form/div[1]/h2',Keys.DOWN)

	time.sleep(1)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[1]/div/div[1]/button/span')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input',u"姓名")
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[2]/div/div[1]/input',u"职位")
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[3]/div/div[1]/textarea',u"履历履历履历履历履历履历履历履历履历履历履历")
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[1]/div/div[3]/div/div/div[2]/form/div[4]/button/span')
	time.sleep(2)

	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[1]/div/div[1]/input',u"法定代表人姓名")
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[3]/div/div[1]/input','410702199012152132')

	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[4]/div/div/div[2]/div[1]/div/div[2]/div[1]/div/button/span')
	os.system("F:\\py\\pysele\\autoJpg.exe")
	time.sleep(3)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[4]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/button/span')
	os.system("F:\\py\\pysele\\autoJpg.exe")
	time.sleep(2)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[5]/div/div[1]/input',100)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[6]/div/div[1]/input',101)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[7]/div/div[1]/input',102)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[1]/div/div[1]/input',u'联系人姓名')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[2]/div/div[1]/input',u'所属部门',)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[3]/div/div[1]/input',u'职位')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[4]/div/div[1]/input',phone)
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[5]/div/div/input',u'办公电话')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[6]/div/div/input','123456')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[7]/div/div[1]/input',u'办公地址')
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[4]/button')
	time.sleep(1)
	#-------------------------------资质信息

	time.sleep(2)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[3]/div[1]/div/div/label[2]/span[1]/span')
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[4]/button')

	#-------------------------------财务信息

	time.sleep(2)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[1]/div/div/div/div[1]/div/button/span')
	os.system("F:\\py\\pysele\\autoJpg.exe")
	time.sleep(2)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[1]/div/div/button/span')
	            
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[1]/div/div/div/input',u'0')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[1]/div/div[2]/div/div/div/input',u'0')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[1]/div/div/div/input',u'0')
	xpah_sendk('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[2]/div/div[3]/div/div/div/input',u'0')
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[2]/div[2]/div[2]/div/div/div[2]/form/div[3]/button/span')
	time.sleep(2)
	xpath_click('//*[@id="app"]/div[3]/div[2]/form/div[3]/button/span')
	time.sleep(2)
	xpath_click('/html/body/div[2]/div/div[3]/button[2]/span')
	time.sleep(2)
