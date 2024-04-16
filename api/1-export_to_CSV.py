#!/usr/bin/python3
"""
This script exports tasks data of a given user to a CSV file.
"""

import csv
import sys
import requests

def export_tasks_to_csv(user_id):
    """
    Fetches tasks data of the given user ID and exports it to a CSV file.

    Args:
        user_id (int): The ID of the user whose tasks are to be exported.
    """
    # Fetch user data
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user_data = response.json()
    username = user_data.get('username')

    # Fetch tasks data
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    tasks_data = response.json()

    # Write tasks data to CSV
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks_data:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_tasks_to_csv(user_id)
