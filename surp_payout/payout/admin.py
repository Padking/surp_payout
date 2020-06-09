from django.contrib import admin

from .models import Person, Payment, Payout

# Register your models here.
admin.site.register(Person)
admin.site.register(Payment)
admin.site.register(Payout)
