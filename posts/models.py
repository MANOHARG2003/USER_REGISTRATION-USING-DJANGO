from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=100)
    roll=models.IntegerField()
    email=models.EmailField(null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True,null=True,blank=True)
    image=models.ImageField(default="blank.png",blank=True,null=True)

    def __str__(self):
        return self.name