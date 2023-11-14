import time

from ui.login_ui import LoginUi
from actions.display import Display
from actions.get import Get
from actions.send_keys import SendKeys
from selenium import webdriver
from actions.oprimirboton import Onclick


class LoginPage:

    def init_page(self, driver: webdriver):
        try:
            Get().get(driver, LoginUi.base_url)
            driver.maximize_window()
            return Display().view_element(driver, LoginUi().button)
        except Exception as inst:
            print("Error: To init the request", inst)

    def enter_credential(self, driver: webdriver, user, password):
        try:
            SendKeys().send_text(driver, LoginUi().input_user, user)
            SendKeys().send_text(driver, LoginUi().input_password, password)
            Onclick().on_click_button(driver, LoginUi().button)
            time.sleep(5)
        except Exception as inst:
            print("Error: insert credential", inst)
