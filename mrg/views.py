from django.shortcuts import render
from django.http import HttpResponse
from mrg.models import Customer
# Create your views here.

def listcustomer(request):
    qs = Customer.objects.values()
    data = list(qs)
    print(data)
    return HttpResponse(render(request,'listcustomer.html',context={'data':data}))