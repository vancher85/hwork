"""Task4. Создать demo_utils.py в котором объединить все предыдущие задания. Написать функцию, которая сперва выводит:
1. Фибоначчи
2. Евклид
3. Счетчик картинок
Ввелите номер Demo функции:
Через input() принимает от пользователя номер задания, и выводит входящие праметры функции, и результат.
Пример:
Ввелите номер Demo функции: 2
Алгоритм евклида: 912, 84. Ответ: 12"""

import fib_1
from nod_2 import nod
from url_3 import pageparser
print("1. Фибоначчи \n"
          "2. Евклид\n"
          "3. Счетчик картинок")
def demo():
    print("введите номер функции")
    choice = int(input())
    if choice == 1:
        print("введите длинну ряда")
        n = int(input())
        fib_1.func(n)
    elif choice == 2:
        print("введите два числа для вычисления nod")
        a,b = input().split()
        a = int(a)
        b = int(b)
        nod(a,b)
    elif choice == 3:
        print("введите урл - формат http://onliner.by")
        str = input()
        pageparser(str)
    else:
        return
demo()

"""Q3: почему когда импортируешь конкретный метод из пакета from nod_2 import nod весь файл исполняется интерпритатором? 
К примеру, если раскомментировать в nod2.py a,b = input().split() и запустить demo_utils.py - сначала будет просить ввести  два числа и только потом print("1. Фибоначчи \n") из demo_utils.py? 
Как правильно использовать методы других пакетов, чтобы лишний код не исполнялся?"""


