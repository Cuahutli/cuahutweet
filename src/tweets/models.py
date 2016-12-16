from django.db import models

# Create your models here.

class Tweet(models.Model):
    """
    Description: Model Description
    """
    #user
    content 	= models.TextField(max_length=140)
    updated		= models.DateField(auto_now=True)
    timestamp	= models.DateField(auto_now_add=True)


    def __str__(self):
    	return str(self.content)

    class Meta:
        pass