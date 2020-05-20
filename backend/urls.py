from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-post-form/', views.post_form, name='post_form'),
    path('add-category/', views.add_category, name='add_category'),
    path('contact-page/', views.contact_form, name='contact_form'),
    path('calculate/', views.calculate, name='calculate'),
    path('login-page/', views.login_view, name='login_view'),
    path('logout-page/', views.logout_view, name='logout_view'),
    path('confirm-logout-page/', views.confirm_logout, name='confirm_logout'),
]
