from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserListDetailViewset, RegisterView, BecomeAgentView

router = DefaultRouter()

router.register('users', UserListDetailViewset, basename='user')
router.register('register', RegisterView, basename='register')
router.register('become-agent', BecomeAgentView, basename='become-agent' )


urlpatterns = [
    path('', include(router.urls)),
]