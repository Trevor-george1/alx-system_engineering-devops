#!/usr/bin/python3
"""script that uses a REST API, given employee id,  returns
    information about his TODO list progress
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"

    # make a GET request to get employee given id
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()

    # GET request for Todos for the employee using id
    todos = requests.get(url + 'todos', params={"userId": sys.argv[1]}).json()

    # filter completed todos and store the titles in alist
    completed = [t.get('title') for t in todos if t.get('completed') is True]

    # print employer's name, completed tasks and total no of tasks
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(completed), len(todos)))

    # display title of completed tasks
    for c in completed:
        print("\t {}".format(c))
