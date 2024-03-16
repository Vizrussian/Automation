# Задача №8. Тренировка всех навыков

# Сценарий: откройте страницу: https://demo.automationtesting.in/WebTable.html ->
# Реализуйте неявное ожидание поиска элементов ->
# Перейдите в раздел "Switch to" -> "Windows" ->
# В разделе "Open New Tabbed Windows" нажмите кнопку "click" ->
# Переключите драйвер на вторую вкладку - > закройте её -> переключитесь обратно на первую вкладку(
#   чтобы закрыть вкладку: после переключения на неё на новой строке добавьте команду driver.close) ->
# Перейдите в раздел "Separate Multiple Windows" и нажмите "click" ->
# Переключите драйвер на вторую вкладку # здесь нужно будет использовать handles[2],
#   тк ранее закрытая вкладка с шага 4 останется в памяти ->
# Используя явное ожидание(EC), проверьте что ссылка = "https://demo.automationtesting.in/Index.html" ->
# Используя явное ожидание(EC), проверьте что в браузере открыто 3 вкладки ->
# В поле "email" напишите любую почту и нажмите на кнопку в виде ">" справа от поля ->
# Используя явное ожидание(EC), проверьте что ссылка = "https://demo.automationtesting.in/Register.html"
#   дополнительно: для всех EC, вынесите часть проверки в переменную

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()
# Get to our site
driver.get("http://demo.automationtesting.in/WebTable.html")
# Switch to -> Windows
switch_to = driver.find_element_by_link_text('SwitchTo')
switch_to.click()
window = driver.find_element_by_link_text('Windows')
window.click()
# Click
click_button = driver.find_element_by_css_selector('#Tabbed button')
click_button.click()
# Close second tab
second_tab = driver.window_handles[1]
driver.switch_to.window(second_tab)
driver.close()
# Separate
first_tab = driver.window_handles[0]
driver.switch_to.window(first_tab)
separate = driver.find_element_by_partial_link_text('Multiple')
separate.click()
multiple = driver.find_element_by_css_selector('#Multiple button')
multiple.click()
# Third tab
third_tab = driver.window_handles[2]
driver.switch_to.window(third_tab)
emp_wait = WebDriverWait(driver, 10)
link_check = emp_wait.until(
    EC.url_to_be("https://demo.automationtesting.in/Index.html"))
# Check tabs
number_of_tabs = emp_wait.until(
    EC.number_of_windows_to_be(3))
# Email
email = driver.find_element_by_id('email')
email.send_keys('Idontknow@gmail.com')
arrow = driver.find_element_by_id('enterimg')
arrow.click()
# Check link
link_check1 = emp_wait.until(
    EC.url_to_be("https://demo.automationtesting.in/Register.html"))
# Exit
driver.quit()
