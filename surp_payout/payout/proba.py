from django.conf import settings
# from surp_payout import settings
# settings.configure(settings)

# import os

# os.environ['DJANGO_SETTINGS_MODULE'] = 'payout.settings'


from models import Person, Payment

from random import choice, randint, randrange

from names import get_first_name, get_last_name


def random_telephone():

    country_code = randint(1, 9)
    first = randint(100, 999)
    second = randint(100, 999)
    last = randint(1, 9999)
    return f"{country_code}{first}{second}{last}"

def generate_user(rate=0.3):

    domains = ['@yandex.com','@outlook.com','@protonmail.com', '@gmail.com', '@yahoo.eu']
    random_cities = ['newyork', 'london', 'paris', 'madrid', 'berlin']
    year = randrange(80,106)
    first_name = get_first_name()
    last_name = get_last_name()
    addition = str(year) if year < 100 else ('_' + choice(random_cities))
    email = f"{first_name.lower()}{last_name.lower()}{addition}{choice(domains)}"
    tel_num = random_telephone()
    amount_payable = randrange(100, 10000, 100)  # сумма платежа начинается со 100 единиц
    balance = rate*amount_payable
    person_record = {'email': email, 'tel_num': tel_num, 'first_name': first_name,
                    'last_name': last_name, 'balance': balance}
    payment_record = {"amount_payable": amount_payable}
    return person_record, payment_record


def fill_in_tables(num_records=1):
    for _ in range(num_records):
        person_rec, payment_rec = generate_user()
        p_1 = Person.objects.create(**person_rec)
        pay = Payment(**payment_rec)
        p_1.payment_set.add(pay, bulk=False)


# fill_in_tables()