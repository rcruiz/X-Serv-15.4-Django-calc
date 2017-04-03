from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound



# Create your views here.
#def say_main(request):
#    return HttpResponse('<h1>Calculadora Django</h1>')
def suma(request, num1, suma, num2):
    return HttpResponse('La suma es ' + str(int(num1) + int(num2)))


def resta(request, num1, resta, num2):
    return HttpResponse('La resta es ' + str(int(num1) - int(num2)))


def multiplica(request, num1, mult, num2):
    return HttpResponse('El producto es ' + str(int(num1) * int(num2)))


def divide(request, num1, div, num2):
    try:
        return HttpResponse('El cociente es ' + str(int(num1) / int(num2)))
    except ZeroDivisionError:
        return HttpResponse('No se puede dividir entre 0')


def el404(request):
    return HttpResponseNotFound('Error 404: Recursos introducidos inválidos.')
