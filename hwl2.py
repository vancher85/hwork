"""# Task 1: nested list.
# Необходимо вывести на экран каждый вложенный элемент списка. for  поддерживает вывод"""
# lst=[[1,2],[3,4],[5,6]]
# for i in lst:
#     for j in i:
#         print(j)

"""# Task 2: new List.
# Необходимо из списка в первом задании собрать новый список без вложенности"""
# lst=[[1,2],[3,4],[5,6]]
# new_list=[]
# for i in lst:
#     for j in i:
#         new_list.append(j)
# print(new_list)

"""# Task 3: Написать функцию(можно и без функции, просто в for),
# которая принимает на вход dict, и если в этом дикте есть ключ 'magic key', то
# выводит на экран значение этого ключа."""
# dct = {'magic key': 'hello world', 'some other key': None}
# for i in dct:
#     if i == "magic key":
#         print(dct.get(i))

"""# Task4: написать функцию(1) с вложенной функцией(2). Функция(1) принимает на вход список, 
# функция(2) не принимает на вход никаких параметров, но добавляет в список переданный в функцию(1) элементе 'injected'"""
# some_list = [1, 2, 3, 4]
# def func1(lst):
#     def func2():
#         lst.append("injected")
#     func2()
# func1(some_list)
# print(some_list)

#Quest: почему ф-ия без return норм работает (python3.7)?