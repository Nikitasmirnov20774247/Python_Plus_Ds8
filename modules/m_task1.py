# ✔ Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# ✔ Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# ✔ Имена пишите с большой буквы.
# ✔ Каждую пару сохраняйте с новой строки.


import json


def func(name1):
    name2 = 'res.json'

    with open(name1, encoding='UTF-8') as f1, \
            open(name2, 'w', encoding='UTF-8') as f2:
        for line in f1:
            print(json.dumps(line.strip().capitalize()), file=f2)

if __name__ == '__main__':
    func('3.txt')
