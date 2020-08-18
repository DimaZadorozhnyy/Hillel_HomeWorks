
class Person:
    def __init__(self, mame, age):
        self.name = mame
        self.age = age
        self.__friends = []

    def know(self, other_person):
        if other_person in self.__friends:
            return
        self.__friends.append(other_person)
        other_person.know(self)

    def is_known(self, other_person):
        if other_person in self.__friends:
            return True
        return False


name_pers_1 = input("Введите имя\n")
age_pers_1 = input("Введите возвраст\n")
name_pers_2 = input("Введите имя\n")
age_pers_2 = input("Введите возвраст\n")

p1 = Person(name_pers_1, age_pers_1)
p2 = Person(name_pers_2, age_pers_2)

p1.know(p2)
print(p1.know(p2))
print(p1.is_known(p2))
print(p2.is_known(p1))


