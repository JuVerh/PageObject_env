from .base_page import BasePage   # импорт базового класса
from selenium.webdriver.common.by import By


class MainPage(BasePage):  # класс MainPage наследуется от BasePage - будет иметь доступ ко всем его атрибутам и методам
    def go_to_login_page(self):  # вместо browser(мы его передаем и сохраняем на этапе создания Page Object)
        # укажем аргумент self, чтобы иметь доступ к атрибутам и методам класса
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        # обращаемся с self тк браузер хранится как аргумент класса BasePage
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
