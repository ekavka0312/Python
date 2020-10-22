#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

numb = input('Введите число: ')
n = int(numb)
nn = int(numb+numb)
nnn = int(numb+numb+numb)
print('Сумма чисел n + nn + nnn: ', n+nn+nnn)
