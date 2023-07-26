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
    iduser = sys.argv[1]
    with open("{}.json".format(iduser), "w") as jsonfile:
        json.dump({iduser: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": us.get("username")
            } for t in todos]}, jsonfile)
