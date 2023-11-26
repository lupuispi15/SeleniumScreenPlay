import time
from ui.login_ui import LoginUi
from actions.display import Display
from actions.get import Get
from actions.send_keys import SendKeys
from selenium import webdriver
from actions.oprimirboton import Onclick
from ui.inicio_ui import HomeUi
from ui.carrito_ui import carritoUi


class CarritoPage:

  def carrito_page(self, driver: webdriver):
    try:
        Get().get(driver, HomeUi.base_url)
        driver.maximize_window()
        return Display().view_element(driver, LoginUi().button)
    except Exception as inst:
        print("Error: To init the request", inst)

  def carrito_item(self, driver: webdriver):
      try:
          return Display().view_element(driver, carritoUi.items)
      except Exception as inst:
          print("Error: To home page request", inst)

  def form_view(self, driver: webdriver):
      try:
          return Display().view_element(driver, carritoUi.formulariocheck)
      except Exception as inst:
          print("Error: To home page request", inst)
