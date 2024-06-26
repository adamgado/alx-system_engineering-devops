#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    e_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(e_id)).json()
    name = employee.get("username")
    todo = requests.get(url + "todos", params={"userId": e_id}).json()

    with open("{}.csv".format(e_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [e_id, name, a.get("completed"), a.get("title")]
         ) for a in todo]
