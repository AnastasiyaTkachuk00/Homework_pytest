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


def test_submit_button():
    submit_button = browser.find_element(By.NAME, 'et_builder_submit_button')
    submit_button.click()
    time.sleep(8)


def test_success_message():
    success_message = browser.find_element(By.XPATH, '//*[.="Please, fill in the following fields:"]')
    assert "Please, fill in the following fields:" in success_message

    browser.close()
