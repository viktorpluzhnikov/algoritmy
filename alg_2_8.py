# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

user_range = input('Введите последовательность:')
user_number = input('Введите число для поиска:')
count = 0

for i in user_range:
    if i == user_number:
        count += 1


print(f'Число {user_number} встречается {count} раз.')