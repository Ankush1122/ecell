from django.shortcuts import render, redirect


def home(request):
    return render(request, 'core/home.html')


def team(request):
    return render(request, 'core/team.html')


def speakers(request):
    return render(request, 'core/speakers.html')


def redir(request):
    response = redirect('/home/')
    return response
