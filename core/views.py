from django.shortcuts import render, HttpResponse, redirect


def home(request):
    return render(request, 'core/home.html')


def redir(request):
    response = redirect('/home/')
    return response
