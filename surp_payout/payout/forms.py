from django import forms
<<<<<<< HEAD
 
class PayoutForm(forms.Form):
    amount_payout = forms.CharField(max_length=30)
    amount_num = forms.FloatField()
=======


class PayoutForm(forms.Form):
    amount_payout = forms.FloatField(
                                    label="Сумма выплаты",
                                    help_text="сумма не должна превышать \
                                    баланс")
    amount_num = forms.CharField(
                                label="Номер счёта", 
                                max_length=30, required=False)
>>>>>>> Начальный коммит
