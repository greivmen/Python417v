import csv
import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# print(todos)

with open('dz_p25.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for d in todos:
        writer.writerow(d)


