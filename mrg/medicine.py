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
            return addMedicine(request)


# 服务
def addMedicine(request):
    name = request.POST.get('name')
    sn = request.POST.get('sn')
    desc = request.POST.get('desc')
    print(name, sn, desc)
    medicine = Medicine.objects.create(name=name,
                                       sn=sn,
                                       desc=desc
                                       )

    return JsonResponse({'ret': 1, 'id': medicine.id})

