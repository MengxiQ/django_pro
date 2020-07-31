import django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login(request):
    response = render(request, 'login.html')
    return HttpResponse(response)


def signin(request):
    name = request.POST.get("name")
    password = request.POST.get("password")
    print(name,password)
    user = authenticate(username=name, password=password)
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                # login函数和本地函数重名所以写了全路径
                django.contrib.auth.login(request, user)
                request.session['usertype'] = 'mgr'
                request.session['name'] = name

                return JsonResponse({'ret':1,'msg': '登录成功'})
            else:
                # 用户不是超级管理员
                return JsonResponse({'ret':0,'msg': '用户不是超级管理员'})
        else:
            # 用户被禁用
            return JsonResponse({'ret':0,'msg': '用户被禁用'})
        # 用户名或者密码错误
    else:
        return JsonResponse({'ret':0,'msg': '用户名或者密码错误'})

def signout(request):
    logout(request)
    return HttpResponseRedirect('/login')

def index(request):
    name = request.session['name']
    # print(name)
    return HttpResponse(render(request, 'index.html', context={'name': name}))