from django.shortcuts import render, HttpResponse

def view_a(request):
    return HttpResponse("view_a")


def view_b(request):
    return HttpResponse("view_b")


def view_x(request):
    return HttpResponse("view_x")