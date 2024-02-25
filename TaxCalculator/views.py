from django.shortcuts import render
from django.http import HttpResponse

tax_rate = 0.15

def Defaultpath(request):
    return render(request,'TaxCalculator/DefaultPath.html')

def anyNumber(request, price):
    price = float(price)
    total_price = price * (1 + tax_rate)
    context = {'price': price, 'total_price': total_price}
    return render(request, 'TaxCalculator/anyNumber.html', context)
   

def taxrate(request):
    context = {'tax_rate': tax_rate}
    return render(request, 'TaxCalculator/taxrate.html', context)