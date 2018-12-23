from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create,name='create'),
    path('', views.index,name='index'),
    path('detail/<int:project_id>/', views.detail,name='detail'),
    path('dashboard/<int:project_id>/', views.dashboard,name='dash'),
    path('pr/', views.project_dashboard,name='projects'),
]
