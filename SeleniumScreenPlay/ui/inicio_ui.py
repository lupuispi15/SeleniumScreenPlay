
class HomeUi:

    base_url = "https://www.saucedemo.com/inventory.html"
    base_url_item = "https://www.saucedemo.com/inventory-item.html?id=4"
    xpath_image_product = '//*[@id="item_4_img_link"]/img'
    xpath_name_product = '//*[@id="item_4_title_link"]/div'
    xpath_info_product = '//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]/div'
    xpath_button_product = '//*[@id="add-to-cart-sauce-labs-backpack"]'
    xpath_price_product = '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div'
    xpath_imagedetail_product = '//*[@id="inventory_item_container"]/div/div/div[1]/img'
    xpath_namedetail_product = '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]'
    xpath_infodetail_product = '//*[@id="inventory_item_container"]/div/div/div[2]/div[2]'
    xpath_pricedetail_product = '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]'
    xpath_buttondetail_product= '//*[@id="add-to-cart-sauce-labs-backpack"]'
