from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BetterLinkViewSet

router = SimpleRouter()
router.register(r'bls', BetterLinkViewSet, basename='bls')

urlpatterns = [
    path('blsr/<str:short_link>/', BetterLinkViewSet.as_view({'get': 'retrieve_and_redirect'}), name='blsr'),
] + router.urls
