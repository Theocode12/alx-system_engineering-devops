#!/usr/bin/python3
"""
Module that extract data from api
"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]

    emp_url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)

    emp_resp = requests.get(emp_url).json()

    emp_name = emp_resp.get('name')

    payload = {'userId': emp_id}
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    total_task = requests.get(todo_url, payload).json()

    with open('USER_ID', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)

        for task in total_task:
            row = [emp_id, emp_name, task.get('completed'), task.get('title')]
            csvwriter.writerow(row)
