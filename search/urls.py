from django.urls import path, include
from . import views
app_name='search'

urlpatterns = [
    path('', views.SearchView.as_view(), name='search')
]