"""3. Еще раз оптимизировать рекурсию. Перевести ее на генераторы списков. Результатом должен вернуться итератор.
a = [
    {
        (1, 2): [
            {'b': 1, 'c': 2},
            'hello world'
        ],
        'b': {'d': 3}
    },
    4,
    5,
    ['hello', 'again']
]
def rec(a):
    result = []
    if isinstance(a, (list, tuple)):
        for i in a:
            result.extend(rec(i))
        return result
    if isinstance(a, dict):
        for i, j in a.items():
            result.extend(rec(i))
            result.extend(rec(j))
        return result
    return [a]
Пример вызова:
print(rec(a))
<generator object rec.<locals>.<genexpr> at 0x7ff5156b7570>
print(list(rec(a)))
[1, 2, 'b', 1, 'c', 2, 'hello world', 'b', 'd', 3, 4, 5, 'hello', 'again']"""

# a = [
#     5,
#     ['hello', 'again']
# ]
# def rec(a):
#     # lst = []
#     if isinstance(a, (list)):
#         b = (rec(i) for i in a)
#         return b
#     return a
# print(rec(a))
# print(list(rec(a)))





# [11:05 AM] Roman Romanyuk
# первое
#
# [11:06 AM] Roman Romanyuk
# твоя рекурсия в разных случаях возвращает тебе разные типы объектов
#
# [11:06 AM] Roman Romanyuk
# в одном - это итератор
#
# [11:06 AM] Roman Romanyuk
# во втором просто значение аттрибута
#
# [11:06 AM] Roman Romanyuk
# return a - вот эта строка
#
# [11:06 AM] Roman Romanyuk
# от этого поведения надо избавиться
#
# [11:06 AM] Roman Romanyuk
# иначе придется пихать ифы в итераторы
#
# [11:06 AM] Roman Romanyuk
# сложыне ифы
#
# [11:06 AM] Roman Romanyuk
# return [a]
#
# [11:06 AM] Roman Romanyuk
# все исправит
#
#
#
# [11:06 AM] Roman Romanyuk
# второе
#
# [11:07 AM] Roman Romanyuk
# итераторт теперь при распаковке тебе всегда возвращает список списков
#
# [11:07 AM] Roman Romanyuk
# а это значит что его надо еще раз распаковать внутри
#
# [11:07 AM] Roman Romanyuk
# b = (j for i in a for j in rec(i))
# Edited
#
# [11:08 AM] Roman Romanyuk
# теперь осталось доделать случай с диктами
#
# [11:08 AM] Roman Romanyuk
# там еще чуть глубже распаковка
#
# [11:08 AM] Roman Romanyuk
# на один уровень
#
# [11:12 AM] Roman Romanyuk
# и вся проблема еще в том, что ['b', [['d', 3 - вот тут у тебя есть значение не список
#
# [11:12 AM] Roman Romanyuk
# 'b' - это тебе все портит
#
# [11:12 AM] Roman Romanyuk
# нзчт



# a = [
#     {
#         (1, 2): [
#             {'b': 1, 'c': 2},
#             'hello world'
#         ],
#         'b': {'d': 3}
#     },
#     4,
#     5,
#     ['hello', 'again']
# ]
# def rec(a):
#     # lst = []
#     if isinstance(a, (list, tuple)):
#         b = [rec(i) for i in a]
#         return b
#     if isinstance(a, dict):
#         b = [rec(i) for i in a.items()]
#         return b
#     return a
# rec(a)
# print(rec(a))
# # print(list(rec(a)))



# def rec(a):
#     # lst = []
#     if isinstance(a, (list, tuple)):
#         for i in a:
#             b = (rec(i) for i in a)
#             # print(b)
#             # print(list(b))
#         return b
#     if isinstance(a, dict):
#         for i in a.items():
#             b = (rec(i) for i in a.items())
#             print(b)
#             print(list(b))
#         return b
#     return a
# print(rec(a))
# print(list(rec(a)))
# # print(list(rec(a)))




# def rec(a):
#     # lst = []
#     if isinstance(a, (list, tuple)):
#         b = (rec(i) for i in a)
#         print(b)
#         print(list(b))
#         return b
#     if isinstance(a, dict):
#         b = (rec(i) for i in a.items())
#         print(b)
#         print(list(b))
#         return b
#     return a
# print(rec(a))
# print(list(rec(a)))





# a = [
#     {
#         (1, 2): [
#             {'b': 1, 'c': 2},
#             'hello world'
#         ],
#         'b': {'d': 3}
#     },
#     4,
#     5,
#     ['hello', 'again']
# ]
# def rec(a):
#     # lst = []
#     if isinstance(a, (list, tuple)):
#         for i in a:
#             b = (i for i in rec(i))
#         return b
#         # return lst
#     if isinstance(a, dict):
#         for i in a.items():
#             b = [i for i in rec(i)]
#         return b
#     return [a]
# print(rec(a))
# print(list(rec(a)))
# # print(list(rec(a)))




# a = [
#     {
#         (1, 2): [
#             {'b': 1, 'c': 2},
#             'hello world'
#         ],
#         'b': {'d': 3}
#     },
#     4,
#     5,
#     ['hello', 'again']
# ]
# def rec(a):
#     lst = []
#     if isinstance(a, (list, tuple)):
#         b = (rec(i) for i in a)
#         print(b)
#         return b
#     if isinstance(a, dict):
#         b = (rec(i) for i in a.items())
#         return b
#     else:
#         lst.append(a)
#         return lst
# print(rec(a))
# print(list(rec(a)))

