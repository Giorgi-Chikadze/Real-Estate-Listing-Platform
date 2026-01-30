from django.urls import path, include
from .views import FavoriteViewSet

from rest_framework.routers import SimpleRouter, DefaultRouter


router = DefaultRouter()

router.register('favorites', FavoriteViewSet)




urlpatterns = [
    path("", include(router.urls)),

]