#!/usr/bin/python3
"""export to csv"""

import json
from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    csv = get('https://jsonplaceholder.typicode.com/todos/')
    final = csv.json()

    table = []
    csv2 = get('https://jsonplaceholder.typicode.com/users/')
    final2 = csv2.json()

    for i in final2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        copy = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in final:
            table = []
            if i['userId'] == int(argv[1]):
                table.append(i['userId'])
                table.append(employee)
                table.append(i['completed'])
                table.append(i['title'])

                copy.writetable(table)