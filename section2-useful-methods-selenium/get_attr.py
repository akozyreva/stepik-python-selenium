from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
chrome_options = Options()
chrome_options.add_argument("--headless")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)
    x_val = browser.find_element_by_id('treasure').get_attribute("valuex")
    assert x_val is not None, "x value wasn't found, please check your test or web site"
    desicion = calc(x_val)
    browser.find_element_by_id("answer").send_keys(desicion)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_xpath("//input[@type='radio' and @value='robots']").click()
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