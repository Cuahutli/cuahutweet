from django.conf.urls import url
from .views import (
    TweetDetailView,
    TweetListView,
    TweetCreateView,
    tweet_detail_view)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'), #/tweet/
    #url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'), #/tweet/1/
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), #/tweet/1/
    url(r'^create/$', TweetCreateView.as_view(), name='create'), #/tweet/1/

]
