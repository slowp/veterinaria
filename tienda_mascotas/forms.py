from django import forms
from tienda_mascotas.models import Animal, Cliente, Adopcion


class Animal_form(forms.ModelForm):

	class Meta:
		model = Animal
		
		fields = [
			'nombre',
			'edad',
			'fecha_ingreso',
		]
		labels = {
			'nombre': 'Nombre',
			'edad': 'Edad aproximada',
			'fecha_ingreso': 'Fecha de Ingreso',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'edad': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_ingreso': forms.TextInput(attrs={'class':'form-control'}),
		}

class Cliente_form(forms.ModelForm):

	class Meta:
		model = Cliente
		
		fields = [
			'documento',
			'nombre',
			'fecha_nacimiento',
		]
		labels = {
			'documento': 'Cedula:',
			'nombre': 'Nombre',
			'fecha_nacimiento': 'Fecha de nacimiento',
		}
		widgets = {
			'documento': forms.TextInput(attrs={'class':'form-control'}),
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
		}


class Adopcion_form(forms.ModelForm):

	class Meta:
		model = Adopcion
		
		fields = [
			'cliente',
			'animal',
			'fecha',
		]
		labels = {
			'cliente': 'Cliente:',
			'animal': 'Animal',
			'fecha': 'Fecha de entrega',
		}
		widgets = {
			'cliente': forms.Select(attrs={'class':'form-control'}),
			'animal': forms.Select(attrs={'class':'form-control'}),
			'fecha': forms.TextInput(attrs={'class':'form-control'}),
		}