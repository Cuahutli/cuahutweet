from django.contrib import admin

# Register your models here.

from .models import Tweet

from .form import TweetModelForm


class TweetModelAdmin(admin.ModelAdmin):
    form = TweetModelForm

admin.site.register(Tweet, TweetModelAdmin)