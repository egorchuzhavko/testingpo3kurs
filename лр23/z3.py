from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/find_link_text"
try:#'224592'
    browser = webdriver.Chrome()
    browser.get(link)
    link=browser.find_element_by_link_text('224592')
    link.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Marina")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrova")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Minsk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Belarus")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла

#Congrats, you've passed the task! Copy this code as the answer for Stepik quiz: 25.21504110170595