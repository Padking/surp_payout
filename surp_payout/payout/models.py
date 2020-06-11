<<<<<<< HEAD
from django.db import models

# from .. import payout
# from utils import generate_user
# import surp_payout.surp_payout.payout.utils
# from payout import utils
# import surp_payout.payout
# import payout.utils
# from surp_payout import utils
# from .payout import utils

from . import utils

class Person(models.Model):
    email = models.EmailField(max_length=254, blank=False)  # , primary_key=True
=======
from django.core.validators import MinValueValidator
from django.db import models

# from . import utils


class Person(models.Model):
    email = models.EmailField(max_length=254, blank=False)
>>>>>>> Начальный коммит
    tel_num = models.PositiveIntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    balance = models.FloatField(default=0)
<<<<<<< HEAD
    
    def __str__(self):
        return self.email

class Payment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount_payable = models.FloatField()  # сделать неотрицательным
    payment_date = models.DateTimeField(auto_now=True)  # присмотреться к аргументу

    # def __str__(self):
    #     return self.
=======

    def __str__(self):
        return self.email


class Payment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount_payable = models.FloatField(validators=[MinValueValidator(0.9)])
    payment_date = models.DateTimeField(auto_now_add=True)

>>>>>>> Начальный коммит

class Payout(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    amount_payout = models.FloatField()
<<<<<<< HEAD
    bid_date = models.DateTimeField(auto_now=True)  # создание заявки
    payout_date = models.DateTimeField(auto_now=True)
    payout_status = models.BooleanField(default=False)
    amount_num = models.CharField(max_length=30, blank=True)


# 2-й способ создания записей в главной и зависимой таблицах - работает
# for _ in range(2):  # изменить на 100
#     person_rec, payment_rec = utils.generate_user()
#     p_1 = Person.objects.create(**person_rec)  # создаём запись для главной таблицы БД
#     pay = Payment(**payment_rec)  # создаём запись для зависимой таблицы БД
#     p_1.payment_set.add(pay, bulk=False)  # устанавливаем связь между записями
=======
    bid_date = models.DateTimeField(auto_now_add=True)
    payout_date = models.DateTimeField(blank=True, null=True)
    payout_status = models.BooleanField(default=False)
    amount_num = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f"Пользователь № {self.person_id}"

def fill_in_tables(num_records=100):
    """Наполняет таблицы БД записями"""
    for _ in range(num_records):
        person_rec, payment_rec = utils.generate_user()
        p_1 = Person.objects.create(**person_rec)
        pay = Payment(**payment_rec)
        p_1.payment_set.add(pay, bulk=False)


# fill_in_tables()
>>>>>>> Начальный коммит
