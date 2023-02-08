from .urls_yasg import urlpatterns_yasg
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('store.urls')),
]

urlpatterns += urlpatterns_yasg