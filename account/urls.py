from . import views
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('upload/', include('uploadfiles.urls')),
    path('registration/', include('registration.urls')),
    path('search/', include('search.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
