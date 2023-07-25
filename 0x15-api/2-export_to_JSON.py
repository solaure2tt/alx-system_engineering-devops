#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
    return json file about his/her TODO list progress.
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    f = sys.argv[1] + ".json"
    tod = {}
    res = []
    idu = "" + sys.argv[1]
    for t in todos:
        username = us.get("name")
        cpl = t.get("completed")
        title = t.get("title")
        tod["task"] = title
        tod["completed"] = cpl
        tod["username"] = username
        res.append(tod)
    j = {}
    j["" + idu] = res
    js = json.dumps(j)
    with open(f, "w") as file:
        file.write(js)
