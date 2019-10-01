"""Task3. Тертий модуль: Используя библиотеку urllib, написать функцию, которая принимает на вход урл,
и на выходе выводит количество картинок на странице"""
from urllib import request
count = 0
def pageparser(url):
    url = request.urlopen(url)
    # print(url.read())
    # print(url.read())
    count = str(url.read()).count("<img")
    print(count)
# pageparser("http://onliner.by")

#Q2: почему если обращаешься 2 раза к url.read(), второй раз возвращается пустая строка?
