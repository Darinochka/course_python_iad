# Напишите рекурсивную функцию sum(a, b), возвращающую сумму
# двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b):
    if a <= 0 and b <= 0:
        return 0
    elif a <= 0 or b <= 0:
        return sum(a-1, b-1) + 1
    else:
        return sum(a-1, b-1) + 1 + 1
