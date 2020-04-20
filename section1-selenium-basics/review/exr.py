from selenium import webdriver
import time

site = 'http://suninjuly.github.io/registration1.html'
try:
    browser = webdriver.Chrome()
    browser.get(site)
    time.sleep(1)
    browser.find_element_by_css_selector('.first_block .first').send_keys('1')
    browser.find_element_by_css_selector('.first_block .second').send_keys('2')
    browser.find_element_by_css_selector('.first_block .third').send_keys('3')
    browser.find_element_by_class_name('btn-default').click()
    time.sleep(1)
    finalText = browser.find_element_by_tag_name('h1').text
    assert "Congratulations! You have successfully registered!" == finalText
finally:
    time.sleep(5)
    browser.quit()