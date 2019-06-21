from django.shortcuts import render, get_object_or_404
from . models import Movie,Song
#from django.http import HttpResponse
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
    return render(request,'movie1/index.html',context)

def detail(request, movie_id):
    #return HttpResponse("<h2>welcome in id :" + str(movie_id) + "</h2>")
    m1=get_object_or_404(Movie, pk=movie_id)
    return render(request,'movie1/index1.html', {'m1':m1})

def favourite(request, movie_id):
    m1 = get_object_or_404(Movie, pk=movie_id)
    try:
        selected_song = m1.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request,'movie1/index1.html', {'m1':m1,
                                   'error_message':"You did not select song"})
    else:
        selected_song.is_favourite=True
        selected_song.save()
        return render(request,'movie1/index1.html', {'m1':m1})
