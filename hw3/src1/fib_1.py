"""Task1. Написать в первом модуле функцию по расчету ряда фибоначчи. На вход принимает число n.
На выходе выдает ряд фибоначчи длинной n"""
# n = int(input())
def func(n):
    list = []
    for i in range(n):
        if i < 2:
            list.append(i)
        else:
            list.append(list[i-1]+list[i-2])
    print(list)
# func(int(input()))