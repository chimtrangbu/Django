from django.contrib import admin
from .models import Movie, Actor, Category, Award, CommentMovie, \
    CommentActor, CommentAward


# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'release_date', 'get_actors']


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor)
admin.site.register(Category)
admin.site.register(Award)
admin.site.register(CommentMovie)
admin.site.register(CommentActor)
admin.site.register(CommentAward)
