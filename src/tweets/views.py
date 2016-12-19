from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Tweet, pk=pk)
        return obj

class TweetListView(ListView):
    #queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context


def tweet_detail_view(request, pk=1):  # pk == id
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, 'tweets/detail_view.html', context)