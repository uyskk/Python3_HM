# Задача-1:
# Примечание: Если уже делали easy задание, то просто перенесите решение сюда.
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.



# ПРИМЕЧАНИЕ: Для решения задачи 2-3 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь "меню" выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
print('sys.argv = ', sys.argv)

def print_help():
    print('help')
    print('changedir <fullderectory>')
    print('lookdir')
    print("mkdir <derectory>" )
    print("mkdeldir <derectory>")

def make_dir():
    if not derectory:
        print("Укажите диреторию вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), derectory)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(derectory))
    except FileExistsError:
        print('директория {} уже существует'.format(derectory))

def make_del_dir():
    if not derectory:
        print("Укажите диреторию вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), derectory)
    try:
        os.rmdir(dir_path)
        print('директория {} удалена'.format(derectory))
    except FileExistsError:
        print('директория {} не существует'.format(derectory))

def look_dir():
    print(os.listdir())

def change_dir():
    if not derectory:
        print('Необходимо указать имя директории вторым параметром')
        return
    try:
        os.chdir(derectory)
        print('Успешно перешли в папку: {}'.format(derectory))
        print('Текущий каталог: ', os.getcwd())
    except FileNotFoundError:
        print('dir_{} - папки не существует'.format(derectory))


do = {
    'help': print_help,
    'mkdir': make_dir,
    'lookdir': look_dir,
    'changedir': change_dir,
    'mkdeldir': make_del_dir,

    }

try:
    derectory = sys.argv[2]
except:
    derectory = None

try:
    fullderectory = sys.argv[4]
except:
    fullderectory = None

try:
    derectory = sys.argv[5]
except:
    derectory = None


try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('wrong key')
        print('write help to get help')