from selenium import webdriver
import time

link ="http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
class_list =['first',"second","third"]
text_list  =['A1','A2','A3']
x=0
try:
    for i in class_list:
        input1 = browser.find_element_by_class_name(class_list[x])
        input1.send_keys(text_list[x])
        x+=1

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name("h1").text
    #print(welcome_text_elt)
    #print(welcome_text)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
   # успеваем скопировать код за 30 секунд
    time.sleep(15)
   # закрываем браузер после всех манипуляций
    browser.quit()
