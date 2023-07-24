# ✔ Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# ✔ После каждого ввода добавляйте новую информацию в
# JSON файл.
# ✔ Пользователи группируются по уровню доступа.
# ✔ Идентификатор пользователя выступает ключём для имени.
# ✔ Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# ✔ При перезапуске функции уже записанные в файл данные
# должны сохраняться.


import json


def add_to_base():
    name1 = 'res2.json'

    try:    
        with open(name1, 'r', encoding='UTF-8') as f:
            data = json.load(f)
    except:
        data = {}

    while True:
        name = input('Введите имя: ')
        try:
            access_code = int(input('Введите уровень доступа от 1 до 7: '))
        except:
            continue
        if not 1 <= access_code <= 7:
            continue
        try:
            personal_id = int(input('Введите id: '))
        except:
            continue
        if personal_id in data:
            continue
        break

    data[personal_id] = [name, access_code]
    with open(name1, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii=False)

if __name__ == '__main__':
    add_to_base()
