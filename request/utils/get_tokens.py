

def get_tokens(request):
    user = request.user
    token = {'access_token': user.access_token,
             'refresh_token': user.refresh_token}
    return token
