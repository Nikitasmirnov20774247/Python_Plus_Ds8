import random


def fill_file(name, count_lines):
    with open(name, 'a', encoding='UTF-8') as f:
        for i in range(count_lines):
            lenght = random.randint(4, 7)
            check = True
            while check:
                password = ''
                for j in range(lenght):
                    tmp = chr(random.randint(97, 122))
                    password = password + tmp
                    if tmp in ['a', 'o', 'u', 'i', 'e']:
                        check = False

            print(password.capitalize(), file=f)

fill_file('2.txt', 10)
