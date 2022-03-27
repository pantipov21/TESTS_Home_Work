import time
import sys
sys.path.append("/usr/lib/python3/dist-packages")
import six
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

URL = "https://passport.yandex.ru/auth/"


class YandexAccessFirefox():
    def __init__(self, url):
        self.login_name = input("Введите логин: ")
        self.login_passwd = input("Введите пароль: ")
        print("Загрузка страницы авторизации...")
        self.driver = webdriver.Firefox()
        self.driver.minimize_window()
        try:
            self.driver.get(url)
        except WebDriverException as e:
            print("Что-то не так с подключением к сети Интернет")
            self.driver.close()
            exit(0)


    def wait_progress(self, a: int):
        print(f'Ждём немного.', end='')
        while a > 0:
            print('.', end='')
            a = a - 1
            time.sleep(1)
        print('\n')
        return 0

    def process(self):
        print("Ввод логина...")
        elem = self.driver.find_element(By.ID, value="passp-field-login")
        elem.send_keys(self.login_name)

        elem = self.driver.find_element(By.ID, value="passp:sign-in")
        elem.click()
        self.wait_progress(5)

        try:
            error_hint = self.driver.find_element(By.ID, value="field:input-login:hint")
            print(error_hint.text)
            self.driver.close()
            return -1
        except Exception as e:
            print("Логин приемлемый")


        print("Ввод пароля...")
        elem = self.driver.find_element(By.ID, value="passp-field-passwd")
        elem.send_keys(self.login_passwd)
        self.wait_progress(2)
        elem = self.driver.find_element(By.ID, value="passp:sign-in")
        elem.click()

        try:
            error_hint = self.driver.find_element(By.ID, value="field:input-passwd:hint")
            print(error_hint.text)
            self.driver.close()
            return -2
        except Exception as e:
            return 0


yandex_access = YandexAccessFirefox(URL)
res = yandex_access.process()
if res == 0:
    print("Авторизация выполнена")
else:
    print("Авторизация НЕ выполнена")



