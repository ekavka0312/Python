#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

numb =  input('Введите число: ')
len_str = len(numb)
i=1
max = int(numb[0])
while i<len(numb):
    if max< int(numb[i]):
        max = int(numb[i])
    i = i+1
print('Самая большая цифра в числе:', max)
