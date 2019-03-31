from django.urls import path
from uploadfiles import views


urlpatterns = [
    path('', views.upload_file, name='file_upload'),
    path('documents/', views.DocumentCollectionView.as_view(), name = 'list_display'),
    path('search', views.SearchView, name='search')
]

