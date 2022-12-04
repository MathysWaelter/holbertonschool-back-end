#!/usr/bin/python3
"""given employee ID, returns information about his/her TODO list progress."""

import json
import requests
import sys

if __name__ == "__main__":
    """ALL MY VARIABLE"""
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    todostxt = todos.text
    userstxt = users.text
    todosjson = json.loads(todostxt)
    usersjson = json.loads(userstxt)
    Id = sys.argv[1]
    final = []
    finaltask = []
    NUMBER_OF_DONE_TASKS = 0
    taskleft = 0

    """FOR RETRIEVE TASK_ID"""
    for key in usersjson:
        if key['id'] == int(Id):
            EMPLOYEE_NAME = key['name']

    """FOR RETRIEVE USER_ID"""
    for value in todosjson:
        if value['userId'] == int(Id):
            final.append(value)

    for taskdone in final:
        if taskdone['completed'] is True:
            finaltask.append(taskdone['title'])
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1

    print("Employee {} is done with tasks({}/20)".format(EMPLOYEE_NAME,
                                                         NUMBER_OF_DONE_TASKS))

    for taskfinal in finaltask:
        print("\t {}".format(taskfinal))
