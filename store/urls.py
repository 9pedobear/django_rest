from .views import BookViewSet
from rest_framework import routers

routers = routers.SimpleRouter()

routers.register(r'book', BookViewSet)

urlpatterns = []
urlpatterns += routers.urls







