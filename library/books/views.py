from django.http import HttpResponse
from django.shortcuts import render


def show_main_page(request):
    return HttpResponse('<h1>Main page</h1>')
