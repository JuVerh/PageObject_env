class BasePage():
    #конструктор — метод, который вызывается, когда создаем объект_
    def __init__(self, browser, url):
        #Конструктор объявляется ключевым словом __init_, в качестве параметров передаем экземпляр драйвера и url адрес
        self.browser = browser#сохраняем экземляр браузера как аттрибут класса
        self.url = url #сохраняем url как аттрибут класса

    def open(self):
        self.browser.get(self.url)
