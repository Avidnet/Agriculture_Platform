from django.http import JsonResponse


def login_required(func):
    def wrapper(request, *args, **kwargs):
        print(request.user)
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return JsonResponse({"message": "you are not authenticated"}, status=401)

    return wrapper
