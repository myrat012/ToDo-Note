from django.shortcuts import render
from django.http import HttpResponse

note = [
    {
        'title': 'title1',
        'context': 'bla bla bla',
        'done': False,
        'start_note': 'August 27, 2018',
        'end_note': ''
    },
    {
        'title': 'title2',
        'context': 'kto to to tam',
        'done': True,
        'start_note': 'August 26, 2018',
        'end_note': ''
    },
]

# Create your views here.
def home(request):
    context = {
        'data':note,
        'title': 'Home Page'
    }
    return render(request, 'note/home.html', context)

def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'note/about.html', context)