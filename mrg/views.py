from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from mrg.models import *
from mrg.auth import auth
import json


# Create your views here.

# 顾客列表
def listcustomer(request):
    if auth(request):
        qs = Customer.objects.values()
        data = list(qs)
        return HttpResponse(render(request, 'customer-list.html', context={'data': data}))


def customer_add(request):
    if auth(request):
        return HttpResponse(render(request, 'customer-add.html'))


def customer_modify(request):
    if auth(request):
        id = request.GET.get('id')
        print(id)
        customer = Customer.objects.get(id=id)
        return HttpResponse(render(request, 'customer-edit.html', context={'name': customer.name,
                                                                            'phone': customer.phone,
                                                                            'address': customer.address,
                                                                            'id':id
                                                                           }))


# 药品列表

def medicine_list(request):
    if auth(request):
        qs = Medicine.objects.values()
        data = list(qs)
        return HttpResponse(render(request, 'medicine-list.html', context={'data': data}))


def medicine_add(request):
    if auth(request):
        return HttpResponse(render(request, 'medicine-add.html'))


# def medicine_modify(request):
#     if auth(request):
#         id = request.GET.get('id')
#         print(id)
#         customer = Medicine.objects.get(id=id)
#         return HttpResponse(render(request, 'customer-edit.html', context={'name': customer.name,
#                                                                             'phone': customer.phone,
#                                                                             'address': customer.address,
#                                                                             'id':id
#                                                                            }))

