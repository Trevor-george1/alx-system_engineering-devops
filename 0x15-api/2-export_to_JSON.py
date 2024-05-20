#!/usr/bin/python3
"""script that fetches data about employee tasks from REST API"""
from json import dump
import requests
import sys


if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get('username')

    tasks = requests.get(url + "users/{}/todos".format(user_id)).json()
    dictionary = {user_id: []}
    for task in tasks:
        dictionary[user_id].append({
                                    "task": task.get('title'),
                                    "completed": task.get('completed'),
                                    "username": username
                                    })
    with open('{}.json'.format(user_id), 'w') as f:
        dump(dictionary, f)
