from django.contrib import admin
from . import models

# Register your models here.


admin.site.register(models.Order, verbose_name="Pedido")
admin.site.register(models.Ordersitem, verbose_name="Item pedido")
