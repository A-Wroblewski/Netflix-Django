# Os contexts servem para criar variáveis que podem ser
# usadas dentro do HTML.
#
# Contextos adicionais podem ser criados nesse arquivo e
# devem ser registrados nos templates nas settings do projeto.
#
# Os nomes das variáveis sempre serão a
# chave do dicionário (context).

from .models import Movie

def recent_movies_list(request):
    movies_list = Movie.objects.all().order_by('-creation_date')[:8]

    if movies_list:
        highlighted_movie = movies_list[0]
    else:
        highlighted_movie = None

    return {'recent_movies_list': movies_list, 'highlighted_movie': highlighted_movie}

def most_viewed_movies(request):
    movies_list = Movie.objects.all().order_by('-views')[:8]

    return {'most_viewed_movies': movies_list}
