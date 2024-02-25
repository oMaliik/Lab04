from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 15

# Create your views here.
def default(request):
    return HttpResponse("this is a site to calculate tax.")


def anyNumber(request, number):
    n=number * 1.15
    return HttpResponse(f'Your total is {n}')


def taxRate(request):
    return render(request, "MyApp/tax_rate.html",{
        "rate": tax_rate
    })