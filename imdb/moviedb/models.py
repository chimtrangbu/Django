from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    """
    Category model : Table for movie categories
    """
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_movies(self):
        return self.movie_set.all()


class Actor(models.Model):
    """
    Actor model : model for Actor / Actress
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    sex = models.CharField(max_length=6, choices=(('Male', 'Male'),
                                                  ('Female', 'Female'),
                                                  ('Other', 'Other')))
    nationality = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.first_name

    def get_movies(self):
        return self.movie_set.all()

    def get_awards(self):
        return self.award_set.all()

    def get_commentactors(self):
        return self.commentactor_set.all()


class Movie(models.Model):
    """
    Movie model : model for Movies
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    release_date = models.DateField()
    category = models.ManyToManyField(Category)
    actors = models.ManyToManyField(Actor, blank=True)
    logo = models.ImageField(upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"

    def get_actors(self):
        result = ''
        for actor in self.actors.all():
            result += ' ' + actor.first_name
        return result

    def get_awards(self):
        return self.award_set.all()

    def get_commentmovies(self):
        return self.commentmovie_set.all()

    def __str__(self):
        return "{0}".format(self.title)


class Award(models.Model):
    """
    Award model : model for awards
    """
    name = models.CharField(max_length=100)
    kind = models.CharField(max_length=5, choices=(('Movie', 'Movie'),
                                                   ('Actor', 'Actor')))
    movies = models.ManyToManyField(Movie, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    poster = models.ImageField(upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name = "Award"
        verbose_name_plural = "Awards"

    def get_commentawards(self):
        return self.commentaward_set.all()

    def __str__(self):
        return "{0}".format(self.name)


class CommentMovie(models.Model):
    """
    Comment model : model for comments of movies
    """
    content = models.TextField(blank=False, max_length=256)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "CommentMovie"
        verbose_name_plural = "CommentMovies"


class CommentActor(models.Model):
    """
    Comment model : model for comments of actors
    """
    content = models.TextField(blank=False, max_length=256)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "CommentActor"
        verbose_name_plural = "CommentActors"


class CommentAward(models.Model):
    """
    Comment model : model for comments of awards
    """
    content = models.TextField(blank=False, max_length=256)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    award = models.ForeignKey(Award, on_delete=models.CASCADE,)

    class Meta:
        verbose_name = "CommentAward"
        verbose_name_plural = "CommentAwards"