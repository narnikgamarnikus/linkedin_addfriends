from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

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


def go_to_network():

	button = WebDriverWait(browser, 100).until(
		EC.presence_of_element_located((By.XPATH, "//span[@id='mynetwork-tab-icon']"))
	)

	button.click()


def add_friend():

	grid = WebDriverWait(browser, 100).until(
		EC.presence_of_element_located((By.XPATH, "//section[@class='mn-pymk-list Elevation-2dp ember-view']"))
	)

	html = browser.page_source
	soup  = BeautifulSoup(html, "html.parser")

	#buttons = soup.findAll("button", { "class" : "button-secondary-small" })
	items = soup.findAll("div", { "class" : "mn-person-info" })

	for item in items:

		print(item)


def main():
	login()

	time.sleep(5)

	go_to_network()

	time.sleep(5)

	add_friend()


if __name__ == '__main__':
	main()