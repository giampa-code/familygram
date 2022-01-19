"""familygram views"""

# Django
from django.http import HttpResponse, JsonResponse

# utilities
from datetime import datetime


def hello_world(request):
    """return a greeting"""
    now = datetime.now().strftime('%d %b %Y - %H:%M')
    return HttpResponse(f'Hi!, current server time is {now}')

def sorted_nums(request):
    """Hi"""
    #import pdb; pdb.set_trace()
    # pasamos del string entero a una lista de numeros, y los pasamos a ints
    numbers = [int(i) for i in request.GET['numbers'].split(",")]
    sorted_numbers = sorted(numbers)
    data = {
        'status':'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted succesfully'
    }
    return JsonResponse(data,json_dumps_params={'indent': 4})
    
def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = f'Sorry {name}, you are not allowed here.'
    else:
        message = f'Hello {name}, welcome to this page.'
    return HttpResponse(message)

def amor(request):
    return HttpResponse("Te amo mucho")