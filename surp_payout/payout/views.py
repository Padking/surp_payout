from django.shortcuts import render
from django.http import HttpResponse

from .forms import PayoutForm
from .models import Person, Payout

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
        about_person = Person.objects.get(pk=person_id)
        person_form = PayoutForm()
        d = {
            "form": person_form,
            "person": about_person,
            }
        return render(request, "person.html", context=d)