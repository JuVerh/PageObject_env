from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage:
    # конструктор — метод, который вызывается, когда создаем объект_
    def __init__(self, browser, url, timeout=10):
        # Конструктор объявляется ключевым словом __init_, в качестве параметров передаем экземпляр драйвера и url адрес
        self.browser = browser  # сохраняем экземляр браузера как аттрибут класса
        self.url = url  # сохраняем url как аттрибут класса
        self.browser.implicitly_wait(timeout)  # неявное ожидание - 10 секунд

    def open(self):
        self.browser.get(self.url)
# метод, чтобы перехватывать исключения
# два аргумента: как искать (css, id и тд) и что искать (строку-селектор).
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
