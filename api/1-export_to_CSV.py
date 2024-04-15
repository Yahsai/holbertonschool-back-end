#!/usr/bin/python3
"""
This script fetches the TODO list progress for a given employee ID
and exports the data to a CSV file.
"""
import csv
import json
import sys
import urllib.request

def get_employee_todo_progress(employee_id):
    """
    Fetch the TODO list progress for the given employee ID and export it to a CSV file.

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

    # Export the data to a CSV file
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos:
            writer.writerow([
                task["userId"],
                employee_name,
                str(task["completed"]),
                task["title"]
            ])

    print(f"CSV file '{employee_id}.csv' created successfully.")

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
