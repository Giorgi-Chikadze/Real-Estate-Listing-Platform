from rest_framework import routers
from .views import PropertyModelviewset

router = routers.DefaultRouter()
router.register('properties', PropertyModelviewset)

urlpatterns = router.urls
