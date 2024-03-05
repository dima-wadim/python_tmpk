
from django.contrib import admin

# Register your models here.
from tmpk.models import Dog, Adres, Prase, Many


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('namb', 'name', 'fase',)
    list_filter = ('namb',)


@admin.register(Adres)
class AdresAdmin(admin.ModelAdmin):
    list_display = ('sity', 'strit',)
    list_filter = ('sity','strit',)


@admin.register(Prase)
class PraseAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost',)

@admin.register(Many)
class ManyAdmin(admin.ModelAdmin):
    list_display = ('man', 'data_op',)
    list_filter = ('data_op',)