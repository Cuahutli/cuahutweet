from django.db import models

# Create your models here.

class Tweet(models.Model):
    """
    Description: Model Description
    """
    content 	= models.TextField()
    


    def __str__(self):
    	return str(self.content) + "   id:  " + str(self.id)

    class Meta:
        pass