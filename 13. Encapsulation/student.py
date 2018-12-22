class Student:
    def __init__(self):
        self.__id = 123
        self.__name = 'John'

    def display(self):
        print(self.__id)
        print(self.__name)


s = Student()

# print(s.__id)
# print(s.__name)

s.display()

print(s._Student__id)
