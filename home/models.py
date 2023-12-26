from django.db import models

# Create your models here.

class Posts(models.Model):
    title=models.CharField(max_length=500000*5000000)
    message=models.TextField(max_length=5000000*500000)
    date=models.DateTimeField()
    image=models.CharField(max_length=500000*50000)