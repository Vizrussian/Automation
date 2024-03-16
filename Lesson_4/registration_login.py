# В этом файле 2 задачи
# Задача №1. Тренировка всех навыков

# Сценарий: откройте https://practice.automationtesting.in/ ->
# Нажмите на вкладку "My Account" ->
# В разделе "Register", введите email для регистрации ->
# В разделе "Register", введите пароль для регистрации (почту и пароль сохраните, потребуюутся в дальнейшем) ->
# Нажмите на кнопку "Register"

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in")

# My account
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
# Email
email = driver.find_element_by_id('reg_email')
email.send_keys('potato@swety.com')
# Password
password = driver.find_element_by_id('reg_password')
password.send_keys('IloveNIPPON-69')
time.sleep(3)
# Register
register_btn = driver.find_element_by_name("register")
register_btn.click()
# Exit
driver.quit()

# Задача №2. Тренировка всех навыков

# Сценарий: откройте https://practice.automationtesting.in/ ->
# Нажмите на вкладку "My Account" ->
# В разделе "Login", введите email для логина ->
# В разделе "Login", введите пароль для логина ->
# Нажмите на кнопку "Login" ->
# Добавьте проверку, что на странице есть элемент "Logout"

from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in")

# My account
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
# Email
email = driver.find_element_by_id('username')
email.send_keys('potato@swety.com')
# Password
password = driver.find_element_by_id('password')
password.send_keys('IloveNIPPON-69')
# Register
register_btn = driver.find_element_by_name('login')
register_btn.click()
# Check "Sign Out"
assert driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link--customer-logout > a')
# Exit
driver.quit()
