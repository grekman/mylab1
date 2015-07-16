from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_page(request):
    hel='<h1> Hello world<h1>'
    return HttpResponse(hel)

def indexmy(request):
    context_mydict = {'title': "It's my first blog", 'boldmessage': "I am bold font from the context"}
    return render(request, 'blog/indexmy.html', context_mydict)
