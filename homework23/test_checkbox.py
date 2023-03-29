import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = "http://the-internet.herokuapp.com/dynamic_controls"
browser.get(link)


def test_check_button():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    check_button = (By.CSS_SELECTOR, 'input[type=checkbox]')
    check = WebDriverWait(browser, 10).until(EC.presence_of_element_located(check_button))
    check.click()


def test_remove_button():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    remove_button = (By.CSS_SELECTOR, '#checkbox-example > button')
    remove = WebDriverWait(browser, 10).until(EC.presence_of_element_located(remove_button))
    remove.click()


def test_check_button_on_page(CSS_SELECTOR):
    return len(browser.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')) > 0


def test_input_field():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    input_field = (By.CSS_SELECTOR, 'input[type=text]')
    input_f = WebDriverWait(browser, 10).until(EC.presence_of_element_located(input_field))
    assert not input_f.is_enabled()


def test_enable_button():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/dynamic_controls"
    browser.get(link)
    enable_button = (By.CSS_SELECTOR, '#input-example > button')
    input_field = (By.CSS_SELECTOR, 'input[type=text]')
    input_f = WebDriverWait(browser, 10).until(EC.presence_of_element_located(input_field))
    enable = WebDriverWait(browser, 10).until(EC.presence_of_element_located(enable_button))
    enable.click()
    time.sleep(10)
    assert input_f.is_enabled()
