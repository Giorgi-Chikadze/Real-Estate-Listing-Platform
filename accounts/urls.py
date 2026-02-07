from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserListDetailViewset, RegisterView

router = DefaultRouter()

router.register('users', UserListDetailViewset, basename='user')
router.register('register', RegisterView, basename='register')


urlpatterns = [
    path('', include(router.urls)),
]