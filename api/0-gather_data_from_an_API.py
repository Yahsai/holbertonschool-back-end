#!/usr/bin/python3
"""
Module: 0-gather_data_from_an_API
"""

import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    Fetches TODO list progress for a given employee ID from a REST API.

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
    employee_name = employee_data.get('name')

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)
