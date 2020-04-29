from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
chrome_options = Options()
chrome_options.add_argument("--headless")


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("Mike")
    browser.find_element_by_name("lastname").send_keys("Smith")
    browser.find_element_by_name("email").send_keys("test@test.orj")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(current_dir, 'input_file.txt')
    browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    browser.quit()