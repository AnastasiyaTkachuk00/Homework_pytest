from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = " https://baraholka.onliner.by/ "
browser.get(link)

find_videocard = browser.find_element(By.CSS_SELECTOR, 'div.b-cm-col   ul  li:nth-child(9)  sup')

find_dress = browser.find_element(By.XPATH, '//div[@class="b-whbd-i"]/div[5]/div[2]/div[2]/ul/li[5]/sup')

find_ad_button = browser.find_element(By.XPATH, '//div[@ class="b-mnforum-header fleamarket__1"]'
                                                '//a[contains( @href,"/fleamarketposting.php")]')
find_ad_button.click()

browser.close()
