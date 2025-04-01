from django.urls import path
from .views import index
from django.contrib.auth import views as auth_views

app_name = 'main'

urlpatterns = [
    path('', index, name = 'index'),
    #path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),

]