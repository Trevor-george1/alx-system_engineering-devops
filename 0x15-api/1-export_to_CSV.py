#!/usr/bin/python3
"""script that uses a REST API, given employee id,  returns
    information about his TODO list progress
"""
import csv
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

    # write the data in cv file
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, mode='w') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user['id'], user['username'],
                            todo['completed'], todo['title']])
