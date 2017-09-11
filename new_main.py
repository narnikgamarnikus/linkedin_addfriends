from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from lxml import html
from selenium.webdriver.common.keys import Keys

url = "https://www.linkedin.com/"

username = ""
password = ""

browser = webdriver.Firefox()

def login():

	browser.get(url)

	pagekey = WebDriverWait(browser, 100).until(
		EC.presence_of_element_located((By.XPATH, "//body[@id='pagekey-uno-reg-guest-home']"))
	)
	application = WebDriverWait(browser, 100).until(
		EC.presence_of_element_located((By.XPATH, "//div[@id='application-body']"))
	)
	main = WebDriverWait(browser, 100).until(
		EC.presence_of_element_located((By.XPATH, "//main[@id='layout-main']"))
	)
	button = WebDriverWait(browser, 100).until(
		EC.presence_of_element_located((By.XPATH, "//input[@id='login-submit']"))
	)
	browser.find_element_by_xpath('//input[@id="login-email"]').send_keys(username)
	browser.find_element_by_xpath('//input[@id="login-password"]').send_keys(password)

	button.click()
	print("login success")


def go_to_network():

	button = WebDriverWait(browser, 100).until(
		EC.presence_of_element_located((By.XPATH, "//span[@id='mynetwork-tab-icon']"))
	)
	button.click()


def load_list_friends():
    
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)


def add_friend():

	list_friends = browser.find_elements_by_xpath('//button[@class="button-secondary-small"]')
	a = 0
	for i in list_friends:
		try:
			time.sleep(2)
			i.click()
			time.sleep(1)
			a += 1
			if a == 5:
				load_list_friends()
				a = 0
		except:
			print('ok')
			browser.refresh()
			time.sleep(5)
			print('refresh page...')


def add_while():
	while True:
		time.sleep(3)
		add_friend()



def main():
	login()

	time.sleep(5)

	go_to_network()

	time.sleep(5)

	add_while()


if __name__ == '__main__':
	main()