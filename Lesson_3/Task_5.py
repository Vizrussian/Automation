# Задача №5 Тренировка неявных ожиданий и метода assert
#
# Сценарий: откройте страницу: http://demo.automationtesting.in/WebTable.html ->
# Реализуйте неявное ожидание поиска элементов ->
# Перейдите в раздел "More" -> "Dynamic Data" (
#   здесь и в дальнейших заданиях используйте клики(их будет 2) вместо выбора по селектору) ->
# Добавьте проверку, что заголовок окна равен "Loading the data Dynamically" ->
# Нажмите на кнопку "Get Dynamic Data" ->
# Выведите в консоли адрес ссылки, которая сгенерируется в теге img (похожий на: https://randomuser.me/api/portraits/...)

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()
# Get to our site
driver.get("http://demo.automationtesting.in/WebTable.html")
# More -> Dynamic Data
more_btn = driver.find_element_by_link_text('More')
more_btn.click()
data_btn = driver.find_element_by_partial_link_text('Data')
data_btn.click()
# Assert
our_head = driver.find_element_by_css_selector('.cont_box_center>h3').text
assert our_head == 'Loading the data Dynamically'
# Get dynamic data
dynamic_data = driver.find_element_by_css_selector('.panel-body #save')
dynamic_data.click()
time.sleep(3)
# Get attribute
link = driver.find_element_by_css_selector('#loading> img')
link_value = link.get_attribute('src')
print(link_value)
# Exit
driver.quit()
