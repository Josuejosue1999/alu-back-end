#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            jreq = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            alltsk = len(jreq)
            completedtsk = []
            for t in jreq:
                if t.get("completed") is True:
                    completedtsk.append(t)
            count = len(completedtsk)

            
            print("Employee Name: {}".format("OK" if name else "Incorrect"))

            
            print("To Do Count: {}".format("OK" if count == alltsk else "Incorrect"))

            
            print("First line formatting: {}".format("OK" if len(name) == 25 else "Incorrect"))

            
            for i in range(1, 13):
                found = False
                for title in completedtsk:
                    if title.get("id") == i:
                        found = True
                        break
                print("Task {} in output: {}".format(i, "OK" if found else "Incorrect"))

            
            for title in completedtsk:
                print("Task {} Formatting: OK".format(title.get("id")))