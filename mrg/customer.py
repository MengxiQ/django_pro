from django.http import HttpResponse,JsonResponse
from mrg.views import *
import json
def dispatcher(request):
    if 'usertype' not in request.session:
        return HttpResponse(render(request, 'login.html', context={'msg': '请先登录！'}))
    elif request.session['usertype'] != 'mgr' :
        return HttpResponse(render(request, 'login.html', context={'msg': '用户非mgr类型'}))
    else:
        if request.method == 'POST':
            return addCustomer(request)
        if request.method == 'DELETE':
            return delCustomer(request)
        if request.method == 'PUT':
            return modifyCustomer(request)


# 服务
def addCustomer(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    print(name, phone, address)
    record = Customer.objects.create(name=name,
                                     phone=phone,
                                     address=address
                                     )
    return JsonResponse({'ret': 1, 'id': record.id})


# put和delete需要从请求体获取
def delCustomer(request):
    data = json.loads(request.body.decode('utf-8'))
    id = data['id']
    try:
        record = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return {'ret': 0, 'msg': f"id为{id}的客户不存在！"}

    record.delete()
    return JsonResponse({'ret': 1, 'id': id})


def modifyCustomer(request):
    data = json.loads(request.body.decode('utf-8'))
    id = data['id']
    try:
        record = Customer.objects.get(id=id)
    except Customer.DoesNotExist:
        return JsonResponse({'ret': 0, 'msg': f"id为{id}的客户不存在！"})

    if 'name' in data:
        record.name = data['name']
    if 'phone' in data:
        record.phone = data['phone']
    if 'address' in data:
        record.address = data['address']
    record.save()
    return JsonResponse({'ret': 1, 'id': id})
