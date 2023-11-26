import unittest
import time
from selenium import webdriver
from tasks.login_page import LoginPage
from tasks.home_page import HomePage
from actions.oprimirboton import Onclick
from ui.carrito_ui import carritoUi
from tasks.carrito_page import CarritoPage
from ui.login_ui import LoginUi
from ui.inicio_ui import HomeUi
from tasks.carrito_page import CarritoPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service



class Test_Carrito(unittest.TestCase):

    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    __user = 'standard_user'
    __user2 = 'performance_glitch_user'
    __password = 'secret_sauce'
    __urlhome = 'https://www.saucedemo.com/inventory.html'

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test1_carrito(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        driver = self.driver
        LoginPage().enter_credential(driver, self.__user, self.__password)
        page_home = HomePage().home_page(self.driver)
        self.assertTrue(page_home)
        Onclick().on_click_button(driver, carritoUi().button_addtocar)
        Onclick().on_click_button(driver, carritoUi().button_carrito)
        carritoitems = CarritoPage().carrito_item(self.driver)
        self.assertTrue(carritoitems)

    def test2_checkout(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        driver = self.driver
        LoginPage().enter_credential(driver, self.__user, self.__password)
        page_home = HomePage().home_page(self.driver)
        self.assertTrue(page_home)
        Onclick().on_click_button(driver, carritoUi().button_addtocar2)
        Onclick().on_click_button(driver, carritoUi().button_carrito)
        carritoitems = CarritoPage().carrito_item(self.driver)
        self.assertTrue(carritoitems)
        Onclick().on_click_button(driver, carritoUi.botoncheckout)
        formulario = CarritoPage().form_view(self.driver)
        self.assertTrue(formulario)

