from django.shortcuts import render, HttpResponse

def view_c(request):
    return HttpResponse("view_c")


def view_d(request):
    return HttpResponse("view_d")