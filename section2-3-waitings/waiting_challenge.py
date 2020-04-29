from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import math
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
chrome_options = Options()
#chrome_options.add_argument("--headless")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get(link)

    # waiting for price
    confirm_btn = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    confirm_btn.click()


    # get num
    num = browser.find_element_by_id("input_value").text
    final_num = calc(num)
    browser.find_element_by_id("answer").send_keys(final_num)

    button = browser.find_element_by_id("solve")
    button.click()

    alert = browser.switch_to_alert()
    alert_text = alert.text
    print(alert_text)

finally:
    # успеваем скопировать код за 30 секунд
    # time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()