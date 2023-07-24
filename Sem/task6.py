# ✔ Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# ✔ Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# ✔ Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.


import pickle
import csv


def pickle_to_csv(file_name):

    with open(file_name, 'rb') as f:
        new_dict = pickle.load(f)
    print(new_dict)
    with open('res3.csv', 'w', newline='', encoding='UTF-8') as f2:

        rows = []
        for personal_id, value in new_dict.items():
            level, name = value
            rows.append({'id': int(personal_id), 'level': int(level), 'name': name})
            
        csv_write = csv.DictWriter(f2, fieldnames=['id', 'level', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)

pickle_to_csv('res3.pickle')
