# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Инициализируем браузер
#driver = webdriver.Firefox()
# Если мы используем Chrome, пишем
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/sankt-peterburg/category/svet"

# Открываем веб-страницу
driver.get(url)

# Задаём 3 секунды ожидания, чтобы веб-страница успела прогрузиться
time.sleep(3)
lamps = driver.find_elements(By.CLASS_NAME, 'WdR1o')

# Выводим светильники на экран
#print(lamps)
parsed_data = []

# Перебираем коллекцию вакансий
# Используем конструкцию try-except, чтобы "ловить" ошибки, как только они появляются
for lamp in lamps:
   try:
# Находим элементы внутри светильника по значению
# Находим названия светильника
      what = 't'
      title = lamp.find_element(By.CSS_SELECTOR, 'img.c9h0M').get_attribute('alt')
# Находим цену
      what = 'p'
      price = lamp.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
# Находим ссылку с помощью атрибута 'href'
      what = 'l'
      link = ''#lamp.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
# Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except Exception as e:
       print("произошла ошибка при парсинге",what,e)
       continue

# Вносим найденную информацию в список
   parsed_data.append([title, price, link])

# Закрываем подключение браузер
driver.quit()
print(parsed_data)