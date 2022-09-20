from django.db import models

# Create your models here.

class Clientes(models.Model):
	nombre = models.CharField(max_length = 30)
	direcciion = models.CharField(max_length = 50)
	email = models.EmailField()
	telefono = models.CharField(max_length = 7)

	def __str__(self):
		return 'Nombre: %s, Direccion: %s, Email: %s, Telefono: %s' %(self.nombre, self.direcciion, self.email, self.telefono)



class Articulos(models.Model):
	nombre = models.CharField(max_length = 30)
	seccion = models.CharField(max_length = 20)
	precio = models.IntegerField()

	def __str__(self):
		return 'Nombre: %s, Seccion: %s, Precio: %s' %(self.nombre, self.seccion, self.precio)


class Pedidos(models.Model):
	numero = models.IntegerField()
	fecha = models.DateField()
	entregado = models.BooleanField()

	def __str__(self):
		return 'Numero: %s, Fecha: %s, Entregado: %s' %(self.numero, self.fecha, self.entregado)

