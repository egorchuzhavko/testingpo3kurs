import time
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)

driver.get("https://hdrezka.ag")
time.sleep(5)

fb=driver.find_element_by_class_name("b-tophead__register")
fb.click()
time.sleep(5)
name = driver.find_element_by_id("email")
name.send_keys("почта")
email = driver.find_element_by_id("name")
email.send_keys("Анастасия")
coment = driver.find_element_by_id("password1")
coment.send_keys("пароль")
time.sleep(5)

submit_button = driver.find_element_by_class_name("fieldsubmit")
submit_button.click()
time.sleep(5)

driver.quit()