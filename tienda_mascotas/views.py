from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from tienda_mascotas.models import Animal, Cliente, Adopcion
from tienda_mascotas.forms import Animal_form, Cliente_form, Adopcion_form

# Create your views here.
def index(request):
	return render(request, "tienda/index.html")

def animal_add(request):
	if request.method == 'POST':
		form = Animal_form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('tienda:list_a')
	else:
		form = Animal_form()

	return render(request, 'tienda/form_animal_add.html', {'form':form})

def cliente_add(request):
	if request.method == 'POST':
		form = Cliente_form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('tienda:list_c')
	else:
		form = Cliente_form()

	return render(request, 'tienda/form_cliente_add.html', {'form':form})

def adopcion_add(request):
	if request.method == 'POST':
		form = Adopcion_form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('tienda:list_c')
	else:
		form = Adopcion_form()

	return render(request, 'tienda/form_adopcion_add.html', {'form':form})

def animal_edit(request, id_animal):
	animal = Animal.objects.get(id=id_animal)
	if request.method == "GET":
		form = Animal_form(instance=animal)
	else:
		form = Animal_form(request.POST, instance=animal)
		if form.is_valid():
			form.save()
		return redirect('tienda:list_a')
	return render(request, 'tienda/form_animal_add.html', {'form':form})

def animal_delete(request, id_animal):
	animal = Animal.objects.get(id=id_animal)
	if request.method == "POST":
		animal.delete()
		return redirect('tienda:list_a')
	return render(request, 'tienda/animal_delete.html', {'animal':animal})

def cliente_edit(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	if request.method == "GET":
		form = Cliente_form(instance=cliente)
	else:
		form = Cliente_form(request.POST, instance=cliente)
		if form.is_valid():
			form.save()
		return redirect('tienda:list_c')
	return render(request, 'tienda/form_cliente_add.html', {'form':form})

def cliente_delete(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	if request.method == "POST":
		cliente.delete()
		return redirect('tienda:list_c')
	return render(request, 'tienda/cliente_delete.html', {'cliente':cliente})

class Animal_list(ListView):
	model = Animal
	template_name = 'tienda/animal_list.html'

class Cliente_list(ListView):
	model = Cliente
	template_name = 'tienda/cliente_list.html'

class Adopcion_list(ListView):
	model = Adopcion
	template_name = 'tienda/adopcion_list.html'

