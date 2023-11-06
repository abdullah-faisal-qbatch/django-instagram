from django.urls import path
from .views import RegisterView
from django.contrib.auth import views as auth_views

from . import views
from .views import login_method

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    # path('signup/', views.signup, name='signup'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    # path('login/', views.login_method, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
