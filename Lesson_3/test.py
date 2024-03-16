import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
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
create_task = driver.find_element_by_css_selector('.fas.fa-plus.fa-sm')
create_task.click()
time.sleep(5)
name_label = driver.find_element_by_xpath('//input[@data-name="name"]')
name_label.send_keys('Test')
# Check status
status_crt = driver.find_element_by_css_selector(".col-sm-6:nth-child(1) select")
status_crt1 = driver.find_element_by_css_selector('[data-name="status"] .selectize-control>.selectize-input')
status_crt1.click()
status_crt2 = driver.find_element_by_css_selector('[data-name="status"] .selectize-dropdown-content')
yu = driver.find_element_by_css_selector('.selectize-dropdown-content div:nth-child(3)')
yu.click()
yy3 = status_crt.get_attribute('value')
print(yy3)
sta2 = status_crt1.get_attribute('value')
if sta2 == 'Not Started':
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
f_t = driver.find_element_by_css_selector(".list-row:nth-child(1) .form-checkbox")
f_t.click()
time.sleep(3)
# Action
action_btn = driver.find_element_by_css_selector('.btn-group.actions>[type="button"]')
action_btn.click()
# Remove task
rm = driver.find_element_by_link_text('Remove')
rm.click()
time.sleep(3)
conf = driver.find_element_by_css_selector('.btn-group > [data-name="confirm"]')
conf.click()
# Exit
time.sleep(5)
driver.quit()