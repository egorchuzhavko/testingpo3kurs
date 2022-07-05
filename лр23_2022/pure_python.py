import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase) :
    def setUp(self) :
        self.driver = webdriver. Chrome()

    # def test_search_in_python_org(self):
    #     driver = self.driver
    #     driver.get(" http://www.python.org ")
    #     self.assertIn("Python", driver.title)
    #     # ждем 5 секунд
    #     time. sleep(5)
    #     elem = driver.find_element_by_name("q")
    #     time.sleep(5)
    #     elem.send_keys("Колледж бизнеса и права")
    #     time.sleep(5)
    #     # нажатие кнопки Enter в найденном элементе
    #     elem. send_keys(Keys.RETURN)
    #     time.sleep(5)
    #     self.assertIn("No results found.", driver.page_source)
    #     time.sleep(5)
    #     elem = driver.find_element_by_name("q")
    #     elem.clear()
    #     time.sleep(5)
    #     elem.send_keys("pycon")
    #     time.sleep(5)
    #     elem.send_keys(Keys.RETURN)
    #     time.sleep(5)
    #     # проверка отсутствия строки "No results found."
    #     # на странице с результатами поиска
    #     self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self) :
        self.driver.close()
    
    # def test_login_logout(self) :
    #     driver = self.driver
    #     driver.get("https://www.python.org/psf-landing/")
    #     time.sleep(5)
    #     elem = driver.find_element_by_link_text("Sign In")
    #     elem.click()
    #     time.sleep(5)
    #     elem = driver.find_element_by_xpath("//input[@name='login']")
    #     elem.send_keys("aenerba")
    #     time.sleep(5)
    #     elem = driver.find_element_by_xpath("//input[@name='password']")
    #     elem.send_keys("qwerty123")
    #     time.sleep(5)
    #     # жмем ввод для отправки формы
    #     elem.send_keys(Keys.RETURN)
    #     time.sleep(5)
    #     self.assertIn("Your account", driver.page_source)
    #     time.sleep(5)
    #     print(driver.page_source)
    #     driver.get("https://www.python.org/accounts/logout/")
    #     time.sleep(5)
    #     elem = driver.find_element_by_css_selector(
    #     'div.container section.main-content form button'
    #     )
    #     elem.click()
    #     time.sleep(5)
    #     self.assertNotIn("Your account", driver.page_source)
    
    # def test_about_breadcrumbs(self):
    #     driver = self.driver
    #     driver.get("http://www.python.org")
    #     elems = driver.find_elements_by_css_selector('#about ul li a')
    #     href_list = []
    #     name_list = []
    #     for e in elems:
    #         href_list.append(e.get_attribute("href"))
    #         name_list.append(e.get_attribute('innerHTML'))

    #     # перебираем полученные ссылки
    #     for i in range(len(href_list)-1):
    #     # переходим по ссылке
    #         driver.get(
    #             href_list[i]
    #         )
    #         # получаем строчку хлебных крошек
    #         elem = driver.find_element_by_css_selector('.breadcrumbs')
    #         # проверка наличия в хлебных крошках ссылки на пункт About
    #         self.assertIn("About", elem.get_attribute('innerHTML'))
    #         # проверка наличия в хлебных крошках
    #         # наличия названия текущено пункта
    #         self.assertIn(
    #             # название текущего пункта
    #             name_list[i],
    #             #строчка хлебных крошек
    #             elem.get_attribute('innerHTML')
    #         )
    #         time.sleep(5)
    
    def test_change_username_profile(self):
        driver=self.driver
        driver = self.driver
        driver.get("https://www.python.org/psf-landing/")
        time.sleep(2)
        elem = driver.find_element_by_link_text("Sign In")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//input[@name='login']")
        elem.send_keys("aenerba")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//input[@name='password']")
        elem.send_keys("qwerty123")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertIn("Your account", driver.page_source)
        time.sleep(2)
        driver.get("https://www.python.org/users/edit/")
        elem=driver.find_element_by_xpath("//input[@id='id_first_name']")
        elem.clear()
        elem.send_keys("Егор")
        elem=driver.find_element_by_xpath("//input[@id='id_last_name']")
        elem.clear()
        elem.send_keys("Чужавко")
        time.sleep(2)
        elem=driver.find_element_by_css_selector("button[name='Submit']")
        elem.click()
        time.sleep(3)
        self.assertIn("Егор Чужавко | Our Users & Members | Python.org",driver.title)
        time.sleep(2)

    def test_login_user(self):
        driver=self.driver
        driver = self.driver
        driver.get("https://www.python.org/accounts/signup/")
        time.sleep(2)
        self.assertIn("Signup for Python.org",driver.title)
        time.sleep(2)
        elem = driver.find_element_by_css_selector("#id_email")
        elem.send_keys("faster.aaa1231@gmail.com")
        elem = driver.find_element_by_xpath("(//input[@id='id_username'])[1]")
        elem.send_keys("aenerba")
        elem = driver.find_element_by_xpath("(//input[@id='id_password1'])[1]")
        elem.send_keys("qwerty123")
        elem=driver.find_element_by_xpath("(//input[@id='id_password2'])[1]")
        elem.send_keys("qwerty123")
        time.sleep(2)
        elem=driver.find_element_by_xpath("(//button[normalize-space()='Sign Up »'])[1]")
        elem.click()
        self.assertIn("A user is already registered with this e-mail address.",driver.page_source)
        self.assertIn("A user with that username already exists.",driver.page_source)        

        

if __name__ =='__main__':
    unittest.main()