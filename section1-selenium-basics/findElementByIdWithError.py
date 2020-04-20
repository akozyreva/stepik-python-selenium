from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

link = "http://suninjuly.github.io/simple_form_find_task.html"
chrome_options = Options()
chrome_options.add_argument("--headless")

try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()