# ✔ Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# ✔ Распечатайте его как pickle строку.


import pickle


def csv_to_picklestring(file_name):
    data = {}
    with open(file_name, encoding='UTF-8') as f:
        for line in f.readlines():
            access_id, level, name = line.strip().split()
            data[access_id] = [level, name]
        res = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')

if __name__ == '__main__':
    csv_to_picklestring('res3.csv')
