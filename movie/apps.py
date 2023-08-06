from django.apps import AppConfig


class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie'

    # funcão que vai rodar quando o aplicativo for todo carregado
    # cria um administrador no caso de usar um outro banco além do sqlite
    def ready(self):
        import os
        from .models import User

        email = os.getenv('ADMIN_EMAIL')
        password = os.getenv('ADMIN_PASSWORD')

        try:
            User.objects.create_user(
                username='admin',
                email=email,
                password=password,
                is_active=True,
                is_staff=True,
                is_superuser=True,
            )
        except:
            pass
