#!/usr/bin/python3
"""The extend Python script to export data in the CSV format.
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    USER_ID = argv[1]
    USER_URL = "https://jsonplaceholder.typicode.com/users/{}" .format(USER_ID)

    USER_NAME = requests.get(USER_URL).json().get('username')

    todo_URL = "https://jsonplaceholder.typicode.com/todos?userID={}".format(
        USER_ID)
    tasks = requests.get(todo_URL).json()

    with open('{}.csv'.format(USER_ID), 'w') as file:
        task_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            task_writer.writerow([int(USER_ID), USER_NAME,
                                 task.get('completed'),
                                 task.get('title')])
