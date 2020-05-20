from django.contrib import admin
from classwork_app.models import Post, Category, UserProfile, About

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(About)
