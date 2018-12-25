from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('projects',views.IndexApi)
router.register('languages',views.PLanguageApi)

urlpatterns = [
    path('create/', views.create,name='create'),
    path('', views.index,name='index'),
    path('detail/<int:project_id>/', views.detail,name='detail'),
    path('dashboard/<int:project_id>/', views.dashboard,name='dash'),
    path('pr/', views.project_dashboard,name='projects'),
    path('add/', views.add_user,name='addusers'),
    path('remove/', views.remove_user,name='removeusers'),
    path('api/',include(router.urls)),
]
