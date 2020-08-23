import json
from datetime import datetime


class Item:
    def __init__(self, budget, info, last_updated):
        self.budget = budget
        self.info = info
        self.last_updated = last_updated

    def as_dict(self):
        return {
            'done': self.budget,
            'info': self.info,
            'last_updated': str(self.last_updated),
        }

    def __repr__(self):
        return self.info


class Student_list:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(f'{self.name}.json', 'r') as file:
                data = json.load(file)
                students = []
                for item in data:
                    students.append(Item(item['budget/contract'], item['info'], item['last_updated']))
                return students
        except FileNotFoundError:
            return []

    @property
    def students_list(self):
        students = ''
        for index, item in enumerate(self.students):
            students += f'\n {index}\t {item.budget}\t {item.info}\t {item.last_updated}'
        return students

# Посмотреть список контрактников
    @property
    def the_contract(self):
        students = ''
        for item in self.students:
            if not item.budget:
                students += f'\n {item.budget}\t {item.info}\t {item.last_updated}'
        return students

# Посмотреть список бюджетников
    @property
    def the_budget(self):
        students = ''
        for item in self.students:
            if item.budget:
                students += f'\n {item.budget}\t {item.info}\t {item.last_updated}'
        return students

    def budget_student(self, index):
        self.students[index].budget = True

    def contract_student(self, index):
        self.students[index].budget = False

    def add_student(self, student):
        self.students.append(student)

    def expel_student(self, student):
        self.students.pop(student)

    def get_task_index(self, student):
        return self.students.index(student)

# Запись в json файл
    def to_json(self):
        with open(f'{self.name}.json', 'w') as file:
            students = []
            for student in self.students:
                students.append(student.as_dict())
            json.dump(students, file, indent=4)


def init_students_list():
    name_group = input('Enter name group\n')
    owner = input('Who owner?\n')
    return Student_list(name_group, owner)


def main():
    group_list = init_students_list()
    try:
        while True:
            action = input('добавить студента - 1,\n'
                           'посмотреть список студентов - 2,\n'
                           'посмотреть список бюджетников - 3,\n'
                           'посмотреть список контрактников - 4,\n'
                           'перевести на контракт - 5\n'
                           'перевести на бюджет - 6\n'
                           'отчислить студента - 7\n'
                           'закончить работу со списком студентов - 0\n')
            if action == '1':
                budget = input('добавить на бюджет - 1, на контракт - 0\n')
                if budget not in {'1', '0'}:
                    continue
                budget = bool(int(budget))
                info = input('name_student'), input("last name")
                group_list.add_student(Item(budget, info, last_updated=datetime.now()))
            elif action == '2':
                print(group_list.students_list)
            elif action == '3':
                print(group_list.the_budget)
            elif action == '4':
                print(group_list.the_contract)
            elif action == "5":
                index = int(input("index"))
                group_list.contract_student(index)
            elif action == '6':
                index = int(input('Введите index'))
                group_list.budget_student(index)
            elif action == '7':
                index = int(input("index"))
                group_list.expel_student(index)
            elif action == '0':
                group_list.to_json()
                return
    except Exception:
        group_list.to_json()


if __name__ == '__main__':
    main()
