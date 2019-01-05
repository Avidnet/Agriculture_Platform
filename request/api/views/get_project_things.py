from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from request.api.views.request_to_platform import Things
from request.utils import login_required, get_tokens


@login_required
@require_http_methods(['GET'])
def get_project_things(request, p_id):
    token = get_tokens(request)
    thing = Things(token)
    id = p_id
    if not id:
        return JsonResponse({"message": "bad request"}, status=400)
    response = thing.get_project_things(id)

    return JsonResponse(response, safe=False, status=200)
