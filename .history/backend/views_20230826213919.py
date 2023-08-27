from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.db.models import Q
 

class HttpResponse(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True,
                 json_dumps_params=None, **kwargs):
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)

    @property
    def content(self):
        return super().content.decode('utf-8')
    
    def __str__(self):
        return self.content
    
    
    
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def render(
    request: HttpRequest,
    template_name: str | Sequence[str],
    context: Mapping[str, Any] | None = ...,
    content_type: str | None = ...,
    status: int | None = ...,
    using: str | None = ...
)-> HttpResponse;

@csrf_exempt

def get_data(request):
    if request.method == 'GET':
        data = request.GET.get('data')
        return HttpResponse(data)
    else:
        return HttpResponse("Hello, world. You're at the polls index.")



    


    



