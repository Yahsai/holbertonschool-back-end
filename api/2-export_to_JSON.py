#!/usr/bin/python3
import requests
import sys
import json

def fetch_and_export_todo_list(employee_id):
    # URL for the REST API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Fetching data from the API
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code != 200:
        print("Failed to fetch TODO list progress.")
        return
    
    todos = response.json()
    
    # Extracting employee name
    employee_name = todos[0]['name'].split()[0]
    
    # Creating list of tasks
    tasks = []
    for todo in todos:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": employee_name
        }
        tasks.append(task_info)
    
    # Writing data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as f:
        json.dump({str(employee_id): tasks}, f, indent=4)
    
    print(f"Data exported to {filename} successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    fetch_and_export_todo_list(employee_id)
