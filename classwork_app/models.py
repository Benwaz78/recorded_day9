from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    url = models.URLField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True)
    phone = models.CharField(max_length=15)

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    desc = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    pst_title = models.CharField(max_length=150, verbose_name='Post Title')
    pst_img = models.ImageField(blank=True, null=True, upload_to='uploads/')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    update_date = models.DateTimeField(auto_now=True, blank=True)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pst_title


class About(models.Model):
    abt_title = models.CharField(max_length=150)
    profile = models.ImageField(blank=True, null=True, upload_to='uploads/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.abt_title

