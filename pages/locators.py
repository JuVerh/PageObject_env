from selenium.webdriver.common.by import By


class MainPageLocators:  # Каждый класс будет соответствовать каждому классу PageObject:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:  # Каждый класс будет соответствовать каждому классу PageObject:
    #кнопка добавления в корзину
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    #Сообщение о том, что товар добавлен в корзину
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, ".alertinner")
    # Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


