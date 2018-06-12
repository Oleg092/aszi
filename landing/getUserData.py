from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from landing.models import Users
import json


def xhr_test(request):
    if request.is_ajax():
        print(request.POST['userId'])  # client data
        try:
            user = get_object_or_404(Users, id=request.POST['userId'])

            print(user.firstname)
        except:
            messages.success(request, "user not found")

    return HttpResponse(json.dumps({
                'name': user.firstname,
                'lastname': user.lastname,
            })
        )
