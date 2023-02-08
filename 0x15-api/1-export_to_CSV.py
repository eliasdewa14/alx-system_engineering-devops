#!/usr/bin/python3
"""The extend Python script to export data in the CSV format.
"""
import requests
from sys import argv


if __name__ == '__main__':
    response = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                            .format(argv[1])).json()

    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={:}'.format(
            argv[1])).json()

    USER_ID = argv[1]
    USER_NAME = response.get('username')

    with open('{:}.csv'.format(argv[1]), 'w') as file:
        for task in tasks:
            file.write('"{}", "{}", "{}", "{}"\n'.format(argv[1], USER_NAME,
                                                         task.get('completed'),
                                                         task.get('title')))
