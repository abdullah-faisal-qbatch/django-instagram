from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('add/room-details/', views.add_room, name='add-room'),
    path('inbox/users/', views.get_users, name='inbox'),
    path('inbox/users/<slug:slug>/', views.user, name='inbox')
]
