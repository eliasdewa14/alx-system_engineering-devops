#!/usr/bin/python3
"""The extend Python script to export data in the CSV format.
"""
import requests
from sys import argv


if __name__ == '__main__':
    USER_ID = argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users" + "/" + USER_ID

    response = requests.get(user_url).json()
    USER_NAME = response.get('username')

    todo = user_url + "/todos"
    tasks = requests.get(todo).json()

    with open('{}.csv'.format(USER_ID), 'w') as file:
        for task in tasks:
            file.write('"{}", "{}", "{}", "{}"\n'.format(USER_ID, USER_NAME,
                                                         task.get('completed'),
                                                         task.get('title')))
