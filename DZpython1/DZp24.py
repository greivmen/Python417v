import json
from random import choice


def gen_person():
    name = ""
    tel = ""

    letters = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'e', 'k', 'l', 'm', 'n']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def random_key():
    key = ""
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(key) != 10:
        key += choice(nums)
    return key


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    key = random_key()
    while key in data:
        key = random_key()

    data[key] = person_dict
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
