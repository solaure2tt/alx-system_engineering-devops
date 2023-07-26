#!/usr/bin/python3
"""return json file about all TODO list of all users.
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    f = "todo_all_employees.json"
    with open(f, "w") as file:
        json.dump({
            us.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": us.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": us.get("id")}).json()]
            for us in users}, file)
