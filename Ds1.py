# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.


import os
import csv
import json
import pickle
from pathlib import Path
from sys import argv


def get_dir_size(path1='.'):
    result = 0

    with os.scandir(path1) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_dir_size(entry.path)

    return result


def get_size(path1='.'):
    if os.path.isfile(path1):
        return os.path.getsize(path1)
    elif os.path.isdir(path1):
        return get_dir_size(path1)


def direct_info(direct: Path, name: str):
    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_dir']
    rows = []

    with open(name + '.json', 'w') as f_json, \
            open(name + '.csv', 'w', newline='', encoding='utf-8') as f_csv, \
            open(name + '.pickle', 'wb') as f_pickle:
        
        for dir_path, dir_name, file_name in os.walk(direct):
            json_data.setdefault(dir_path, {})
            
            for dirs in dir_name:
                size = get_size(dir_path + '\\' + dirs)
                json_data[dir_path].update({dirs: {'size': size, 'file_or_dir': 'directory'}})
                rows.append({'name': dirs, 'path': dir_path, 'size': size, 'file_or_dir': 'directory'})
            
            for files in file_name:
                size = get_size(dir_path + '\\' + files)
                json_data[dir_path].update({files: {'size': size, 'file_or_dir': 'file'}})
                rows.append({'name': files, 'path': dir_path, 'size': size, 'file_or_dir': 'file'})

            print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')

        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(json_data)}', f_pickle)


def direct_info_run():
    try:
        if len(argv) == 2:
            print(argv)
            direct_info(Path(argv[1]), 'result')
        else:
            direct = os.getcwd()
            direct_info(Path(direct), 'result')
    except Exception as e:
        print(f'!! Введён некорректный путь до файла !!\n{e}')


if __name__ == '__main__':
    direct_info_run()
