from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from request.api.views.request_to_platform import Things
from request.utils import login_required, get_tokens


@login_required
@require_http_methods(['GET'])
def get_thing_detail(request, p_id, t_id):
    token = get_tokens(request)
    thing = Things(token)
    # p_id = request.GET.get('project_id')
    # t_id = request.GET.get('thing_id')
    if not p_id or not t_id:
        return JsonResponse({"message": "bad request"}, status=400)
    response = thing.get_thing_data(p_id, t_id)

    return JsonResponse(response, safe=False, status=200)
