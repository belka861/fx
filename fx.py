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


while True:

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

	name1=driver.find_element_by_xpath('//*[@id="live_name"]')
	name1.send_keys(name)

	last_name=driver.find_element_by_xpath('//*[@id="live_last_name"]')
	last_name.send_keys(surname)
	
	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[1]')
	select.click()

#lang
	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[2]/div/div[2]/ul/li[3]')
	select.click()



	select=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[1]')
	select.click()
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

	domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',  'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv']
	password=""
	for i in range (1,5):
		password=password+random.choice('01234567890')

	username=generate_username(1)[0]+password
	domain=random.choice(domains)
	email=username+"@"+domain

	e=driver.find_element_by_xpath('//*[@id="live_email"]')
	e.send_keys(email)


	b=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/button')
	b.click()

	time.sleep(20)
	driver.close()
	driver.quit()
	sys.exit()
