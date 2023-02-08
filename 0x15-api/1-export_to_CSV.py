#!/usr/bin/python3
"""The extend Python script to export data in the CSV format.
"""
import requests
from sys import argv


if __name__ == '__main__':
    user_url = 'https://jsonplaceholder.typicode.com/users/' + argv[1]

    response = requests.get(user_url).json()
    todos = user_url + "/todos"
    tasks = requests.get(todos).json()

    USER_ID = argv[1]
    USER_NAME = response.get('username')

    with open('{}.csv'.format(argv[1]), 'w') as file:
        for task in tasks:
            file.write('"{}", "{}", "{}", "{}"\n'.format(argv[1], USER_NAME,
                                                         task.get('completed'),
                                                         task.get('title')))
