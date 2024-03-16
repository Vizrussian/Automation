# Задача №6. Тренировка всех навыков
#
# Сценарий: откройте страницу: http://demo.automationtesting.in/WebTable.html ->
# Реализуйте неявное ожидание поиска элементов ->
# Перейдите в раздел "More" -> "File Upload" ->
# Загрузите файл с картинкой ->
# Нажмите на кнопку "Remove" ->
# Загрузите пустой файл с расширением .txt (можно создать в блокноте) ->
# Закройте появившееся красное сообщение об ошибке (
#   дополнительно: добавьте проверку что кнопка upload недоступна для нажатия)

from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:/chromedriver')
driver.implicitly_wait(5)
driver.maximize_window()
# Get to our site
driver.get("http://demo.automationtesting.in/WebTable.html")
# More -> File upload
more_btn = driver.find_element_by_link_text('More')
more_btn.click()
file_upload = driver.find_element_by_partial_link_text('Upload')
file_upload.click()
# Upload .jpg
our_png = 'C:\w.png'
upload = driver.find_element_by_css_selector('[type="file"]')
upload.send_keys(our_png)
# Remove
remove = driver.find_element_by_css_selector('.fileinput-remove>span')
remove.click()
# Upload .txt
our_txt = 'C:\y.txt'
upload.send_keys(our_txt)
# Close error
error = driver.find_element_by_class_name('kv-error-close')
error.click()
# Check Upload button
check_upload = driver.find_element_by_css_selector('.fileinput-upload.fileinput-upload-button')
check_value = check_upload.get_attribute('disabled')
if check_value is not None:
    print('Upload button is disabled')
else:
    print('Upload button is not disabled')
# Exit
driver.quit()
