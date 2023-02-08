#!/usr/bin/python3
"""The extend Python script to export data in the CSV format.
"""
import requests
from sys import argv


if __name__ == '__main__':
    USER_ID = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/' + USER_ID

    response = requests.get(user_url).json()
    todo = user_url + "/todos"
    tasks = requests.get(todo).json()

    USER_NAME = response.get('username')

    with open('{}.csv'.format(argv[1]), 'w') as file:
        for task in tasks:
            file.write('"{}", "{}", "{}", "{}"\n'.format(argv[1], USER_NAME,
                                                         task.get('completed'),
                                                         task.get('title')))
