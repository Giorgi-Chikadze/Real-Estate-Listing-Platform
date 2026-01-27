from django.urls import path, include
from .views import AreaViewSet, CityViewSet

from rest_framework_nested import routers
from rest_framework.routers import SimpleRouter, DefaultRouter


router = DefaultRouter()
router.register('city', CityViewSet)
router.register('area', AreaViewSet)

city_router = routers.NestedDefaultRouter(
    router,
    'city',
    lookup='city'
)

city_router.register('areas', AreaViewSet, basename='city-areas')



urlpatterns = [
    path("", include(router.urls)),
    path("", include(city_router.urls))

]