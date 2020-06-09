from django import forms
 
class PayoutForm(forms.Form):
    amount_payout = forms.CharField(max_length=30)
    amount_num = forms.FloatField()