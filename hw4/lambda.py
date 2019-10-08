"""Task2. Написать lambda функцию, которая принимает на вход дикт и название файла, форматирует его в json и записывает в файл.
Для преобразования dict -> json изучите модуль json из стандартной библиотеки python.
Пример вызова:
json_writer({'key': 'value'}, 'example.json')
Дикт {'key': 'value'} должен быть записан в файл example.json"""

from json import dump
(lambda dict1, file: dump(dict1, open(file, 'w')))({'dic1t': 1, 'dictionary': 8}, "text.json")

# json_writer = lambda dict, file: dump(dict, open(file, 'w'))
# json_writer({'dict': 1, 'dictionary': 7}, "text.json")

# print((lambda x,y:x+y)(3,2))

# Note that dump and load convert between files and objects, while dumps and loads convert between strings and objects