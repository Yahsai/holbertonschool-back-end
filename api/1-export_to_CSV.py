#!/usr/bin/python3
"""Module to create CSV"""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    EMPLOYEE_DATA = requests.get(
        f'https://jsonplaceholder.typicode.com/users?Id={user_id}').json()

    todo_DATA = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()

    EMPLOYEE_NAME = EMPLOYEE_DATA[int(user_id)-1].get("name")
    USER_ID = EMPLOYEE_DATA[int(user_id)-1].get("id")
    USERNAME = EMPLOYEE_DATA[int(user_id)-1].get("username")

    with open(f'{user_id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for tasks in todo_DATA:
            writer.writerow(
                [USER_ID, USERNAME,
                 tasks.get('completed'), tasks.get('title')])
