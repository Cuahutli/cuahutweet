from rest_framework import generics

from tweets.models import Tweet
from .serializer import  TweetModelSerializer

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        return Tweet.objects.all()