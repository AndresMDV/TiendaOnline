from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos


class ClientesAdmin(admin.ModelAdmin):
	list_display=("nombre", "direccion", "telefono")
	search_fields = ("nombre",)


class ArticulosAdmin(admin.ModelAdmin):
	list_display=("nombre", "seccion", "precio")
	search_fields = ("nombre",)
	list_filter=("seccion","precio",)

class PedidosAdmin(admin.ModelAdmin):
	list_display=("numero", "fecha", "entregado")
	search_fields = ("numero",)
	list_filter=("fecha", "entregado",)
	date_hierarchy = "fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)

