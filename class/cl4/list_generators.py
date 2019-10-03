# generator
# a = list(range(100))
# b = [i for i in a]
# print(b)

# # #iterator
# a=[1,2,3]
# b = (i for i in a)
# print(next(b))
# print(next(b))
# print(next(b))


from sys import getsizeof
# # #generator
# a = list(range(1000))
# print(getsizeof(a))
#
# b = [i for i in a]
# print(getsizeof(b))
#
# c = [i for i in b if i % 2 == 0]
# print(getsizeof(c))


# # #iterator
# a = range(1000)
# print(getsizeof(a))
# b = (i for i in a)
# print(getsizeof(b))
# c = (i for i in b if i % 2 == 0)
# print(list(c))


# a = list(range(100))
# b = [[1,2,4] for i in a]
# print(b)
# c = [j for i in b for j in i if j % 2 == 0]
# print(c)

# def xor(a,b):
#     if (a or b) and not (a and b):
#         return True
#     return False
#
# lambda_func = (lambda a,b: True if (a or b) and not (a and b) else False)
#
# print(lambda_func(True, False))
# print(lambda_func(False, False))

# xor = (lambda a,b,c: list(zip(a,b,c)))
# print(xor)
