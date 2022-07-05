import time
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()
# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)
# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://bga.by/contacts")
time.sleep(5)
# Метод find_element_by_tag_name позволяет найти нужный элемент на сайте по названию тега, указав путь к нему.
# Ищем поле для ввода текста
textarea = driver.find_element_by_tag_name("textarea")
# Напишем текст в поле "Сообщение"
textarea.send_keys("Мой первый тест через Selenium")
# Метод find_element_by_id позволяет найти нужный элемент на сайте по его ID, указав путь к нему.
# Ищем поле для ввода текста
username = driver.find_element_by_id("124158159")
# Напишем текст в поле "Имя"
username.send_keys("Здесь введено мое имя")
time.sleep(5)



email=driver.find_element_by_id("124158160")
email.send_keys("exampleemail@gmail.com")
time.sleep(5)



# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element_by_css_selector("#submitFormContacts")
# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)
# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()