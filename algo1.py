# squares = [x**2 for x in range(1,11)]
# print(squares)

# keys = [1,2,3,4]
# values = ['one','two','three','four']
# dictionary = dict(zip(keys,values))
# print(dictionary)

# is_even = lambda x: x % 2 == 0
# print(is_even(10))

# list1 = [1,2,3,4]
# list2 = [3,5,6,7,8,9,8]
# intersection = list(set(list1) & set(list2))
# print(intersection)

# most_common = max(set(list2), key=list2.count)
# print(most_common)

# def my_func(a,b,c):
#     return (a + b > c) and (a + c > b) and (b + c > a)
# print(my_func(3,1,5))


# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     return distance_to_pump / mpg <= fuel_left

# print(zero_fuel(100,50,1))

# def enough(cap, on, wait):
#     return 0 if (on+wait<cap) else abs(cap-on-wait)

# print(enough(20,5,5))

# def open_or_senior(data):
#     res = []
#     for i in data:
#         res.append('Senior' if i[0] >=55 and i[0] > 7 else 'Open')
#     return res

# print(open_or_senior([[18,20],[45,2],[61,12],[37,6],[21,21],[78,9]]))


# def sum_array(arr):
#     return sum(arr) - max(arr) - min(arr) if isinstance(arr,list) and len(arr) > 1 else 0


# def remove_every_other(my_list):
#     return my_list[::2]

# print(remove_every_other(["Keep", "Remove", "Keep", "Remove", "Keep",]))


# def roman_to_int(s):
#     roman = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#     total = 0
#     prev_value = 0
#     for char in reversed(s):  # обходим строку справа налево
#         value = roman[char]
#         if value < prev_value:
#             total -= value  # если меньше предыдущего — вычитаем
#         else:
#             total += value
#             prev_value = value

#     return total

# print(roman_to_int("VC"))

import time
from collections import deque

N = 100_000  # Количество вставок

# Вставка в начало list
start_list = time.time()
lst = []
for i in range(N):
    lst.insert(0, i)
end_list = time.time()
list_time = end_list - start_list

# Вставка в начало deque
start_deque = time.time()
dq = deque()
for i in range(N):
    dq.appendleft(i)
end_deque = time.time()
deque_time = end_deque - start_deque

print(f"Время вставки в начало списка list: {list_time} секунд")
print(f"Время вставки в начало deque: {deque_time} секунд")
