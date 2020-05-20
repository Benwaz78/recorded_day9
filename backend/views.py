from django.shortcuts import render, redirect
from classwork_app.models import Category
from backend.functions import calculate
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from backend.forms import CategoryForm, PostForm, ContactForm


# Create your views here.
@login_required(login_url='/backoffice/login-page/')
def index(request):
    return render(request, 'dashboard/index.html')


@login_required(login_url='/backoffice/login-page/')
def add_category(request):
    if request.method == 'POST':
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            messages.success(request, 'Data submitted successfully')
            category = CategoryForm()
    else:
        category = CategoryForm()
    return render(request, 'dashboard/add-category.html', {'cat':category})


@login_required(login_url='/backoffice/login-page/')
def post_form(request):
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()
            messages.success(request, 'Data submitted successfully')
            post = PostForm()
    else:
        post = PostForm()
    return render(request, 'dashboard/add-post.html', {'pst':post})





def calculate(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        calculate1 = request.POST.get('calculate')
        # calculate(int(num1), int(num2), calculate1, 'Add')
        if calculate1 == 'Add':
            add = int(num1) + int(num2)
            messages.success(request, add)
        elif calculate1 == 'Subt':
            subt = int(num1) - int(num2)
            messages.success(request, subt)
        elif calculate1 == 'Div':
            try:
                div = int(num1)/int(num2)
                messages.success(request, div)
            except ZeroDivisionError  as e:
                messages.error(request, e)
    return render(request, 'dashboard/calculator.html')
   

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:index')
        else:
            messages.error(request, 'Username Or Password is incorrect')
    return render(request, 'classwork_app/login.html')

@login_required(login_url='/backoffice/login-page/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')
    
@login_required(login_url='/backoffice/login-page/')
def confirm_logout(request):
    return render(request, 'dashboard/confirm-logout.html')


def contact_form(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request, 'Data saved')
    else:
        contact = ContactForm()
    return render(request, 'classwork_app/contact.html', {'con':contact})



# states = {
#     'key1':'Value1'
#     'key2':'Value2'
#     'key3':'Value3'
# }

# print(states['key1'])