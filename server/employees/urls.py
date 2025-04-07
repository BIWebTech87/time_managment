from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers

from .views import EmployeeVeiwSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

app_name = 'employees'

employees_routers = routers.DefaultRouter()
employees_routers.register(r'employees', EmployeeVeiwSet, basename='employees')

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='employee_login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', include(employees_routers.urls)),

]
