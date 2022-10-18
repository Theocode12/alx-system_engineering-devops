#!/usr/bin/python3
"""
Module that extract data from api
"""

import requests
from sys import argv


def main():
    """
    Main function
    """
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])

    emp_resp = requests.get(emp_url).json()

    emp_name = emp_resp.get('name')

    payload = {'userId': {argv[1]}}
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    total_task = requests.get(todo_url, payload).json()

    payload = {'userId': {argv[1]}, 'completed': 'true'}
    task_done_resp = requests.get(todo_url, payload).json()

    print("Employee {} is done with tasks({}/{}):".
          format(emp_name, len(task_done_resp), len(total_task)))

    for task in task_done_resp:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
