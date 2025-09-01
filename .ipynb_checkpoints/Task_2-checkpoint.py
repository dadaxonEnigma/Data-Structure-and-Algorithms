# 1. Функция принимает один аргумент
def my_numbs_first(*args):
    output = 0
    for numb in args:
        output += numb
    return output

print(my_numbs_first(1,2,3,4,5,6))

# 2. Функция принимает два аргумента
def my_numbs_second(*args, start = 0):
    output = 0
    for numb in args:
        output += numb
    return output + start

print(my_numbs_second(*[1,2,3,4,5],5))

# 3.  Напишите функцию, которая принимает список чисел. Он
# должен вернуть среднее значение (т.е. среднее арифметическое) этих чисел

def my_numb(*args):
    std = 0
    for numb in args:
        std += numb 
    return int(std / len(args))

print(my_numb(*[1,2,3,4,5]))