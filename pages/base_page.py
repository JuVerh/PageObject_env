from selenium.common.exceptions import NoSuchElementException

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
