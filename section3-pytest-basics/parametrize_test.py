import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


links = [
    236895,
    236896,
    236897,
    236898,
    236899,
    236903,
    236904,
    236905,
]
@pytest.mark.parametrize('links', links)
def test_send_answers_to_stepik_pages(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))

    textarea = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, "textarea"))
    ).send_keys(str(answer))

    browser.find_element_by_css_selector("button.submit-submission").click()

    text_answer = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH,
                                          "//pre[@class='smart-hints__hint']"))
    ).text

    assert "Correct!" == text_answer, f"expected answer - Corrcet, actual is: '{text_answer}'"