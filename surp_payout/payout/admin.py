from django.contrib import admin

from .models import Person, Payment, Payout

<<<<<<< HEAD
# Register your models here.
admin.site.register(Person)
admin.site.register(Payment)
admin.site.register(Payout)
=======

class MyModelAdmin(admin.ModelAdmin):
    change_form_template = "admin/payout/custom_change_form.html"


admin.site.register(Person)
admin.site.register(Payment)
admin.site.register(Payout, MyModelAdmin)
>>>>>>> Начальный коммит
