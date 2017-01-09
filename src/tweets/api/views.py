from django.db.models import Q

from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from tweets.models import Tweet
from .serializer import  TweetModelSerializer
from .pagination import  StandardResultsPagination


class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "No permitido"
        if request.user.is_authenticated():
            is_liked = Tweet.objects.like_toggle(request.user, tweet_qs.first())
            return Response({'liked': is_liked})
        return Response({"message": message}, status=400)



## con esta clase de la api retweetearimos
class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = "No permitido"
        if tweet_qs.exists() and tweet_qs.count() == 1:
            new_tweet = Tweet.objects.retweet(request.user, tweet_qs.first())
            if new_tweet is not None:
                data = TweetModelSerializer(new_tweet).data
                return Response(data)
            message = "No puede ser retweeteado más de 1 vez al día"
        return Response({"message": message}, status=400)


class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(TweetListAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context


    def get_queryset(self, *args, **kwargs):
        requested_user = self.kwargs.get("username")
        if requested_user:
            qs = Tweet.objects.filter(user__username=requested_user).order_by('-timestamp')  ## my tweets
        else:
            im_following = self.request.user.profile.get_following()  # none if is a zero
            qs1 = Tweet.objects.filter(user__in=im_following) ## following tweets
            qs2 = Tweet.objects.filter(user=self.request.user) ## my tweets
            qs = (qs1 | qs2).distinct().order_by('-timestamp') # both tweets

        #qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs