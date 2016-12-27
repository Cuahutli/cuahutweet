from django.conf.urls import url
from django.views.generic import RedirectView

from .views import (
    TweetListAPIView,
    TweetCreateAPIView
)

urlpatterns = [
    url(r'^$', TweetListAPIView.as_view(), name='list'), #/api/tweet
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'), #/api/tweet
]