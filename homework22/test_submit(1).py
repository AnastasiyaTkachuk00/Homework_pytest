import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://ultimateqa.com/filling-out-forms/"
browser.get(link)
browser.maximize_window()


def test_name_field():
    name_field = browser.find_element(By.ID, 'et_pb_contact_name_0')
    name_field.click()
    name_field.send_keys('Test')
    time.sleep(3)


def test_message_field():
    message_field = browser.find_element(By.ID, 'et_pb_contact_message_0')
    message_field.click()
    message_field.send_keys('Test')
    time.sleep(4)


def test_submit_button():
    submit_button = browser.find_element(By.NAME, 'et_builder_submit_button')
    submit_button.click()
    time.sleep(5)


def test_success_message():
    success_message = browser.find_element(By.CSS_SELECTOR, '#et_pb_contact_form_0 > div > p')
    time.sleep(5)

    assert 'Thanks for contacting us' in success_message
