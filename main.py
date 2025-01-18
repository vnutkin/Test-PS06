# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
import re
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


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
print(len(lamps))
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
      prices = lamp.find_element(By.CSS_SELECTOR, 'div.pY3d2')
      price = prices.find_element(By.CSS_SELECTOR, "[data-testid='price']").text
# Находим ссылку с помощью атрибута 'href'
      what = 'l'
      link = lamp.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')
      match = re.search(r'([\d\s]+(?:\.[\d]+)?)', price)

      if match:
           # Извлекаем найденное число и преобразуем его в число с плавающей запятой
        float_price = float(match.group(1).replace(' ', ''))
      else:
        float_price = "Цена не найдена"
# Вставляем блок except на случай ошибки - в случае ошибки программа попытается продолжать
   except Exception as e:
       print("произошла ошибка при парсинге",what,e)
       continue

# Вносим найденную информацию в список
   parsed_data.append([title, price,float_price, link])

# Закрываем подключение браузер
driver.quit()
#print(parsed_data)
with open("svet.csv", 'w',newline='', encoding='utf-8') as file:
    # Используем модуль csv и настраиваем запись данных в виде таблицы
    # Создаём объект
    writer = csv.writer(file)
    # Создаём первый ряд
    writer.writerow(['Наименование товара', 'цена строкой','цена числом', 'ссылка на товар'])
    # Прописываем использование списка как источника для 'цена',рядов таблицы
    writer.writerows(parsed_data)