import unittest
import time
from selenium import webdriver
from tasks.login_page import LoginPage
from tasks.home_page import HomePage
from actions.oprimirboton import Onclick
from ui.login_ui import LoginUi
from ui.inicio_ui import HomeUi
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Test_Home(unittest.TestCase):

    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    __user = 'standard_user'
    __password = 'secret_sauce'
    __urlhome = 'https://www.saucedemo.com/inventory.html'



    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test1_home_view(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        driver = self.driver
        LoginPage().enter_credential(driver, self.__user, self.__password)
        page_home = HomePage().home_page(self.driver)
        self.assertTrue(page_home)

    def test2_details_product(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)
        driver = self.driver
        LoginPage().enter_credential(driver, self.__user, self.__password)
        page_home = HomePage().home_page(self.driver)
        self.assertTrue(page_home)
        Onclick().on_click_button(driver, HomeUi().xpath_name_product)
        button_addtocar_item1 = HomePage().page_itembutton_1(self.driver)
        image_item1 = HomePage().page_itemimage_1(self.driver)
        price_item1_mochila = HomePage().page_itemprice_1(self.driver)
        name_item1 = HomePage().page_itemprice_1(self.driver)
        info_item1 = HomePage().page_itemprice_1(self.driver)
        self.assertTrue(button_addtocar_item1 and price_item1_mochila and image_item1 and name_item1 and info_item1)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()