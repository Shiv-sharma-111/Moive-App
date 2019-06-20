from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>hii this is shivam sharma</h2>")

def detail(request, movie_id):
    return HttpResponse("<h2>welcome in id :" + str(movie_id) + "</h2>")
