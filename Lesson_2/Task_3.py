# Задача №3 (здесь мы не проходили ожидания, поэтому используем time.sleep)
# Предусловие: создан пользователь
# Сценарий: логин в систему- > ввод значения id (получившегося в предыдущем тесте) в поле Employee Id - >
# нажатие на кнопку Search - > нажатие на иконку "Корзина" (справа от найденного пользователя) - >
# нажатие на "Yes, Delete" в диалоговом окне.

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
# Get to our site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
# Login
login = driver.find_element_by_css_selector('input[name="username"]')
login.send_keys("Admin")
password = driver.find_element_by_css_selector('input[placeholder="Password"]')
password.send_keys("admin123")
login_btn = driver.find_element_by_class_name('oxd-button')
login_btn.click()
time.sleep(3)
# Click PIM
pim_button = driver.find_element_by_link_text('PIM')
pim_button.click()
time.sleep(3)
# Search our employee
id_button = driver.find_element_by_css_selector("div:nth-child(2) > input")
id_button.send_keys('0350LA')
search_button = driver.find_element_by_css_selector('button[type="submit"]')
search_button.click()
time.sleep(3)
# Delete employee
trash_btn = driver.find_element_by_css_selector('.oxd-icon.bi-trash')
trash_btn.click()
time.sleep(3)
# Confirm
confirm_button = driver.find_element_by_css_selector('.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin')
confirm_button.click()
# Exit
driver.quit()
