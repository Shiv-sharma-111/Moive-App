from django.shortcuts import render
from . models import Movie
from django.http import HttpResponse
from django.http import Http404
from django .template import loader

def index(request):
    all_movies= Movie.objects.all()
    template = loader.get_template('movie1/index.html')
    context = {
      'all_movies':all_movies,
    }
    #for a in all_movies:
        #url = '/movie1/'+ str(a.id) + '/'
        #html = '<a href = " '+ url + ' ">' + a.actor + '</a><br>'
    return HttpResponse(template.render(context, request))

def detail(request, movie_id):
    #return HttpResponse("<h2>welcome in id :" + str(movie_id) + "</h2>")
    try:
        m1 = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist
        raise Http404("this is wrong")

    return HttpResponse(template.render(context, request))
