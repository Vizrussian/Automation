# Задача №1. Тренировка всех навыков

# Сценарий: откройте https://practice.automationtesting.in/ ->
# Проскролльте страницу вниз на 600 пикселей ->
# Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE" ->
# Нажмите на вкладку "REVIEWS" ->
# Поставьте 5 звёзд ->
# Заполните поле "Review" сообщением: "Nice book!" ->
# Заполните поле "Name" ->
# Заполните "Email" ->
# Нажмите на кнопку "SUBMIT"

from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.maximize_window()
driver.get("https://practice.automationtesting.in")

# Scroll page 600px
driver.execute_script('window.scrollBy(0,600);')
# Click book
selenium_book = driver.find_element_by_partial_link_text('Selenium')
selenium_book.click()
# Click reviews
reviews_btn = driver.find_element_by_css_selector('.reviews_tab>a')
reviews_btn.click()
# Click 5 star
five_star = driver.find_element_by_css_selector('.stars .star-5')
five_star.click()
# Add comment
add_comment = driver.find_element_by_id('comment')
add_comment.send_keys('Nice book!')
# Name
name = driver.find_element_by_id('author')
name.send_keys('Potato')
# Email
email = driver.find_element_by_id('email')
email.send_keys('papato@swety.com')
# Submit
submit_btn = driver.find_element_by_css_selector('#submit.submit')
submit_btn.click()
# Exit
driver.quit()
