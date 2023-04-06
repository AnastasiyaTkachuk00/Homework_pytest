import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://ultimateqa.com/filling-out-forms/"
browser.get(link)
browser.maximize_window()


def test_1():
    name_field = browser.find_element(By.ID, 'et_pb_contact_name_0')
    name_field.click()
    name_field.send_keys('Test')
    time.sleep(3)

    message_field = browser.find_element(By.ID, 'et_pb_contact_message_0')
    message_field.click()
    message_field.send_keys('Test')
    time.sleep(4)

    submit_button = browser.find_element(By.NAME, 'et_builder_submit_button')
    submit_button.click()
    time.sleep(5)

    success_message = browser.find_element(By.CSS_SELECTOR, '#et_pb_contact_form_0 > div > p')
    success_text = success_message.text
    assert 'Thanks for contacting us' in success_text


def test_2():
    name_field = browser.find_element(By.ID, 'et_pb_contact_name_0')
    name_field.click()
    name_field.send_keys('Test')
    time.sleep(3)

    submit_button = browser.find_element(By.NAME, 'et_builder_submit_button')
    submit_button.click()
    time.sleep(8)

    success_message = browser.find_element(By.XPATH, '//*[.="Please, fill in the following fields:"]')
    success_text = success_message.text
    assert 'Please, fill in the following fields:' in success_text


def test_3():
    message_field = browser.find_element(By.ID, 'et_pb_contact_message_0')
    message_field.click()
    message_field.send_keys('Test')
    time.sleep(4)

    submit_button = browser.find_element(By.NAME, 'et_builder_submit_button')
    submit_button.click()
    time.sleep(5)

    success_message = browser.find_element(By.XPATH, '//*[@id="et_pb_contact_form_0"]/div/p')
    success_text = success_message.text
    assert 'Please, fill in the following fields:' in success_text
