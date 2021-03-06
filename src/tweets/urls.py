from django.conf.urls import url
from django.views.generic import RedirectView
from .views import (
    RetweetView,
    TweetDetailView,
    TweetDeleteView,
    TweetListView,
    TweetCreateView,
    TweetUpdateView,
    tweet_detail_view)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^search$', TweetListView.as_view(), name='list'), #/tweet/
    url(r'^create/$', TweetCreateView.as_view(), name='create'), #/tweet/1/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), #/tweet/1/
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='retweet'), #/retweet
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), #/tweet/1/update/
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), #/tweet/1/delete/


]
