from django.db import models

class users(models.Model):
    user_name = models.CharField(max_length=64)
    pass_word = models.CharField(max_length=64) 
