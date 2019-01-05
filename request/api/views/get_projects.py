from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from request.api.views.request_to_platform import Projects
from request.utils import login_required, get_tokens


@login_required
@require_http_methods(['GET'])
def get_projects(request):
    token = get_tokens(request)
    p = Projects(token)
    response = p.get_projects()
    return JsonResponse(response, safe=False, status=200)
