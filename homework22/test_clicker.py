from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://ultimateqa.com/complicated-page/"
browser.get(link)

css_button = browser.find_element(By.CSS_SELECTOR, 'div.et_pb_button_module_wrapper'
                                                   '.et_pb_button_4_wrapper'
                                                   '.et_pb_button_alignment_left.et_pb_module  a')
css_button.click()

xpath_button = browser.find_element(By.XPATH, '//div[@class="et_pb_button_module_wrapper '
                                              'et_pb_button_4_wrapper '
                                              'et_pb_button_alignment_left et_pb_module"]/a')
xpath_button.click()


class_button = browser.find_element(By.CLASS_NAME, 'et_pb_button_module_wrapper '
                                                   'et_pb_button_4_wrapper '
                                                   'et_pb_button_alignment_left et_pb_module')
class_button.click()

browser.close()
