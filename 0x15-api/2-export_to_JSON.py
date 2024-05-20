#!/usr/bin/python3
"""script that fetches data about employee tasks from REST API"""
from json import dump
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/user/{}".format(user_id)
    response = requests.get(url)
    username = response.json().get('username')

    url = "https://jsonplaceholder.typicode.com/user/{}/todos".format(user_id)
    response = requests.get(url)
    tasks = response.json()
    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })
    with open('{}.json'.format(user_id), 'w') as f:
        dump(dictionary, f)
