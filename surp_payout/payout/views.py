from datetime import datetime
import re
import requests

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from .forms import PayoutForm
from .models import Person, Payout

<<<<<<< HEAD
def index(request):
    return HttpResponse("Hello world")


def persons(request, person_id):
    # output = "<h2>User № {0} </h2>".format(person_id)
    # return HttpResponse(output)
    if request.method == "POST":
        # amount_payout = request.POST.get("amount_payout")  # получаю содержимое полей html-формы
        # amount_num = request.POST.get("amount_num")
        # print(f"Желаемый размер выплаты пользователю для занесения в БД {amount_payout}")
        # print(f"Счёт на который подлежит отправка: {amount_num}")
        payout = Payout()
        payout.person_id = person_id
        payout.amount_payout = request.POST.get("amount_payout")
        payout.amount_num = request.POST.get("amount_num")
        payout.save()
        """
        Здесь выполнить переадресацию в корень сайта
        """
    else:  # путешественник хочет получить инфу о своём балансе (GET)
=======

def index(request):
    return HttpResponse("Корень приложения")


def persons(request, person_id):
    if request.method == "POST":  # пользователь запрашивает выплату
        data = request.POST.get("amount_payout")
        person = Person.objects.get(pk=person_id)
        if float(data) > person.balance:
            return HttpResponse("Сумма выплаты превышает баланс! \
                                Выполните повторный запрос")
        person_form = PayoutForm(request.POST)
        if person_form.is_valid():
            payout = Payout()
            payout.person_id = person_id
            payout.amount_payout = request.POST.get("amount_payout")
            payout.amount_num = request.POST.get("amount_num")
            payout.save()
            return HttpResponse("Запрос на выплату принят")
        else:  # пользователь ввёл невалидные данные
            return HttpResponse("Неверные данные")
    else:  # пользователь хочет получить состояние своего баланса
>>>>>>> Начальный коммит
        about_person = Person.objects.get(pk=person_id)
        person_form = PayoutForm()
        d = {
            "form": person_form,
            "person": about_person,
            }
<<<<<<< HEAD
        return render(request, "person.html", context=d)
=======
        return render(request, "person.html", context=d)


def action_func(
    request,
    url_for_webhook="https://webhook.site/b259ed73-a646-4832-bf4f-d1690992956b",
    url_for_redirect="http://127.0.0.1:8000/admin/payout/payout/"):
    
    url_to_get_pk = request.build_absolute_uri()
    regex_result = "{}".format(*re.findall('/\d+/', url_to_get_pk))
    payout_id = regex_result.strip("/")
    payout = Payout.objects.get(pk=payout_id)
    if payout.payout_status is True:
        return HttpResponseRedirect(url_for_redirect)
    else:  # заявка на выплату не обработана
        payout.person.balance -= payout.amount_payout
        payout.payout_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payout.payout_status = True
        payout.person.save()
        payout.save()
        if payout.amount_num:  # указан счёт для выплаты
            data = {
                "account": payout.amount_num,
                "amount": payout.amount_payout,
            }
            r = requests.post(url_for_webhook, data=data)
            return HttpResponseRedirect(url_for_redirect)
        else:
            return HttpResponseRedirect(url_for_redirect)
>>>>>>> Начальный коммит
