#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import time
print(time.ctime()) #Вывод текущей даты

time_usr = int(input('введите время в секундах: '))
print(time.ctime(time_usr)) #перевод с использованием встроенной функции

#Перевод вручную в нужный формат
minutes = time_usr // 60
ss = time_usr % 60
hour = minutes // 60
mm = minutes % 60

print("Время в формате чч:мм:сс", hour, ':', mm, ':', ss)


