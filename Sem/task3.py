# ✔ Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.


import json
import csv


def json_to_csv(name):

    with open(name, encoding='UTF-8') as f1, \
            open('res3.csv', 'w', newline='', encoding='UTF-8') as f2:
                data = json.load(f1)
                rows = []

                for personal_id, value in data.items():
                    name, level = value
                    rows.append({'level': int(level), 'id': int(personal_id), 'name': name})

                csv_write = csv.DictWriter(f2, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
                csv_write.writeheader()
                csv_write.writerows(rows)

json_to_csv('res2.json')
