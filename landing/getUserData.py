from django.core import serializers
from django.http import HttpResponse
from landing.models import Users
import json


def getUsersList(request):
    if request.is_ajax():
        users = Users.objects.all().only('email', 'lastname', 'firstname', 'birthDate')
        print(users)
        context = serializers.serialize('json', users, indent=2, use_natural_foreign_keys=True, use_natural_primary_keys=True)
        return HttpResponse(json.dumps(context), content_type='application/json',
                                )
