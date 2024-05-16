from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.
def movie_list(request):
    movies=Movie.objects.all()
    # print (movies.values())
    data={'movies':list(movies.values())}
    # print(data)
    return JsonResponse(data)

def movie_details(request,pk):
    movie=Movie.objects.get(pk=pk)
    # print(movie.name)
    data={'name':movie.name,
          'description':movie.description,
          'status':movie.active}
    return JsonResponse(data)
              