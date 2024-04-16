#!/usr/bin/python3
"""
This script fetches the TODO list progress for a given employee ID
and exports the data to a JSON file.
"""
import json
import sys
import urllib.request

def get_employee_todo_progress(employee_id):
    """
    Fetch the TODO list progress for the given employee ID and export it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # API endpoint
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch data from the API
    try:
        with urllib.request.urlopen(url) as response:
            todos = json.load(response)
    except urllib.error.HTTPError:
        print(f"No user found with ID {employee_id}")
        return

    # Get the employee's name
    try:
        employee_name = next(user['name'] for user in todos if user['id'] == employee_id)
    except StopIteration:
        employee_name = f"Employee {employee_id}"

    # Export the data to a JSON file
    data = {
        str(employee_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            for task in todos
        ]
    }

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    print(f"JSON file '{employee_id}.json' created successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)