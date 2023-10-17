from django.contrib import admin
from tienda.models import HistorialCompra, Carrito

# Register your models here.
class HistorialCompraAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')

class CarritoAdmin(admin.ModelAdmin):

    readonly_fields = ('created', 'updated')


admin.site.register(HistorialCompra, HistorialCompraAdmin)
admin.site.register(Carrito, CarritoAdmin)