# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.

# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10


list = [10, 5, 7, 3, 3, 0, 5, 7, 3, 8]

number = int (input('Введите число Х: '))
near_number = list [0]
defination = abs(list [0] - number)
for i in range (len (list)):
    if abs(list [i] - number) < defination:
        near_number = list[i]
        defination = abs(number - list [i])
        

print (near_number)

