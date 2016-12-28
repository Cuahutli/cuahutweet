from django.conf.urls import url
from django.views.generic import RedirectView
from .views import (
    UserDetailView,
    UserFollowView
)

urlpatterns = [
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='detail'), #/user/1/
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='follow'), #/user/1/
]
