#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys
import json


def add():
    name = input("Фамилия и инициалы ")
    post = input("Номер группы ")
    a = int(input("Русский язык "))
    b = int(input("Математика "))
    c = int(input("Информатика "))
    d = int(input("История "))
    e = int(input("Физика "))
    student = {
        'name': name,
        'post': post,
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
    }
    students.append(student)
    if len(students) > 1:
        students.sort(key=lambda item: item.get('name', ''))

def list():
    for idx, student in enumerate(students, 1):
        print(
            '{:>7}: ФИО: {}, Номер группы: {}, Русский язык: {}, Математика: {}, Информатика: {}, История: {}, Физика: {};'.format(
                idx,
                student.get('name', ''), student.get('post', ''), student.get('a', 0),
                student.get('b', 0), student.get('c', 0),
                student.get('d', 0), student.get('e', 0)))

def bad():
    count = 0
    for student in students:
        if (student.get('a') == 2) or (student.get('b') == 2) or (student.get('c') == 2) \
                or (student.get('d') == 2) or (student.get('e') == 2):
            count += 1
            print('{:>4}: {}'.format(count, student.get('name', '')))
    if count == 0:
        print("Таких студентов не выявлено.")

def help():
    print("Список команд:\n")
    print("add - Добавить студента;")
    print("list - Список студентов;")
    print("bad - Студенты с плохой успеваемостью;")
    print("help - отобразить справку;")
    print("end - завершить работу с программой.")

def load():
    parts = command.split(' ', maxsplit=1)
    with open(parts[1], 'r') as f:
        students = json.load(f)

def save():
    parts = command.split(' ', maxsplit=1)
    with open(parts[1], 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False)

if __name__ == '__main__':
    students = []
    while True:
        command = input(">>> ").lower()
        if command == 'end':
            break
        elif command == 'add':
            add()
        elif command == 'list':
            list()
        elif command == 'bad':
            bad()
        elif command == 'help':
            help()
        elif command.startswith('save '):
            save()
        elif command.startswith('load '):
            load()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)