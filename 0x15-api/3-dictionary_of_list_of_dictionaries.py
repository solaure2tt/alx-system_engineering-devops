#!/usr/bin/python3
"""return json file about all TODO list of all users.
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users/").json()
    f = "todo_all_employees.json"
    j = {}
    for us in users:
        todos = requests.get(url + "todos",
                             params={"userId": us.get("id")}).json()
        tod = {}
        res = []
        idu = us.get("id")
        for t in todos:
            username = us.get("username")
            cpl = t.get("completed")
            title = t.get("title")
            tod["task"] = title
            tod["completed"] = cpl
            tod["username"] = username
            res.append(tod)
        j[idu] = res
    js = json.dumps(j)
    with open(f, "w") as file:
        file.write(js)
