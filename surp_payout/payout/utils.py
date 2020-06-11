<<<<<<< HEAD
import random
=======
>>>>>>> Начальный коммит
from random import choice, randint, randrange

from names import get_first_name, get_last_name


def random_telephone():
    """ Создаёт номер телефона пользователя в формате мобильного"""
<<<<<<< HEAD
    country_code = randint(1,9)
    first = random. randint(100, 999)
    second = random. randint(100, 999)
    last = random. randint(1, 9999)
    return f"{country_code}{first}{second}{last}"

=======
    country_code = randint(1, 9)
    first = randint(100, 999)
    second = randint(100, 999)
    last = randint(1, 9999)
    return f"{country_code}{first}{second}{last}"


>>>>>>> Начальный коммит
def generate_user(rate=0.3):
    """
    Формирует записи для таблиц БД

    :param rate: доля от суммы платежа
    """
<<<<<<< HEAD
    domains = ['@yandex.com','@outlook.com','@protonmail.com', '@gmail.com', '@yahoo.eu']
    random_cities = ['newyork', 'london', 'paris', 'madrid', 'berlin']
    year = randrange(80,106)
=======
    domains = ['@yandex.com', '@outlook.com', '@protonmail.com',
                '@gmail.com', '@yahoo.eu']
    random_cities = ['newyork', 'london', 'paris', 'madrid', 'berlin']
    year = randrange(80, 106)
>>>>>>> Начальный коммит
    first_name = get_first_name()
    last_name = get_last_name()
    addition = str(year) if year < 100 else ('_' + choice(random_cities))
    email = f"{first_name.lower()}{last_name.lower()}{addition}{choice(domains)}"
    tel_num = random_telephone()
    amount_payable = randrange(100, 10000, 100)
    balance = rate*amount_payable
<<<<<<< HEAD
    person_record = {'email': email, 'tel_num': tel_num, 'first_name': first_name,
                    'last_name': last_name, 'balance': balance}
    payment_record = {"amount_payable": amount_payable}
    return person_record, payment_record

# print(generate_user())

# def f(**kwargs):
#     print(kwargs)

# x = {'email': 'LindaWilliams_newyork@yandex.com', 'tel_num': '24281494445', 'first_name': 'Linda'}
# f(**x)

# print(get_first_name())
=======
    person_record = {'email': email, 'tel_num': tel_num, 
                    'first_name': first_name,
                    'last_name': last_name, 'balance': balance}
    payment_record = {"amount_payable": amount_payable}
    return person_record, payment_record
>>>>>>> Начальный коммит
