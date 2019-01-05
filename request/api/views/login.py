import json
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from .request_to_platform import Auth
from django.http import JsonResponse


def login(request):
    data = json.loads(request.body)
    if not data.get('username') or not data.get('password'):
        return JsonResponse({"message": "bad data"}, status=400)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return JsonResponse({"message": "user not found"}, status=404)
    else:
        user_login(request, user)
        print('sssss')
        auth = Auth()
        response = auth.login(username, password, False)
        access = response.get('access_token')
        refresh = response.get('refresh_token')
        user.access_token = access
        user.refresh_token = refresh
        user.save()
        return JsonResponse({"message": "ok"}, status=200)
