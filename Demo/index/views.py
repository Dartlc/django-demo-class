from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    """
        index program
    :param request: None
    :return: str
    """

    return HttpResponse(f'<h1> Hello World</h1>')
