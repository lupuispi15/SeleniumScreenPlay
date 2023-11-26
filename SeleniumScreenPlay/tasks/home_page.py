import time
from ui.login_ui import LoginUi
from actions.display import Display
from actions.get import Get
from actions.send_keys import SendKeys
from selenium import webdriver
from actions.oprimirboton import Onclick
from ui.inicio_ui import HomeUi


class HomePage:
    def home_page(self, driver: webdriver):
        try:
            return Display().view_element(driver, HomeUi().xpath_name_product)
        except Exception as inst:
            print("Error: To home page request", inst)

    def page_itembutton_1(self, driver: webdriver):
        try:
            return Display().view_element(driver, HomeUi().xpath_buttondetail_product)
        except Exception as inst:
            print("Error: To home page request", inst)

    def page_itemprice_1(self, driver: webdriver):
        try:
            return Display().view_element(driver, HomeUi().xpath_pricedetail_product)
        except Exception as inst:
            print("Error: To home page request", inst)

    def page_itemimage_1(self, driver: webdriver):
        try:
            return Display().view_element(driver, HomeUi().xpath_imagedetail_product)
        except Exception as inst:
            print("Error: To home page request", inst)

    def page_itemname_1(self, driver: webdriver):
        try:
            return Display().view_element(driver, HomeUi().xpath_namedetail_product)
        except Exception as inst:
            print("Error: To home page request", inst)

    def page_iteminfo_1(self, driver: webdriver):
        try:
            return Display().view_element(driver, HomeUi().xpath_infodetail_product)
        except Exception as inst:
            print("Error: To home page request", inst)