import json
from urllib import response

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import _json

from subscribe.models import Car


def index(request):
    response = json.dumps(request.GET.get('name'))
    return HttpResponse(request.GET.get('validationToken'), content_type='text/plain')

def get_car(request, name):
    response = json.dumps([{'name': request.GET.get('name')}])

    return HttpResponse(response, content_type='text/json')

# Create your views here.
