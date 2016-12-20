from django.test import TestCase

# Create your tests here.

from .models import Tweet
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='cuahutli68136813');

    def test_tweet_item(self):
        object = Tweet.objects.create(
            user= User.objects.first(),
            content='Some random content'
        )

        self.assertTrue(object.content, "Some random content")
        self.assertTrue(object.id, 1)
        absolute_url = reverse("tweet:detail", kwargs={"pk":1})
        self.assertTrue(object.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        object = Tweet.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )

        absolute_url = reverse("tweet:detail", kwargs={"pk": object.pk})
        self.assertTrue(object.get_absolute_url(), absolute_url)
