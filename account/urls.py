from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from account import views as account_views

urlpatterns = [
    path('', account_views.index, name='index'),
    path('login/', account_views.user_login, name='login'),
    path('logout/', account_views.user_logout, name='logout'),
    path('signup/', account_views.register, name='signup'),
    path('admin/', admin.site.urls),
    path('upload/', include('uploadfiles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
