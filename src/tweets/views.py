from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Tweet
# Create your views here.

# Create

# Update

# Delete

# List/Search

# Retrieve



class TweetDetailView(DetailView):
    #template_name = 'tweets/detail_view.html'
    queryset = Tweet.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        print(pk)
        obj = get_object_or_404(Tweet, pk=pk)
        return obj

class TweetListView(ListView):
    #template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        #context["another_list"] = Tweet.objects.all()
        #print(context)
        return context


def tweet_detail_view(request, pk=1):  # pk == id
    #obj = Tweet.objects.get(pk=pk) # GET from database
    obj = get_object_or_404(Tweet, pk=pk)
    print(obj)
    context = {
        "object": obj
    }
    return render(request, 'tweets/detail_view.html', context)