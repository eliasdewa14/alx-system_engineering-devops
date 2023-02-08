#!/usr/bin/python3
"""a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == '__main__':
    response = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                            .format(argv[1])).json()

    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={:}'.format(
            argv[1])).json()

    EMPLOYEE_NAME = response.get('name')
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []

    for task in tasks:
        if task.get('completed'):
            TASK_TITLE.append(task)
            NUMBER_OF_DONE_TASKS += 1
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, len(tasks)))

    for tt in TASK_TITLE:
        print("\t {}".format(tt.get('title')))
