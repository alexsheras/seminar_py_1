#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов
#. Вместе они сделали S журавликов. Сколько журавликов 
# сделал каждый ребенок, если известно, что Петя и Сережа
#  сделали одинаковое количество журавликов, а Катя сделала 
# в два раза больше журавликов, чем Петя и Сережа вместе?

import random


S = random.randrange(0, 99, 3)
print(f'Сумма журавликов на всех: {S}')

qty_Petr = int(S/6)
qty_Kate = int(S/6*4)
qty_Sergey = int(S/6)

print(qty_Petr, qty_Kate, qty_Sergey)
