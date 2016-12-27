from django.conf import settings
from django.urls import reverse
from django.db import models
from .validators import validate_content

# Create your models here.

class Tweet(models.Model):
    """
    Description: Model Description
    """
    #user
    user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
    #content 	= models.TextField(max_length=140)
    content     = models.CharField(max_length=140, validators=[validate_content])
    updated		= models.DateTimeField(auto_now=True)
    timestamp	= models.DateTimeField(auto_now_add=True)


    def __str__(self):
    	return str(self.content)

    # haciendo esta función ya no sería necesario en la vista utilizar succes_url
    # aún cuando se implemente este metodo, si se usa success_url  reempleazaría a lo que regresa get_absolute_url()
    def get_absolute_url(self):
        return reverse("tweet:detail", kwargs={"pk":self.pk})

    class Meta:
        ordering = ['-timestamp', 'content']

    """
        esta es otra manera de hacer la validación similar a lo que está en form.py
         def clean_content(self, *args, **kwargs):
             content = self.cleaned_data.get("content")
             if content == "abc":
                 raise forms.ValidationError("No puede ser ABC")
             return content
    """
    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError(" El contenido No puede ser ABC")
    #     return super(Tweet, self).clean(*args, **kwargs)