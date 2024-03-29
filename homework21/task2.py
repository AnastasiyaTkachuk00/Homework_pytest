import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_web(browser):
    chrome = webdriver.Chrome()
    url = 'https://demoqa.com/text-box'
    chrome.get(url=url)
    chrome.maximize_window()
    full_name = chrome.find_element(By.ID, "userName")
    full_name.click()
    full_name.send_keys('tk_anastasiya')
    time.sleep(5)
    assert full_name.get_attribute('value') == "tk_anastasiya"

    email = chrome.find_element(By.ID, "userEmail")
    email.click()
    email.send_keys('tk_anasasiya@gmail.com')
    time.sleep(5)
    assert email.get_attribute('value') == "tk_anasasiya@gmail.com"

    curr_addr = chrome.find_element(By.ID, "currentAddress")
    curr_addr.click()
    curr_addr.send_keys('Minsk')
    time.sleep(5)
    assert curr_addr.get_attribute('value') == "Minsk"

    perm_addr = chrome.find_element(By.ID, "permanentAddress")
    perm_addr.click()
    perm_addr.send_keys('Lida')
    time.sleep(5)
    assert perm_addr.get_attribute('value') == "Lida"

    submit_button = chrome.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(5)

    chrome.close()
