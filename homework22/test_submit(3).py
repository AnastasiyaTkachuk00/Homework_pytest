import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://ultimateqa.com/filling-out-forms/"
browser.get(link)
browser.maximize_window()

message_field = browser.find_element(By.ID, 'et_pb_contact_message_0')
message_field.click()
message_field.send_keys('Test')
time.sleep(4)

submit_button = browser.find_element(By.NAME, 'et_builder_submit_button')
submit_button.click()
time.sleep(5)

success_message = browser.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div/p')
time.sleep(10)
assert success_message == 'Please, fill in the following fields:'

browser.close()
