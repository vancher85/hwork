# # good example to practice MOR
class Parent1:
    def __init__(self):
        self.a = None
    def meth1(self):
        print('a')
        return self.a


class Parent2:
    def __init__(self):
        self.b = None

    def meth2(self):
        print('b')
        return self.b

class Child(Parent1,Parent2):
    def __init__(self):
        super(Child, self).__init__()
        # Parent2.__init__(self)

c = Child()
c.a = '2'
# c.b = 'c'
print(c.meth1())
# print(c.meth2())


# class Bird:
#     def __init__(self):
#         self.name1 = 'bird'
#     def bird_name(self):
#         print('I\'m method1')
#         return self.name1
#
# class Animals:
#     def __init__(self):
#         self.name2 = 'animal'
#     def animal_name(self):
#         print('I\'m method2')
#         return self.name2
#
# class Pet(Bird, Animals):
#     def __init__(self, pet_type=None):
#         self.pet_type = pet_type
#         super(Pet, self).__init__()
#         Animals.__init__(self)
#     def pet_voice(self):
#         if self.pet_type == "dog":
#             print(c.name2, "wow!")
#         else:
#             print(c.name1, "4ik 4rik!")
#             print(c.bird_name())
# c = Pet(pet_type='bird')
# c.pet_voice()
# # print(c.bird_name())

# a = Animals()
# print(a.animal_name())
# print(Pet.__mro__)
# print(c.name1)
# print(c.name2)
# print(c.bird_name())
# print(c.animal_name())

print((838873204 << 32) + 0)
#
print(( pow(2, 23) * 101 ) + 12430)
