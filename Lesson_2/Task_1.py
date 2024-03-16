# Задача №1 (здесь мы не проходили ожидания, поэтому используем time.sleep)
# Откройте страницу https://opensource-demo.orangehrmlive.com/ и напишите тест для логина в систему.

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
# Get to our site
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
# Enter login and password
login = driver.find_element_by_css_selector('input[name="username"]')
login.send_keys("Admin")
password = driver.find_element_by_css_selector('input[placeholder="Password"]')
password.send_keys("admin123")
# Click login
login_btn = driver.find_element_by_class_name('oxd-button')
login_btn.click()
# Exit
driver.quit()
