"""1. С помощью итератора(генератор списков, который возвращает итератор (...)) распаковать списки в линейный:
lst = [[[1, 2, 3],[1, 2, 3],[1, 2, 3]], [[1, 2, 3],[1, 2, 3],[1, 2, 3]], [[1, 2, 3],[1, 2, 3],[1, 2, 3]]]
Пример вызова:
unpacked = (....)
print(unpacked)
<generator object rec.<locals>.<genexpr> at 0x7ff5156b7570>
print(list(unpacked))
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]"""

# through iterator
lst = [[[1, 2, 3],[4, 5, 6],[7, 8, 9]],[[10, 11, 12],[13, 14, 15],[16, 17, 18]], [[19, 20, 21],[22, 23, 24],[25, 26, 27]]]
unpacked = (y for i in lst for j in i for y in j)
print(unpacked)
print(list(unpacked))





# through inner list
# unpacked = (x for x in lst)
# for i in unpacked:
#     for j in i:
#         for y in j:
#             print(y)


# разница м/у итерируемым объекто и итератором
# x = [1, 2, 3]
# y = iter(x)
# z = iter(x)
# print(next(y))
# print(next(y))
# print(next(z))
# print(type(x))
# print(type(y))