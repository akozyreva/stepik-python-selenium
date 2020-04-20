from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import math
import time

link = "http://suninjuly.github.io/find_link_text"
chrome_options = Options()
chrome_options.add_argument("--headless")

try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)
    link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    button = browser.find_element_by_link_text(link_text)
    button.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()