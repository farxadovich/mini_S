from django.contrib import admin
from .models import Toifa, Mahsulot


# admin.site.register(Mahsulot)
# admin.site.register(Toifa)

class ToifaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi',)



class MahsulotAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomi', 'narx', 'soni',)


admin.site.register(Toifa, ToifaAdmin)
admin.site.register(Mahsulot, MahsulotAdmin)