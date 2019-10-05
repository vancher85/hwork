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
#     lst = []
    if isinstance(a, (list, tuple)):
        b = (rec(i) for i in a)
        # j = (i for i in b)
        print(list(b))
        return b
    if isinstance(a, dict):
        b = (rec(i) for i in a.items())
        print(list(b))
        return b
    return a
rec(a)
print(rec(a))
# print(list(rec(a)))



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

