from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import Http404
from classwork_app.models import About, Post, Category
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'classwork_app/index.html')

def about(request):
    about_data = About.objects.all()
    return render(request, 'classwork_app/about.html', {'about1':about_data})

def about_detail(request, abt_id):
    try:
        detail = About.objects.get(id=abt_id)
    except About.DoesNotExist:
        raise Http404('Model or page does not exist')
    return render(request, 'classwork_app/detail.html', {'dt':detail})

def users(request):
    get_users = User.objects.all()
    return render(request, 'classwork_app/users.html', {'users':get_users})

def post_list(request, post_id):
    count_records = Post.objects.filter(category__id=post_id).count()
    get_cat_name = get_object_or_404(Category, id=post_id)
    try:
        list_post = Post.objects.filter(category__id=post_id)
    except Post.DoesNotExist:
        raise Http404('Post not found here')
    args = {'pst_list':list_post, 'count':count_records, 'name':get_cat_name}
    return render(request, 'classwork_app/post-list.html', args)

def service(request):
    return render(request, 'classwork_app/services.html')
