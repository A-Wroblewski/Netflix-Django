import os
from .models import User
from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie'

    # funcão que vai rodar quando o aplicativo for todo carregado
    def ready(self):
        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv('ADMIN_PASSWORD')

        users = User.objects.filter(email=email)

        if not users:
            User.objects.create_superuser(
                username='admin',
                email=email,
                password=password,
            )
