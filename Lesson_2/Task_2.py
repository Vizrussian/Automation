# Задача №2 (здесь мы не проходили ожидания, поэтому используем time.sleep)
# Сценарий: логин в систему - > переход в пункт меню PIM(находится слева) ->
# переход на вкладку Add Employee(находится по центру наверху) - >
# заполнение полей First, Last Name, Employee Id - >
# нажатие на кнопку Save(после чего происходит автоматический переход в профиль – это финальный результат).

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
# Add employee
add_button = driver.find_element_by_css_selector('.orangehrm-header-container>[type="button"]')
add_button.click()
time.sleep(3)
# Enter data and save
first_name = driver.find_element_by_name('firstName')
first_name.send_keys('Lelys')
last_name = driver.find_element_by_name('lastName')
last_name.send_keys('Afanasyevich')
id_name = driver.find_element_by_css_selector(".oxd-grid-2 .oxd-input")
id_name.send_keys('LA')
save_button = driver.find_element_by_css_selector('button[type=submit]')
save_button.click()
# Exit
driver.quit()
