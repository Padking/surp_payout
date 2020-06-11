from django import forms


class PayoutForm(forms.Form):
    amount_payout = forms.FloatField(
                                    label="Сумма выплаты",
                                    help_text="сумма не должна превышать \
                                    баланс")
    amount_num = forms.CharField(
                                label="Номер счёта", 
                                max_length=30, required=False)
