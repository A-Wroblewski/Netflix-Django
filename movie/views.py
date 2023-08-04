from django.shortcuts import redirect, reverse
from .models import Movie, User
from .forms import HomePageForm, CreateAccountForm
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# function based view (FBV)
# def homepage(request):
#     return render(request, 'homepage.html')


# class based view (CBV)
class HomePage(FormView):
    template_name = 'homepage.html'
    form_class = HomePageForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('movie:home_movies')

        # redireciona pra homepage
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        user = User.objects.filter(email=email)
        self.request.session['email'] = email

        if user:
            return reverse('movie:login')

        return reverse('movie:create_account')


# def home_movies(request):
#     context = {}
#     movies_list = Movie.objects.all()
#     context['movies_list'] = movies_list
#     return render(request, 'home_movies.html', context)


# a ListView retorna uma lista com o nome object_list
class HomeMovies(LoginRequiredMixin, ListView):
    template_name = 'home_movies.html'
    model = Movie


# a DetailView retorna 1 item do nosso modelo Movie (object)
class MoviesDetails(LoginRequiredMixin, DetailView):
    template_name = 'movies_details.html'
    model = Movie

    def get(self, request, *args, **kwargs):
        movie = self.get_object()  # pega o filme que o usuário escolheu
        movie.views += 1
        movie.save()  # registra a modificação no banco

        # pega o usuário logado e adiciona o filme nos vistos
        user = request.user
        user.watched_movies.add(movie)

        # faz o redirecionamento para a url do filme
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MoviesDetails, self).get_context_data(**kwargs)

        related_movies = Movie.objects.filter(category=self.get_object().category)
        context['related_movies'] = related_movies

        return context


class MoviesSearch(LoginRequiredMixin, ListView):
    template_name = 'movies_search.html'
    model = Movie

    def get_queryset(self):
        user_search = self.request.GET.get('query')

        if user_search:
            object_list = self.model.objects.filter(title__icontains=user_search)
            return object_list

        return self.model.objects.all()


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit_profile.html'
    model = User
    fields = ['first_name', 'last_name', 'email']

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def get_success_url(self):
        return reverse('movie:home_movies')


class CreateAccount(FormView):
    template_name = 'create_account.html'
    form_class = CreateAccountForm

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('movie:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        email = self.request.session.get('email')
        context['form']['email'].initial = email

        return context
