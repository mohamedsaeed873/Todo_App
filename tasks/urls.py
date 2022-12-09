from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="list"),
    path('update_task/<str:pk>/', views.update_task , name="update_task"),
    path('delete/<str:pk>/', views.delete , name="delete"),
]
