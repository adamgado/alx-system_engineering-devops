#!/usr/bin/python3
"""returns information about employee TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    tasks_done = [a.get("title") for a in todo if a.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(tasks_done), len(todo)))
    [print("\t {}".format(a)) for b in tasks_done]
