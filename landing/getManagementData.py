import json
from django.core import serializers
from django.http import HttpResponse
from landing.models import Requirements


def getManagementData(request):
    if request.is_ajax():
        try:
            requirements = Requirements.objects.all()
            context = serializers.serialize("json", requirements)
            return HttpResponse(json.dumps(context), content_type='application/json'
                                )
        except:
            return HttpResponse(json.dumps({
                "Error": "not requirements"
            }))
