#!/usr/bin/python3
"""
This script fetches the TODO list progress for a given employee ID
using the jsonplaceholder API.
"""
import json
import sys
import urllib.request

def get_employee_todo_progress(employee_id):
    """
    Fetch the TODO list progress for the given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # API endpoint
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch data from the API
    with urllib.request.urlopen(url) as response:
        todos = json.load(response)

    # Count completed and total tasks
    completed_tasks = sum(1 for task in todos if task['completed'])
    total_tasks = len(todos)

    # Get the employee's name
    employee_name = next(user['name'] for user in todos if user['id'] == employee_id)

    # Display the output
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todos:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)