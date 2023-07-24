# ✔ Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.


import json
import pickle
import os
from os import listdir
from os.path import isfile, join


def json_to_pickle():
    onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    # print(onlyfiles)

    for file in onlyfiles:
        if file.split('.')[-1] == 'json':
            print(file)
            new_name = file.split('.')[0]
            pickle_file_name = new_name + '.pickle'
            print(pickle_file_name)
            with open(file, 'r', encoding='UTF-8') as f1:
                with open(pickle_file_name, 'wb') as f2:
                    data = json.load(f1)
                    print(data)
                    pickle.dump(data, f2)

json_to_pickle()
