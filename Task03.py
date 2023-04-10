# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы и заранее известно какой алфавит надо использовать.

# Примеры/Тесты:
# Input:   ноутбук
# Output:  12

# Input:   notebook
# Output:  14

# (*) Примечание.
# Подумайте о том какие структуры данных здесь наиболее удобно использовать, чтобы просто проверять в какую группу попадает буква, а также просто накапливать сумму очков.



Eng_dict = 'qwertyuiopasdfghjklzxcvbnm'

Rus_Dict = 'йцукенгшщзхъфывапролджэячсмитьбюё'

Points_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
                4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
Points_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
                4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФШЪ'}

word = input('Введите слово на русском или английском языке: ')

if word[0].lower() in Eng_dict:
    summa = 0
    for letter in word:
        for key, value in Points_English.items():
            if letter.upper() in value:
                summa += key
    print(f'Стоимость введенного слова = {summa}')
else:
    if word[0].lower() in Rus_Dict:
        summa = 0
        for letter in word:

            for key, value in Points_Russian.items():
                if letter.upper() in value:
                    summa += key
    print(f'Стоимость введенного слова = {summa}')


# points = {1:'АВЕИНОРСТAEIOULNSTR',
#       	2:'ДКЛМПУDG',
#       	3:'БГЁЬЯBCMP',
#       	4:'ЙЫFHVWY',
#       	5:'ЖЗХЦЧK',
#       	8:'ШЭЮJZ',
#       	10:'ШЭЮQZ'}
# word = input().upper()

# summa = 0
# for letter in word:
#     for key, value in points.items():
#             if letter.upper() in value:
#                 summa += key
# print(summa)
