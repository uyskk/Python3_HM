import math
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

print("\nTask1")
def fibonacci(n, m):
    i=1
    ListOfFib=[1,1]
    while i<m:
        ListOfFib.append(ListOfFib[i-1]+ListOfFib[i])
        i+=1
    return ListOfFib[n:m]

print(fibonacci(2,7))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


print("\nTask2")
def sort_to_max(origin_list):
    for i in range(0,len(origin_list)-1):
        for j in range(i+1,len(origin_list)):
            if origin_list[i]>origin_list[j]:
                origin_list[i],origin_list[j]=origin_list[j],origin_list[i]
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

print("\nTask3")
def myOwnFilter(func,list):
    List=[]
    for i in list:
        if func(i):
            List.append(i)
    return List

def moreThan10(n):
    if n>10:
        return True
    else:
        return False

List=[1,2,3,4,10,11,12,3,14]
print(myOwnFilter(moreThan10,List))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


def is_parallelogram(a1, a2, a3, a4):
    if abs(a3[0] - a2[0]) == abs(a4[0] - a1[0]) and \
       abs(a2[1] - a1[1]) == abs(a3[1] - a4[1]):
        return True
    return False