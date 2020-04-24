from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import math
import time

link = "http://suninjuly.github.io/math.html"
chrome_options = Options()
chrome_options.add_argument("--headless")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    desicion = calc(x)
    browser.find_element_by_id("answer").send_keys(desicion)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_xpath("//label[contains(text(),'Robots rule')]").click()
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