# Вариант 1
# 1) Для какого наибольшего целого неотрицательного A выражение
# (x + y ≤ 22) ∨ (y ≤ x – 6) ∨ (y ≥ A))
# тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?

# Код:


'''def f(x, y, a):
    return (x + y <= 22) or (y <= x - 6) or (y >= a)


for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        for y in range(1, 1001):
            if f(x, y, a) == False:
                fl = False
                break
        if fl == False:
            fl = False
            break
    if fl == True:
        print(a)'''

# 2)Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа A формула
# ДЕЛ(A, 9) ∧ (ДЕЛ(280, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(730, x)))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?

# Код:
import asyncio

'''def f(x, a):
    return (a % 9 == 0) and ((280 % x == 0) <= ((a % x != 0) <= (730 % x != 0)))


for a in range(1, 1001):
    fl = True
    for x in range(1, 1001):
        if f(x, a) == False:
            fl = False
            break
    if fl:
        print(a)
        break'''


# 3)Введём выражение M & K, обозначающее поразрядную конъюнкцию M и K (логическое «И» между соответствующими битами двоичной записи). Определите наименьшее натуральное число A, такое что выражение
# (X & 53 = 0) → ((X & 19 ≠ 0) → (X & A ≠ 0))
# тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной X)?

# Код:


# def f(x, a):
#     return (x&25!=0)<=((x&19==0) <= (x&a!=0))
#
#
# for a in range(1, 1001):
#     fl = True
#     for x in range(1, 1001):
#         if f(x, a) == False:
#             fl = False
#             break
#     if fl:
#         print(a)
#         break


# def f(x, a):
#     return (((x%2==0) <= (x%3!=0)) or (x + a >=100))
#
#
# for a in range(1, 1001):
#     fl = True
#     for x in range(1, 1001):
#         if f(x, a) == False:
#             fl = False
#             break
#     if fl:
#         print(a)
#         break

def f(a, x):
    return (x & a == 0) <= ((x & 31 != 0) <= (x & 35 != 0))
for a in range(50, 121):
    fl = True
    for x in range(1, 1001):
        if f(a, x) == False:
            fl = False
            break
    if fl:
        print(a)