from django.conf.urls import url
from django.views.generic import RedirectView

from .views import (
    LikeToggleAPIView,
    RetweetAPIView,
    TweetListAPIView,
    TweetCreateAPIView
)

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'), #/api/tweet
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), #/api/tweet
    url(r'^(?P<pk>\d+)/retweet/$', RetweetAPIView.as_view(), name='retweet'), #/api/tweet
    url(r'^(?P<pk>\d+)/like/$', LikeToggleAPIView.as_view(), name='like-toggle'), #/api/tweet
]