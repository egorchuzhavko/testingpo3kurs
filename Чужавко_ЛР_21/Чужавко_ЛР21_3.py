import time
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://beyondvelocity.blog/contact/")
time.sleep(5)

name = driver.find_element_by_id("g3-name")
name.send_keys("Имя")
email = driver.find_element_by_id("g3-email")
email.send_keys("почта")
coment = driver.find_element_by_id("contact-form-comment-g3-comment")
coment.send_keys("Комментарий")
time.sleep(5)

submit_button = driver.find_element_by_class_name("pushbutton-wide")
submit_button.click()
time.sleep(5)

driver.quit()