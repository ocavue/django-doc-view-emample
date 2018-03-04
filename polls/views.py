from django.http import HttpResponse, JsonResponse
from django.views.generic import View


def index(request):
    """
    A example of Function-based view

    method:
        get
    request:
        None
    response:
        type: html
    """
    return HttpResponse("Hello, world. You're at the polls index.")


class User(View):
    """
    A example of Class-based view

    method:
        get
    request:
        id
    respones:
        type: json
        example:

            ```
            {
                "data": {
                    "user": {
                        "id": "123",
                        "name": "qwertyuiop",
                        "create_date": "1970-01-01"
                    }
                },
                "error": false
            }
            {
                "msg": "error message",
                "error": true
            }
            ```

    more info:
        add login authentication in future

    """

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get("id", None)
        if not user_id:
            return JsonResponse(
                {
                    "msg": "Can not find id in query",
                    "error": True
                }
            )
        return JsonResponse(
            {
                "data": {
                    "user": {
                        "id": user_id,
                        "name": "qwertyuiop",
                        "create_date": "1970-01-01"
                    }
                },
                "error": False
            }
        )
