import json
from django.core import serializers
from django.http import HttpResponse
from landing.models import Defence


def getSziList(request):
    if request.is_ajax():
        try:
            defence = Defence.objects.all()
            context = serializers.serialize("json", defence)
            return HttpResponse(json.dumps(context), content_type='application/json'
                                )
        except:
            return HttpResponse(json.dumps({
                "Error": "not defence"
            }))
