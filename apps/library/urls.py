from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')
router.register(r'client/(?P<id_client>[^/.]+)/books', LoanViewSet, basename='client-books')

urlpatterns = [
    path('', include(router.urls)),
]
