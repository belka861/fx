from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
from phone_gen import PhoneNumber
from selenium.webdriver.common.keys import Keys
import sys, random

# Import pandas
import pandas as pd
import time,datetime

from random_username.generate import generate_username

def _click(xpath):
	r=driver.find_element_by_xpath(xpath)
	r.click()
	return True

logfile="fx.log"
def _log(message):
    fh=open(logfile,"a",encoding="cp1251")
    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    print(text)
    fh.write(text)
    fh.close()
    return True



with open ("names.txt", "r", encoding='utf-8', errors='ignore') as myfile:
	names=myfile.readlines()

with open ("surnames.txt", "r", encoding='utf-8', errors='ignore') as myfile:
	surnames=myfile.readlines()


while True:
	while True:
#	try:
# reading csv file 
##		max_sur=round(df.size/6-1)
#		random_sur_id=random.randint(1, max_sur)
 #
#		surname=df['Surname'][random_sur_id]


#		df=pd.read_csv("russian_names.csv", header=0, sep=';')
#		max_sur=round(df.size/6-1)
#		random_sur_id=random.randint(1, max_sur)
#		name=df['Name'][random_sur_id]

#		with open ("names.txt", "r", encoding='utf-8', errors='ignore') as myfile:
#			data=myfile.readlines()
		
		name=names[random.randint(1, len(names)-1)]
		surname=surnames[random.randint(1, len(surnames)-1)]


		print (name, surname)


		PATH = 'C:\Program Files (x86)\chromedriver.exe'
		driver = webdriver.Chrome(PATH,options=chrome_options)
#		driver = webdriver.Chrome(PATH)
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

#		import win32clipboard
#		win32clipboard.OpenClipboard()
#		email = win32clipboard.GetClipboardData()
#		win32clipboard.CloseClipboard()

#  String output = driver.findElement(By.xpath("/html/body/div[1]/div[5]/div/div/div[1]/div[2]/div[1]/div")).getText();
 # File DestFile= new File("extractedFilePath");
#  FileUtils.writeStringToFile(DestFile, output);


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

		#counbtries
#		countries=[75]
		countries=[11,15,20,27,52,53,55,61,65,70,74,78,90,98,103,108,110,116,117,119,132,143,146,153,163,169,170,188,189,201,202,205,213,218,219,221,75]
		crandom=random.choice(countries)
#		codes={75,11}		
#		crandom=random.randint(2, 150)
#		if (crandom==37):
#			crandom=38
#		if (crandom==12):
#			crandom=13
		print (crandom)
		co=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/div[1]/div[2]/ul/li['+str(crandom)+']')
		print (co.text)
		ph=PhoneNumber(co.text)
		tn=ph.get_number(full=False)
#		tnf=ph.get_number()
#		_log (tnf)
		_log (tn)
#		print (tn)

#		sys.exit()
		co.click()

#		time.sleep(1)
#time.sleep(2)                      python
#		tn=random.randint(10**crandom, 9999999)
#tns="+371"+str(tn)
#tns="+7925"+str(tn)
#		tns="2"+str(tn)
		tns=str(tn)
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
#		_log (email + " "+password)
		username=generate_username(1)[0]+password
		domain=random.choice(domains)
#		email=username+"@"+domain
		b=driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div/form/button')
		b.click()
		driver.switch_to.window(driver.window_handles[1])

		#wait for wmail
#		time.sleep(15)
		try:
			r = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li/div[1]')))
		except:
			print ("timeout")
			driver.close()
			driver.quit()
			pass
		r.click()
#		print ("found")
#		sys.exit()
		try:
			r = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/p[6]/a')))
		except:
			print ("timeout clicking")
			driver.close()
			driver.quit()
			pass


#		r=driver.find_element_by_xpath('//*[@id="__layout"]/div/aside/div[1]/div[2]/div/div/ul/li/div[1]')
		r.click()
		time.sleep(1)
		#click on link
#		r=driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td/div/p[6]/a')
#		r.click()
		r=driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div/div[1]/article/div/div[3]/span/div/center/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td').text
		_log (r)
		
#		time.sleep(3)
#		sys.exit()
#		driver.switch_to.window(driver.window_handles[0])
#		driver.get('https://24xfx.com/bbct/Documents')
#		time.sleep(5)
#		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')
#		time.sleep(5)
#		driver.get('https://24xfx.com/bbct/Documents/Address')
#		time.sleep(5)
#		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')


#		driver.get('https://24xfx.com/bbct/Documents/CC')
#		time.sleep(5)
#		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')

#		driver.get('https://24xfx.com/bbct/Documents/Deposit')
#		time.sleep(5)
#		driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div/div[2]/div[1]/div/div/input').send_keys('c:\\temp\\'+str(random.randint(1, 27))+'.jpg')



		time.sleep(10)
#	b=driver.find_element_by_xpath('//*[@id="Logout-button"]')
#	b.click()
		driver.close()
		driver.quit()
#	except:
#		driver.close()
##		print ("exception")

