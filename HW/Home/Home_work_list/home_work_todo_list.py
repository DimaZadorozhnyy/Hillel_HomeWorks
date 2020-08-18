"""
Написать класс, который позволит сохранить список дел, отмечать сделанное и показывать то, что нужно сделать.
Хранить список дел в json файле
При запуске программы должна появится меню с вариантами действий: добавить в список, вывести весь список, вывести
список не сделанных дел, отметить как сделаное
"""


import json
from datetime import datetime


class Item:
    def __init__(self, done, info, last_updated):
        self.done = done
        self.info = info
        self.last_updated = last_updated

    def as_dict(self):
        return {
            'done': self.done,
            'info': self.info,
            'last_updated': str(self.last_updated),
        }

    def __repr__(self):
        return self.info


class TodoList:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(f'{self.name}.json', 'r') as file:
                data = json.load(file)
                tasks = []
                for item in data:
                    tasks.append(Item(item['done'], item['info'], item['last_updated']))
                return tasks
        except FileNotFoundError:
            return []

    @property
    def tasks_list(self):
        tasks = ''
        for index, item in enumerate(self.tasks):
            tasks += f'\n {index}\t {item.done}\t {item.info}\t {item.last_updated}'
        return tasks

    @property
    def not_ready_tasks(self):
        tasks = ''
        for item in self.tasks:
            if not item.done:
                tasks += f'\n {item.done}\t {item.info}\t {item.last_updated}'
        return tasks

    def last_updated_task(self, index):
        self.tasks[index].last_updated = datetime.now()

    def done_task(self, index):
        self.tasks[index].done = True

    def undone_task(self, index):
        self.tasks[index].done = False

    def add_task(self, task):
        self.tasks.append(task)

    def get_task_index(self, task):
        return self.tasks.index(task)

    def to_json(self):
        with open(f'{self.name}.json', 'w') as file:
            tasks = []
            for task in self.tasks:
                tasks.append(task.as_dict())
            json.dump(tasks, file, indent=4)


def init_todo_list():
    list_name = input('Enter list name\n')
    owner = input('Who owner?\n')
    return TodoList(list_name, owner)


def main():
    todo_list = init_todo_list()
    try:
        while True:
            action = input('добавить в список - 1,\n'
                           ' посмотреть список - 2,\n'
                           ' отметить как выполненое - 3,\n'
                           ' посмотреть не выполненые - 4,\n'
                           ' закончить работу со списком - 0\n')
            if action == '1':
                done = input('добавить выполненый таск - 1, невыполненый - 0\n')
                if done not in {'1', '0'}:
                    continue
                done = bool(int(done))
                info = input('Some info')
                todo_list.add_task(Item(done, info, last_updated=datetime.now()))
            elif action == '2':
                print(todo_list.tasks_list)
            elif action == '4':
                print(todo_list.not_ready_tasks)
            elif action == '3':
                index = int(input('Введите index'))
                todo_list.done_task(index)
            elif action == '0':
                todo_list.to_json()
                return
    except Exception:
        todo_list.to_json()


if __name__ == '__main__':
    main()
