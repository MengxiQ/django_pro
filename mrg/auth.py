from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

def auth(request):
    if 'usertype' not in request.session:
        return HttpResponse(render(request, 'login.html', context={'msg': '请先登录！'}))
    elif request.session['usertype'] != 'mgr' :
        return HttpResponse(render(request, 'login.html', context={'msg': '用户非mgr类型'}))
    else:
        return True