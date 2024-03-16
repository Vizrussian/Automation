# Задача №7. Тренировка всех навыков

# Сценарий: откройте страницу: http://demo.automationtesting.in/WebTable.html ->
# Реализуйте неявное ожидание поиска элементов ->
# Перейдите в раздел "More" -> "JQuery ProgressBar" ->
# Реализуйте явное ожидание(EC) для проверки, что кнопка "Close" невидима (
#   для этого, предварительно вручную нажмите на кпоку "Start Download" и в появившемся окне возьмите селектор кнопки "Close") ->
# Нажмите кнопку "Start Download" ->
# Реализуйте явное ожидание(EC) для проверки, что кнопка называется "Cancel Download" ->
# Закройте окно -> снова откройте ->
# Реализуйте явное ожидание(EC) для проверки, что в окне присутствует текст "Complete!"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()
# Get to our site
driver.get("http://demo.automationtesting.in/WebTable.html")
# More -> JQ
more_btn = driver.find_element_by_link_text('More')
more_btn.click()
jq_btn = driver.find_element_by_partial_link_text('Bar')
jq_btn.click()
# Close
close_btn = WebDriverWait(driver, 10).until(
    EC.invisibility_of_element_located((By.CLASS_NAME, 'ui-dialog-buttonset')))
# Start download
start = driver.find_element_by_css_selector('.col-xs-4>#downloadButton')
start.click()
# Cancel download
cancel_btn = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.ui-dialog-buttonset>button'), 'Cancel Download'))
cancel = driver.find_element_by_css_selector('.ui-dialog-buttonset>button')
cancel.click()
# Completed
completed = driver.find_element_by_css_selector('.col-xs-4>#downloadButton')
completed.click()
completed_btn = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#dialog>.progress-label'), 'Complete!'))
# Exit
driver.quit()
