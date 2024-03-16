# Задача №3. Тренировка модальные окна (здесь мы не проходили ожидания, поэтому используем time.sleep)
# Здесь я экспериментировал и не присваивал переменным значения локаторов, а обращался напрямую

# Сценарий: переходим на сайт-> переходим "SwitchTo" - > "Alerts" ->
# Нажимаем на кнопку "click the button to display an alert box:" ->
# Выводим в консоль содержимое окна alert и нажимаем "OK" (
#   дополнительно: добавим тест, что содержимое равно тексту "I am an alert box!" , а если не равно,
#   тогда в консоли выводим сообщение об ошибке) ->
# Получаем адрес текущей ссылки ->
# Открываем новую вкладку в браузере, вводим ссылку из предыдущего шага и переходим по ней ->
# Нажимаем на "Alert with OK & Cancel" -> "click the button to display a confirm box" ->
# В модальном окне нажимаем "Отмена" - >
# Открываем новую вкладку в браузере, вводим ссылку полученную в предыдущих шагах и переходим по ней ->
# Нажимаем на "Alert with Textbox"-> "click the button to demonstrate the prompt box" ->
# В модальном окне, вводим текст: "Ура! Задание выполнено!" и нажимаем "OK"

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
# Get to our site
driver.get("https://demo.automationtesting.in/WebTable.html")
driver.find_element_by_link_text('SwitchTo').click()
driver.find_element_by_link_text('Alerts').click()
# Click the button
time.sleep(3)
driver.find_element_by_css_selector('.btn.btn-danger').click()
# Alert window
text_btn = driver.switch_to.alert.text
blank = "I am an alert box!"
if text_btn == blank:
    print(text_btn)
else:
    print('Bad luck, bro. Try again')
driver.switch_to.alert.accept()
# New tab
current_page = driver.current_url
time.sleep(3)
driver.execute_script("window.open();")
window_second = driver.window_handles[1]
driver.switch_to.window(window_second)
driver.get(current_page)
# Alert with OK
time.sleep(3)
driver.find_element_by_partial_link_text('Cancel').click()
driver.find_element_by_css_selector('.btn.btn-primary').click()
driver.switch_to.alert.dismiss()
# Third tab
time.sleep(3)
driver.execute_script("window.open();")
window_third = driver.window_handles[2]
driver.switch_to.window(window_third)
driver.get(current_page)
# Alert with textbox
time.sleep(3)
driver.find_element_by_partial_link_text('Textbox').click()
driver.find_element_by_css_selector('.btn.btn-info').click()
driver.switch_to.alert.send_keys('Ура! Задание выполнено!')
driver.switch_to.alert.accept()
# Exit
driver.quit()
