from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Questions


def signup(request):
    return render(request, 'sign-up-1.html', {})

def signin(request):
    return render(request, 'sign-in-1.html', {})

def profile(request):
    return render(request, 'square-profile.html', {})

#def editor(request):
    #return render(request, 'circle-editor.html', {})

class EditorView(ListView):
    model = Questions
    template_name = 'circle-editor.html'

def friends(request):
    return render(request, 'square-friends.html', {})

def leaderboard(request):
    return render(request, 'square-notifications.html')

def play(request):
    return render(request, 'circle-knowledge-base.html')

def results(request):
    return render(request, 'results.html')
