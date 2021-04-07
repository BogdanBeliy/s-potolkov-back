from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ['name', 'descr']


admin.site.register(Testimonials)
admin.site.register(Gallery)
admin.site.register(NewClient)
admin.site.register(NewSalePotolok)
