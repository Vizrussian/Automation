# Задача №1. Тренировка select и check box (здесь мы не проходили ожидания, поэтому используем time.sleep)

# Сценарий: переходим на сайт->
# Выбираем английский язык ->
# Нажатие на кнопку "Tasks" ->
# Открываем фильтр ->
# Выбираем "Only My" ->
# Выбираем все задачи ->
# Нажимаем кнопку "Action" ->
# Выбираем "Mass Update" ->
# Проверяем что "Update" недоступна для выбора ->
# Закрываем окно ->
# Нажимаем "Create Task" ->
# Проверяем значение в селекторе по умолчанию ->
# Вводим значение "Test" в имя задачи ->
# Нажимаем "Save" ->
# Нажимаем "Tasks" ->
# Выбираем первую задачу ->
# Нажимаем кнопку "Action" ->
# Выбираем "Remove" ->
# Подтверждаем

import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
# Get to our site
driver.get("https://demo.us.espocrm.com")
time.sleep(3)
# Select language
element = driver.find_element_by_id("field-language")
select = Select(element)
select.select_by_value("en_US")
login_btn = driver.find_element_by_css_selector('.btn-s-wide')
login_btn.click()
time.sleep(3)
# Click tasks
task_btn = driver.find_element_by_link_text('Tasks')
task_btn.click()
time.sleep(3)
# Open filter
filter_label = driver.find_element_by_css_selector('.filters-label')
filter_label.click()
# Check box
only_my = driver.find_element_by_css_selector("li.checkbox:nth-child(11)")
only_my.click()
time.sleep(3)
# Select all tasks
select_all = driver.find_element_by_css_selector('.select-all')
select_all.click()
time.sleep(3)
# Action -> mass update
action_btn = driver.find_element_by_css_selector('.btn-group.actions>[type="button"]')
action_btn.click()
mass_update = driver.find_element_by_link_text('Mass Update')
mass_update.click()
time.sleep(3)
# Check update button
upd_disable = driver.find_element_by_css_selector('[data-name="update"]')
ed = upd_disable.get_attribute('disabled')
if ed is not None:
    print('Update is disabled')
else:
    print('Update is not disabled')
close = driver.find_element_by_css_selector('[aria-hidden="true"]')
close.click()
time.sleep(3)
# Create task
create_task = driver.find_element_by_css_selector('.fas.fa-plus.fa-sm')
create_task.click()
time.sleep(5)
name_label = driver.find_element_by_xpath('//input[@data-name="name"]')
name_label.send_keys('Test')
# Check status
status_task = driver.find_element_by_css_selector(".col-sm-6:nth-child(1) select")
task_value = status_task.get_attribute('value')
if task_value == 'Not Started':
    print('All right')
else:
    print('Error')
# Save
save_btn = driver.find_element_by_css_selector(".btn-xs-wide:nth-child(1)")
save_btn.click()
time.sleep(3)
# Tasks
tasks = driver.find_element_by_link_text('Tasks')
tasks.click()
time.sleep(3)
# Select first task
first_task = driver.find_element_by_css_selector(".list-row:nth-child(1) .form-checkbox")
first_task.click()
time.sleep(3)
# Action
action_btn = driver.find_element_by_css_selector('.btn-group.actions>[type="button"]')
action_btn.click()
# Remove task
remove_btn = driver.find_element_by_link_text('Remove')
remove_btn.click()
time.sleep(3)
# Confirm
confirm_btn = driver.find_element_by_css_selector('.btn-group > [data-name="confirm"]')
confirm_btn.click()
# Exit
time.sleep(5)
driver.quit()
