from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

def curso(self):
    curso = Curso(nombre= 'Desarrollo Web', camada= '1111')

    curso.save()

    documento = f'El curso es: {curso.nombre}, la camada: {curso.camada}'

    return HttpResponse(documento)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def curos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')










