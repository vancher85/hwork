# class Parent1:
#     def __init__(self):
#         self.a = None
#     def meth1(self):
#         print('a')
#         return self.a
#
#
# class Parent2:
#     def __init__(self):
#         self.b = None
#
#     def meth2(self):
#         print('b')
#         return self.b
#
# class Child(Parent1,Parent2):
#     pass
#
# c = Child()
# c.b = 'c'
# print(c.meth1())
# print(c.meth2())


# class Parent1:
#     def __init__(self):
#         self.a = 'a'
#     def meth1(self):
#         print('I\'m method1')
#         return self.a
# class Parent2:
#     def __init__(self):
#         self.b = 'b'
#     def meth2(self):
#         print('I\'m method2')
#         return self.b
# # d = Parent1()
# # print(d.meth1())
#
# class Child(Parent1, Parent2):
#     def __init__(self):
#         self.c = 'c'
#         super(Child, self).__init__()
#         Parent2.__init__(self)
#     def meth1(self):
#         return self.c
#     def meth3(self):
#         result = super(Child, self).meth1()
#         print(result)
#         return result
#     pass
# c = Child()
# print(c.meth2())
