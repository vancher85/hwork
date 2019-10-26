# class Human(object):
#     count = 0
#     hands = 2
#     legs = 2
#     head = 1
#
#     @classmethod
#     def counter(cls):
#         cls.count += 1
#
#     def __init__(self, name): # конструктор - метод объекта со ссылкой на текущий объект
#         self.name = name
#         # print('I\'m init')
#         # print(self.name)
#         self.counter()
#
#     def run(self):
#         print('{} is running'.format(self.name))
#
# oleg = Human('Oleg')
# dima = Human('dima')
# dima.legs = 3
# alis = Human('alis')
# Human.legs = 4
#
# print(Human.count)

# for i in oleg, dima, alis:
#     print(i.run())
#     print(Human.run(i))