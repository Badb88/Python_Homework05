# a) Добавьте игру против бота

import random
print()
r = random.randint(1, 2)
candy = 2021
pn = 0
p1 = 0
p2 = 0
print(f"Жеребьёвкой определено, что первым ходит игрок № {r}.")
while candy > 0:
    if r == 1:
        print(f"\nКоличество конфет: {candy}\n")
        p1 = int(input("Ходит игрок № 1. Возьмите количество конфет, но не более 28: "))
        print()
        while p1 > candy:
            p1 = int(input("Ошибка! Возьмите количество конфет не более чем осталось: "))
            print()
        while int(p1) <= 0 or int(p1) > 28:
            p1 = int(input("Вы можете взять от 1 до 28 конфет: "))
            print()
            while p1 > candy:
                p1 = int(input("Ошибка! Возьмите количество конфет не более чем осталось: "))
                print()
        candy -= p1
        pn = 1
        print(f"\nКоличество конфет: {candy}\n")
        if candy == 0:
            break
        p2 = random.randint(1, 28)
        while p2 > candy:
            p2 = random.randint(1, 28)
        while int(p2) <= 0 or int(p2) > 28:
            p2 = random.randint(1, 28)
            while p2 > candy:
                p2 = random.randint(1, 28)
        print(f"Игрок № 2 взял {p2} конфет.")
        candy -= p2
        pn = 2
        if candy == 0:
            break
    else:
        print(f"\nКоличество конфет: {candy}\n")
        p2 = random.randint(1, 28)
        while p2 > candy:
            p2 = random.randint(1, 28)
        while int(p2) <= 0 or int(p2) > 28:
            p2 = random.randint(1, 28)
            while p2 > candy:
                p2 = random.randint(1, 28)
        print(f"Игрок № 2 взял {p2} конфет.")
        candy -= p2
        pn = 2
        if candy == 0:
            break
        print(f"\nКоличество конфет: {candy}\n")
        p1 = int(input("Ходит игрок № 1. Возьмите количество конфет, но не более 28: "))
        print()
        while p1 > candy:
            p1 = int(input("Ошибка! Возьмите количество конфет не более чем осталось: "))
            print()
        while int(p1) <= 0 or int(p1) > 28:
            p1 = int(input("Вы можете взять от 1 до 28 конфет: "))
            print()
            while p1 > candy:
                p1 = int(input("Ошибка! Возьмите количество конфет не более чем осталось: "))
                print()
        candy -= p1
        pn = 1
        if candy == 0:
            break
if pn == 1:
    print()
    print('--- Выиграл Игрок № 1 ! ---')
    print()
else:
    print()
    print('--- Выиграл Игрок № 2 ! ---')
    print()