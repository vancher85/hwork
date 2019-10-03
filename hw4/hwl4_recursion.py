# def rec(a):
#     print(a)
#     return rec
#
# rec('hello')('world')

##############
# recursion shows all type of elements
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
#
# def rec(a):
#     if isinstance(a, list):
#         print('a: list')
#         for i in a:
#             rec(i)
#     elif isinstance(a, dict):
#         print('a: dict')
#         for i, j in a.items():
#             rec(i)
#             rec(j)
#     # elif isinstance(a, str):
#     #     print('a: str')
#     else:
#         print('a:{}'.format(type(a)))
# rec(a)


###########
# rec() with lst in arg

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
#
# def rec(a, lst=None):
#     if lst is None:
#         lst = []
#     if isinstance(a, (list, tuple)):
#         # print('a: list')
#         for i in a:
#             rec(i, lst)
#     elif isinstance(a, dict):
#         # print('a: dict')
#         for i, j in a.items():
#             rec(i, lst)
#             rec(j, lst)
#     # elif isinstance(a, str):
#     #     print('a: str')
#     else:
#         # print('a:{}'.format(type(a)))
#         lst.append(a)
#     return lst
# print(rec(a))



##################################
# optimization - rec() without lst in arg
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
#
# lst = []
# def add(b):
#     lst.append(b)
#     return
#
# def rec(a):
#     if isinstance(a, (list, tuple)):
#         for i in a:
#             rec(i)
#     elif isinstance(a, dict):
#         for i, j in a.items():
#             rec(i)
#             rec(j)
#     elif isinstance(a, str):
#         add(a)
#     else:
#         add(a)
# rec(a)
# print(lst)
# print(lst)
