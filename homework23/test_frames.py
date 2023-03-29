from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_frame():
    browser = webdriver.Chrome()
    link = "http://the-internet.herokuapp.com/iframe"
    browser.get(link)

    frame_field = (By.CLASS_NAME, 'large-12 columns')
    frame_locator = (By.XPATH, '//*[@id="mce_0_ifr"]')
    frame_obj = WebDriverWait(browser, 3).until(EC.presence_of_element_located(frame_locator))
    browser.switch_to.frame(frame_obj)

    message_locator = (By.XPATH, '//*[@id="tinymce"]/p')
    message = WebDriverWait(browser, 10).until(EC.presence_of_element_located(message_locator))
    assert message.text == 'Your content goes here.'

    browser.close()
