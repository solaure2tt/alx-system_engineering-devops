#!/usr/bin/python3
""" script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress.
"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    us = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    csvfile = "{}.csv".format(sys.argv[1])
    with open(csvfile, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        idu = sys.argv[1]
        username = us.get("username")
        [writer.writerow(
            [idu, username, t.get("completed"), t.get("title")]
         ) for t in todos]
