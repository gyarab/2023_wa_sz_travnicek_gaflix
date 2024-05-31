from django.contrib import admin
from filmy.models import Movie, Director, Genre

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'footage', 'genres_display']

class DirectorAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)
