from selenium import webdriver
import config

browser = webdriver.Chrome()
browser.get("https://github.com")
browser.maximize_window()

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys(config.username)
password_box = browser.find_element_by_id("password")
password_box.send_keys(config.password)
password_box.submit()
