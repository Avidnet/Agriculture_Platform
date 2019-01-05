from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from request.api.views.request_to_platform import *

# Create your views here.


@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    print("in login")
    data = request.POST
    print(data)

    uname = data.get("username")
    pwd = data.get("password")
    rem = data.get("remember")

    print(uname, pwd, rem)

    if uname and pwd:
        auth = Auth()
        response = auth.login(uname, pwd, rem)
        return JsonResponse(response, status=200, safe=False)

    else:
        print("no")


@csrf_exempt
@require_http_methods(['POST'])
def refresh(request):
    print("in refresh")
    data = request.POST
    print(data)

    acc = data.get('access_token', "no acc")
    ref = data.get('refresh_token', "no ref")

    print(acc, ref)

    if acc != 'no acc' and ref != "no ref":

        print("in auth")

        auth = Auth()
        response = auth.refresh(acc, ref)
        print(response)

        return JsonResponse(response, status=200, safe=False)

    else:
        print("no")


@csrf_exempt
@require_http_methods(['GET'])
def projects(request):
    print("in refresh")
    data = request.GET
    print(data)

    token = data.get('token', "no token")

    print(token)

    if token != 'no token':

        print("in auth")

        auth = Projects(token)
        response = auth.get_projects()
        print(response)

        return JsonResponse(response, status=200, safe=False)

    else:
        print("no")
