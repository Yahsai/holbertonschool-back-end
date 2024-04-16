#!/usr/bin/python3
import json
import requests

ROOT_URL = "https://jsonplaceholder.typicode.com/"

TODOS = requests.get(f'{ROOT_URL}todos/').json()
USERNAMES = requests.get(f'{ROOT_URL}users/').json()

if __name__ == "__main__":
    from sys import argv

    USER_ID = int(argv[1])

    USERNAME = USERNAMES[USER_ID - 1]['username']
    USER_TASKS = tuple(
        task
        for task in TODOS
        if task['userId'] == USER_ID
    )

    result = {
        str(USER_ID): [
            {
                'task': task['title'],
                'completed': task['completed'],
                'username': USERNAME
            } for task in USER_TASKS
        ]
    }

    with open(f'{USER_ID}.json', "w") as output_file:
        json.dump(result, output_file)