#!/usr/bin/python3

"""Script to export data in the JSON format"""

if __name__ == "__main__":
    import json
    import os
    import requests
    from sys import argv

    try:
        u_id = argv[1]
        api_url = f"https://jsonplaceholder.typicode.com/users/{u_id}"
        api_url2 = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"

        response = requests.get(api_url).json()
        EMPLOYEE_NAME = response.get('username')
        response = requests.get(api_url2).json()

        f_name = os.path.join(f"{u_id}.json")
        u_list = {u_id: [{"task": task["title"], "completed": task["completed"], "username": EMPLOYEE_NAME} for task in response]}

        with open(f_name, 'w', encoding='utf-8') as f:
            json.dump(u_list, f, indent=4)

        print(f"JSON file '{f_name}' created successfully.")
    except (IndexError, ValueError):
        print("Usage: python script.py <employee_id>")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

