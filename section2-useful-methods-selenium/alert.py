from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import math
import os 

link = "http://suninjuly.github.io/alert_accept.html"
chrome_options = Options()
chrome_options.add_argument("--headless")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)

    browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to_alert()
    alert.accept()

    num = browser.find_element_by_id("input_value").text
    final_num = calc(num)
    browser.find_element_by_tag_name("input").send_keys(final_num)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    browser.quit()