from django.urls import path
from uploadfiles import views


urlpatterns = [
    path('', views.upload_file, name='file_upload'),
    path('documents/', views.DocumentListView.as_view(), name = 'list_display'),
    path('documents/', views.DocumentListView.as_view(), name = 'list_display')
]

