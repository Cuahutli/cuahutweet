from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView
    )
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin

class RetweetView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated():
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(tweet.get_absolute_url())

# Create
class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    #success_url = reverse_lazy("tweet:detail")
    login_url = '/admin/'


# Update
class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    #success_url = '/tweet/'
    login_url = '/admin/'

# Delete
class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    # para usar el reverse se utiliza lo que está en el tag name en las urls, cuando se usa include, se crea un namespace
    # y se llama namespace:name de la url.
    #success_url = reverse_lazy("home")
    success_url = reverse_lazy("tweet:list")

# List/Search

# Retrieve
class TweetDetailView(LoginRequiredMixin, DetailView):
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Tweet, pk=pk)
        return obj

class TweetListView(LoginRequiredMixin, ListView):
    #queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy('tweet:create')
        return context


def tweet_detail_view(request, pk=1):  # pk == id
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, 'tweets/detail_view.html', context)