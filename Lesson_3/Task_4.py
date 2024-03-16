# Задача №4. Тренировка явных ожиданий
# Здесь я экспериментировал и не присваивал переменным значения локаторов, а обращался напрямую

# Сценарий: откройте страницу: http://demo.automationtesting.in/WebTable.html ->
# Перейдите в раздел "More" -> "Loader" ->
# Реализуйте явное ожидание(EC) для отображения текста "Run" ->
# Нажмите кнопку "Run" ->
# Реализуйте явное ожидание(EC) что слово "Lorem" содержится в тексте модального окна ->
# Реализуйте явное ожидание(EC) для нажатия в модальном окне на кнопку "Save Changes" и нажмите на неё

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
# Get to our site
driver.get("http://demo.automationtesting.in/WebTable.html")
# More -> Loader
driver.find_element_by_link_text('More').click()
driver.find_element_by_link_text('Loader').click()
# Find run
run_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.panel-default>.panel-body>button')))
# Click run
driver.find_element_by_css_selector('.panel-body > #loader').click()
# Find Lorem
lorem_element = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.modal-body>p'),'Lorem'))
# Save changes
element_check = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,'.modal-footer>.btn-primary')))
driver.find_element_by_css_selector('.modal-footer>.btn-primary').click()
# Exit
driver.quit()

