# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


list1 = [9, 12, 3, 2, 44, 5, 0, 10, 1, 32]
print('list1:', list1)
list2 = list(map(lambda x:x**2, list1))
print('list2:', list2)

# Результат
# list1: [9, 12, 3, 2, 44, 5, 0, 10, 1, 32]
# list2: [81, 144, 9, 4, 1936, 25, 0, 100, 1, 1024]



# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

spisok1 = [1,3 ,64 ,15 ,13 ,15 ,1 ,17 ,3 ,34 ]
print('spisok1:', spisok1)
spisok2 = list(map(lambda x:x**2, spisok1))
print('spisok1:', spisok1)
       


# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4


list1 = [7, 6, 2, -7, -2, 15, 12, 16, 4, 24, -5, 89, 64, 81]
list2 = [i for i in list1 if  i >= 0 and i%4 and not i%3]
print(list2)