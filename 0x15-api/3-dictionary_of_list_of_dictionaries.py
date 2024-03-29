#!/usr/bin/python3
"""The extend Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    dictionary = {}
    for user in users:
        USER_ID = user.get('id')
        USER_NAME = user.get('username')
        dictionary[USER_ID] = []
        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID) +
            '/todos/').json()
        for task in tasks:
            dictionary[USER_ID].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": USER_NAME
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
