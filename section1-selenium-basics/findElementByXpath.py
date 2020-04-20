from selenium import webdriver
from selenium.webdriver.chrome.options import Options

link = "http://suninjuly.github.io/find_xpath_form"
chrome_options = Options()
chrome_options.add_argument("--headless")

try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)
    
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла