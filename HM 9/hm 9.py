# Самостоятельно познакомиться с паттернами Factory (фабрика) и Factory method (фабричный метод) и решить следующую задачу:
# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>). 
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение: 
# Должна быть возможность создать необходимый тег, явно его не создавая, т. е не через img = Image(), 
# а через фабричный метод или фабрику, например factory.create_tag(name).»

# *Дополнительно:
# Реализовать возможность опциональной передачи атрибутов для тегов, т. е атрибуты могут быть 
# (src для image, href для a и. т. д.) , а могут и не быть.


import abc


class Tag(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_html(self):
        pass


class Image(Tag):
    def __init__(self):
        self.src = "img"

    def get_html(self):
        return "<></{}>".format(self.src)


class Input(Tag):
    def __init__(self):
        self.in_type = "input"

    def get_html(self):
        return "<></{}>".format(self.in_type)

class Text(Tag):
    def __init__(self):
        self.text = "p"

    def get_html(self):
        return "<></{}>".format(self.text)


class Link(Tag):
    def __init__(self):
        self.link = 'a'

    def get_html(self):
        return "<></{}>".format(self.link)

class None_text(Tag):
    def __init__(self):
        self.none_text = ''

    def get_html(self):
        return "<></{}>".format(self.none_text)

class Tagfactory:

    @staticmethod
    def create_tag(name):
        if name == 'image':
            return Image()
        elif name == 'input':
            return Input()
        elif name == 'a':
            return Link()
        elif name == 'p':
            return Text()
        elif name == '':
            return None_text()

factory = Tagfactory()
elements = ["image", "input", 'a', 'p', '']
for el in elements:
    print(factory.create_tag(el).get_html())