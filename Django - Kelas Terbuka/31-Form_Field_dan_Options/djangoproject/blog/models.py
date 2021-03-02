from django.db import models

# Create your models here.
class PostModel(models.Model):
   title    = models.CharField(max_length=50)
   author   = models.CharField(max_length=50)
   body     = models.TextField()
   category = models.CharField(max_length=50)

   def __str__(self):
       return f"{self.id}. {self.title}"
   