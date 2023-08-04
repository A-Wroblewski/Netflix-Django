from django.contrib import admin
from .models import Movie, Episode, User
from django.contrib.auth.admin import UserAdmin

fields = list(UserAdmin.fieldsets)
fields.append(('History', {'fields': ('watched_movies',)}))

UserAdmin.fieldsets = tuple(fields)

# Register your models here.

admin.site.register(Movie)
admin.site.register(Episode)
admin.site.register(User, UserAdmin)
