"""The extend Python script to export data in the JSON format.
"""
import requests
from sys import argv
import json


if __name__ == '__main__':
    response = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                            .format(argv[1])).json()

    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={:}'.format(
            argv[1])).json()

    USER_ID = argv[1]
    USER_NAME = response.get('username')

    dictionary = {USER_ID: []}
    for task in tasks:
        dictionary[USER_ID].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": USER_NAME
        })
    with open('{}.json'.format(USER_ID), 'w') as filename:
        json.dump(dictionary, filename)
