# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class People:
    def __init__(self, name, patronymic, surname):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
 
    def get_full_name(self):
        return self.name + ' ' + self.patronymic + ' ' + self.surname
 
    def get_short_name(self):
        return '{} {}.{}.'.format(self.surname.title(), self.name[0].upper(), self.patronymic[0].upper())
 
 
# if __name__ == '__main__':  # Тестирование.
#     people1 = People('Иван', 'Иванович', 'Иванов')
#     print(people1.get_full_name())
#     print(people1.get_short_name())
 
 
class Student(People):
    def __init__(self, name, patronymic, surname, mom, dad, school_class):
        People.__init__(self, name, patronymic, surname)
        self.mom = mom
        self.dad = dad
        self.school_class = school_class
 
 
# if __name__ == '__main__':  # Тестирование.
#     st_1 = Student('Семен', 'Семенович', 'Семенов', 'Анна Михайлова', 'Алексанр Семенов', '7а')
#     st_2 = Student('Сергей', 'Сергеевич', 'Сергеев', 'Ольга Сергеева', 'Андрей Сергеев', '7б')
#     st_3 = Student('Олег', 'Олегович', 'Петров', 'Юлия Петрова', 'Олег Петров', '7а')
#     print(Student.all_classes(st_1))
 
 
class Teacher(People):
    def __init__(self, name, patronymic, surname, subject):
        People.__init__(self, name, patronymic, surname)
        self.subject = subject
 
 
class Class_rooms:
    def __init__(self, class_room, teachers):
        self.class_room = class_room
        self.teachersdict = {t.subject: t for t in teachers}
 
 
 
if __name__ == '__main__':  # Тестирование.
    teachers = [Teacher('Иван', 'Иванович', 'Иванов', 'Математика'),
                Teacher('Петр', 'Петрович', 'Петров', 'Литература'),
                Teacher('Сидор', 'Сидорович', 'Сидоров', 'Физика'),
                Teacher('Дмитрий', 'Дмитриевич', 'Дмитриев', 'История'),
                Teacher('Никита', 'Никитиевич', 'Никишин', 'Биология')]
    classes = [Class_rooms('11 А', [teachers[0], teachers[1], teachers[2]]),
               Class_rooms('11 Б', [teachers[1], teachers[3], teachers[4]]),
               Class_rooms('10 А', [teachers[3], teachers[1], teachers[0]])]
    parents = [People('Семен', 'Семенович', 'Семенов'),
               People('Светлана', 'Савельевна', 'Семенова'),
               People('Роман', 'Романович', 'Романов'),
               People('Римма', 'Романовна', 'Романова'),
               People('Сергей', 'Сергеевич', 'Сергеев'),
               People('Юлия', 'Викторвна', 'Сергеева')]
    students = [Student('Игорь', 'Cеменович', 'Семенов', parents[0], parents[1], classes[0]),
                Student('Ольга', 'Романова', 'Романова', parents[2], parents[3], classes[1]),
                Student('Александр', 'Сергеевич', 'Сергеев', parents[4], parents[5], classes[2])]
    print('Список классов в школе: ')
    for f in classes:
        print(f.class_room)
 
    for f in classes:
        print('Учителя, преподающие в {} классе:'.format(f.class_room))
        for teacher in classes[0].teachersdict.values():
            print(teacher.get_full_name())
    for f in classes:
        print("Ученики в классе {}:".format(f.class_room))
        for st in students:
            print(st.get_short_name())
 
   
   
   # Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, surname, name, middle_name):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
 
    def get_fullname(self):
        full_name = self.surname + " " + self.name + " " + self.middle_name
        return full_name
 
    def get_shortname(self):
        print(f"{self.surname.title()} {self.name[0].upper()}.{self.middle_name[0].upper()}")
 
 
class Teacher(Person):
    def __init__(self, surname, name, middle_name, subject):
        super().__init__(surname, name, middle_name)
        self.subject = subject
 
 
class Student(Person):
    def __init__(self, surname, name, middle_name, class_num, mother, father):
        super().__init__(surname, name, middle_name)
        self.mother = mother
        self.father = father
        self.class_num = class_num
 
    def get_parents(self):
        print(f"Маму зовут: {self.surname}а {self.mother}\n"
              f"Отца зовут: {self.surname} {self.father}")
 
 
class Class_rooms():
    def __init__(self, class_number, subjects, teachers):
        self.class_number = class_number
        self.subjects = {subjects: teachers}
    
        
 
 
classes = [Class_rooms("5A", "Математика", "Ловцов Андрей Михайлович"),
           Class_rooms("6A", "Физика", "Слуцкая Елена Викторовна")]
 
teachers = [Teacher("Ловцов", "Андрей", "Михайлович", "Математика"),
            Teacher("Беляев", "Петр", "Андреевич", "Физкультура"),
            Teacher("Слуцкая", "Елена", "Викторовна", "Физика"),
            Teacher("Тишина", "Мария", "Анатольевна", "Химия")]
 
students = [Student("Андрейцев", "Илья", "Андреевич", "11Б", "Анна", "Андрей"),
            Student("Булкин", "Пирожок", "Маркович", "11А", "Хлеб", "Масло"),
            Student("Марков", "Дмитрий", "Андреевич", "5Б", "Евгения", "Андрей"),
            Student("Александр", "Сергеевич", "Пушкин", "6А", "Надежда", "Сергей")]
 
# shcholar_name = input("Введите ФИО интересующего ученика: ")
# for scholar in students:
#     if scholar.get_fullname() == shcholar_name:
#         scholar.get_parents()
#         break
# else:
#     print("Такого ученика нет в школе")
