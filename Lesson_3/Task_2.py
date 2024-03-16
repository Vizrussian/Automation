# Задача №2. Тренировка upload, script

# Сценарий: переходим на сайт->
# Заполняем обязательные поля для регистрации(а так же поля: Date of Birth, Password, Confirm Password) ->
# Загружаем любой файл в раздел "Photo" ->
# Проскроллить страницу вниз на 300 пикселей ->
# Нажимаем на кнопку "Submit" ->
# Добавляем проверку, что произошёл переход на страницу: "http://demo.automationtesting.in/WebTable.html"

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
# Get to our site
driver.get("https://demo.automationtesting.in/Register.html")
# Enter first and last name
first_name = driver.find_element_by_css_selector('[placeholder="First Name"]')
first_name.send_keys('Patoka')
last_name = driver.find_element_by_css_selector('[placeholder="Last Name"]')
last_name.send_keys('Two')
# Enter email and phone number
email_name = driver.find_element_by_css_selector('[type="email"]')
email_name.send_keys('Patoka@gmail.com')
phone_number = driver.find_element_by_css_selector('[type="tel"]')
phone_number.send_keys('8005553535')
# Select our gender
gender = driver.find_element_by_css_selector('[value="Male"]')
gender.click()
# Select birthday
year = driver.find_element_by_id('yearbox')
year_selector = Select(year)
year_selector.select_by_value('1977')
month = driver.find_element_by_css_selector('[placeholder="Month"]')
month_selector = Select(month)
month_selector.select_by_value('August')
day = driver.find_element_by_id('daybox')
day_selector = Select(day)
day_selector.select_by_value('30')
# Enter password
pass_word = driver.find_element_by_id('firstpassword')
pass_word.send_keys('Aokigahara6')
sec_ond = driver.find_element_by_id('secondpassword')
sec_ond.send_keys('Aokigahara6')
# Set picture
selfie = ('C:\w.png')
set_photo = driver.find_element_by_id('imagesrc')
set_photo.send_keys(selfie)
# Scroll 300px
driver.execute_script("window.scrollBy(0, 300);")
# Submit
submit_btn = driver.find_element_by_id('submitbtn')
submit_btn.click()
# Current URL
our_page = driver.current_url
future_page = ('http://demo.automationtesting.in/WebTable.html')
if our_page == future_page:
    print('All clear!')
else:
    print('We are here -->', our_page)
    print('But we must be here -->', future_page)
# Exit
driver.quit()
