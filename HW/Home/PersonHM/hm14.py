class Person:

    def __init__(self, name, age, friend='Jon 22'):
        self.name = name
        self.age = age
        self.__friends = [friend]

    @property
    def friend(self):
        return self.__friends

    @friend.setter
    def friend(self, value):
        if value not in self.__friends:
            self.__friends.append(value)
        elif value in self.__friends:
            print(True)


pers1 = Person('Dima', 22)


print(pers1.friend)
a = 'да'
while a == 'да':
    a = input("Продолжить да/нет?")
    if a != 'да':
        break
    pers1.friend = input("Введите имя и возвраст\n")
    print(pers1.friend)

