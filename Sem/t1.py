import random


def fill_file(name, count_lines):
    with open(name, 'a', encoding='UTF-8') as f:
        for i in range(count_lines):
            print(f'{random.randint(-1000, 1000)}|{random.uniform(-1000, 1000)}',file=f)

fill_file('1.txt', 10)
