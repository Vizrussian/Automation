# Задача №4
# Для сайта https://www.saucedemo.com/ напишите тест,
# в котором добавляется 3 товара в корзину и проверяется количество товаров в корзине.

# Сценарий: зайти на сайт -> залогиниться -> добавить любых 3 товара в корзину ->
# перейти в корзину -> проверить что количество товаров в корзине = 3

from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
# Get to our site
driver.get("https://www.saucedemo.com/")
# Login
login = driver.find_element_by_name("user-name")
login.send_keys("standard_user")
password = driver.find_element_by_css_selector('input[placeholder="Password"]')
password.send_keys("secret_sauce")
login_btn = driver.find_element_by_css_selector(".submit-button.btn_action")
login_btn.click()
# Add 3 items
backpack = driver.find_element_by_id("add-to-cart-sauce-labs-backpack")
backpack.click()
bike_light = driver.find_element_by_id("add-to-cart-sauce-labs-bike-light")
bike_light.click()
fleece_jacket = driver.find_element_by_id("add-to-cart-sauce-labs-fleece-jacket")
fleece_jacket.click()
# Go to cart
cart = driver.find_element_by_class_name("shopping_cart_link")
cart.click()
# Check items in cart
items_count = driver.find_elements_by_class_name("cart_item")
if len(items_count) == 3:
    print("В корзине 3 товара")
else:
    print("Ошибка. Количество товаров в корзине: " + str(len(items_count)))
# Exit
driver.quit()
