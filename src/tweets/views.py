from django.shortcuts import render

# Create your views here.

# Create

# Update

# Delete

# List/Search

# Retrieve
from .models import Tweet


def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id) #GET from database
    context = {
        "object": obj
    }
    return render(request, "tweets/detail_view.html", context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)
