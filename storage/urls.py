from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('download/<str:filename>/', views.download_file, name='download_file'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('list/', views.list_files, name='list_files'),
]
