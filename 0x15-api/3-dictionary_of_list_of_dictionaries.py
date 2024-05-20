#!/usr/bin/python3
"""script that fetches data about employee tasks from REST API"""
from json import dump
import requests
import sys


if __name__ == '__main__':

    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        tasks = requests.get(url + "users/{}/todos".format(user_id)).json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                                        "username": username,
                                        "task": task.get('title'),
                                        "completed": task.get('completed'),
                                        
                                        })
    with open('todo_all_employees.json', 'w') as f:
        dump(dictionary, f)
