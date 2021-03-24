import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#Your chrome driver directory
PATH = "/home/ricardo/chromedriver"

#Device setup
mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


def bot():
	driver = webdriver.Chrome(PATH, desired_capabilities = chrome_options.to_capabilities())

	#Your promotion
	driver.get("https://a.aliexpress.com/_mqVbrUB")

	driver.implicitly_wait(10)
	slash_promotion_button = driver.find_element_by_class_name("am-button")
	slash_promotion_button.click()

	driver.implicitly_wait(10)
	ActionChains(driver).move_to_element(slash_button).click(slash_button)

	time.sleep(1)
	account_link_button = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div/a')
	account_link_button.click()
	register_button = driver.find_element_by_class_name("fm-tabs-tab")
	register_button.click()


	#Fill form
	email = ''.join(random.choice(string.ascii_letters) for x in range(15))

	email_input = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[2]/input')
	email_input.click()
	email_input.send_keys(email+"@gmail.com")

	pass_input = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/div[3]/input')
	pass_input.click()
	pass_input.send_keys(email)

	complete_button = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[1]/div/div/button')
	complete_button.click()

	slash_button = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div[4]/div/div/a')
	slash.click()

	time.sleep(3)
	driver.close()

repeat = int(input("Number of accounts: "))
for i in range(repeat):
	bot()
