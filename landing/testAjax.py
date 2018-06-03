from django.http import HttpResponse


def xhr_test(request):
    if request.is_ajax():
        print(request.POST)   # client data
        message = "Hello AJAX"
    else:
        message = "Hello"
    return HttpResponse(message)
