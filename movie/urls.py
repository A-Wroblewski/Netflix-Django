from django.urls import path, reverse_lazy
from .views import HomePage, HomeMovies, MoviesDetails, MoviesSearch, EditProfile, CreateAccount
from django.contrib.auth import views as auth_view

app_name = 'movie'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('movies/', HomeMovies.as_view(), name='home_movies'),
    path('movies/<int:pk>', MoviesDetails.as_view(), name='movies_details'),
    path('search/', MoviesSearch.as_view(), name='movies_search'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name='edit_profile'),
    path('create_account/', CreateAccount.as_view(), name='create_account'),
    path('change_password/', auth_view.PasswordChangeView.as_view(template_name='edit_profile.html', success_url=reverse_lazy('movie:home_movies')), name='change_password'),
]
