from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
import sys, random

# Import pandas
import pandas as pd
import time

from random_username.generate import generate_username

def _click(xpath):
	r=driver.find_element_by_xpath(xpath)
	r.click()
	return True

while True:
	try:
# reading csv file 
		df=pd.read_csv("russian_surnames.csv", header=0, sep=';')
		max_sur=round(df.size/6-1)
		random_sur_id=random.randint(1, max_sur)

		surname=df['Surname'][random_sur_id]


		df=pd.read_csv("russian_names.csv", header=0, sep=';')
		max_sur=round(df.size/6-1)
		random_sur_id=random.randint(1, max_sur)
		name=df['Name'][random_sur_id]

		print (name, surname)


		PATH = 'C:\Program Files (x86)\chromedriver.exe'
		driver = webdriver.Chrome(PATH)
		driver.maximize_window()
		driver.delete_all_cookies()
		driver.get("https://24xforex.com/ru/register")

		driver.execute_script("window.open('about:blank', 'tab2');")
		driver.switch_to.window("tab2")
		driver.get('https://temp-mail.io/en')
		time.sleep(1)
	#copy email
		r=driver.find_element_by_xpath('//*[@id="__layout"]/div/header/div[3]/button[1]/span')
		r.click()

		driver.switch_to.window(driver.window_handles[0])
		e=driver.find_element_by_xpath('//*[@id="live_email"]')
		e.send_keys(Keys.CONTROL, 'v') # paste


#	sys.exit()
#r=driver.find_element_by_xpath('//*[@id="primary-menu"]/li[9]/div/a[2]')
#r.click()

#driver.get("https://trade.globalallianceltd.com/registration-ru")


#driver.implicitly_wait(10)
#time.sleep(2)

#r=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[1]')
#r.click()

#driver.implicitly_wait(3)

#r=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[2]')
#r.click()

#from selenium.webdriver.common.keys import Keys

#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#sys.exit()
#driver.implicitly_wait(100)
#webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#time.sleep(2)

#r=driver.find_element_by_xpath('//*[@id="top-nav"]/div[2]/div[4]/button')
#r.click()
#time.sleep(2)
#r=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div/div[1]/div[2]')
#r.click()
#time.sleep(2)

# create action chain object
#action = ActionChains(driver)
  
# context click the item
#action.context_click(on_element = element)
#driver.implicitly_wait(100)
#print ("right sidebar")
#sys.exit()
#print(driver.page_source)
		name1=driver.find_element_by_xpath('//*[@id="live_name"]')
		name1.send_keys(name)
#sys.exit()
#time.sleep(2)

		last_name=driver.find_element_by_xpath('//*[@id="live_last_name"]')
		last_name.send_keys(surname)
	
		select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[1]')
		select.click()

#lang
		select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[2]/ul/li[3]')
		select.click()



		select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]')
		select.click()
#sys.exit()
		co=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[2]/ul/li[110]')
		co.click()

		time.sleep(1)
#time.sleep(2)
		tn=random.randint(1000000, 9999999)
#tns="+371"+str(tn)
#tns="+7925"+str(tn)
		tns="2"+str(tn)
		phone=driver.find_element_by_id('live_phone')
#phone.clear()
		phone.send_keys(tns)


		select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[3]/label')
		select.click()
	
		select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[4]/label')
		select.click()
	
		driver.execute_script('document.getElementById("live_check").checked=true;')
#sys.exit()
#select=driver.find_element_by_css_selector('#live_check')
#select.click()
#WebElement we = driver.findElement(By.xpath("//span[contains(string(),'Remote PC')]"));
#Actions clickTriangle= new Actions(driver);
#clickTriangle.moveToElement(we).moveByOffset(-10, -5).click().perform();              



#time.sleep(2)
#birth=driver.find_element_by_id('user-birthday-reg')
#birth.click()
#time.sleep(2)
#day=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[1]/div[1]/input')

#d=random.randint(1, 28)
#ds=str(d)
#if (d<10):
#	ds="0"+ds
#day.send_keys(ds)

#time.sleep(2)#

#month=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[1]/div[2]/input')

#d=random.randint(1, 12)
#ds=str(d)
#if (d<10):
#	ds="0"+ds
#month.send_keys(ds)
#time.sleep(2)

#year=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[1]/div[3]/input')
#d=random.randint(1960, 2000)
#year.send_keys(str(d))
#time.sleep(2)
#driver.implicitly_wait(5)
#butrt
#b=driver.find_element_by_xpath('//*[@id="app"]/div[5]/div/section/div[1]/div[2]/div/div[2]/div[2]/button[1]')
#b.click()
#time.sleep(2)
#driver.close()
#driver.quit()

		domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',  'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv']
		password=""
		for i in range (1,5):
			password=password+random.choice('01234567890')

		username=generate_username(1)[0]+password
		domain=random.choice(domains)
		email=username+"@"+domain
		b=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/button')
		b.click()
		driver.switch_to.window(driver.window_handles[1])
		time.sleep(15)
		r=driver.find_element_by_xpath('//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li/div[1]')
		r.click()
		time.sleep(1)
		r=driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/p[6]/a')
		r.click()
		time.sleep(3)

		driver.switch_to.window(driver.window_handles[0])
		driver.get('https://24xfx.com/bbct/Documents')
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')
		time.sleep(5)
		driver.get('https://24xfx.com/bbct/Documents/Address')
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')


		driver.get('https://24xfx.com/bbct/Documents/CC')
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')

		driver.get('https://24xfx.com/bbct/Documents/Deposit')
		time.sleep(5)
		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')



		time.sleep(5)
#	b=driver.find_element_by_xpath('//*[@id="Logout-button"]')
#	b.click()
		driver.close()
		driver.quit()
	except:
		pass

