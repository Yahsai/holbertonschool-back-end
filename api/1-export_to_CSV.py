#!/usr/bin/python3
"""
Module: 1-export_to_CSV
"""

import csv
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    Fetches TODO list progress for a given employee ID from a REST API and exports it to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    employee_data = response.json()
    username = employee_data.get('username')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    todos = response.json()

    filename = "{}.csv".format(employee_id)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, username, todo['completed'], todo['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)
