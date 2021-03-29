from django.urls import path

from . import views

urlpatterns = [
    path('group/<slug:slug>/', views.group_posts, name='group'),
    path('group/', views.group_index, name='group_index'),
    path('', views.index, name='index')
]
