import unittest
from selenium import webdriver
import time


class TestRegistration(unittest.TestCase):
    def reg_form(self, link_url):
        browser = webdriver.Chrome()
        browser.get(link_url)

        # Ваш код, который заполняет обязательные поля
        placeholders = ['Input your first name', 'Input your last name',
                        'Input your email']
        data = ['Mike', 'Smith', "mike@test.com"]
        for i in range(len(placeholders)):
            input_field = browser.find_element_by_xpath("//input[@placeholder=" + "'" + placeholders[i] + "'" + "]")
            input_field.send_keys(data[i])
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        congrat_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, congrat_text,
                         f"{welcome_text} is another than {congrat_text}")
        browser.quit()

    def test_abs1(self):
        self.reg_form("http://suninjuly.github.io/registration1.html")

    def test_registration2(self):
        self.reg_form("http://suninjuly.github.io/registration2.html")


if __name__ == "__main__":
    unittest.main()