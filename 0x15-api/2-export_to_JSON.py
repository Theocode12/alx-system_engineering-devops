#!/usr/bin/python3
"""
Module that extract data from api
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    filename = '{}.json'.format(emp_id)
    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    emp_resp = requests.get(emp_url).json()
    emp_name = emp_resp.get('username')

    todo_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
                                                                        emp_id)

    total_task = requests.get(todo_url).json()

    with open(filename, 'w') as jsfile:
        for task in total_task:
            row = {
                    emp_id: [
                        {"task": task.get('title'),
                         "completed": task.get('completed'),
                         "username": emp_name}
                    ]
                }
            json.dump(row, jsfile)
