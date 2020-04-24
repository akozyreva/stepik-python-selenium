from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import math
import time

link = "http://suninjuly.github.io/selects1.html"
chrome_options = Options()
chrome_options.add_argument("--headless")


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)
    # //select[@id='dropdown']
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    print(num1, num2)
    sum = int(num1) + int(num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum)) # select sum of values

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    # успеваем скопировать код за 30 секунд
    # time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()