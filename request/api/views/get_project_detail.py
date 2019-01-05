from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from request.api.views.request_to_platform import Projects
from request.utils import login_required, get_tokens


@login_required
@require_http_methods(['GET'])
def get_project_detail(request, id):
    token = get_tokens(request)
    p = Projects(token)
    id = id
    if not id:
        return JsonResponse({"message": "bad request"}, status=400)
    r = p.get_project_detail(id)
    return JsonResponse(r, safe=False, status=200)
