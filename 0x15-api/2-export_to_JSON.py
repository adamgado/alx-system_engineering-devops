#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
import sys

if __name__ == "__main__":
    e_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(e_id)).json()
    name = employee.get("username")
    todo = requests.get(url + "todos", params={"userId": e_id}).json()

    with open("{}.json".format(e_id), "w") as jsonfile:
        json.dump({e_id: [{
                "task": a.get("title"),
                "completed": a.get("completed"),
                "username": name
            } for a in todo]}, jsonfile)
