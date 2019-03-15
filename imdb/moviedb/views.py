from django import forms
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Movie, Actor, Award, CommentMovie, CommentActor, \
    CommentAward
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView


class MovieListView(ListView):
    model = Movie
    context_object_name = 'movies'
    paginate_by = 3


class MovieCreateView(CreateView):
    model = Movie
    fields = '__all__'
    success_url = reverse_lazy('moviedb:movie')


class EditCommentMovieForm(forms.ModelForm):
    class Meta:
        model = CommentMovie
        fields = 'content',


class CommentMovieUpdateView(UpdateView):
    model = CommentMovie
    form_class = EditCommentMovieForm

    def get_success_url(self):
        return reverse_lazy('moviedb:movie_detail',
                            kwargs={'pk': self.get_object().movie_id})


class CommentMovieDeleteView(DeleteView):
    model = CommentMovie

    def get_success_url(self):
        return reverse_lazy('moviedb:movie_detail',
                            kwargs={'pk': self.get_object().movie_id})


class MovieDetailView(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentMovie.objects.filter(
            movie_id=self.kwargs["pk"]).order_by('-time')
        context['edit_comment_form'] = EditCommentMovieForm
        return context

    def post(self, request, *args, **kwargs):
        movie_id = self.kwargs["pk"]
        movie = Movie.objects.get(pk=movie_id)
        user = self.request.user
        content = request.POST.get("content")
        CommentMovie.objects.create(movie=movie, user=user, content=content)

        return HttpResponseRedirect(
            reverse_lazy('moviedb:movie_detail', kwargs={"pk": movie_id}))


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['description', 'actors', 'category', 'logo']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('moviedb:movie_detail',
                            kwargs={'pk': self.get_object().pk})


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('moviedb:movie')


class ActorListView(ListView):
    model = Actor
    context_object_name = 'actors'
    paginate_by = 3


class ActorCreateView(CreateView):
    model = Actor
    fields = '__all__'
    success_url = reverse_lazy('moviedb:actor')


class EditCommentActorForm(forms.ModelForm):
    class Meta:
        model = CommentActor
        fields = 'content',


class CommentActorUpdateView(UpdateView):
    model = CommentActor
    form_class = EditCommentActorForm

    def get_success_url(self):
        return reverse_lazy('moviedb:actor_detail',
                            kwargs={'pk': self.get_object().actor_id})


class CommentActorDeleteView(DeleteView):
    model = CommentActor

    def get_success_url(self):
        return reverse_lazy('moviedb:actor_detail',
                            kwargs={'pk': self.get_object().actor_id})


class ActorDetailView(DetailView):
    model = Actor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentActor.objects.filter(
            actor_id=self.kwargs["pk"]).order_by('-time')
        context['edit_comment_form'] = EditCommentActorForm
        return context

    def post(self, request, *args, **kwargs):
        actor_id = self.kwargs["pk"]
        actor = Actor.objects.get(pk=actor_id)
        user = self.request.user
        content = request.POST.get("content")
        CommentActor.objects.create(actor=actor, user=user, content=content)

        return HttpResponseRedirect(
            reverse_lazy('moviedb:actor_detail', kwargs={"pk": actor_id}))


class ActorUpdateView(UpdateView):
    model = Actor
    fields = '__all__'
    success_url = reverse_lazy('moviedb:actor_detail')

    def get_success_url(self):
        return reverse_lazy('moviedb:actor_detail',
                            kwargs={'pk': self.get_object().pk})


class ActorDeleteView(DeleteView):
    model = Actor
    success_url = reverse_lazy('moviedb:actor')


class AwardListView(ListView):
    model = Award
    context_object_name = 'awards'
    paginate_by = 3


class AwardCreateView(CreateView):
    model = Award
    fields = '__all__'
    success_url = reverse_lazy('moviedb:award')


class EditCommentAwardForm(forms.ModelForm):
    class Meta:
        model = CommentAward
        fields = 'content',


class CommentAwardUpdateView(UpdateView):
    model = CommentAward
    form_class = EditCommentAwardForm

    def get_success_url(self):
        print(self.get_object().award_id)
        return reverse_lazy('moviedb:award_detail',
                            kwargs={'pk': self.get_object().award_id})


class CommentAwardDeleteView(DeleteView):
    model = CommentAward

    def get_success_url(self):
        return reverse_lazy('moviedb:award_detail',
                            kwargs={'pk': self.get_object().award_id})


class AwardDetailView(DetailView):
    model = Award

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = CommentAward.objects.filter(
            award_id=self.kwargs["pk"]).order_by('-time')
        context['edit_comment_form'] = EditCommentAwardForm
        return context

    def post(self, request, *args, **kwargs):
        award_id = self.kwargs["pk"]
        award = Award.objects.get(pk=award_id)
        user = self.request.user
        content = request.POST.get("content")
        CommentAward.objects.create(award=award, user=user, content=content)

        return HttpResponseRedirect(
            reverse_lazy('moviedb:award_detail', kwargs={"pk": award_id}))


class AwardUpdateView(UpdateView):
    model = Award
    fields = ['actors', 'movies', 'poster']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('moviedb:award_detail',
                            kwargs={'pk': self.get_object().pk})


class AwardDeleteView(DeleteView):
    model = Award
    success_url = reverse_lazy('moviedb:award')
