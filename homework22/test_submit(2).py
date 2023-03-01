import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://ultimateqa.com/filling-out-forms/"
browser.get(link)
browser.maximize_window()

name_field = browser.find_element(By.ID, 'et_pb_contact_name_0')
name_field.click()
name_field.send_keys('Test')
time.sleep(3)

submit_button = browser.find_element(By.NAME, 'et_builder_submit_button')
submit_button.click()
time.sleep(8)

success_message = browser.find_element(By.XPATH, '//*[.="Please, fill in the following fields:"]')
assert success_message == 'Please, fill in the following fields:'

browser.close()
